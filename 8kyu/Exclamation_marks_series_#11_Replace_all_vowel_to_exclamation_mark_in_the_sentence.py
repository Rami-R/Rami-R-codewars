'''Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples
replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"'''
#My solution :
def replace_exclamation(st):
    rst=[]
    for i in st:
        if i in 'aeiouAEIOU':
            i = '!'
        rst.append(i)
    return "".join(rst)