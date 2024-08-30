from Bio import SeqIO

def remove_hypothetical_proteins(input_fasta, output_fasta):
    """
    Remove proteins labeled as 'hypothetical protein' from a FASTA file.

    Arguments:
    - input_fasta: Path to the input FASTA file.
    - output_fasta: Path to the output FASTA file with non-hypothetical proteins.
    """
    # Open the output file for writing
    with open(output_fasta, "w") as output_handle:
        # Read through the input FASTA file
        for record in SeqIO.parse(input_fasta, "fasta"):
            # Check if the description contains 'hypothetical protein'
            if "hypothetical protein" not in record.description.lower():
                # Write the record to the output file if it's not a hypothetical protein
                SeqIO.write(record, output_handle, "fasta")
    
    print(f"Filtered non-hypothetical proteins saved to {output_fasta}.")

if __name__ == "__main__":
    # Example usage
    input_fasta = "dp-proteome.faa"  # Replace with your input file path
    output_fasta = "dp-proteome_filtered.faa"  # Output file path
    remove_hypothetical_proteins(input_fasta, output_fasta)
