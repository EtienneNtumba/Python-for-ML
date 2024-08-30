import pandas as pd

def parse_diamond_results(diamond_file):
    # Lire les résultats de DIAMOND
    columns = [
        "query_id", "subject_id", "percent_identity", "alignment_length",
        "mismatches", "gap_openings", "q_start", "q_end", "s_start", "s_end",
        "e_value", "bit_score"
    ]
    df = pd.read_csv(diamond_file, sep="\t", names=columns)
    return df

def identify_extensions_insertions(df):
    extensions = []
    for _, row in df.iterrows():
        q_length = row["q_end"] - row["q_start"] + 1
        s_length = row["s_end"] - row["s_start"] + 1
        if q_length > s_length:
            extension_length = q_length - s_length
            extensions.append({
                "query_id": row["query_id"],
                "subject_id": row["subject_id"],
                "q_start": row["q_start"],
                "q_end": row["q_end"],
                "s_start": row["s_start"],
                "s_end": row["s_end"],
                "extension_length": extension_length,
                "type": "extension"
            })
        elif s_length > q_length:
            insertion_length = s_length - q_length
            extensions.append({
                "query_id": row["query_id"],
                "subject_id": row["subject_id"],
                "q_start": row["q_start"],
                "q_end": row["q_end"],
                "s_start": row["s_start"],
                "s_end": row["s_end"],
                "insertion_length": insertion_length,
                "type": "insertion"
            })
    return extensions

def save_results(extensions, output_file):
    df = pd.DataFrame(extensions)
    df.to_csv(output_file, index=False, sep="\t")
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    diamond_file = "dp_vs_euk+ago.tsv"
    output_file = "extensions_insertions.tsv"

    df = parse_diamond_results(diamond_file)
    extensions = identify_extensions_insertions(df)
    save_results(extensions, output_file)
