import zlib

codes = [[1, 'z,'], [2, '8('], [3, '9C'], [4, '3W'], [5, 'J5'], [6, 'I"'], [7, '4['], [8, '-1'], [9, '+6'], ['a', 'e7'],
         ['b', '1z'], ['c', '2V'], ['d', 'v6'], ['e', 'Q4'], ['f', ':8'], ['g', '1I'], ['h', 'n2'], ['i', 'S4'],
         ['j', 'P_'], ['k', 'b*'], ['l', ' l'], ['m', '#R'], ['n', '3p'], ['o', "'2"], ['p', '^f'], ['q', 'r>'],
         ['r', '&d'], ['s', '4E'], ['t', '6!'], ['u', ']f'], ['v', '{5'], ['w', '8['], ['x', '%3'], ['y', 'u '],
         ['z', '7d'], ['A', '1M'], ['B', '_8'], ['C', 'w7'], ['D', 'g4'], ['E', 'i1'], ['F', '7%'], ['G', 'U*'],
         ['H', 't7'], ['I', '{9'], ['J', 'j\\'], ['K', '2:'], ['L', 'X;'], ['M', 'Q9'], ['N', "2'"], ['O', '[F'],
         ['P', 'M3'], ['Q', '8"'], ['R', '1;'], ['S', '(3'], ['T', 'p*'], ['U', '|E'], ['V', '5/'], ['W', 'O*'],
         ['X', '[3'], ['Y', '1p'], ['Z', '7e'], ['!', ']I'], ['@', '/f'], ['#', '/l'], ['$', '~8'], ['%', '+7'],
         ['^', 'b{'], ['&', '*5'], ['*', '.3'], ['(', 'P~'], [')', '*9'], [' ', '(k'], ['<', '{n'], ['>', "j'"],
         [':', 'W~'], ['"', 'K9'], ['{', '6c'], ['}', 'V9'], ['|', 'P<'], ['_', '1@'], ['+', '{A'], ['/', 'F4'],
         ['*', 'g2'], ['+', 'N1'], ['~', '1 '], [',', 'K/'], ['.', '=4'], [';', '2X'], ["'", 'o!'], ['[', 'a5'],
         [']', '4#'], ['\\', 'g7'], ['-', '>y'], ['=', 't*'], ['`', 'y5']]


def hashEncrypt(value):
    crypt = []
    for i in value:
        code = ''
        for c in codes:
            if i == c[0]:
                code = c[1]
        crypt.insert(0, code)
    s = ''
    s = s.join(crypt).encode()
    c = zlib.compress(s, 9)
    print(f'Compressed from length of {len(s)} to {len(c)}')
    return c


def hashDecrypt(value):
    value = zlib.decompress(value)
    value = value.decode()
    print(value)
    crypt = []
    for i in range(len(value) - 1, 0, -2):
        code = value[i - 1] + value[i]
        for c in codes:
            if code == c[1]:
                crypt.append(c[0])

    s = ''
    return s.join(crypt)


# he = hashEncrypt('This is encoded')
# he = hashEncrypt("Hello my name is mohamed")
encrypt = "Loreml ]\'[.,\.]/\.[\].,[\],[ipsum dolor sit amet, consectetur adipiscing elit. Morbi feugiat vestibulum sapien, non mollis nulla congue et. Morbi accumsan, odio eget semper dignissim, urna nisi pulvinar dui, sed porttitor nisl tortor quis leo. Sed venenatis tincidunt leo eu bibendum. Aliquam rutrum leo vitae urna aliquet, at iaculis urna commodo. Nunc sodales dapibus tincidunt. Donec tincidunt erat vel lectus ultricies, in ornare arcu vestibulum. Donec lacinia eros justo, ac fringilla est sagittis sed. Vivamus ultricies risus et aliquet aliquet."
# encrypt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
he = hashEncrypt(encrypt)
hd = hashDecrypt(he)
print(he)
print(hd)

