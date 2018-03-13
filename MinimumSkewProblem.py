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
    print skew
    return skew

def MinimumSkewProblem(text):
    skew_array = SkewDiagram(text)
    min_value = max(skew_array)
    result = []
    count = 0
    for i in skew_array:
        if i == min_value:
            result.append(count)
        count += 1
    return result

text = "GCATACACTTCCCAGTAGGTACTG"
data = MinimumSkewProblem(text)
print(" ".join(str(x) for x in data))