# définition des IDs valides
correct_username = "momo"
correct_password = 123

#nombre max de tentatives
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    input_username = input("entrez votre nom : ")
    try:
        input_password = int(input("entrez votre mot de passe : "))
    except ValueError:
        print("le mot de passe doit etre un nombre")
        attempts += 1
        continue

    # vérification des IDs
    if input_username == correct_username and input_password == correct_password:
        print("bienvenue !")
        break
    else:
        print("erreur, veuillez réessayer")
        attempts += 1

# si le nombre maximum de tentatives est atteint
if attempts == max_attempts:
    print("nombre maximum de tentatives atteints. Accès refusé")
