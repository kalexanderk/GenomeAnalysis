chars = "ACGT"
def neighbors(pattern, d):
    assert(d <= len(pattern))
    if d == 0:
        return [pattern]
    r2 = neighbors(pattern[1:], d-1)
    r = [c + r3 for r3 in r2 for c in chars if c != pattern[0]]
    if (d < len(pattern)):
        r2 = neighbors(pattern[1:], d)
        r += [pattern[0] + r3 for r3 in r2]
    return r

text = "CCA"
d = 1
res = neighbors(text, d)
for i in res:
    if i == text:
        print "yes"
res.append(text)
print ("\n".join(str(x) for x in res))
print len(res)

