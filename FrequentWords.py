def PatternCount(text, pattern):
    count=0
    lentext=len(text)
    lenpattern = len(pattern)
    for i in range(lentext - lenpattern+1):
        if text[i:i+lenpattern] == pattern:
            count += 1
    return count

#shows words in the text with the highest frequency
def FrequentWords(text, k):
    frequentpatt = []
    countarr = []
    for i in range(len(text)-k+1):
        pattern=text[i:i+k]
        countarr.append(PatternCount(text, pattern))
    maxcount = max(countarr)
    print countarr
    for i in range(len(text) - k+1):
        if countarr[i]==maxcount:
            frequentpatt.append(text[i:i+k])
    frequentpattunique=set(frequentpatt)
    return frequentpattunique

text = "atgaccgggatactgataaaaaaaagggggggggcgtacacattagataaacgtatgaagtacgttagactcggcgccgccgacccctattttttgagcagatttagtgacctggaaaaaaaatttgagtacaaaacttttccgaataaaaaaaaagggggggatgagtatccctgggatgacttaaaaaaaagggggggtgctctcccgatttttgaatatgtaggatcattcgccagggtccgagctgagaattggatgaaaaaaaagggggggtccacgcaatcgcgaaccaacgcggacccaaaggcaagaccgataaaggagatcccttttgcggtaatgtgccgggaggctggttacgtagggaagccctaacggacttaataaaaaaaagggggggcttataggtcaatcatgttcttgtgaatggatttaaaaaaaaggggggggaccgcttggcgcacccaaattcagtgtgggcgagcgcaacggttttggcccttgttagaggcccccgtaaaaaaaagggggggcaattatgagagagctaatctatcgcgtgcgtgttcataacttgagttaaaaaaaagggggggctggggcacatacaagaggagtcttccttatcagttaatgctgtatgacactatgtattggcccattggctaaaagcccaacttgacaaatggaagatagaatccttgcataaaaaaaagggggggaccgaaagggaagctggtgagcaacgacagattcttacgtgcattagctcgcttccggggatctaatagcacgaagcttaaaaaaaaggggggga"
print (" ".join(str(x) for x in FrequentWords(text, 15)))
