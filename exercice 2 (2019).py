# 1)

def estCroissant (liste):

    prec = liste[0]
    drap = True

    # while
    for ele in liste:
        drap = drap and prec[1] <= ele[1]
        prec = ele

    return drap


# 2)

# renvoie un booléen vrai si les 2 activités sont compatibles
def activites_compatibles (t1, t2):

    assert len(t1)==len(t2)==3 and 0<=t1[0]<t1[1]<=23 and 0<=t2[0]<t2[1]<=23 ,"pb activité "
    return t1[1]<=t2[0] or t2[1]<=t1[0]


def planifGlouton (liste):

    # Precondition
    assert estCroissant (liste), "La liste n'est pas triee"

    solution = [liste[0]]
    for activite in liste:

        if activites_compatibles (solution[-1], activite):
            solution.append (activite)

    return solution


# 3)

def planifExh3 (liste):

    n = len (liste)
    solution = []

    for ind_a in range (n):
        for ind_b in range (ind_a + 1, n):
            for ind_c in range (ind_b + 1, n):

                activite_a = liste[ind_a]
                activite_b = liste[ind_b]
                activite_c = liste[ind_c]

                valide = activites_compatibles (activite_a, activite_b)
                valide = valide and activites_compatibles (activite_a, activite_c)
                valide = valide and activites_compatibles (activite_b, activite_c)

                if valide:
                    solution.append ([activite_a, activite_b, activite_c])

    return solution


# 4)

def planifBack (liste):

    n = len (liste)
    aux = [False] * 24
    placer (liste, aux)


def placer (liste, aux):

    if est_sol (liste, aux):
        aux.append ([liste, aux])

    activite = liste[0]
    possible = True

    for heure in range (activite[0], activite[1]):
        # ajout possible
        if not aux[heure]:
            aux[heure] = True
        
        else:
            possible = False

    if possible:
        placer (liste[1 :], aux[:])

    aux = [False] * 24


def est_sol (liste, aux):

    return True


# Tests

if __name__ == '__main__':

    # exemple 1

    L_t = [(10,12,"belote"),(11,12,"ping pong"),(12,14,"gym douce"),(15,16,"aikido")]
    assert estCroissant (L_t)

    # une solution gloutonne
    L_g = [(10, 12, 'belote'), (12, 14, 'gym douce'), (15, 16, 'aikido')]
    assert planifGlouton (L_t) == L_g

    # les solutions exhaustives de longueur 3 
    L_exch3 = [
        [(10, 12, 'belote'), (12, 14, 'gym douce'), (15, 16, 'aikido')],
        [(11, 12, 'ping pong'), (12, 14, 'gym douce'), (15, 16, 'aikido')]
    ]
    assert planifExh3 (L_t) == L_exch3

    # les solutions optimales
    L_back = [
        [(10, 12, 'belote'), (12, 14, 'gym douce'), (15, 16, 'aikido')],
        [(11, 12, 'ping pong'), (12, 14, 'gym douce'), (15, 16, 'aikido')]
    ]
    assert planifBack (L_t) == L_back

    # exemple 2

    L_t = [(9,10,"bridge"),(8,10,"cirque"),(10,12,"gym"),(11,13,"bridge"),(13,14,"judo"),(16,20,"boxe")]
    assert estCroissant (L_t)

    # une solution_gloutonne
    Lg_1 = [(9, 10, 'bridge'),(10, 12, 'gym'),(13, 14, 'judo'),(16, 20, 'boxe')]

    #les solutions exhaustives de longueur 3 
    L_exh3 = [
        [(8, 10, 'cirque'), (10, 12, 'gym'), (13, 14, 'judo')],
        [(8, 10, 'cirque'), (10, 12, 'gym'), (16, 20, 'boxe')],
        [(8, 10, 'cirque'), (11, 13, 'bridge'), (13, 14, 'judo')],
        [(8, 10, 'cirque'), (11, 13, 'bridge'), (16, 20, 'boxe')],
        [(8, 10, 'cirque'), (13, 14, 'judo'), (16, 20, 'boxe')],
        [(9, 10, 'bridge'), (10, 12, 'gym'), (13, 14, 'judo')],
        [(9, 10, 'bridge'), (10, 12, 'gym'), (16, 20, 'boxe')],
        [(9, 10, 'bridge'), (11, 13, 'bridge'), (13, 14, 'judo')],
        [(9, 10, 'bridge'), (11, 13, 'bridge'), (16, 20, 'boxe')],
        [(9, 10, 'bridge'), (13, 14, 'judo'), (16, 20, 'boxe')],
        [(10, 12, 'gym'), (13, 14, 'judo'), (16, 20, 'boxe')],
        [(11, 13, 'bridge'), (13, 14, 'judo'), (16, 20, 'boxe')]
    ]

    # les solutions optimales
    L_back = [
        [(9, 10, 'bridge'),(10, 12, 'gym'),(13, 14, 'judo'),(16, 20, 'boxe')],
        [(9, 10, 'bridge'),(11, 13, 'bridge'),(13, 14, 'judo'),(16, 20, 'boxe')], 
        [(8, 10, 'cirque'),(10, 12, 'gym'),(13, 14, 'judo'),(16, 20, 'boxe')], 
        [(8, 10, 'cirque'),(11, 13, 'bridge'),(13, 14, 'judo'),(16, 20, 'boxe')]
    ]
