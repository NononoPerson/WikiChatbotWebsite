from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("Chatbot"))


from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import wikipedia

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Chat history (simple global list for demo)
chat_history = []
@app.route("/", methods=["GET", "POST"])
@login_required
def home():
    global chat_history

    if request.method == "GET":
        chat_history = []  # Clears chat on fresh open
        return render_template("index.html", chat_history=chat_history, username=current_user.username)

    if request.method == "POST":
        question = request.form.get("question", "").lower()
        answer = None

        if not question:
            answer = "Please type a question."
        elif "what is my name" in question:
            answer = f"Your name is {current_user.username}."



        # Part 1 Questions
    elif "where is pallavi international school gandipet located" in question:
        answer = "Gandipet, Hyderabad, Telangana, India."
    elif "what is the full address of pallavi international school gandipet" in question:
        answer = "Near Osman Sagar Lake, Gandipet, Hyderabad, Telangana – 500075."
    elif "in which city is pallavi international school gandipet" in question:
        answer = "Hyderabad."
    elif "which state is pallavi international school gandipet in" in question:
        answer = "Telangana."
    elif "when was pallavi international school gandipet established" in question:
        answer = "2018."
    elif "is pallavi international school gandipet affiliated with cbse" in question:
        answer = "Yes."
    elif "what is the cbse affiliation number of pallavi international school gandipet" in question:
        answer = "3630263 (verify for final notes as affiliation updates periodically)."
    elif "what classes does pallavi international school gandipet offer" in question:
        answer = "Pre-Primary to Grade 10 currently, with plans to expand up to Grade 12."
    elif "does the school have pre-primary sections" in question:
        answer = "Yes, from Nursery."
    elif "is english the medium of instruction at pallavi international school gandipet" in question:
        answer = "Yes."
    elif "what board syllabus does the school follow" in question:
        answer = "CBSE."
    elif "who is the principal of pallavi international school gandipet" in question:
        answer = "Mrs. Anitha Rao (verify for current year)."
    elif "who is the chairperson of pallavi international school gandipet" in question:
        answer = "Part of the Pallavi Group of Schools under Pallavi Educational Society, founded by Shri M. Srinivasa Rao."
    elif "does pallavi international school gandipet have a school website" in question:
        answer = "Yes, https://pallavimodelschools.org/gandipet/"
    elif "is it a co-educational school" in question:
        answer = "Yes."
    elif "does the school have an international curriculum" in question:
        answer = "No, it follows CBSE, though termed ‘International’ for its global teaching approach."

    # 🏫 ➡️ Part 2 questions
    elif "what extracurricular activities does the school offer" in question:
        answer = "Dance, music, art & craft, sports, yoga, and more."
    elif "does the school have sports facilities" in question:
        answer = "Yes, including indoor and outdoor games."
    elif "what are the main sports offered" in question:
        answer = "Cricket, football, basketball, volleyball, and indoor games like chess and carrom."
    elif "does pallavi international school gandipet have a library" in question:
        answer = "Yes."
    elif "does the school have a computer lab" in question:
        answer = "Yes."
    elif "does the school have a science lab" in question:
        answer = "Yes."
    elif "what languages are taught in the school" in question:
        answer = "English, Hindi, Telugu (verify for any additional languages offered currently)."
    elif "does the school have dance classes" in question:
        answer = "Yes."
    elif "does the school have music classes" in question:
        answer = "Yes."
    elif "are there art and craft activities in the school" in question:
        answer = "Yes."
    elif "does the school celebrate annual day" in question:
        answer = "Yes."
    elif "does the school celebrate sports day" in question:
        answer = "Yes."
    elif "does the school celebrate national festivals" in question:
        answer = "Yes, including Independence Day and Republic Day."
    elif "does the school conduct science exhibitions" in question:
        answer = "Yes."
    elif "does the school have student council elections" in question:
        answer = "Yes."
    elif "does the school organise educational trips" in question:
        answer = "Yes."
    elif "does the school conduct parent teacher meetings" in question:
        answer = "Yes, regularly."
    elif "does the school have cctv cameras" in question:
        answer = "Yes."
    elif "does the school have a cafeteria or canteen" in question:
        answer = "Yes."
    elif "does the school provide medical facilities" in question:
        answer = "Yes, with an infirmary and nurse."
    elif "does the school have fire safety equipment" in question:
        answer = "Yes."
    elif "does the school have safe drinking water" in question:
        answer = "Yes."
    elif "is there a playground in the school" in question:
        answer = "Yes."
    elif "does the school have transport tracking" in question:
        answer = "Yes."
    elif "is gps enabled tracking available in school buses" in question:
        answer = "Yes."

    # 🏫 ➡️ Part 3 questions
    elif "does the school provide counselling facilities" in question:
        answer = "Yes, for academic and emotional support."
    elif "does the school conduct olympiad exams" in question:
        answer = "Yes, for Maths, Science, English and others as per availability."
    elif "does the school conduct spell bee competitions" in question:
        answer = "Yes."
    elif "does the school organise inter school competitions" in question:
        answer = "Yes."
    elif "does the school conduct assemblies" in question:
        answer = "Yes, regularly."
    elif "are students given homework" in question:
        answer = "Yes, as per CBSE guidelines and grade levels."
    elif "is homework checked regularly" in question:
        answer = "Yes."
    elif "does the school give holiday homework" in question:
        answer = "Yes, during vacations to reinforce learning."
    elif "does the school have a grievance redressal system" in question:
        answer = "Yes."
    elif "does the school follow the no homework policy for primary classes" in question:
        answer = "Yes, for Grades 1-2 as per CBSE norms."
    elif "does the school have an app for parent communication" in question:
        answer = "Yes, it uses a dedicated parent app for updates."
    elif "does the school have parent orientation programs" in question:
        answer = "Yes, before every academic session begins."
    elif "does the school have an annual magazine" in question:
        answer = "Yes."
    elif "does the school have an alumni association" in question:
        answer = "Currently developing as it is a newer branch."
    elif "does the school provide special education support" in question:
        answer = "Yes, to the extent feasible and with counsellor support."
    elif "does the school have activity clubs" in question:
        answer = "Yes, including eco club, literary club, math club etc."
    elif "does the school conduct career counselling for students" in question:
        answer = "Yes, especially for senior grades."
    elif "does the school conduct parent teacher association meetings" in question:
        answer = "Yes, regularly."
    elif "does the school have an admission test" in question:
        answer = "Yes, for assessment before admission."
    elif "what documents are required for admission" in question:
        answer = "Birth certificate, Aadhar, previous report card, TC (if applicable), passport size photos."
    elif "does the school provide sibling concession" in question:
        answer = "Yes, as per management policies."
    elif "is there any referral benefit for parents" in question:
        answer = "Yes, parents can refer and get benefits as per current offers."
    elif "does the school provide fee installment options" in question:
        answer = "Yes."
    elif "what is the school contact number" in question:
        answer = "9100974444 / 9100984444."
    elif "what is the school email id" in question:
        answer = "info.gandipet@pallavimodelschools.org."
    elif "what is the school motto" in question:
        answer = "\"Knowledge, Character, Excellence.\""
    elif "what is the school vision" in question:
        answer = "To create global citizens with Indian values."
    elif "what is the school mission" in question:
        answer = "To provide holistic education fostering academic excellence and ethical values."
    else:
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": question}
                    ]
                )
                answer = response.choices[0].message.content
            except Exception as e:
                answer = f"Error: {str(e)}"
    if answer is None:
            answer = "Sorry, I don't know the answer."

    chat_history.append({"question": question, "answer": answer})
    return render_template("index.html", chat_history=chat_history, username=current_user.username)

    # ✅ Ensure a fallback return if neither GET nor POST (extra safety)
    return render_template("index.html", chat_history=chat_history, username=current_user.username)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials")
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists")
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully. Please login.")
            return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
