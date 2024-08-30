from Bio.Blast import NCBIXML

def parse_blast_results(blast_xml_file, e_value_threshold=1e-5):
    with open(blast_xml_file) as result_handle:
        blast_records = NCBIXML.parse(result_handle)
        conserved_sequences = []
        for blast_record in blast_records:
            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    if hsp.expect < e_value_threshold:
                        conserved_sequences.append({
                            "query_id": blast_record.query_id,
                            "subject_id": alignment.hit_id,
                            "e_value": hsp.expect,
                            "identity": hsp.identities,
                            "length": hsp.align_length
                        })
        return conserved_sequences

conserved_in_diplonemids = parse_blast_results("Dp-vs-diplonemids-blast.txt")
conserved_in_eukaryotes = parse_blast_results("Dp-vs-eukaryotes-blast.txt")

# Print conserved sequences
for seq in conserved_in_diplonemids:
    print(f"Query: {seq['query_id']}, Subject: {seq['subject_id']}, E-value: {seq['e_value']}, Identity: {seq['identity']}/{seq['length']}")

for seq in conserved_in_eukaryotes:
    print(f"Query: {seq['query_id']}, Subject: {seq['subject_id']}, E-value: {seq['e_value']}, Identity: {seq['identity']}/{seq['length']}")
