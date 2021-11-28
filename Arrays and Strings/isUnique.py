def isUnique(string):
    letters = {}
    for i in string:
        if i in letters:
            return False
        letters[i] = True
    return True

print(isUnique("qwmmerty"))