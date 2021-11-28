def isOneAway(string1, string2):
    l1 = len(string1)
    l2 = len(string2)
    if abs(l1 - l2) > 1:
        return False
    elif l1 == l2:
        diff = 0
        for i in range(l2):
            if string1[i] != string2[i]:
                diff += 1
                if diff > 1:
                    return False
    else:
        shift = 0 
        if l1 > l2:
            long, short = string1, string2 
        else:
            long, short = string2, string1
        for i in range(len(short)):
            if short[i] != long[i+shift]:
                if shift == 1:
                    return False
                if short[i] == long[i+1]:
                    shift = 1
    return True

print(isOneAway("pale","pae"))