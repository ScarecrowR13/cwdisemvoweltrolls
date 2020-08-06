def disemvowel(string):
    z = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for i in string:
        if i in z:
            string = string.replace(i, "")
    return(string)
