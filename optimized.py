# Solution optimale

def wallet_dynamique(budget, actions):

    matrice = [[0 for x in range(budget + 1)] for x in range(len(actions) + 1)]

    for i in range(1, len(actions) + 1):
        for w in range(1, budget + 1):
            if actions[i-1][1] <= w:
                matrice[i][w] = max(actions[i-1][2] + matrice[i-1][w-actions[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]


    w = budget
    n = len(actions)
    actions_selection = []

    while w >= 0 and n >= 0:
        e = actions[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            actions_selection.append(e)
            w -= e[1]

        n -= 1

    montant_depense = 0
    taux_cumul = 0

    for i in range(len(actions_selection)):
        montant_depense += actions_selection[i][1]
        taux_cumul += actions_selection[i][2]

    print("Budget dépensé : ", montant_depense, "€")
    print("nb d'actions : ",len(actions_selection))
    print("taux d'intrêt moyen",round(taux_cumul/len(actions_selection)), "%")

    return actions_selection




wallet = [('Action-1', 20, 5),
    ('Action-2', 30, 10),
    ('Action-3', 50, 15),
    ('Action-4', 70, 20),
    ('Action-5', 60, 17),
    ('Action-6', 80, 25),
    ('Action-7', 22, 7),
    ('Action-8', 26, 11),
    ('Action-9', 48, 13),
    ('Action-10', 34, 27),
    ('Action-11', 42, 17),
    ('Action-12', 110, 9),
    ('Action-13', 38, 23),
    ('Action-14', 14, 1),
    ('Action-15', 18, 3),
    ('Action-16', 8, 8),
    ('Action-17', 4, 12),
    ('Action-18',  10, 14),
    ('Action-19', 24, 21),
    ('Action-20',  114, 18)]

print('Liste des actions : ', wallet_dynamique(500, wallet))

