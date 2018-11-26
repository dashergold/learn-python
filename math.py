from random import randint
import sys



def generate_random_number():
    return randint(-10, 12)

def generate_random_operation():
    op = randint(0, 2)
    if op == 0:
        return "+"
    elif op == 1:
        return "-"
    else:
        return "*"

def get_int(prompt):
    print(prompt)
    sValue = input()
    return int(sValue)


def ask_user_rounds():
    rounds = 0
    while rounds <= 0:
        rounds = get_int("How many rounds would you like to play?")
        if rounds > 0: 
            return rounds
        else:
            print("No you don't!")

def ask_user_question(a,b,operation):
    return get_int("What is "+str(a)+" "+ operation + " " + str(b)+"?")
    
def score_user_reply(a,b,operation,answer):
    if operation == "+":
        correct_answer = a+b
    elif operation == "-":
        correct_answer = a-b
    elif operation == "*":
        correct_answer = a*b
    else:
        sys.exit("Unknown operation")

    if answer == correct_answer:
        print("Well done!!")
        return 1
    else:
        print("The correct answer was "+ str(correct_answer))
        return 0

#ask user how many rounds
#repeat that many times
#   generate random numbers
#   generate random operation
#   ask user question
#   score user reply
#   add score to total score   
#print results

total_score = 0
rounds = ask_user_rounds()
for i in range(rounds):
    print("round "+str(i + 1))
    n1 = generate_random_number()
    n2 = generate_random_number()
    op = generate_random_operation()
    a = ask_user_question(n1,n2,op)
    s = score_user_reply(n1,n2,op,a)
    total_score += s
print("you got " + str(total_score)+" points!")
