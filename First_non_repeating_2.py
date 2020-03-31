# First non repeating Character
def count_character(string):
    dic = {}
    for i in string:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] = dic[i]+1
    return dic

def first_non_repeating(string,dic):
    for i in range(0,len(string)):
        if dic[string[i]] == 1:
            return i

a = "sayan"
print(a[first_non_repeating(a,count_character(a))])
