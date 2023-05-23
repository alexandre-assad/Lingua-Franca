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

@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    return(str(select)) # just to see what select is

@app.route('/', methods=['GET', 'POST'])
def getText():
    if request.method == 'POST':
        # Retrieve the text from the textarea
        texte = request.form.get('Traduire')
        toLanguage = request.form.get("traduction_select")
        print(toLanguage)
        
        #traduction = translator.translate(texte,dest=toLanguage).text
        # Print the text in terminal for verification
        #print(traduction)
        
        
        return render_template('index.html',data=langues)
        
        
  
    return render_template('index.html',data=langues)

if __name__ == "__main__":
    app.run()