1st step :
-I downloaded the API by using the library googletrans
Because it is an old library, i needed to download a new version, with this line on the terminal :

py -m pip install googletrans==4.0.0-rc1

So, I use a very easy library that i would talk more later

2st step :
-I downloaded the library Flask on python with this line on the terminal :
py -m pip install Flask
I wrote the basic code to run it (only 7 lines !) then i started to learn about the syntax and everything else on :
https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application
https://flask.palletsprojects.com/en/2.2.x/
https://flask.palletsprojects.com/en/2.2.x/tutorial/
https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3


3rd step :
- I build the shape of the website, without adding my translator
I used a lot https://stackoverflow.com to all the technicals questions i had.
For exemple : 
https://stackoverflow.com/questions/69219696/flask-how-can-i-send-a-text-from-python-to-a-html-textarea
https://stackoverflow.com/questions/32019733/getting-value-from-select-tag-using-flask

4th step :
-I try on a python script the api googletrans
It was very easy. I created an Translator object, then it has the method translate which takes parameters (text,source_language,destination_language) and return a lot of informations. The one that was important was .text

So for exemple :
Translator_object = Translator()
Translator_object.translate("Salut mon ami !",src=fr,dest=en).text
=> Hi my friend

It has a second usefull method, the detect one, which can detect the source_language from a message.
So for exemple:
Translator.detect("Salut mon ami").lang
=> frby

5th step:
-I link the html file with the translator, using submit input

