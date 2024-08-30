# Read the contents of Extensions1.txt and Insertion1.txt
with open('Extensions1.txt', 'r') as file:
    extensions1 = set(file.read().splitlines())

with open('Insertion1.txt', 'r') as file:
    insertion1 = set(file.read().splitlines())

# Find common proteins in both Extensions1.txt and Insertion1.txt
common_proteins = extensions1.intersection(insertion1)

# Write the common proteins to a new file
with open('CommonExtensionsInsertions.txt', 'w') as file:
    for protein in common_proteins:
        file.write(protein + '\n')

print("Common proteins have been written to CommonExtensionsInsertions.txt.")
