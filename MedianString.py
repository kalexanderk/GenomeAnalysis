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

def NumberToPattern(input_number, length_of_output_pattern):
    array_of_intermediate_code = []

    def NumberToPatternHelp(number):
        if number < 4:
            array_of_intermediate_code.append(number)
            return 0
        remainder = number - 4*(number/4)
        number = number/4
        array_of_intermediate_code.append(remainder)
        NumberToPatternHelp(number)

    NumberToPatternHelp(input_number)
    if len(array_of_intermediate_code) < length_of_output_pattern:
        for i in range(length_of_output_pattern-len(array_of_intermediate_code)):
            array_of_intermediate_code.append(0)

    #reverse array_of_intermediate_code
    array_of_intermediate_code=array_of_intermediate_code[::-1]

    result_array = []
    for i in array_of_intermediate_code:
        if i == 0:
            result_array.append("A")
        if i == 1:
            result_array.append("C")
        if i == 2:
            result_array.append("G")
        if i == 3:
            result_array.append("T")
    return result_array


def MedianString(k, dna_list):
    distance = len(dna_list)*len(dna_list[0])
    for i in range(pow(4,k)-1):
        pattern = NumberToPattern(i, k)
        if distance > DistanceBetweenPatternAndStrings(pattern, dna_list):
            distance = DistanceBetweenPatternAndStrings(pattern,dna_list)
            median = pattern
    return median

with open('/home/alextr/dataset_158_9.txt') as input_data:
    k = int(input_data.readline())
    dna_list = [line.strip() for line in input_data.readlines()]

print ''.join(MedianString(k, dna_list))
