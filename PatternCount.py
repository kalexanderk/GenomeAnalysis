#counts number of patterns in the text
def PatternCount(text, pattern):
    count=0
    lentext=len(text)
    lenpattern = len(pattern)
    for i in range(lentext - lenpattern):
        if text[i:i+lenpattern] == pattern:
            count += 1
    return count

print PatternCount("GGACCTCAGGACAGGACCGAGCGGACCTTTCCGGACCTTTCGGACCTTAGGAGACCTTTGGACCTT", "GGA")