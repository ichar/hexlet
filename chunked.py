def chunked(n, data):
    chunks = []
    rows = [x for x in data]
    while rows:
        chunk = []
        for i in range(0, n):
            if rows:
                chunk.append(rows.pop(0))
        if isinstance(data, str):
            chunks.append(''.join(chunk))
        elif isinstance(data, tuple):
            chunks.append(tuple(chunk))
        else:
            chunks.append(chunk)

    return chunks

print(chunked(2, [1,2,3,4,5]))
print(chunked(2, (1,2,3,4,5)))
print(chunked(3, '12345678901234567890'))
