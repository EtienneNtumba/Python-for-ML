import pandas as pd

def find_insertions_extensions(alignment_file, output_file, evalue_threshold=0.001, min_identity=50.0):
    """
    Identifies potential insertions and extensions in the query proteome.

    Arguments:
    - alignment_file: Path to the DIAMOND alignment results file (TSV format).
    - output_file: Path to the output file to save identified regions.
    - evalue_threshold: E-value threshold for considering significant alignments (default 0.001).
    - min_identity: Minimum percentage identity to consider for alignments (default 50.0).
    """
    # Load alignment results
    df = pd.read_csv(alignment_file, sep='\t', header=None)

    # Define column names for DIAMOND output
    df.columns = ['query_id', 'subject_id', 'percent_identity', 'alignment_length', 'mismatches', 
                  'gap_opens', 'q_start', 'q_end', 's_start', 's_end', 'e_value', 'bit_score']

    # Filter alignments based on e-value and identity thresholds
    filtered_df = df[(df['e_value'] <= evalue_threshold) & (df['percent_identity'] >= min_identity)]

    # Identify regions with gaps (insertions) and extended regions (extensions)
    insertions = filtered_df[filtered_df['gap_opens'] > 0]
    extensions = filtered_df[(filtered_df['q_start'] == 1) | (filtered_df['q_end'] == filtered_df['alignment_length'])]

    # Save the identified regions to an output file
    with open(output_file, 'w') as f:
        f.write("Insertions:\n")
        f.write(insertions.to_string(index=False))
        f.write("\n\nExtensions:\n")
        f.write(extensions.to_string(index=False))

    print(f"Insertions and extensions saved to {output_file}.")

if __name__ == "__main__":
    # Example usage
    alignment_file = "dp_vs_euk+ago.tsv"
    output_file = "insertions_extensions.tsv"
    find_insertions_extensions(alignment_file, output_file)
