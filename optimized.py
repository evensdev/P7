
#Initialisation des variables qui servirons à afficher les résultats après l'execution de la fonction
#On s'intéresse au gain possible de réaliser, la meilleure combinaison, la taille de la liste d'actions
#Et le montant dépensé afin de s'assurer de l'exploitation optimale du budget


max_gain = 0
best_combination = None
taille = 0
depense = 0


#On utilisera l'algorithme du sac à dos pour effectuer de la programmation dynamique
#W représentera la capacité du sac soit le "budget maximal" de 500€
#Wi représentera le poids de l'objet i soit la clé "coût" de l'action
#Vi représentera la valeur de l'objet i soit la clé "bénéfice" de l'action
#n représentera la "quantité" d'actions dans la liste





#On crée une matrice en 2 dimensions
#Le budget maximal sera représenté par n+1 quantités de colonnes correspondant à la valeur du budget en commencant par la colonne de valeur 0
#Chaque ligne de la matrice correspondra à celle d'une action de la liste  (voir): https://bit.ly/397xbzn


#création de la fonction portefeuille dynamique avec en paramètres :
#1. le montant du budget = 500 et 2. la liste d'actions

def wallet_dynamique(budget, actions):
    
    #On représente en colonne le budget en n colonnes de zeros
    #On représente en lignes les actions en n quantité d'actions
    
    matrice = [[0 for x in range(budget + 1)] for x in range(len(actions) + 1)]
    
    
    
    #On fait une boucle pour chaque ligne d'actions en partant d'une ligne nulle d'où 20 + 1 ligne 

    for i in range(1, len(actions) + 1):
        
        
        #Pour chaque ligne on affecte chaque colonnes par pas de 1 jusqu'à la colonne finale
        #En commancant par une colonne de valeur zéro d'où 500 + 1 colonne
        
        
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
    gains = 0

    for i in range(len(actions_selection)):
        montant_depense += actions_selection[i][1]
        gains += actions_selection[i][-1]

    print("Budget dépensé : ", montant_depense, "€")
    print("Nb d'actions : ",len(actions_selection))  
    print("Gains : ",gains,"€")
    
    return actions_selection, matrice[-1][-1]



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



