def HammingDistance(p, q):
    if len(q) != len(p):
        return -1;
    else:
        result = 0
        for i in range(len(p)):
            if p[i] != q[i]:
                result += 1
        return result

p = "CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA"
q = "CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG"
print HammingDistance(p, q)