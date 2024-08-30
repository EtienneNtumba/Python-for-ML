# Read the list of selected proteins
with open('selected_proteins_MS-SET1_Ext_insert1.txt', 'r') as file:
    selected_proteins = set(file.read().splitlines())

# Prepare to write the selected protein sequences to a new FASTA file
with open('dp-proteome_filtered.faa', 'r') as input_fasta, open('selected_proteins.faa', 'w') as output_fasta:
    write_flag = False  # A flag to indicate when to write a sequence

    for line in input_fasta:
        if line.startswith('>'):  # This line is a header
            # Extract the protein ID from the header
            protein_id = line.split()[0][1:]  # Remove '>' and extract the ID
            if protein_id in selected_proteins:
                write_flag = True
                output_fasta.write(line)  # Write the header
            else:
                write_flag = False
        else:
            if write_flag:
                output_fasta.write(line)  # Write the sequence line

print("FASTA file with selected proteins has been created: selected_proteins.faa")
