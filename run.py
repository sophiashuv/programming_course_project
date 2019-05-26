from flask import Flask, render_template, request, session
from main import *
app = Flask(__name__, template_folder="templates", static_folder='static')
app.secret_key = 'super secret key'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index.html')
def back_home():
    return render_template('index.html')


@app.route('/help.html')
def help_page():
    return render_template('help.html')


@app.route('/login.html', methods=['GET', 'POST'])
def start_my_page():
    return render_template('login.html')


@app.route('/logged', methods=['GET', 'POST'])
def logging():
    password = request.form.get('psw')
    login = request.form.get('login')
    session['login'] = login
    if check_login(login, password):
        return render_template('my-page.html')
    else:
        return render_template('login.html')


@app.route('/redirect')
def redirect():
    return render_template('reestr-form.html')


@app.route('/my-page.html', methods=['GET', 'POST'])
def my_page():
    return render_template('my-page.html')


@app.route('/renewpage', methods=['GET', 'POST'])
def submit():
    daily_data = dict()
    daily_data['login'] = session.get('login')
    daily_data['date'] = request.form.get('day')
    daily_data['time'] = request.form.get('time')
    daily_data['value'] = request.form.get('level')
    daily_data['meals'] = request.form.get('food')
    daily_data['grams'] = request.form.get('weight')
    daily_data['consumed'] = food_preferenses(session.get('login'), daily_data['meals'], daily_data['grams'], daily_data['date'])[1]
    diadram_xo(session.get('login'), daily_data['meals'], daily_data['grams'], daily_data['date'])
    insulin_dose_picture(daily_data['login'], daily_data['value'])
    add_user_data(session.get('login'), daily_data)
    daily_diagram(daily_data['login'])
    weekly_diagram(daily_data['login'])

    if request.method == 'POST':
        return render_template('my-page2.html')
    return render_template('my-page.html')


@app.route('/back', methods=['GET', 'POST'])
def back():
    return render_template('my-page.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/reestr-form.html')
def registration():
    return render_template('reestr-form.html')


@app.route("/adduser", methods=['GET', 'POST'])
def add_to_base():
    user = dict()
    user['name'] = request.form.get('name')
    user['surname'] = request.form.get('surname')
    user['login'] = request.form.get('login')
    user['password'] = request.form.get('password')
    user['tel_number'] = request.form.get('tel_number')
    user['country'] = request.form.get('country')
    user['city'] = request.form.get('city')
    user['address'] = request.form.get('address')
    user['email'] = request.form.get('email')
    user['sex'] = request.form.get('sex')
    user['age'] = request.form.get('age')
    user['date_of_birth'] = request.form.get('date_of_birth')
    user['height'] = request.form.get('height')
    user['weight'] = request.form.get('weight')
    user['type_of_diabet'] = request.form.get('type_of_diabet')
    user['physical_activity'] = request.form.get('physical_activity')
    user['type_of_short_act_insulin'] = request.form.get('type_of_short_act_insulin')
    user['type_of_long_act_insulin'] = request.form.get('type_of_long_act_insulin')
    user['normal_level_of_shugar'] = request.form.get('normal_level_of_shugar')
    user['XO'] = request.form.get('XO')
    user['doctor'] = request.form.get('doctor')
    user['doctor_email'] = request.form.get('doctor_email')
    user['doctor_tel'] = request.form.get('doctor_tel')
    creating_json(request.form.get('login'))
    add_user(user)

    if request.method == 'POST':
        return render_template('my-page.html')
    elif request.method == 'GET':
        return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=False)
