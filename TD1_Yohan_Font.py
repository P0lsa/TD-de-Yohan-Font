def formatage(lexique):
    dico = open(dico_path)
    d = dico.readlines()
    for i in range (len(d)):
        d[i] = d[i][:-1]
    return d
    
def inventaire(tirage):
    compteur={}
    for lettre in tirage :
        if not lettre in compteur.keys():          
            compteur[lettre] = 1
        else :
            compteur[lettre] +=1
    return compteur

def scrabble (tirage, dico_path, n):
    d=formatage(dico_path) # On formate la liste des mots du lexique
    mots_possibles=[]
    m = 0
    compteur=inventaire(tirage) #On fait l'inventaire des lettres qu'on a
    for mots in d:
        faisable = True
        compteur1 = {}
        for lettre in mots:
            if not lettre in compteur1.keys():          
                compteur1[lettre] = 1
            else :
                compteur1[lettre] += 1 #On fait l'inventaire des lettres dont on a besoin pour constituer le mot
        k = 0
        while faisable and k<len(compteur):
            for lettre in compteur1.keys():
                faisable = faisable and lettre in compteur.keys() and compteur[lettre]>= compteur1[lettre] #On vérifie si on peut constituer le mot
            k = k + 1
        if faisable:
            mots_possibles.append(mots)
    max_pt = 0
    for i in range(len(mots_possibles)):
        if len(mots_possibles[i])>max_pt:
            max_pt = len(mots_possibles[i])
    solutions = []
    for mots in mots_possibles:
        if len(mots) == max_pt:
            solutions.append(mots)
    return(solutions)

t= ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
path = 'frenchssaccent.dic'

print(scrabble(t,path,8))

#ex 3 : un dictionnaire

def calcul_pt(dico_pts, mots):
    pts = 0
    for lettre in mots:
        pts = pts + dico_pts[lettre]
    return pts

def scrabble_points(dico_pts,tirage, dico_path, n):
    dico = open(dico_path)
    d = dico.readlines()
    for i in range (len(d)):
        d[i] = d[i][:-1]
    poss=[]
    m = 0
    compteur = {}
    for lettre in tirage :
        if not lettre in compteur.keys():          
            compteur[lettre] = 1
        else :
            compteur[lettre] +=1 
    for w in d:
        if len(w) >= m:
            faisable = True
            compteur1 = {}
            for lettre in w:
                if not lettre in compteur1.keys():          
                    compteur1[lettre] = 1
                else :
                    compteur1[lettre] += 1
            k = 0
            while faisable and k<len(compteur):
                for lettre in compteur1.keys():
                    faisable = faisable and lettre in compteur.keys() and compteur[lettre]>= compteur1[lettre]
                k = k + 1
            if faisable:
                m = len(w)
                poss.append(w)
    max_pt = 0
    for i in range(len(poss)):
        t = calcul_pt(dico_pts,poss[i])
        if t>max_pt:
            max_pt = t
    solutions = []
    for w in poss:
        temp = calcul_pt(dico_pts,w)
        if temp == max_pt:
            solutions.append(w)
    return(solutions, max_pt)

points = {1 : 'aeilnorstu', 2 : 'dgm', 3 : 'bcp', 4: 'fhv',8 : 'jq',10 : 'kwxyz'}

def swap (dico):
    """swap les points et les lettres"""
    new = {}
    for (key,item) in dico.items():
        for lettre in item :
            new[lettre] = key
    return new

print(swap(points))

print(scrabble_points(swap(points), t, path, 8))


#ex 4 :


def recherche (dico):#on recherche si un seul -1 est présent dans le dictionnaire et vérifie qu'aucune valeur n'est inférieure et on renvoie la lettre de ce -1
    t = False
    t2 = False #indique si on en trouve au moins 2 
    t3 = False 
    l = None
    for lettre in dico.keys():
        if not t and dico[lettre] == -1:
            t = True
            l = lettre
        elif t and dico[lettre] == -1:
            t2 = True
        elif dico[lettre]< -1:
            t3 = True
    return t and not t2 and not t3, l


def scrabble_joker(dico_pts,tirage, dico_path, n):
    dico = open(dico_path)
    d = dico.readlines()
    joker = False
    if '?' in tirage :
        joker = True
    for i in range (len(d)):
        d[i] = d[i][:-1]
    poss=[]
    m = 0
    compteur = {}
    for lettre in tirage :
        if not lettre in compteur.keys():          
            compteur[lettre] = 1
        else :
            compteur[lettre] +=1 
    for w in d:
        faisable = True
        compteur1 = {}
        joker_used = False
        l_joker = None
        for lettre in w:
            if not lettre in compteur1.keys():          
                compteur1[lettre] = 1
            else :
                compteur1[lettre] += 1
        compteur2 = {}
        for lettre in compteur1.keys():
            if lettre in compteur.keys():
                compteur2[lettre] = compteur[lettre] - compteur1[lettre]
            else : 
                compteur2[lettre] = - compteur1[lettre]
        for lettre in compteur2.keys():
            faisable = compteur2[lettre] >= 0 and faisable 
        r = recherche(compteur2)
        if joker and not joker_used and r[0]:
            joker_used = True
            faisable = True
            l_joker = r[1]
        if faisable:
            poss.append((w, joker_used, l_joker))
    max_pt = 0
    for i in range(len(poss)):
        t = calcul_pt(dico_pts,poss[i][0])
        if poss[i][1] :
            t = t - calcul_pt(dico_pts, poss[i][2])
        if t>max_pt:
            max_pt = t
    solutions = []
    for word in poss:
        temp = calcul_pt(dico_pts,word[0]) 
        if word[1]:
            temp = temp - calcul_pt(dico_pts, word[2])
        if temp == max_pt:
            solutions.append(word)
    return(solutions, max_pt)


tirage2 = ['r', 'r', 'r', '?', 'l', 'r', 's', 'z']
print(scrabble_joker(swap(points), tirage2 , path, 8))



