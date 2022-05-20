def normalize_url(url):
    s = '://'
    if url:
        if s in url and url:
            x=url.split(s)
            p, a = '-', url
            if len(x)==2 and len(x[0]) < 6:
                 p,a =x[0],x[1]
            elif len(x)>2:
                 a=s.join(x[1:])

            return '%s%s%s' %(p in ('http', 'https', '-') and 'https' or p, s, a)
        else:
            return 'https%s%s' % (s, url)
    return url

urls= ('http://ya.ru',
       'yandex.ru',
       'http://yandex.ru',
       'google.com',
       'http://google.com',
       'ai.fi',
       'ftp://xx.com',
       'https://httpsecurity.com',
       'httpsecurity.com',
       'https://httpbin.org/redirect-to?url=http://google.com',
       'httpbin.org/redirect-to?url=https://google.com',
       'https://httpbin.org/redirect-to?url=http://google.com'
)


for n,url in enumerate(urls):
    print('--> %s:%s' % (n,normalize_url(url)))

def test():
    assert normalize_url('yandex.ru') == 'https://yandex.ru'
    assert normalize_url('http://yandex.ru') == 'https://yandex.ru'
    assert normalize_url('https://yandex.ru') == 'https://yandex.ru'
    assert normalize_url('httpsecurity.com') == 'https://httpsecurity.com'
    assert normalize_url('https://httpbin.org/redirect-to?url=http://google.com') == 'https://httpbin.org/redirect-to?url=http://google.com'

test()
