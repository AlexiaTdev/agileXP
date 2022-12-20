import os
commande = {}


# Hello world
def init():
    print("Hello World")

# Creation d un article    
def creerUnArticle(quantite, prixU):
    if quantite == None :
        quantite=verifyInput('int',"Combien voulez vous d'article?", "quantité est un nombre")
    if prixU == None :
        prixU=verifyInput('int',"Quel est le prix unitaire de l'article?", "prix unitairte non correct")
    commande[len(commande)] = [int(quantite), int(prixU)]
    return(saisirPUEtQuantite(quantite,prixU))

# verification de l'input et retourne la valeur quand c est un integer entre en l input
def verifyInput(type_var, message, messageErreur, variable=None):
    # Si on veut que ce soit un integer
    if type_var == 'int':
        while isinstance(variable, str) or (variable == None):
            try:
                x = int(input(message))
                return x
                break
            except ValueError:
                print(messageErreur)

# Saisir donnee d'un article
def saisirPUEtQuantite(quantite, prixUnitaire):
    return (str(quantite) + "     " + str(prixUnitaire) + "     " + str(int(quantite)*int(prixUnitaire)))

def calculerTotalHTCommande():
    totalHT=0
    for article in commande:
        totalHT = int(commande[article][0])*int(commande[article][1]) + totalHT
    return totalHT

# Proposer ajout un article
def proposerAjouterArticle():
    choix=input("Voulez vous ajouter un article? o pour oui, n pour non ")
    ajouterUnArticle(choix)
    
# Imprimer la commande
def printCommandeEntier():
    for article in commande:
        print(saisirPUEtQuantite(commande[article][0],commande[article][1]))
        
# Ajouter un article    
def ajouterUnArticle(choix):
    if choix =='o':
        print(creerUnArticle(None, None))
    if choix =='n':
        printCommandeEntier()
    else:
        proposerAjouterArticle()

def printFooter():
    print("-------------------------------")
    print("Total without taxes" + "     " + str(calculerTotalHTCommande()))

if __name__ == "__main__":
    init()
    print(creerUnArticle(None, None))
    proposerAjouterArticle()
    printFooter()