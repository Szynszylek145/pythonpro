meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            }

word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")

if word in meme_dict.keys():
    # Co powinniśmy zrobić, jeśli słowo zostało znalezione?
    print(meme_dict[word])
else:
    # Co powinniśmy zrobić, jeśli słowo nie zostało znalezione?
    print("Nie ma jeszcze takiego słowa w naszym słowniku. Ale za niedługo będzie!")
