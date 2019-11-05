from flask import Flask, render_template, redirect, url_for, request
from histogram import histogram
from stochastic_sampling import stochastic_sample

# creating a histogram
histo = histogram()
# Flask app for tweet generator
app = Flask(__name__)


def capitalize_first_word(words):
    """Capitalize the word letter of a string.
       Param: words(list): str to go in sentence
       Return: modified_words(list): str where first str is capitalized
    """
    first_word = words[0]
    first_letter = first_word[0].upper()
    rest_of_word = first_word[1:]
    reassigned_word = first_letter + rest_of_word
    words[0] = reassigned_word
    return words


@app.route("/")
def index():
    '''Display a sentence on each reload.'''
    # generate 10 words on default for first load of page
    words = list()
    for i in range(10):
        words.append(stochastic_sample(histo))
    words = capitalize_first_word(words)
    return render_template("index.html", words=words)


@app.route("/reload")
def reload():
    '''Redirect user to a new load of the home page.'''
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
