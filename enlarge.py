# https://ru.hexlet.io/challenges/python_lists_enlarge_image_exercise
def show(image):
    for line in image:
        print(line)

def enlarge(arr):
    out = []
    for row in arr:
        line= ''
        for x in row:
            line+= x*(2)
            
        out.append(line)
        out.append(line)

    return out

image = [
    '***',
    '* *',
    '* *',
    '***',
]

show(image)
show(enlarge(image))
