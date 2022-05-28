
def hamming_weight(num):
    out = 0
    for x in bin(num):
        if x != '1':
            continue
        out += 1
    return out


#print(hamming_weight(101))
