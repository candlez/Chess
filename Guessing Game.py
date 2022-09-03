import random

words = ["dog", "cat", "horse", "pig", "giraffe", "elephant", "lion", "tiger", "sheep", "cheetah", "bear", "owl",
         "red", "blue", "orange", "green", "yellow", "black", "purple", "pink", "white", "gold", "silver",
         "cake", "pie", "pizza", "grape", "apple", "pear", "cupcake", "spaghetti", "grapefruit", "banana"]


def generate_word():
    return words[random.randrange(0, len(words), 1)]


def give_hint(word, a):
    if a == 0:
        return "The word is " + str(len(word)) + " letters long."
    elif a == 1:
        return "The first letter is " + word[0] + "."
    elif a == 2:
        return "The last letter is " + word[-1] + "."


def play_game(answer):
    score = 0
    if answer == "yes":
        game_state = "on"
        while game_state == "on":
            strikes = 0
            secret_word = generate_word()
            guessed_word = False
            while not(guessed_word or strikes == 3):
                print(give_hint(secret_word, strikes))
                if input("Guess the Word:") == secret_word:
                    score = score + 3 - strikes
                    print("Correct!")
                    guessed_word = True
                else:
                    strikes = strikes + 1
                    print("Incorrect!")
            if strikes == 3:
                print("The word was " + secret_word + ".")
                print("Your final score was " + str(score) + ".")
                game_state = "off"
    elif answer == "Yes":
        game_state = "on"
        while game_state == "on":
            strikes = 0
            secret_word = generate_word()
            guessed_word = False
            while not(guessed_word or strikes == 3):
                print(give_hint(secret_word, strikes))
                if input("Guess the Word:") == secret_word:
                    score = score + 3 - strikes
                    print("Correct!")
                    guessed_word = True
                else:
                    strikes = strikes + 1
                    print("Incorrect!")
            if strikes == 3:
                print("The word was " + secret_word + ".")
                print("Your final score was " + str(score) + ".")
                game_state = "off"
    else:
        print("You should say \"yes\" or \"no\" next time!")


def infinite_game():
    answer = "nothing"
    while answer != ("no" or "No"):
        answer = input("Would You Like To Play the Game?")
        if answer != ("no" or "No"):
            play_game(answer)
    print("ok")


infinite_game()
