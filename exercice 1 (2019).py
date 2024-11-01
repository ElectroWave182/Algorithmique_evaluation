# 1) Solution naïve

def fixe_n (liste):

    trouve = False
    for ind in range (len (liste)):

        ele = liste[ind]
        if ele == ind - 1:
            trouve = True

    return trouve


# 2) Diviser pour régner

def fixe_dpr (liste):
    
    n = len (liste)
    if n == 1:
        return liste[0] == -1

    else:
        milieu = n // 2
        ele = liste[milieu]

        if ele == milieu - 1:
            return True

        elif ele > milieu - 1:
            return fixe_dpr (liste[: milieu])

        else:
            # L'on compense le décalage
            quartile = (n + milieu) // 2
            liste[quartile] -= milieu

            return fixe_dpr (liste[milieu :])


assert not fixe_n ([0])
assert not fixe_n ([8, 45, 256])
assert fixe_n ([-1])
assert fixe_n ([-845, -42, 1])

assert not fixe_dpr ([0])
assert not fixe_dpr ([8, 45, 256])
assert fixe_dpr ([-1])
assert fixe_dpr ([-845, -42, 1])
