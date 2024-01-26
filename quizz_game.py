#------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter your answer (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)

#------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("INCORRECT")
        return 0
#------------------------------
def display_score(correct_guesses, guesses):
    print("------------------------------")
    print("RESULT")
    print("------------------------------")
    print("Answer: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: " + str(score) + "%")
#------------------------------
def play_again():
    response = input("Do you want to play again (yes or no): ")
    responses = response.upper()
    if responses == "YES":
        return True
    else:
        return False



#------------------------------

questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "What year are we living in?: ": "C",
    "Is the earth round?: ": "B"
}
options = [["A. Guido van Rossum", "B. Issac Newton", "C. Nikola Tesla", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2023"],
           ["A. 2004", "B. 2016", "C. 2023", "D. 2024"],
           ["A. Flat", "B. Round", "C. What is Earth", "D. There's no earth"]
]

#------------------------------

new_game()

while play_again():
    new_game()
print("Bye!!")

