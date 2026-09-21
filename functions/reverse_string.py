def reverse(string1):
    string2 = ""

    index = len(string1)

    while index > 0:
        string2 += string1[index - 1]
        index = index - 1
    return string2

print(reverse("1234abcd"))