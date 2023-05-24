from flask import *
from googletrans import Translator, LANGUAGES

translator = Translator(service_urls=[
      'translate.google.com',])

langues = LANGUAGES
print(langues)




print(translator.translate('veritas lux mea',dest="fr").text)
app = Flask(__name__)


    
@app.route('/')
def index():
    return render_template('index.html',data=langues)


@app.route('/', methods=['GET', 'POST'])
def getText():
    if request.method == 'POST':
        # Retrieve the text from the textarea
        texte = request.form.get('Traduire')
        toLanguage = request.form.get("traduction_select")
        fromLanguage = request.form.get("traduire_select")
       
        
        traduction = translator.translate(texte,src=fromLanguage,dest=toLanguage).text
        auto_language = f"La langue détectée : {langues[translator.detect(texte).lang]}"
       
        
        
        return render_template('index.html',data=langues,sample_input=traduction,sample_text=texte,detect_language=auto_language)
        
   
  
    return render_template('index.html',data=langues)

if __name__ == "__main__":
    app.run()