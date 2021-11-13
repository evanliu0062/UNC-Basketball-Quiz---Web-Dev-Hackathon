from flask import Flask, render_template, request

hack110: Flask = Flask(__name__)

score: int = 0

question_1: str = input("What UNC Basketball player is currently on the team? \n a. Armondo Bacot \n b. Tyler Hansbrough \n c. Grayson Allen \n d. Marcus Paige \n Answer: ")
if question_1 == "a":
    score += 10
    print("Correct!")
elif question_1 == "c":
    score -= 5
    print("-5 for that.")
else:
    print("Incorrect!")
question_2: str = input("How many total national championships has UNC won in men's basketball? \n a. 9 \n b.6 \n c.7 \n d.3 \n Answer: ")
if question_2 == "c":
    score += 10
    print("Correct!")
else:
    print("Incorrect")
question_3: str = input("When was UNC's most recent national championship? \n a. 2009 \n b. 2017 \n c. 2019 \n d. 2005 \n Answer: ")
if question_3 == "b":
    score += 10
    print("Correct!")
else:
    print("Incorrect")
question_4: str = input("Which jersey number is not already retired? \n a. 23 \n b. 50 \n c. 5 \n d. 12 \n Answer: ")
if question_4 == "c":
    score += 10
    print("Correct!")
else:
    print("Incorrect")
question_5: str = input("Which year did Tyler Hansbrough win National Player of The Year? \n a. 2009 \n b. 2012 \n c. 2008 \n d. 2010 \n Answer: ")
if question_5 == "a":
    score += 10
    print("Correct!")
else:
    print("Incorrect!")
question_6: str = input("Who is the current head coach of the UNC men's basketball team? \n a. Roy Williams \n b. Hubert Davis \n c. Caleb Love \n d. CJ Skender \n Answer: ")
if question_6 == 'b':
    score += 10
    print("Correct!")
else:
    print("Incorrect!")
question_7: str = input("Which famous basketball player played for UNC during the '81-'82 season? \n a. Michael Jordan \n b. Lebron James \n c. The Toon Squad \n d. Daniel Santona \n Answer: ")
if question_7 == 'a':
    score += 10
    print("Correct!")
else:
    print("Incorrect!")
question_8: str = input("What year/season did UNC play its first season ever? \n a. 1915-16 \n b. 1938-39 \n c. 1962-63 \n d. 1910-11 \n Answer: ")
if question_8 == 'd':
    score += 10
    print("Correct!")
else:
    print("Incorrect!")
question_9: str = input("How many head coaches has UNC had in the history of the program? \n a. 19 \n b. 25 \n c. 6\n d. 17 \n Answer: ")
if question_9 == "a":
    score += 10
    print("Correct!")
else:
    print("Incorrect!")
question_10: str = input("In what year did Roy Williams retire? \n a. 2021 \n b. 2019 \n c. 2020 \n d. Has not retired \n Answer: ")
if question_10 == "a":
    score += 10
    print("Correct!")
else:
    print("Incorrect!")
    
print(f"Congrats! You made it to the end of our quiz! You finished with {score} points! Great job!")


if __name__ == '__main__':
    hack110.run(debug=True)