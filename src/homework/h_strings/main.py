from src.homework.h_strings.strings import get_hamming_distance, get_dna_complement

dna1 = "ATCGATCG"
dna2 = "ATAGCTAG"
hamming_distance = get_hamming_distance(dna1, dna2)
print("Hamming Distance:", hamming_distance)

dna = "ATCGATCG"
complement = get_dna_complement(dna)
print("DNA Complement:", complement)
