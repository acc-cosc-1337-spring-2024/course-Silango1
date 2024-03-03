# /src/homework/h_strings/strings.py

def get_hamming_distance(dna1, dna2):
    """
    Calculates the Hamming distance between two DNA sequences.
    
    Arguments:
    dna1 (str): The first DNA sequence.
    dna2 (str): The second DNA sequence.
    
    Returns:
    int: The Hamming distance between the two sequences.
    """
    if len(dna1) != len(dna2):
        raise ValueError("DNA sequences must have the same length")
    
    distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
    
    return distance

def get_dna_complement(dna):
    """
    Finds the complement of a given DNA sequence.
    
    Arguments:
    dna (str): The DNA sequence.
    
    Returns:
    str: The complement of the input DNA sequence.
    """
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in dna)
