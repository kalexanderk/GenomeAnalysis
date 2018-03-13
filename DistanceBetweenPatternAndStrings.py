from itertools import imap
from operator import ne


def hamming_distance(seq1, seq2):
    'Returns the Hamming distance between equal-length sequences.'
    if len(seq1) != len(seq2):
        raise ValueError('Undefined for sequences of unequal length.')
    return sum(imap(ne, seq1, seq2))

def DistanceBetweenPatternAndStrings(Pattern, dna_list):
    k = len(Pattern)
    lr = len(dna_list[0])
    distance = 0
    for row in dna_list:
        hamm_dist = lr+1
        for i in xrange(lr-k+1):
            if hamm_dist > hamming_distance(Pattern, row[i:i+k]):
                hamm_dist = hamming_distance(Pattern, row[i:i+k])
        distance = distance + hamm_dist
    return distance

with open('/home/alextr/dataset_5164_1.txt') as input_data:
    pattern = input_data.readline()
    dna_list = [line.strip() for line in input_data.readlines()]
pattern = pattern[0:-1]
# pattern = "AAA"
# dna_list = ["TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT"]
dna_list = dna_list[0].split(' ')

print DistanceBetweenPatternAndStrings(pattern, dna_list)
