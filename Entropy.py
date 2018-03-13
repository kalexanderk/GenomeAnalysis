import math


def entropy(motifs_matrix):
    sum_entropy=0
    t=len(motifs_matrix)
    print t
    for column in range(len(motifs_matrix[0])):
        n_A = 0
        n_C = 0
        n_T = 0
        n_G = 0
        for row in range(len(motifs_matrix)):
            if motifs_matrix[row][column] == "A":
                n_A += 1
            if motifs_matrix[row][column] == "C":
                n_C += 1
            if motifs_matrix[row][column] == "T":
                n_T += 1
            if motifs_matrix[row][column] == "G":
                n_G += 1
        n_A = n_A * 1.
        n_C = n_C * 1.
        n_G = n_G * 1.
        n_T = n_T * 1.
        print n_A, n_C, n_G, n_T
        print

        if n_A == 0:
            pl_A = 0
        else:
            pl_A = n_A/t*math.log(n_A/t, 2)

        if n_C == 0:
            pl_C=0
        else:
            pl_C = n_C/t*math.log(n_C/t, 2)

        if n_T == 0:
            pl_T=0
        else:
            pl_T = n_T/t*math.log(n_T/t,2)

        if n_G == 0:
            pl_G=0
        else:
            pl_G = n_G/t*math.log(n_G/t, 2)

        sum_entropy += pl_A + pl_C + pl_G + pl_T

    return -sum_entropy

motifs = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"
]
print entropy(motifs)



