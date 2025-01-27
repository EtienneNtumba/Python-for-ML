# DeepVariant Nextflow Pipeline

## Overview

This repository contains a **Nextflow** pipeline for variant calling using **DeepVariant**, **TBprofiler**, and **SnpEff**. It is designed for analyzing *Mycobacterium tuberculosis* (lineage 4) variants from **FASTQ** files and predicting antibiotic resistance.

## Features

- **Read Alignment**: Uses **BWA-MEM** to align paired-end FASTQ reads to the reference genome (**H37Rv**).
- **Variant Calling**: Uses **DeepVariant** to identify genomic variants.
- **Resistance Profiling**: Applies **TBprofiler** to determine antibiotic resistance from called variants.
- **Functional Annotation**: Uses **DeepSEA** to predict the regulatory impact of variants.
- **Variant Annotation**: Uses **SnpEff** for variant effect prediction.
- **Fully Automated**: Implemented in **Nextflow** for scalability and reproducibility.

## Installation

### Requirements

Ensure you have the following dependencies installed:

- [Nextflow](https://www.nextflow.io/docs/latest/getstarted.html)
- Docker (or Singularity/Conda for alternative execution)
- BWA-MEM, Samtools, DeepVariant, TBprofiler, SnpEff, DeepSEA

### Clone Repository

```bash
git clone https://github.com/EtienneNtumba/deepvariant-nextflow.git
cd deepvariant-nextflow
```

## Usage

### Input Data Structure

Ensure your data is organized as follows:

```
data/
├── sample1_R1.fastq.gz
├── sample1_R2.fastq.gz
├── sample2_R1.fastq.gz
├── sample2_R2.fastq.gz
└── H37Rv.fasta  # Reference genome
```

### Run Pipeline

To execute the pipeline:

```bash
nextflow run main.nf -profile docker
```

### Expected Output

The pipeline will generate the following:

```
output/
├── sample1.sorted.bam
├── sample1.vcf.gz
├── sample1_tbprofiler.json
├── sample1_deepsea.vcf
├── sample1_annotated.vcf
├── sample2.sorted.bam
├── sample2.vcf.gz
├── sample2_tbprofiler.json
├── sample2_deepsea.vcf
└── sample2_annotated.vcf
```

## Customization

You can modify `nextflow.config` to change computational resources and execution profile.

## Citation

If you use this pipeline in your research, please cite:

- DeepVariant: Poplin et al., Nature Biotechnology, 2018
- TBprofiler: Coll et al., Nature Communications, 2015
- DeepSEA: Zhou et al., Nature Genetics, 2015
- SnpEff: Cingolani et al., Bioinformatics, 2012

## Contact

For questions or contributions, please contact [EtienneNtumba](https://github.com/EtienneNtumba).

