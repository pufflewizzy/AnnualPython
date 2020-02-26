# homework
def removeSpace(s):
    return s.replace(" ", "")

def capitalize(s):
    build = ""
    space = True
    for i in range(len(s)):
        if space:
            build += s[i].upper()
            space = False
        elif s[i] == " ":
            build += " "
            space = True
        else:
            build += s[i]

    return build

# challenge
def switch(s):
    build = ""
    for i in range(len(s)):
        if s[i].isupper():
            build += s[i].lower()
        else:
            build += s[i].upper()

    return build
