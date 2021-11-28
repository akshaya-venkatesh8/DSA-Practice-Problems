def getUrlSpacing1(string):
    return string.strip().replace(" ", "%20")

def getUrlSpacing2(string):
    letters = list(string)
    final = ''
    l = len(letters) - 1
    i = 0
    while letters[l] == " ":
        l -= 1
    while i <= l:
        if letters[i] == ' ':
            final += '%20'
        else:
            final += letters[i]
        i+=1
    return final

print(getUrlSpacing1("Mr J Smith "))
print(getUrlSpacing2("Mr J Smith "))