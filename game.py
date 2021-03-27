import random
file = open("words.txt", "r")
words = file.readlines()
new_list = []
for word in words:
	new_list.append(word.strip())
running = True
score = 0
def GenerateWord():
	global output_word
	output_word = random.choice(new_list)
GenerateWord()
while running:
    print(output_word)
    user_typing = input("Type the word you see on the screen: ")
    if user_typing == output_word:
        GenerateWord()
        score += 1
        print("correct. Your score is " + str(score) + ".")
    elif user_typing != output_word:
        print("looks like you lost!")
        running = False
    if score == 100:
        print("Well done. You finsihed the game and won! Carry on like this and you will be a touch typer")
        running = False
