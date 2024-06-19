import random

def get_level():
    while True:
        level = input("Enter Level 1, 2, 3: ")
        if level in ["1", "2", "3"]:
            break
        print("Error: Invalid input! \n")
    return level

def get_questions():
    while True:
        try:
            questions = int(input("Enter number of questions to ask: (3 to 10) "))
        except:
            print("Error: Please enter an integer value between 3 and 10!")
            continue
        if questions in range(3,11):
            break
        print("Error: Please enter an integer value between 3 and 10!")
    return questions

def ask_question(level):
    correct = False
    counter = 0
    if level == 1:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
    elif level == 2:
        a = random.randint(10, 99)
        b = random.randint(10, 99)
    else:
        a = random.randint(100, 999)
        b = random.randint(100, 999)

    while (correct == False) and (counter < 3):
        try:
            answer = int(input(f"{a} + {b} = "))
        except:
            print("WRONG!!!\n")
            counter += 1
            continue
        if (answer == a + b):
            print("CORRECT!!!\n")
            return True
        else:
            counter += 1
            print("WRONG!!!\n")
    print(f"Correct Answer: {a} + {b} = {a+b} \n")
    return False

def main():
    level = get_level()
    questions = get_questions()
    correct = 0

    for x in range(questions):
        if ask_question(int(level)):
            correct += 1
    
    print(f"\n\nYou got {correct} out of {questions} questions correct: {100 * correct / questions:.2f}%")
    


main()
