from operator import itemgetter

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


# BEGIN (write your solution here)
def to_roman(value):
    out = ''
    v = value
    out = ''
    for key, x in sorted(NUMERALS.items(), key=itemgetter(1), reverse=1):
        r = int(v / x)
        out += key * r
        v = v % x
    return out


def to_arabic(value):
    out = 0
    v = value
    p = ''
    while v:
        for key, x in sorted(NUMERALS.items(), key=itemgetter(1), reverse=1):
            if len(key) == 1 and not set(v).difference(set(key)) and len(v) > 3:
                return False
            if v.startswith(key):
                if p and x > NUMERALS[p]:
                    return False
                out += x
                v = v[len(key):]
                p = key
                break
            else:
                continue
    return out
# END

print('2549:%s' % to_roman(2549))
print('59:%s' % to_roman(59))
print('3000:%s' %to_roman(3000))
print('-----------')

print('MMM:%s' % to_arabic('MMM'))
print('LVIIII:%s' % to_arabic('LVIIII'))
print('LIX:%s'% to_arabic('LIX'))
print('MMDXXXXIX:%s' % to_arabic('MMDXXXXIX'))
print('MMDVVVVVVVVVIIII:%s' % to_arabic('MMDVVVVVVVVVIIII'))
print('4:%s' % to_arabic('IV'))
print('15:%s' % to_arabic('VX'))

def test_to_roman():
    assert to_roman(0) == ''
    assert to_roman(1) == 'I'
    assert to_roman(2) == 'II'
    assert to_roman(4) == 'IV'
    assert to_roman(5) == 'V'
    assert to_roman(6) == 'VI'
    assert to_roman(27) == 'XXVII'
    assert to_roman(48) == 'XLVIII'
    assert to_roman(59) == 'LIX'
    assert to_roman(93) == 'XCIII'
    assert to_roman(141) == 'CXLI'
    assert to_roman(163) == 'CLXIII'
    assert to_roman(402) == 'CDII'
    assert to_roman(575) == 'DLXXV'
    assert to_roman(911) == 'CMXI'
    assert to_roman(1024) == 'MXXIV'
    assert to_roman(2020) == 'MMXX'
    assert to_roman(3000) == 'MMM'


def test_to_arabic():
    assert to_arabic('') == 0
    assert to_arabic('I') == 1
    assert to_arabic('II') == 2
    assert to_arabic('IV') == 4
    assert to_arabic('V') == 5
    assert to_arabic('VI') == 6
    assert to_arabic('XXVII') == 27
    assert to_arabic('XLVIII') == 48
    assert to_arabic('LIX') == 59
    assert to_arabic('XCIII') == 93
    assert to_arabic('CXLI') == 141
    assert to_arabic('CLXIII') == 163
    assert to_arabic('CDII') == 402
    assert to_arabic('DLXXV') == 575
    assert to_arabic('CMXI') == 911
    assert to_arabic('MXXIV') == 1024
    assert to_arabic('MMXX') == 2020
    assert to_arabic('MMM') == 3000
    assert to_arabic('IIII') is False
    assert to_arabic('VX') is False
