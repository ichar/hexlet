# BEGIN (write your solution here)
trans = {
    'dna': 'GCTA',
    'rna': 'CGAU'
}


def to_rna(data):
    return ''.join([trans['rna'][trans['dna'].index(x.upper())] for x in data])
# END

assert to_rna("ACGTGGTCTTAA") == 'UGCACCAGAAUU' 

print(to_rna("ACGTGGTCTTAA"))
