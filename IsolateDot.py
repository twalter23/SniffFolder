
def check(string, char):

    if char in string:
        result=True
    else:
        result=False
    return result


# Driver Code
s = "Folder.txt"
char = '.'
print(check(s, char))