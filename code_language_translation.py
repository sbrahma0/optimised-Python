'''
Minion language translation
lower case = 97 - 110 - 122
'''

def solution(x):
    result = ''
    for i in x:
        if ord(i) >= 97 and ord(i) < 110:
            result = result + chr(122-(ord(i)-97))
        elif ord(i) >= 110 and ord(i) <= 122:
            result = result + chr(97+(122-ord(i)))
        else:
            result = result + i
    return result

  # Driver
string = "?"
r = solution(string)
print(r)
