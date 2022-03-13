import itertools

# importation du package itertools permettant de générer toutes les combinaisons
# création d'un liste avec les actions et leurs taux d'intérêts

actions = [
    {'ref': 'Action-1', 'coût': 20, 'taux': 5},
    {'ref': 'Action-2', 'coût': 30, 'taux': 10},
    {'ref': 'Action-3', 'coût': 50, 'taux': 15},
    {'ref': 'Action-4', 'coût': 70, 'taux': 20},
    {'ref': 'Action-5', 'coût': 60, 'taux': 17},
    {'ref': 'Action-6', 'coût': 80, 'taux': 25},
    {'ref': 'Action-7', 'coût': 22, 'taux': 7},
    {'ref': 'Action-8', 'coût': 26, 'taux': 11},
    {'ref': 'Action-9', 'coût': 48, 'taux': 13},
    {'ref': 'Action-10', 'coût': 34, 'taux': 27},
    {'ref': 'Action-11', 'coût': 42, 'taux': 17},
    {'ref': 'Action-12', 'coût': 110, 'taux': 9},
    {'ref': 'Action-13', 'coût': 38, 'taux': 23},
    {'ref': 'Action-14', 'coût': 14, 'taux': 1},
    {'ref': 'Action-15', 'coût': 18, 'taux': 3},
    {'ref': 'Action-16', 'coût': 8, 'taux': 8},
    {'ref': 'Action-17', 'coût': 4, 'taux': 12},
    {'ref': 'Action-18', 'coût': 10, 'taux': 14},
    {'ref': 'Action-19', 'coût': 24, 'taux': 21},
    {'ref': 'Action-20', 'coût': 114, 'taux': 18},
]

# Initialisation des gains maximums
max_gain = 0

# Initialisation de la variable contenant les meilleures combinaisons
best_combination = None

# Initialisation de la taille des combinaisons
taille = 0

# Création d'une boucle permettant d'effectuer toutes les combinaisons en respectant les contraintes de coûts et de rentabilité maximums
for taille in range(2, len(actions) + 1):

    for combination in itertools.combinations(actions, taille):
        total_gain = 0
        total_price = 0

        for element in combination:
            total_price += element['coût']
            total_gain += element['coût'] * element["taux"] / 100

        if (total_price <= 500 and total_gain > max_gain):
            max_gain = total_gain
            best_combination = combination

# Affichage de la rentabilité maximal obtenue en Euros
# Affichage des combinaisons permettant d'obtenir le resultat. Il permet de dépenser 498€  d'actions et gagner 99,01 € en 2 ans

print('Gain:', round(max_gain, 1), "€")
print('Combinaison rentable:', best_combination)
