from Bio import SeqIO
import sys

def remove_hypothetical_proteins(input_file, output_file):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for record in SeqIO.parse(infile, "fasta"):
            if "hypothetical protein" not in record.description.lower():
                SeqIO.write(record, outfile, "fasta")
        print(f"Filtered sequences saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_hypothetical_proteins.py <input_fasta> <output_fasta>")
        sys.exit(1)

    input_fasta = sys.argv[1]
    output_fasta = sys.argv[2]

    remove_hypothetical_proteins(input_fasta, output_fasta)
