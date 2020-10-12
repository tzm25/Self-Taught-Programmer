print("Quizzing game")

import requests
import json
import pprint
import random
score_correct=0
score_incorrect=0
url="https://opentdb.com/api.php?amount=1"
endgame=""

while endgame!="quit":
    r=requests.get(url)
    if(r.status_code!=200):
        print=input("Sorry, there was a problem retrieving the question. Press enter to try again or type 'quit' to quit")
    else:
        valid_answer=False
        answer_number=1
        data= json.loads(r.text)
        question=data['results'][0]['question']
        answers=data['results'][0]['incorrect_answers']
        correct_answer=data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)

        print(question + "\n")

        for answer in answers:
            print(str(answer_number)+"- "+answer)
            answer_number+=1
        while valid_answer==False:
            user_answer=input("Type the number of the correct answer:")
            try:
                user_answer=int(user_answer)
                if user_answer>len(answers) or user_answer<=0:
                    print("Invalid answer")
                else:
                    valid_answer=True
            except:
                print("Invalid number. Use only numbers")

        
        user_answer=answers[int(user_answer)-1]

        if user_answer==correct_answer:
            score_correct+=1
            print("Congraculationsd!Your answer is correct")
        else:
            print("Sorry!,The correct answer is", correct_answer)
            score_incorrect+=1

        print("\n###################")
        print("Your score is:")
        print("Correct answers:" + str(score_correct))
        print("Incorrect answers:" + str(score_incorrect))
        print("###################")
        
        endgame=input("Press enter to play again or type 'quit' to end the game.").lower()

print("Thansks for playing")
        
    

