def entasser(liste, n, i):
    i_max = i
    i_fg = 2 * i + 1
    i_fd = 2 * i + 2

    if i_fg < n and liste[i_fg] > liste[i_max]:
        i_max = i_fg

    if i_fd < n and liste[i_fd] > liste[i_max]:
        i_max = i_fd

    if i_max != i:
        liste[i], liste[i_max] = liste[i_max], liste[i]
        entasser(liste, n, i_max)


def construire_tas(liste):
    liste = liste[:]
    n = len(liste)
    for i in range(n // 2 - 1, -1, -1):
        entasser(liste, n, i)
    
    return liste

def tri_tsa(liste):
    n = len(liste)
    liste_2 = liste[:]
    result = []

    for i in range(n - 1, -1, -1):
        result.append(liste_2[0])
        liste_2[0] = liste_2[i]
        liste_2.pop()
        if liste_2:
            entasser(liste_2, len(liste_2), 0)

    return result


arbre = [10, 22, 5, 18, 20, 25, 40, 30, 35, 12]

print("Arbre original:", arbre)
tas = construire_tas(arbre)
print("TASmax:", tas)
sorted_list = tri_tsa(tas)
print("Tri par TAS:", sorted_list)

