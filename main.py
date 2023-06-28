# Import
from flask import Flask, render_template,request, redirect
# Connecting the database library
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Connecting SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creating a DN
db = SQLAlchemy(app)
# Creating a table

class Card(db.Model):
    # Creating columns
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Title
    title = db.Column(db.String(100), nullable=False)
    # Description
    subtitle = db.Column(db.String(300), nullable=False)
    # Text
    text = db.Column(db.Text, nullable=False)

    # Outputting the object and id
    def __repr__(self):
        return f'<Card {self.id}>'
    

#Assignment #2. Create the User table









#Запуск страницы с контентом
@app.route('/', methods=['GET','POST'])
def login():
        error = ''
        if request.method == 'POST':
            form_login = request.form['email']
            form_password = request.form['password']
            
            #Задание №4. Реализовать проверку пользователей
            


            
        else:
            return render_template('login.html')



@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        login= request.form['email']
        password = request.form['password']
        
        #Задание №3. Реализовать запись пользователей
        

        
        return redirect('/')
    
    else:    
        return render_template('registration.html')


#Запуск страницы с контентом
@app.route('/index')
def index():
    #Отображение объектов из БД
    cards = Card.query.order_by(Card.id).all()
    return render_template('index.html', cards=cards)

#Запуск страницы c картой
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get(id)

    return render_template('card.html', card=card)

#Запуск страницы c созданием карты
@app.route('/create')
def create():
    return render_template('create_card.html')

#Форма карты
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        #Создание объкта для передачи в дб

        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')





if __name__ == "__main__":
    app.run(debug=True)