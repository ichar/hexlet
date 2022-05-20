def filter_string(text, smb):
    out = ''
    exclude =(smb,smb.lower(),smb.upper())
    print(exclude)
    for s in text:
        if s not in exclude:
            out += s

    #print('==>', out)
    return out.strip()

def test():
    text = 'I look back if you are lost'
    assert filter_string(text, 'w') == 'I look back if you are lost'
    assert filter_string(text, 'I') == 'look back f you are lost'


test()
