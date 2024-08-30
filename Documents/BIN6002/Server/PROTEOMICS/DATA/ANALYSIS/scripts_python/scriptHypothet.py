from Bio import SeqIO
import sys 

# Chemin vers le fichier FASTA source
input_fasta = sys.argv[1]
# Chemin vers le fichier FASTA de sortie
output_fasta = sys.argv[2] #'hypothetical_proteins.fasta'

def filter_hypothetical_proteins(input_fasta, output_fasta):
    # Ouvrir le fichier de sortie en mode écriture
    with open(output_fasta, 'w') as output_handle:
        # Itérer sur chaque enregistrement du fichier FASTA d'entrée
        for record in SeqIO.parse(input_fasta, 'fasta'):
            # Vérifier si 'hypothetical protein' est dans la description
            if 'hypothetical protein' in record.description:
                # Écrire l'enregistrement filtré dans le fichier de sortie
                SeqIO.write(record, output_handle, 'fasta')

# Appeler la fonction pour filtrer les protéines hypothétiques
filter_hypothetical_proteins(input_fasta, output_fasta)

print("Les protéines hypothétiques ont été extraites et sauvegardées dans", output_fasta)
