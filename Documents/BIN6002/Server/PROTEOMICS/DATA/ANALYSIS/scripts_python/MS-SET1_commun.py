import sys

# Ensure the script has the correct number of arguments
if len(sys.argv) != 4:
    print("Usage: python script_name.py <Extensions1.txt> <Insertion1.txt> <output_file>")
    sys.exit(1)

# Read the contents of Extensions1.txt and Insertion1.txt
with open(sys.argv[1], 'r') as file:
    extensions1 = set(file.read().splitlines())

with open(sys.argv[2], 'r') as file:
    insertion1 = set(file.read().splitlines())

# Find the common proteins in both Extensions1.txt and Insertion1.txt
common_proteins = extensions1.intersection(insertion1)

# Write the common proteins to the output file specified by the user
with open(sys.argv[3], 'w') as file:
    for protein in common_proteins:
        file.write(protein + '\n')

print(f"Common proteins have been written to {sys.argv[3]}.")
