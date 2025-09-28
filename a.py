import time
input1 = input("hi! i will ask you some questions of math , press y")

if input1.lower() == 'y':
    print("first question is 2+2")
    question1 = input("->")
    if question1 == '4':
        print("looking for your answer..")
        time.sleep(3)
        print("your answer is correct!! congrulations , but not now , to the next question!! to continue press n")
        next = input("->")
    else:
     print("you done wrong loser!!")
    if next == 'n':
        print("5x5")
        question2 = input("-->")
        if question2 == '25':
            print("yay you are so pro pro , im proud of you , if you want second version of this , i can make it but for other classes!!^^ bye for now!!")
        else:
            print("you = no math classses , go study maths")