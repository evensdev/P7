# Solution optimale

import itertools


def wallet_dynamique(budget, actions):

    matrice = [[{"gain": 0,"combinations":[]} for x in range(budget * 100 + 1)] for x in range(len(actions) + 1)]

    for i in range(1, len(actions) + 1):
        
        for w in range(1, budget * 100 + 1):
            
            if actions[i-1][1] <= w:
                
                action_price = actions[i-1][1] * 100
                action_gain = actions[i-1][1] * actions [i-1][2] / 100

                
                
                if(action_gain + matrice[i-1][w-(actions[i-1][1] * 100)]["gain"] > matrice[i-1][w]["gain"]):
                   
                
                    matrice[i][w] = {"gain": action_gain + matrice[i-1][w-actions[i-1][1] * 100]["gain"],
                        "combinations": [actions[i-1][1]] + matrice[i-1][w]["combinations"]}
                    
                    
                else:
                    matrice[i][w] = matrice[i-1][w]
                    
            else:
                matrice[i][w] = matrice[i-1][w]      
               
                
                      
    print("Gains : ", round(matrice[-1][-1]["gain"]),"€")        
    print("best combinations : ", matrice[-1][-1]["combinations"])
                            
                
    w = budget
    n = len(actions)


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


print(wallet_dynamique(500, wallet))
