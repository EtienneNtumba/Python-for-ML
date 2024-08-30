from Bio import SeqIO

def read_fasta(file_path):
    sequences = list(SeqIO.parse(file_path, "fasta"))
    return sequences

def find_longest_sequences(sequences):
    homologs = {}
    
    for seq_record in sequences:
        seq_id = seq_record.id
        seq_len = len(seq_record.seq)
        
        # Assuming homologous sequences have similar IDs with slight differences
        # Here we just consider the sequence ID without the last part (before '|')
        # e.g., for 'seq|1' and 'seq|2', 'seq' would be the common part
        homolog_group = '|'.join(seq_id.split('|')[:-1])
        
        if homolog_group not in homologs:
            homologs[homolog_group] = seq_record
        else:
            if seq_len > len(homologs[homolog_group].seq):
                homologs[homolog_group] = seq_record
    
    longest_sequences = list(homologs.values())
    return longest_sequences

def write_fasta(sequences, output_file):
    SeqIO.write(sequences, output_file, "fasta")

def main(input_fasta, output_fasta):
    sequences = read_fasta(input_fasta)
    longest_sequences = find_longest_sequences(sequences)
    write_fasta(longest_sequences, output_fasta)
    print(f"Longest sequences written to {output_fasta}")

# Usage
input_fasta = "test1.faa"
output_fasta = "longest_sequences.faa"
main(input_fasta, output_fasta)
