def compressString(string1):
    final = ''
    count = 1
    for i in range(1, len(string1)):
        if string1[i-1] != string1[i]:
            final += string1[i-1]+ str(count)
            count = 1
        else:
            count += 1
    final = final+string1[i-1]+str(count)
    return final if len(final) < len(string1) else string1

print(compressString("aabb"))