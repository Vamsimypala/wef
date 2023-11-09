from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('me\interface.html')

@app.route('/csesyllabus')
def csesyllabus():
    return render_template('csesyllabus.html')

@app.route('/1-1subjects')
def subjects_1_1():
    return render_template('1-1subjects.html')

@app.route('/1-1c')
def c_language_1_1():
    return render_template('1-1c.html')

@app.route('/1-1eng')
def english_1_1():
    return render_template('1-1eng.html')

@app.route('/1-1mat')
def mathematics_1_1():
    return render_template('1-1mat.html')

@app.route('/ecesyllabus')
def ecesyllabus():
    return render_template('ecesyllabus.html')

@app.route('/loginpage1')
def loginpage1():
    return render_template('loginpage1.html')

@app.route('/mtech')
def mtech():
    return render_template('mtech.html')

@app.route('/btech')
def btech():
    return render_template('btech.html')

@app.route('/1-1phy')
def phy():
    return render_template('1-1phy.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/process')
def process():
    return render_template('process.html')

if __name__ == '__main__':
    app.run(debug=True)
