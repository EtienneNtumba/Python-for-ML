#!/bin/bash

# Définition des variables
FASTQ_DIR="./data"
REF="H37Rv.fasta"
OUT_DIR="./output"
THREADS=8

mkdir -p $OUT_DIR

# Étape 1 : Indexation du génome de référence
bwa index $REF

# Étape 2 : Alignement des lectures FASTQ
for sample in $(ls $FASTQ_DIR/*_R1.fastq.gz | sed 's/_R1.fastq.gz//' | xargs -n1 basename); do
    echo "Traitement de $sample ..."

    bwa mem -t $THREADS $REF $FASTQ_DIR/${sample}_R1.fastq.gz $FASTQ_DIR/${sample}_R2.fastq.gz > $OUT_DIR/${sample}.sam
    samtools view -bS $OUT_DIR/${sample}.sam | samtools sort -o $OUT_DIR/${sample}.sorted.bam
    samtools index $OUT_DIR/${sample}.sorted.bam
    rm $OUT_DIR/${sample}.sam

    # Étape 3 : Variant Calling avec DeepVariant
    docker run -v "$(pwd):/data" google/deepvariant \
      /opt/deepvariant/bin/run_deepvariant \
      --model_type=WGS \
      --ref=/data/$REF \
      --reads=/data/${sample}.sorted.bam \
      --output_vcf=/data/${sample}.vcf.gz \
      --output_gvcf=/data/${sample}.g.vcf.gz \
      --num_shards=$THREADS

    # Étape 4 : Analyse de la Résistance avec TBprofiler
    tb-profiler profile -i $OUT_DIR/${sample}.vcf.gz -o $OUT_DIR/${sample}_tbprofiler

    # Étape 5 : Annotation Fonctionnelle avec DeepSEA
    python deepsea.py --vcf $OUT_DIR/${sample}.vcf.gz --ref $REF --output $OUT_DIR/${sample}_deepsea.vcf

    # Étape 6 : Filtrage et Annotation Finale
    bcftools filter -i 'QUAL>30' $OUT_DIR/${sample}.vcf.gz > $OUT_DIR/${sample}_filtered.vcf
    snpEff -v H37Rv $OUT_DIR/${sample}_filtered.vcf > $OUT_DIR/${sample}_annotated.vcf

    echo "Analyse complète pour $sample terminée."
done
