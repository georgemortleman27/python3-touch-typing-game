import random
alphabet_list = ["a","b", "c", "d", "e", "f", "g", "h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
running = True
score = 0
def GenerateLetters():
    global letter1
    global letter2
    global letter3
    global letter4
    global letter5
    global letter6
    letter1 = alphabet_list[random.randint(0,25)]
    letter2 = alphabet_list[random.randint(0,25)]
    letter3 = alphabet_list[random.randint(0,25)]
    letter4 = alphabet_list[random.randint(0,25)]
    letter5 = alphabet_list[random.randint(0,25)]
    letter6 = alphabet_list[random.randint(0,25)]
GenerateLetters()
while running:
    letter_jumble = letter1 + letter2 + letter3 + letter4 + letter5 + letter6
    print(letter_jumble)
    user_typing = input("Type the word (sortof) you see on the screen: ")
    if user_typing == letter_jumble:
        GenerateLetters()
        score += 1
        print("correct. Your score is " + score)
    elif user_typing != letter_jumble:
        print("looks like you lost!")
        running = False
    if score == 100:
        print("Well done. You finsihed the game and won! Carry on like this and you will be a touch typer")
        running = False
