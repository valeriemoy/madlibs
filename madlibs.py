"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return render_template("home.html")


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Display the Mad Lib form"""

    is_playing = request.args.get("play")

    if is_playing == "False":
        return render_template("goodbye.html")
    else:
        adjectives = ["squishy", "slithering", "irate", "fluffy", "shiny"]
        return render_template("game.html", adjectives=adjectives)


@app.route('/madlib')
def show_madlib():
    """Display the filled-in Mad Lib"""

    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    verb = request.args.get("verb")
    all_animals = request.args.getlist("animals")
    num_animals = len(all_animals)
    first_animals = all_animals[0:-1]
    last_animal = all_animals[-1:]

    return render_template("madlibs.html",
                           person=person,
                           color=color,
                           noun=noun,
                           adjective=adjective,
                           verb=verb,
                           num_animals=num_animals,
                           first_animals=first_animals,
                           last_animal=last_animal)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
