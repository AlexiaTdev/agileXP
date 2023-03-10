import prgm

#Id 1
def testVerificationAffichageHelloWorld():
    # etant donne le démarrage du programme,
    # quand je lis la console,
    # alors je vois le texte "hello world"
    print('None')

#Id 2 (depend ID1)
def testsaisirPUEtQuantite():
    #Etant donné une commande
    # Quand j'ajoute un article, je renseigne un prix unitaire et une quantité
    # Alors le prix total de l'article est calculé (articleTotalPrice = quantity*unit price)
    # Et la ligne suivante s'affiche :
        # quantity + "                " + unit price + "                " + articleTotalPrice
    assert prgm.saisirPUEtQuantite(2,4,"") == "     2     4     8", "problème de quantité, d'unité ou de prix total de l'article"

#Id 3 (depend ID2)
def testAjoutArticle():
    #etant donné une commande où j'ai terminé de renseigner un article,
    #quand on me propose de rajouter un article et que je réponds oui, 
    #alors je continue l'ajout d'article
    prgm.creerUnArticle(1,1,"")
    assert len(prgm.commande) == 2, "problème d'ajout"

    #etant donné une commande où j'ai terminé de renseigner un article,
    #quand on me propose de rajouter un article et que je réponds non, 
    #alors je finis ma commande
    for article in prgm.commande:
        assert (prgm.saisirPUEtQuantite(prgm.commande[article][0], prgm.commande[article][1],prgm.commande[article][2])) == "     1     1     1", "problème d'affichage de la liste d article"


#Id 4 (depend ID2)
def testAfficherLePrixTotal():
    # Etant donné une commande possédant au moins 1 article,
    # quand je veux compléter ma commande
    # alors j'affiche une ligne de la manière suivante :
        #"-----------------------------------------------------"
        #"Total without taxes" + totalHT
    prgm.creerUnArticle(1,1,"")
    assert prgm.calculerTotalHTCommande() == 1, "probleme de total HT"

#Id 5 (depend ID2)
def testCalculPrixTTC():
    # etant donné les articles saisis
    # quand je veux compléter ma commande
    # alors on calcule le prix TTc (prixTTC = montant hors taxe - réduction + montant TVA) et l'affiche de la maniere suivante
        #"-----------------------------------------------------"
        #"Total prices" + total TTC
    print('None')

#Id 6 (depend ID1)
def testListeDesCodesTva():
    # Etant donné le démarrage du programme
    # Quand je lis la console
    # Alors je vois la liste des codes TVA affichés après le "hello world"
    print('None')

#Id 7 (depend ID6)
def testDemanderCodeEtatEtAfficherTVA():
    #Etant donné la liste des taux de TVA affichées par état,
    #quand je renseigne le code de l'état,
    #alors j'affiche le taux de TVA correspondant de la manière suivante :
        #"Tax" + tauxdeTVA + "%"
    print('None')

#Id 8 (depend ID7)
def testNePlusAfficherTvaMaisAplLiquer():
    #Etant donné le renseignement du code etat,
    #quand j'affiche le taux de TVA,
    #alors le montant de la TVA est calculé
    #ET j'affiche les élément de la manière suivante :
	    #"Tax" + tauxdeTVA + "%" + montant de la TVA
    #ET la liste des taux TVA n'est plus affichée au démarrage de l'application
    print('None')

#Id 9 (depend ID4)
def testAfficherMontantTotalReduction():
    #etant donne un article avec un prix unitaire, une quantité et un prix total par article,
    #quand j'ai une commande avec au moins un article,
    #alors j'affiche un taux de réduction fixe de 0e de la manière suivante :
	#       "Discount " et tout a droite "-"+0e
    assert (len(prgm.commande)!=0) and (prgm.ligneDeReduction(0)=="Discount               -0"), "erreur sur la reduction de depart"

#Id 10 (depend ID9)
def testDemanderUserSaisieTauxReduction():
    #Etant donne une commande avec un taux de réduction fixe de 0e,
    #quand je renseigne le taux de réduction à appliquer,
    #alors est calculé le total without taxes de la commande et le montant de la réduction,
    #ET on affiche les lignes suivantes :
        #"-----------------------------------------------------"
        #"Total without taxes" + totalHT
        #"Discount " et tout a droite "-"+montant de la réduction+"e"
    print('None')
    
#Id 11 (depend ID1)
def afficheTauxReductionDebutProgramme():
    #Etant donné l'ouverture du programme
    #Je veux afficher la liste des taux de réduction au démarrage du programme
    #Afin d'avoir les réductions possibles (en deux colonnes Order value et Discount rate)
    print('None')

#Id 12 (depend ID9)
def testAfficherTauxReduction():
    #etant donne une commande avec un montant de réduction (de 0e),
    #quand j'ai un total et un montant de réduction,
    #alors j'affiche un taux de réduction appliqué à côté du montant de la réduction de la manière suivante, sur une même ligne :
	#       "Discount "+pourcentageReduction +"%"  et tout a droite "-"+montantDeLaReduction
    print('None')

#Id 13, 14, 15, 16, 17 (depend ID10 & ID{Id}-1)
def testVerificationPresaisiTauxReduct():
    # Etant donnees que le prix total HT d'une commande,
    # Quand le prix est supérieur à 1000e,
    # Alors on attribue un pourcentage de réduction tel que (<prix total, pourcentage reduction>):
        # Cas <1000,3>
        # Cas <5000,5>
        # Cas <7000,7>
        # Cas <10000,10>
        # Cas <15000,15>
    print('none')

#Id 18
def testInputUserProductName():
    #etant donne l'ajout d'un article possédant une quantité et un unit price,
    #quand j'entre la désignation de l'article,
    #alors j'affiche une ligne avec les éléments suivants  :
	#designation + quantity + unit price + articleTotalPrice
    assert prgm.saisirPUEtQuantite(2,4,"stylo") == "stylo     2     4     8", "problème de quantité, d'unité ou de prix total de l'article"

#Id 19 (depend ID7, ID19)
def testReduction20siFR20000():
    # etant donne une commande,
    # quand le montant total HT de la commande est supérieure à 20 000 ET que le code pays est "FR",
    # alors le pourcentage de Réduction (pourcentageReduction) sera de 20%
    print('None')


##SUITE DE TESTS AUTOMATISES
# ID2
testsaisirPUEtQuantite()
testAfficherLePrixTotal()
testAjoutArticle()
testInputUserProductName()
testAfficherMontantTotalReduction()