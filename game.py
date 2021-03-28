import random
import time
import string
starting_time = time.time()
running = True
list_of_characters = string.ascii_lowercase + string.digits
score = 0
char1 = random.choice(list_of_characters)
char2 = random.choice(list_of_characters)
char3 = random.choice(list_of_characters)
char4 = random.choice(list_of_characters)
char5 = random.choice(list_of_characters)
char6 = random.choice(list_of_characters)
character_for_user_to_type = char1 + char2 + char3 + char4 + char5 + char6
while running:
    print(character_for_user_to_type)
    user_typing = input("Type what you see on the screen: ")
    if user_typing == character_for_user_to_type:
        score += 1
        char1 = random.choice(list_of_characters)
        char2 = random.choice(list_of_characters)
        char3 = random.choice(list_of_characters)
        char4 = random.choice(list_of_characters)
        char5 = random.choice(list_of_characters)
        char6 = random.choice(list_of_characters)
        character_for_user_to_type = char1 + char2 + char3 + char4 + char5 + char6
        print("correct. Your score is " + str(score) + ".")
    elif user_typing != character_for_user_to_type:
        print("looks like you lost!")
        running = False
    if score == 100:
        ending_time = time.time()
        print("Well done. You finsihed the game and won! Carry on like this and you will be a touch typer")
        time_since_run = int(ending_time - starting_time)
        minutes = int(time_since_run / 60)
        float_minutes = time_since_run / 60
        seconds = int((float_minutes * 60) - (minutes * 60))
        minutes_units = "minutes"
        seconds_units = "seconds"
        if minutes == 1:
            minutes_units = "minute"
        if seconds == 1:
            seconds_units = "second"
        print("You finished in " + str(minutes) + " " + minutes_units + " and " + str(seconds) + " " + seconds_units + ".")
        running = False
