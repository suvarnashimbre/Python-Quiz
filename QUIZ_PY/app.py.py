from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "quiz_secret"

# ---------------- QUESTIONS ----------------
questions = [
    {
        "q": "Which of the following is the correct extension for python file?",
        "options": ["1. Python", "2. .pl", "3. .p", "4. .py"],
        "ans": "4. .py"
    },
    {
        "q": "Who developed Python?",
        "options": ["1. James Gosling", "2. Guido van Rossum", "3. Dennis Ritchie", "4. Bjarne Stroustrup"],
        "ans": "2. Guido van Rossum"
    },
    {
        "q": "Which keyword is used for function in python?",
        "options": ["1. def", "2. function", "3. define", "4. Fun"],
        "ans": "1. def"
    }
]


# ---------------- LOGIN ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["name"] = request.form["name"]
        session["roll"] = request.form["roll"]
        session["class"] = request.form["class"]
        session["score"] = 0
        session["qno"] = 0
        return redirect(url_for("quiz"))

    return render_template("login.html")

# ---------------- QUIZ ----------------
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    qno = session["qno"]

    if request.method == "POST":
        selected = request.form.get("option")
        if selected == questions[qno]["ans"]:
            session["score"] += 1
        session["qno"] += 1
        qno = session["qno"]

    if qno >= len(questions):
        return redirect(url_for("result"))

    return render_template("quiz.html",
                           question=questions[qno],
                           qno=qno + 1,
                           total=len(questions))

# ---------------- RESULT ----------------
@app.route("/result")
def result():
    return render_template("result.html",
                           name=session["name"],
                           roll=session["roll"],
                           class_name=session["class"],
                           score=session["score"],
                           total=len(questions))

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run()

