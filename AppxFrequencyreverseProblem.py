from collections import defaultdict
from itertools import combinations, product, izip

def rev_comp(pattern):
    patternrc = []
    for i in range(len(pattern)):
        if pattern[i] == "A":
            patternrc.append("T")
        if pattern[i] == "T":
            patternrc.append("A")
        if pattern[i] == "G":
            patternrc.append("C")
        if pattern[i] == "C":
            patternrc.append("G")
    patternrc = patternrc[::-1]
    return ''.join(patternrc)

def kmer_mismatches(kmer, d):
    mismatches = [kmer]  # Initialize mismatches with the k-mer itself (i.e. d=0).
    alt_bases = {'A':'CGT', 'C':'AGT', 'G':'ACT', 'T':'ACG'}
    for dist in xrange(1, d+1):
        for change_indices in combinations(xrange(len(kmer)), dist):
            for substitutions in product(*[alt_bases[kmer[i]] for i in change_indices]):
                new_mistmatch = list(kmer)
                for idx, sub in izip(change_indices, substitutions):
                    new_mistmatch[idx] = sub
                mismatches.append(''.join(new_mistmatch))
    return mismatches

def freq_words_with_mm_and_rev_comp(seq, k, d):
    # Frequency analysis so we don't generate mismatches for the same k-mer more than once.
    kmer_freq = defaultdict(int)
    for i in xrange(len(seq)-k+1):
        kmer_freq[seq[i:i+k]] += 1
        kmer_freq[rev_comp(seq[i:i+k])] += 1

    # Get all of the mismatches for each unique k-mer in the sequence, appearing freq times.
    mismatch_count = defaultdict(int)
    for kmer, freq in kmer_freq.iteritems():
        for mismatch in kmer_mismatches(kmer, d):
            mismatch_count[mismatch] += freq

    # Computing the maximum value is somewhat time consuming to repeat, so only do it once!
    max_count = max(mismatch_count.values())
    return sorted([kmer for kmer, count in mismatch_count.iteritems() if count == max_count])

text = "TGAGTTGACTGATGATGATCAAATGAGTTAAAGTTTCGTTTGATGAAAAGTTTCTCAAAAAATGAAAATGATGATGATGATGATGAGACTGATCAAAGACGACAAAAAAGTTAAAGACGTTTCGACGACGTTGTTTGAGACTCGACGACAAAAAATGATGATGAGACGACTGAGTTAAATCAAAGTTGTTGTTTCGACGACGTTGACGTTTGAGACAAAAAATGAAAAGACGTTGAC"
k = 6
d = 3
most_freq_kmers = freq_words_with_mm_and_rev_comp(text, k, d)
print ' '.join(most_freq_kmers)
