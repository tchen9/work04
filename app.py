from flask import Flask

my_app = Flask(__name__)

@my_app.route("/")
def hi():
    return 'Welcome!!!'

@my_app.route("/games")
def game():
    return 'No games available yet.'

@my_app.route("/contact")
def contact():
    return 'Come back soon.'

if __name__ == '__main__':
    my_app.debug == True
    my_app.run()
