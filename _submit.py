# homework
def window(str, sub):
    ans = str
    contains = True
    for i in range(len(str)):
        for a in range(i + 1, len(str) + 1):
            holder = str[i:a]

            for k in sub:
                if holder.count(k) == 0:
                    contains = False

            if contains and len(holder) < len(ans):
                ans = holder

            contains = True

    return ans

# challenge
def convert(n):
    return n, str(bin(n))[2:], str(oct(n))[2:], str(hex(n))[2:]
