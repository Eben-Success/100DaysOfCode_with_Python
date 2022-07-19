import random
from logo import logo


word_list = ["realmadrid", "barcelona", "chelsea", "arsenal"]

chosen_word = random.choice(word_list)

# Test the code by checking the random number
print(f'\n Ops, the right word is {chosen_word} \n')

word_length = len(chosen_word)

# Creating a variable called 'lives' to keep track to the number lives left
lives = 6

# Display dashes equal to the random letter the user
# has to guess

display = []
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    # Request for a letter from user
    guess = input("\nGuess a number \n").lower()

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
        else:
            print("No match")

    # If guesss if not a letter in the chosen_word, reduce 'live' by 1
    # If lives goes down to 0 and then the game should stop and it should
    # print "You Lose"



    # Joining all the element in the list and converting themn into string
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")
