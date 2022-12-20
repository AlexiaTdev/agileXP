# Pour enregistrer les travaux sur ta branche github
# commande exemple: make msg="add user table" save-all
# avec msg comme variable str
save-all:
	git add *
	git commit -m "MAJ code: $(msg)"
	git push

# Pour faire un merge d'une branche sur le master
# commande exemple: make b="feature/id2" merge-master
merge-master:
	git checkout master
	git merge $(b)
	git push

# Pour lancer le test
# commande exemple: make test
-t:
	python .\testPrgm.py

# Pour lancer l'application python
# commande exemple: make b="feature/id2" merge-master
-l:
	python .\prgm.py