from random import *

chars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
         'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '!', '@', '#', '$', '%', '^', '&', '*',
         '(', ')', '<', '>', ':', '\"', '{', '}', '|', '_', '+', '/', '*', '+', '~', ',', '.', ';', '\'', '[', ']',
         '\\', '-', '=', '`']

codes = []
nums = chars[0:9]
strs = chars[9:61] # The space or ' ' is left out at chars[62] as if the strip function is used on the string it at last charcheter it wont decode
spcl = chars[62:94]  # The space or ''  and dot or '.' and comma or ',' are part of this


def getCode():
    randNum = randint(0, len(nums) - 1)
    randStrs = randint(0, len(strs) - 1)
    randSpcl = randint(0, len(spcl) - 1)
    rands = [str(nums[randNum]), str(strs[randStrs]), str(spcl[randSpcl])]
    code = sample(rands, 2)
    shuffle(code)
    return code


def main():
    for c in chars:
        code = getCode()
        runLoop = False
        for i in codes:
            if code[0] + code[1] == i[1]:
                runLoop = True
        while runLoop:
            code = getCode()
            for i in codes:
                if code[0] + code[1] == i[1]:
                    runLoop = True
                else:
                    runLoop = False
        code = code[0] + code[1]
        codes.append([c, code])


main()
#
for a in codes:
    print(str(a))

print(codes)
