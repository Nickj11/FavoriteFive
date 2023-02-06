from app import app
from flask import render_template

@app.route('/')
def homePage():
    Favorite_artists = {'Micheal Jackson': 'Micheal.png', "Andre 3000": 'andre3000.png', "J-Cole": 'jcole.png',  "Taylor Swift": 'Taylorswift.png' , "Lil Wayne": 'lilwayne.png'}
    return render_template('Home.html', Favorite_artists = Favorite_artists )


# @app.route('/contact')
# def contactPage():
#     return render_template('contact.html')

# @app.route('/about')
# def aboutPage():
#     return render_template('about.html')

# @app.route('/contact')
# def contactPage():
#     return render_template('contact.html')


# @app.route('/sign-up')
# def SignPage():
#     return render_template('sign-up.html')
    