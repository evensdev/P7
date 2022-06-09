#Importation du package itertools qui nous permettra d'utiliser la fonction combinations
#La fonction combinations permet de tester des combinaisons d'éléments pour obtenir le résultat maximal


import itertools

#La liste d'actions est représentée en sous forme de dictionnaire avec des clées et valeurs

actions = [
    {'ref':'Action-1','coût':20, 'benefice':5},
    {'ref':'Action-2','coût':30, 'benefice':10},
    {'ref':'Action-3','coût':50, 'benefice':15},
    {'ref':'Action-4','coût':70, 'benefice':20},
    {'ref':'Action-5','coût':60, 'benefice':17},
    {'ref':'Action-6','coût':80, 'benefice':25},
    {'ref':'Action-7','coût':22, 'benefice':7},
    {'ref':'Action-8','coût':26, 'benefice':11},
    {'ref':'Action-9','coût':48, 'benefice':13},
    {'ref':'Action-10','coût':34, 'benefice':27},
    {'ref':'Action-11','coût':42, 'benefice':17},
    {'ref':'Action-12','coût':110, 'benefice':9},
    {'ref':'Action-13','coût':38, 'benefice':23},
    {'ref':'Action-14','coût':14, 'benefice':1},
    {'ref':'Action-15','coût':18, 'benefice':3},
    {'ref':'Action-16','coût':8, 'benefice':8},
    {'ref':'Action-17','coût':4, 'benefice':12},
    {'ref':'Action-18','coût':10, 'benefice':14},
    {'ref':'Action-19','coût':24, 'benefice':21},
    {'ref':'Action-20','coût':114, 'benefice':18}
]


#Initialisation des variables qui servirons à afficher les résultats après l'execution de la fonction
#On s'intéresse au gain possible de réaliser, la meilleure combinaison, la taille de la liste d'actions
#Et le montant dépensé afin de s'assurer de l'exploitation optimale du budget


max_gain = 0
best_combination = None
taille = 0
depense = 0



#La boucle permettra de sauvegarder les combinaisons d'actions dépensant le maxium de budget
#L'ensemble des résultat seront stockés dans la variable "best_combination"

for taille in range(2, len(actions)+1):
    
    
    

    #Mise en place de l'itérateur de combinaison avec 2 arguments n-uplets de longueur r, ordonnés, sans répétition d'éléments
    #On a en argument la liste d'actions et sa taille
    #Initialisation des variables gains et prix total qui seront incrémentées par la boucle
    #À chaque fois qu'on aura une action, on affectera son prix à total_price et son bénéfice à total_gain
    
    for combination in itertools.combinations(actions,taille):
        total_gain = 0
        total_price = 0
        
        
        
        #incrementation des variables prix total et total gain pour chaque chaque combinaison retenues par l'algorithme
        #les clés "bénéfices" et "coûts" permettront de prendre les bonnes valeurs à incrémenter dans les variables
        
        for element in combination:
            total_price += element['coût']
            total_gain += element['coût'] * element["benefice"] / 100
            
            
        #je délimite le budget maximal à dépenser grâce à une boucle conditionnelle
        #si le prix total est inférieur à 500 et que le gain total est supérieur au gain maximal
        #alors on arrêtera la boucle et on sauvegardera les résultats dans les variables
        
        if(total_price <= 500 and total_gain > max_gain):
            max_gain = total_gain
            best_combination = combination

          
        
#boucle pour afficher chaque actions de la liste contenant les meilleures combinaisons
#on récupère le côut de chaque action et on l'affecte à la variable dépense pour avoir le coût total

for i in range(len(best_combination)):
    depense += best_combination[i]['coût']

    
    
    
#On affiche le montant dépensé au total
#On affiche le nombre d'actions utilisé
#On affiche le gain total des actions
    
print("Montant dépensé :", depense, "€")            
print("Nb d'actions : ", len(best_combination))
print("Gains :",round(total_gain),"€")


#On affiche la liste d'actions de la combinaison gagnante

for i in range(len(best_combination)):
    print(best_combination[i])

 
