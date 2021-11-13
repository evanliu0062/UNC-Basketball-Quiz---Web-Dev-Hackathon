from flask import Flask, render_template, request
from helpers import user

app: Flask = Flask(__name__)

users: list[user] = []
user_number: int = 0

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        global users
        global user_number

        fname: str = request.form['fname']
        lname: str = request.form['lname']
        score: int = 0
        
        

        response_question_1: str = request.form['player']
        if response_question_1 == "Armando Bacot":
            score += 10
        elif response_question_1 == "Grayson Allen":
            score -= 5
    
        response_question_2: str = request.form['nattys']
        if response_question_2 == "7":
            score += 10

        response_question_3: str = request.form['recent']
        if response_question_3 == "2017":
            score += 10
    
        response_question_4: str = request.form['jersey']
        if response_question_4 == "5":
            score += 10

        response_question_5: str = request.form['year']
        if response_question_5 == "2009":
            score += 10

        response_question_6: str = request.form['head']
        if response_question_6 == 'Hubert Davis':
            score += 10

        response_question_7: str = request.form['famous']
        if response_question_7 == 'Michael Jordan':
            score += 10

        response_question_8: str = request.form['season']
        if response_question_8 == '1910-11':
            score += 10

        response_question_9: str = request.form['coaches']
        if response_question_9 == "19":
            score += 10

        response_question_10: str = request.form['retire']
        if response_question_10 == "2021":
            score += 10
        
        fan_grade: str
        if score <= 30:
            fan_grade = "F-"
        if score > 30 and score <= 40:
            fan_grade = "F"     
        if score > 40 and score <= 50:
            fan_grade = "D"
        if score > 50 and score <= 60:
            fan_grade = "C"
        if score > 60 and score <= 70:
            fan_grade = "B"
        if score > 70 and score <= 80:
            fan_grade = "A"
        if score > 80:
            fan_grade = "A+"
        
        fan_rating: str       
        if score <= 40:
            fan_rating = "You are not a fan and you definitely do not go to UNC.  :("     
            
        if score > 40 and score <= 60:
            fan_rating = "You are a casual fan. You may or may not be a student at UNC.  :|"

        if score > 60:
            fan_rating = "You are a diehard fan and definitely go to UNC!  :)"
               

        if fname == '' or lname == '':
            return render_template("quiz.html")
            
        new_user: user = user(user_number, fname, lname, score)
        users.append(new_user)

        user_number += 1

        return render_template("result.html", score=score, fan_rating=fan_rating, fan_grade=fan_grade)
        
    return render_template("quiz.html")


@app.route('/all-results')
def all_results():
    return render_template('all-results.html', users=users)


@app.route('/user<usernumber>')
def display_user(usernumber: str):
    return render_template('user.html', user=users[int(usernumber)])


if __name__ == '__main__':
    app.run(debug=True)