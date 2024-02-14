import random

def get_questions():
    questions = [
        {
            "questions" : "what is capital of France?",
            "options" : ["A.Tokyo", "B.London", "C.Paris", "D.Madrid"],
            "correct_answer" : "B"
        },
        {
            "questions" : "what is the largest animal in india?",
            "options" : ["A.Elephant", "B.Cow", "C.Rabit", "D.Dog"],
            "correct_answer" : "A"
        },
                {
            "questions" : "what is the largest Bird in india?",
            "options" : ["A.peacock", "B.Black Drongo", "C.Lesser Flamingo", "D.Grey Heron"],
            "correct_answer" : "B"
        },
                {
            "questions" : "Which planet is known as the Red Planet?",
            "options" : ["A.Earth", "B. Mars", "C. Jupiter", "D.Venus"],
            "correct_answer" : "B"
        },
                {
            "questions" : "What is the largest mammal?",
            "options" : ["A.Elephant", "B.Blue Whale", "C.Giraffe", "D.cow"],
            "correct_answer" : "B"
        },
                {
            "questions" : "What is the capital of Japan?",
            "options" : ["A.Beijing", "B.Tokyo", "C.Seoul", "D.Bangkokg"],
            "correct_answer" : "B"
        },
                {
            "questions" : "What is the chemical symbol for gold?",
            "options" : ["A.Au", "B.Ag", "C.Fe", "D.Hg"],
            "correct_answer" : "A"
        },
                {
            "questions" : " Which river is the longest in the world?",
            "options" : ["A.Nile", "B.Amazon ", "C.Yangtze", "D.Mississippi-Missouri"],
            "correct_answer" : "A"
        },
        
        
    ]
    return random.choice(questions)

def display_questions(questions):
    print(questions["questions"])
    for i in questions["options"]:
        print(i)
        
def Game():
    print("Welcome To KBC Game")
    
    money = 0
    try:
     for i in range(1,9):
        questions = get_questions()
        display_questions(questions)
        
        user_input = input("Enter your choice (A or B or C or D or 0 For Quit ): ").upper()
        if user_input == 0:
            break

        elif user_input == questions["correct_answer"]:
            print("Correct Answer!!")
            money += 10000
            print(f"You won the {money}")
            if money == 50000 and money == 100000:
                if user_input != questions["correct_answer"]:
                    break
                print("You won 50000")
        elif user_input != questions["correct_answer"]:
            print("Wrong Answer")
            print(f"you won {money}")
            break
        elif user_input != "A" or "B" or "C" or "D":
            print("Enter valid Choice")
            break
    except:
        print("Enter valid Choice")
            

    
    
    
Game()