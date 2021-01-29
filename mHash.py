import zlib

codes = [[1, '5\\'], [2, '1+'], [3, 'C*'], [4, ')6'], [5, '\\8'], [6, '+q'], [7, '<9'], [8, '5,'], [9, '3#'],
         ['a', ')5'], ['b', 'G$'], ['c', '9;'], ['d', '6;'], ['e', '+9'], ['f', '<H'], ['g', '7Z'], ['h', 'c4'],
         ['i', '9I'], ['j', '2z'], ['k', 'm('], ['l', 'Y9'], ['m', '4V'], ['n', '1~'], ['o', 'n3'], ['p', '>6'],
         ['q', 'e2'], ['r', '7&'], ['s', '>5'], ['t', '2x'], ['u', '7a'], ['v', '1z'], ['w', '1y'], ['x', '1<'],
         ['y', 'G,'], ['z', '<7'], ['A', '#4'], ['B', 'X('], ['C', '.1'], ['D', '"4'], ['E', 'J2'], ['F', 'c&'],
         ['G', '9C'], ['H', ')g'], ['I', 'Q2'], ['J', 'P}'], ['K', 'S"'], ['L', 'I&'], ['M', '4='], ['N', '\\5'],
         ['O', '(2'], ['P', "'X"], ['Q', 'g,'], ['R', '2o'], ['S', 'i8'], ['T', '%6'], ['U', 'M5'], ['V', "2'"],
         ['W', '}5'], ['X', '*2'], ['Y', 'r~'], ['Z', ')4'], [' ', 'W8'], ['!', '9!'], ['@', '6:'], ['#', 'I~'],
         ['$', 'l3'], ['%', '%5'], ['^', '_7'], ['&', 'B5'], ['*', '2S'], ['(', 'K]'], [')', 'k6'], ['<', '2$'],
         ['>', 'T.'], [':', '*6'], ['"', '_O'], ['{', '8V'], ['}', '_4'], ['|', '7+'], ['_', '=9'], ['+', ',9'],
         ['/', 'K5'], ['*', 'E9'], ['+', 'v3'], ['~', '5I'], [',', 's|'], ['.', 'P6'], [';', 'j!'], ["'", 'G<'],
         ['[', '*o'], [']', '@D'], ['\\', 'o7'], ['-', '<M'], ['=', '3t'], ['`', '8*']]


def hashEncrypt(value):
    crypt = []
    for i in value:
        code = ''
        for c in codes:
            if i == c[0]:
                code = c[1]
        crypt.insert(0, code)
    s = ''
    s = s.join(crypt)
    # s = zlib.compress(s, 9)

    return s


def hashDecrypt(value):
    # value = zlib.decompress(value, 9)
    # print(value)
    crypt = []
    # print(len(value))
    for i in range(len(value) - 1, 0, -2):
        code = value[i - 1] + value[i]
        for c in codes:
            if code == c[1]:
                crypt.append(c[0])

    s = ''
    return s.join(crypt)

# encrypt = "Loreml ]\'[.,\.]/\.[\].,[\],[ipsum dolor sit amet, consectetur adipiscing elit. Morbi feugiat vestibulum sapien, non mollis nulla congue et. Morbi accumsan, odio eget semper dignissim, urna nisi pulvinar dui, sed porttitor nisl tortor quis leo. Sed venenatis tincidunt leo eu bibendum. Aliquam rutrum leo vitae urna aliquet, at iaculis urna commodo. Nunc sodales dapibus tincidunt. Donec tincidunt erat vel lectus ultricies, in ornare arcu vestibulum. Donec lacinia eros justo, ac fringilla est sagittis sed. Vivamus ultricies risus et aliquet aliquet."

# he = hashEncrypt(encrypt)
# he = b"1I3pS4n26!Q4#R'2(3"
# hd = hashDecrypt(he)
# print(hd)
