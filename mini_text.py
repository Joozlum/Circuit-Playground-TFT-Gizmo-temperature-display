"""
Mini CHAR

This module creates the labels for displaying CHAR on the TFT Gizmo
using as small of a font as possible.
"""


CHAR = {
    '0': [1, 0, 1, 1, 1, 1, 1, 0, 0],
    '1': [0, 0, 0, 0, 1, 0, 1, 0, 0],
    '2': [1, 1, 1, 0, 1, 1, 0, 0, 0],
    '3': [1, 1, 1, 0, 1, 0, 1, 0, 0],
    '4': [0, 1, 0, 1, 1, 0, 1, 0, 0],
    '5': [1, 1, 1, 1, 0, 0, 1, 0, 0],
    '6': [1, 1, 1, 1, 0, 1, 1, 0, 0],
    '7': [1, 0, 0, 0, 1, 0, 1, 0, 0],
    '8': [1, 1, 1, 1, 1, 1, 1, 0, 0],
    '9': [1, 1, 0, 1, 1, 0, 1, 0, 0],
    '.': [0, 0, 0, 0, 0, 0, 0, 0, 1],
    '-': [0, 1, 0, 0, 0, 0, 0, 0, 0],
    'm': [[1, 0, 0, 1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0, 1, 0, 0]],
    'i': [[1, 0, 1, 0, 1, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 0]],
    'n': [[1, 0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 1, 0, 1, 0, 1, 0, 0]]

    }

line_drawer = [
    lambda x,y: ((x+1, y), (x+2, y), (x+3, y)),
    lambda x,y: ((x+1, y+4), (x+2, y+4), (x+3, y+4)),
    lambda x,y: ((x+1, y+8), (x+2, y+8), (x+3, y+8)),
    lambda x,y: ((x, y+1), (x, y+2), (x, y+3)),
    lambda x,y: ((x+4, y+1), (x+4, y+2), (x+4, y+3)),
    lambda x,y: ((x, y+5), (x, y+6), (x, y+7)),
    lambda x,y: ((x+4, y+5), (x+4, y+6), (x+4, y+7)),
    lambda x,y: ((x+2, y+2),),
    lambda x,y: ((x+2, y+6),)
    ]

def ctb(num, text='', start_x=0, start_y=0, _round=2):
    if type(num) == 'int':
        num = str(num)
    else:
        num = str(round(num, _round))

    p_on = []
    _x, _y = start_x, start_y
    for d in num:
        for _i, c in enumerate(CHAR[d]):
            if c:
                p_on.extend(line_drawer[_i](_x, _y))
        _x +=6

    if text:
        _x += 8
        for d in text:
            for part in CHAR[d]:
                for _i, c in enumerate(part):
                    if c:
                        p_on.extend(line_drawer[_i](_x, _y))
                _x += 4
            _x += 3
    return p_on, (_x-2, _y+8)


if __name__ == '__main__':
    from random import uniform

    for n in range(10):
        _n = n
        print(f'{_n}')
        print(f'{ctb(_n)}')
    for n in range(2):
        _n = uniform(0, 10)
        test_p, test_s = ctb(_n, 'min')
        print(f'{_n}')
        print(test_p)
        print(test_s)


