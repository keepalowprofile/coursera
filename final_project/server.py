import machinetranslation
from machinetranslation.translator import english_to_french
from machinetranslation.translator import french_to_english

from flask import Flask, render_template, request

app = Flask(__name__)
app=Flask(__name__,template_folder='Templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/englishToFrench', methods=['POST'])
def translate_english_to_french():
    english_text = request.form['englishText']
    english_translated_text = english_to_french(english_text)
    return english_translated_text

@app.route('/frenchToEnglish', methods=['POST'])
def translate_french_to_english():
    french_text = request.form['englishText']
    french_translated_text = french_to_english(french_text)
    return french_translated_text

if __name__ == '__main__':
    app.run(debug='TRUE',port=8080)
