from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)


class User:
    def __init__(self, id, username, password, email, token, date_created, character):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.token = token
        self.date_created = date_created
        self.character = character

    def __repr__(self):
        return f'<User: {self.username}>'


class Heroes:
    def __init__(self, id, name, description, owner, date_created, super_power, comics_appeared_in):
        self.id = id
        self.name = name
        self.description = description
        self.owner = owner
        self.date_created = date_created
        self.super_power = super_power
        self.comics_appeared_in = comics_appeared_in


users = []
users.append(User(id=1, username='Chris', password='123ABC', email='chris123@gmail.com'))
users.append(User(id=2, username='Johnny', password='John5032', email='johnny43@gmail.com'))
users.append(User(id=3, username='Carlos', password='444Ac!', email='carloshenry@gmail.com'))

heroes = []
users.append(Heroes(id=1, name='Iron Man', description='Iron Man is a billionare.', owner='Marvel', date_created='1963', superpower='Powered armor', comics_appeared_in='80'))
users.append(Heroes(id=2, name='Thor', description='Thor is a thunder god.', owner='Marvel', date_created='1962', superpower='Thunder god', comics_appeared_in='80'))
users.append(Heroes(id=3, name='Batman', description='Batman is a billionare.', owner='DC Comics', date_created='1939', superpower='Super rich', comics_appeared_in='80'))

app = Flask(__name__)
app.secret_key = '4X21#4@89fi'


@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')

