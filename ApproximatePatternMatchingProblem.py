def HammingDistance(p, q):
    if len(q) != len(p):
        return -1;
    else:
        result = 0
        for i in range(len(p)):
            if p[i] != q[i]:
                result += 1
        return result

def ApproximateMatching(d, pattern, text):
    positions = []
    lentext = len(text)
    lenpattern = len(pattern)
    for i in range(lentext - lenpattern + 1):
        if HammingDistance(text[i:i + lenpattern], pattern) <= d:
            positions.append(i)
    return positions

d = 2
pattern = "AAAAA"
text = "AACAAGCTGATAAACATTTAAAGAG"
data = ApproximateMatching(d, pattern, text)
print(" ".join(str(x) for x in data))

