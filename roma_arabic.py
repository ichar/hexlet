from operator import itemgetter

roman = {
'I': 1,
'V': 5,
'X': 10,
'L': 50,
'C': 100,
'D': 500,
'M': 1000
}
NUMERALS = {  # noqa: WPS407
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}


def to_roman(value):
    #I=1, V=5, X=10, L=50, C=100, D=500 M=1000
    out  = ''
    v= value
    for key,x in sorted(NUMERALS.items(),key=itemgetter(1),reverse=1):
        if v.startswith(key):
            r= int(v/x)
            out += key*r
            v = v%x
    return out


def to_arabic(value):
    if not value:
        return 0
    out = 0
    for key in value:
        if key == 'I' and p not in 'VXI':
            out-=roman.get(key,1)
        else:
            out+=roman.get(key,1)
        p = key
    return out
        


print(to_roman(2549))
print(to_roman(59))
print(to_roman(3000))
print('-----------')
print('MMM:%s' % to_arabic('MMM'))
print('LVIIII:%s' % to_arabic('LVIIII'))
print('LIX:%s'% to_arabic('LIX'))
print('MMDXXXXIX:%s' % to_arabic('MMDXXXXIX'))
print('MMDVVVVVVVVVIIII:%s' % to_arabic('MMDVVVVVVVVVIIII'))
