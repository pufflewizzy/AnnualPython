# homework
def totalDuration(h1, m1, s1, h2, m2, s2):
    s3 = (s1 + s2) % 60
    m3 = (m1 + m2 + (int((s1 + s2) / 60))) % 60
    h3 = (h1 + h2 + int((m1 + m2 + (int((s1 + s2) / 60))) / 60)) % 60
    return str(h3) + ":" + str(m3) + ":" + str(s3)

# challenge
def totalDurationChallenge(h1, m1, s1, h2, m2, s2):
    un = totalDuration(h1, m1, s1, h2, m2, s2).split(":")
    if int(un[0]) < 10:
        un[0] = "0" + un[0]
    if int(un[1]) < 10:
        un[1] = "0" + un[1]
    if int(un[2]) < 10:
        un[2] = "0" + un[2]

    return un[0] + ":" + un[1] + ":" + un[2]
