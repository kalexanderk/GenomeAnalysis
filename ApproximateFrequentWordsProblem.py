def HammingDistance(p, q):
    if len(q) != len(p):
        return -1;
    else:
        result = 0
        for i in range(len(p)):
            if p[i] != q[i]:
                result += 1
        return result

def ApproximatePatternCount(text, pattern, d):
    count=0
    lentext=len(text)
    lenpattern = len(pattern)
    for i in range(lentext - lenpattern+1):
        if HammingDistance(text[i:i+lenpattern], pattern) <= d:
            count += 1
    return count

#shows words in the text with the highest frequency
def ApproximateFrequentWords(text, k, d):
    frequentpatt = []
    countarr = []
    for i in range(len(text)-k+1):
        pattern=text[i:i+k]
        countarr.append(ApproximatePatternCount(text, pattern, d))
    maxcount = max(countarr)
    print countarr
    print maxcount
    for i in range(len(text) - k +1):
        if countarr[i] == maxcount:
            frequentpatt.append(text[i:i+k])
    frequentpattunique=set(frequentpatt)
    return frequentpattunique

d = 0
k = 2
text = "ATT"
data = ApproximateFrequentWords(text, k, d)
print(" ".join(str(x) for x in data))