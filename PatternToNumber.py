# PATTERN TO NUMBER (INSERT pattern)
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


print "Result:"
print PatternToNumber("AT")