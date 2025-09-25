while True:
    word = input("What do you think Grandma likes?")

    if "" in word or "" in word:
        print(f"Grandma doesn't like {word}! ")
    else:
        print(f"Grandma likes {word}.")
    
    print (" ")