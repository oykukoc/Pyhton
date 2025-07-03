
questions = ("How Many elements are in the periodic table?: ",
           "How Many legs does a cat have?: ",
           "How many bones are int the human body?: ",
           "Which planet in the solar system is the hottest?: ",
           "Which animal lays the largest eggs?: ")

options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. 1","B. 2","C. 3","D. 4"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus","C. Earth","D. Mars"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"))

answers = ("C", "D", "A", "B", "D")
guesses = []
score = 0
questionNum = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[questionNum]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[questionNum]:
        score += 1
        print("Correct!")
        print(f"Your'e score is {score}")
    else:
        print("Incorrect!")
        print(f"{answers[questionNum]} is the correct answer")
        print(f"Your'e score is {score}")
    questionNum += 1

print("----------------")
print("    RESULTS     ")
print("----------------")

print("Answers: ", end="")
for answer in answers:
    print(answer,end="")
print()

print("Guesses: ",end="")
for guess in guesses:
    print(guess,end="")
print()

print(f"Your score is {score}")
