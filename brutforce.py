import itertools

actions = [
    {'ref': 'Action-1', 'coût': 20, 'benefice': 5},
    {'ref': 'Action-2', 'coût': 30, 'benefice': 10},
    {'ref': 'Action-3', 'coût': 50, 'benefice': 15},
    {'ref': 'Action-4', 'coût': 70, 'benefice': 20},
    {'ref': 'Action-5', 'coût': 60, 'benefice': 17},
    {'ref': 'Action-6', 'coût': 80, 'benefice': 25},
    {'ref': 'Action-7', 'coût': 22, 'benefice': 7},
    {'ref': 'Action-8', 'coût': 26, 'benefice': 11},
    {'ref': 'Action-9', 'coût': 48, 'benefice': 13},
    {'ref': 'Action-10', 'coût': 34, 'benefice': 27},
    {'ref': 'Action-11', 'coût': 42, 'benefice': 17},
    {'ref': 'Action-12', 'coût': 110, 'benefice': 9},
    {'ref': 'Action-13', 'coût': 38, 'benefice': 23},
    {'ref': 'Action-14', 'coût': 14, 'benefice': 1},
    {'ref': 'Action-15', 'coût': 18, 'benefice': 3},
    {'ref': 'Action-16', 'coût': 8, 'benefice': 8},
    {'ref': 'Action-17', 'coût': 4, 'benefice': 12},
    {'ref': 'Action-18', 'coût': 10, 'benefice': 14},
    {'ref': 'Action-19', 'coût': 24, 'benefice': 21},
    {'ref': 'Action-20', 'coût': 114, 'benefice': 18}
]

max_gain = 0
best_combination = None
taille = 0
depense = 0
taux_cumul = 0

for taille in range(2, len(actions) + 1):

    for combination in itertools.combinations(actions, taille):
        total_gain = 0
        total_price = 0

        for element in combination:
            total_price += element['coût']
            total_gain += element['coût'] * element["benefice"] / 100

        if (total_price <= 500 and total_gain > max_gain):
            max_gain = total_gain
            best_combination = combination

for i in range(len(best_combination)):
    depense += best_combination[i]['coût']
    taux_cumul += best_combination[i]['benefice']

taux_moyen = round(taux_cumul / len(best_combination))

print("Montant dépensé :", depense, "€")
print("Nb d'actions : ", len(best_combination))
print("taux d'intérêt moyen :", round(taux_cumul / len(best_combination)), "%")
print("Gains :", taux_moyen)

for i in range(len(best_combination)):
    print(best_combination[i]['ref'])

