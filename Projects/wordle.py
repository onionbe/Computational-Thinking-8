import random

# Pick a word at random
word_list = ["abide", "about", "above", "abuse", "actor", "acute", "adapt", "admit", "adopt", "adult", "after", "again", "agent", "agree", "ahead", "alarm", "album", "alert", "alike", "alive", "allow", "alone", "along", "alter", "angel", "anger", "angle", "angry", "apart", "apple", "apply", "arena", "argue", "arise", "armor", "arrow", "aside", "asset", "audio", "audit", "avoid", "award", "aware", "bacon", "badge", "bagel", "baker", "basic", "basin", "beach", "beard", "beast", "began", "begin", "begun", "being", "bench", "birth", "black", "blame", "blank", "blast", "bleed", "blend", "bless", "blind", "block", "blood", "board", "boast", "bonus", "books", "boost", "booth", "bored", "brain", "brand", "brave", "bread", "break", "breed", "brick", "brief", "bring", "broad", "broke", "brown", "brush", "build", "burst", "buyer", "cabin", "cable", "camel", "candy", "carry", "catch", "cause", "chain", "chair", "chalk", "champ", "chant", "charm", "chart", "chase", "cheap", "cheat", "check", "cheer", "chest", "chief", "child", "chill", "china", "choic", "choke", "claim", "class", "clean", "clear", "clerk", "click", "climb", "clock", "close", "cloud", "coach", "coast", "color", "comic", "could", "count", "craft", "crash", "cream", "creek", "crime", "crisp", "crowd", "crown", "cruel", "crush", "curve", "daily", "dance", "dairy", "death", "delay", "depth", "devil", "diary", "dirty", "dizzy", "dough", "dozen", "draft", "drain", "drama", "dream", "dress", "drift", "drink", "drive", "drops", "earth", "eight", "elect", "elite", "empty", "enjoy", "enter", "entry", "equal", "error", "essay", "event", "every", "exact", "exist", "extra", "faith", "fancy", "fault", "favor", "feast", "fetch", "field", "fight", "final", "first", "flame", "flash", "fleet", "flesh", "float", "flood", "floor", "flour", "focus", "force", "forge", "forth", "found", "frame", "fraud", "fresh", "friend", "fruit", "funny", "giant", "given", "glass", "globe", "glory", "grade", "grain", "grand", "grant", "grass", "great", "green", "greet", "guard", "guest", "guide", "habit", "happy", "heart", "heavy", "honor", "horse", "hotel", "house", "human", "humor", "ideal", "image", "imply", "index", "inner", "input", "issue", "ivory", "jacket", "joint", "judge", "juice", "knife", "knock", "label", "labor", "large", "later", "laugh", "layer", "learn", "leave", "legal", "level", "light", "limit", "local", "logic", "loose", "lucky", "lunch", "magic", "major", "maker", "march", "match", "maybe", "metal", "meter", "might", "minor", "model", "money", "month", "moral", "motor", "mouse", "mouth", "movie", "music", "never", "night", "noise", "north", "novel", "nurse", "occur", "offer", "often", "onion", "order", "other", "owner", "paint", "panel", "paper", "party", "peace", "pearl", "phase", "phone", "photo", "piece", "pilot", "pitch", "place", "plain", "plane", "plant", "plate", "point", "porch", "pound", "power", "press", "price", "pride", "prime", "print", "prize", "proof", "proud", "queen", "quick", "quiet", "quite", "radio", "raise", "range", "reach", "ready", "refer", "relax", "reply", "right", "river", "roast", "rough", "round", "route", "royal", "ruler", "salad", "scale", "scene", "score", "scout", "sense", "serve", "seven", "shall", "shape", "share", "sharp", "sheep", "sheet", "shelf", "shell", "shift", "shine", "shirt", "shock", "shoot", "short", "sight", "since", "skill", "sleep", "slice", "slide", "slope", "small", "smart", "smell", "smile", "smoke", "snack", "snake", "solid", "solve", "sorry", "sound", "space", "speak", "speed", "spend", "spice", "split", "sport", "stage", "stain", "stand", "start", "state", "steam", "steel", "stick", "still", "stock", "stone", "store", "storm", "story", "strip", "study", "stuff", "style", "sugar", "sweet", "table", "taste", "teach", "teeth", "thank", "theme", "there", "thick", "thief", "thing", "think", "third", "three", "throw", "tight", "title", "toast", "today", "token", "topic", "touch", "tough", "tower", "track", "trade", "train", "treat", "trend", "trial", "tribe", "trick", "truck", "trust", "truth", "twice", "under", "union", "unity", "until", "upper", "upset", "urban", "usage", "usual", "value", "visit", "vital", "voice", "voter", "watch", "water", "wheel", "where", "which", "while", "white", "whole", "whose", "woman", "world", "worry", "worth", "would", "wound", "write", "wrong", "youth"
]
hidden_word = random.choice(word_list)

print("WELCOME TO WORDLE!")
print(" ")
print("Please type in a 5 letter word for each guess, all in lower case. Good Luck!")

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""
    
    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    # Second letter guess
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
    # Third letter guess
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    # Fourth letter guess
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    #Fifth letter guess
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    

    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

print(f"You used {i+1} guesses")