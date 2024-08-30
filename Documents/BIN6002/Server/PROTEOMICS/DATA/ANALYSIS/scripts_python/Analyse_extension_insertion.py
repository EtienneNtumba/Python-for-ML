# Read the contents of Extensions1.txt and Insertion1.txt
with open('Extensions1.txt', 'r') as file:
    extensions1 = set(file.read().splitlines())

with open('Insertion1.txt', 'r') as file:
    insertion1 = set(file.read().splitlines())

# Find unique proteins in Extensions1.txt that are not in Insertion1.txt
unique_to_extensions = extensions1 - insertion1

# Find unique proteins in Insertion1.txt that are not in Extensions1.txt
unique_to_insertion = insertion1 - extensions1

# Find proteins that are unique to either Extensions1.txt or Insertion1.txt
unique_to_both = unique_to_extensions.union(unique_to_insertion)

# Write the unique proteins to new files
with open('Extensions2.txt', 'w') as file:
    for protein in unique_to_extensions:
        file.write(protein + '\n')

with open('Insertion2.txt', 'w') as file:
    for protein in unique_to_insertion:
        file.write(protein + '\n')

# Write the unique proteins to both to a new file
with open('UniqueToBoth.txt', 'w') as file:
    for protein in unique_to_both:
        file.write(protein + '\n')

print("Unique proteins have been written to Extensions2.txt, Insertion2.txt, and UniqueToBoth.txt.")
