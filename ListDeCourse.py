import sys

list_de_course = []
while True:
    choix = int(input(""" VOTRE LISTE DE COURSE
1. Ajouter un élement dans la liste
2. Retirer un élement de la liste
3. Afficher les élements dans la liste
4. Vide la liste
5. Quitter
Votre choix !?
""" ))
    if choix == 1:
         element = input("Entrez nom de l'élement: ").capitalize()
         list_de_course.append(element)
         print(f"L'element {element} a bien été ajouté a la liste")
    elif choix == 2:
        element = input("Entrez l'élement à retirer: ").capitalize()
        if element in list_de_course:
           list_de_course.remove(element)
           print(f"L'éléments {element} a bien été retiré ")
        else:
           print(f"L'élement {element} n'existe pas dans la liste")
    elif choix == 3:
       if list_de_course:
         print(list_de_course)
       else:
            print("Votre liste est vide")
    elif choix == 4:
        list_de_course = []
        print("Votre liste de course a été vidé")
    elif choix == 5:
       print("A bientot")
       sys.exit()

