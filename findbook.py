# BEGIN (write your solution here)
def find_where(libs, book):
    if not book:
        return libs[0]
    found = 0
    for x in libs:
        for key in ('title', 'author', 'year'):
            if key not in book:
                continue
            if x.get(key) == book[key]:
                found = 1
            else:
                found = 0
                break
        if found:
            return x
    return None
# END

TITLE, AUTHOR, YEAR = 'title', 'author', 'year'
BOOKS = [
    {TITLE: 'Book of Fooos', AUTHOR: 'Foo', YEAR: 1111},
    {TITLE: 'Cymbeline', AUTHOR: 'Shakespeare', YEAR: 1611},
    {TITLE: 'The Tempest', AUTHOR: 'Shakespeare', YEAR: 1611},
    {TITLE: 'Book of Foos Barrrs', AUTHOR: 'FooBar', YEAR: 2222},
    {TITLE: 'Still foooing', AUTHOR: 'FooBar', YEAR: 333},
    {TITLE: 'Happy Foo', AUTHOR: 'FooBar', YEAR: 4444},
]

def test_find_where():
    assert find_where(BOOKS, {}) == BOOKS[0]

    assert find_where(BOOKS, {AUTHOR: 'Pushkin'}) is None

    assert find_where(BOOKS, {YEAR: 1111, AUTHOR: 'Pushkin'}) is None

    assert find_where(BOOKS, {"genre": None}) is None

    assert find_where(
        BOOKS, {YEAR: 1111},
    ) == {TITLE: 'Book of Fooos', AUTHOR: 'Foo', YEAR: 1111}

    assert find_where(
        BOOKS, {AUTHOR: 'Shakespeare', YEAR: 1611},
    )[TITLE] == 'Cymbeline'

    assert find_where(BOOKS, BOOKS[2]) == BOOKS[2]

test_find_where()
