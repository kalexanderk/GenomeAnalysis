def SkewDiagram(text):
    skew = []
    skew.append(0)
    count = 0
    for i in text:
        if i == "G":
            skew.append(skew[count] + 1)
        elif i == "C":
            skew.append(skew[count] - 1)
        else:
            skew.append(skew[count])
        count += 1
    return skew

text = "GAGCCACCGCGATA"
data = SkewDiagram(text)
print(" ".join(str(x) for x in data))