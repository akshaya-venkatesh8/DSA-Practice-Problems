def isRotation(string1, string2):
    if len(string1) != len(string2): return False
    return is_substring(string1+string1, string2)

def is_substring(string1, string2):
    print(string1)
    for i in range(len(string1) - len(string2) + 1):
        is_substr = True
        for j in range(len(string2)):
            if string1[i+j] != string2[j]:
                is_substr = False
                break
        if is_substr:
            return True
    return is_substr

print(isRotation("aba", "aab"))
print(isRotation("aba", "aad"))