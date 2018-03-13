def SymbolToNumber(symbol):
    if symbol == "A":
        return 0
    if symbol == "C":
        return 1
    if symbol == "G":
        return 2
    if symbol == "T":
        return 3

def PatternToNumber(pattern):
    if pattern=="":
        return 0
    symbol=pattern[len(pattern)-1]
    prefix=pattern[0:len(pattern)-1]
    return 4*PatternToNumber(prefix) + SymbolToNumber(symbol)

def ComputingFrequencies(text, k):
    frequencyarray = []
    for i in range(pow(4, k)):
        frequencyarray.append(0)
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        j = PatternToNumber(pattern)
        frequencyarray[j] += 1
    return frequencyarray

k=7
text = "GAATGGGTCACGGTGCTTTATTTCACGTTATAGCCCTAAGGGCCGAGACTCTCAGCTGGTGACGCTACGGCGCAACCATTTGCAGGCCTTGCGGATATCGCACGGTGTTTACCTGGACTGCAGCCGAACGTCGTCGTCCCGGGAAGGACGCGTCAATTAGTTGGAATCCAAATGGGATTAAACGAGCGAGGCTAAGCAATCGGTGCAGCAAGAAGTTTACCACAGCCATACATCGGCCGACCGTAGAGAGGTCAAAAAGAGCGAGTATGTTGGTCGTCACTACCTAATATATACGTTGATTACCCTCTACGTGCACCCGACCGAAACGGACCTCGTTTACATCCTCGTGGTGTTTGGGATCTTTCACTGACGGCGCTTAGACGCGGACGGCGACTTCTGTTCCGCCGGGTTTGGGAAGTACATTGTTTAGCGGATGCCATAGTGCAGACACTTTTACTTTCCACCACATTCTTTGTGGTTTCATACGGCCCTTTCTGGCATCCCACGTGACATTAGCACATGTGCGTTAGACCTGGTGATATTAAGATCGCGGCTTTCAAAGCGTCCGCAAATTTGATGATGCGACGTCCCGGTCCAAAGAAACCCCGTGATACTATGTGCCGGTGTGGAGCCATTATTCTTCGCCATTACAGGTTAAACACGATCTTTCCCTGGCTCCGAGGTAGGATCGAGAGAGTCAAGACTAGTGGGCTTGTAAACATCAGGTATTCAAAAGACGCAGCAACCCCTAATGCTTTCTGGACGCACCTAAGTTCCAGCCCAATTCTACCCGAG"
data = ComputingFrequencies(text, k)
print (" ".join(str(x) for x in data))