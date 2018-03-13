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

d = 1
pattern = "AA"
text = "TACGCATTACAAAGCACA"
print ApproximatePatternCount(text, pattern, d)