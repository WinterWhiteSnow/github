from remoteok import remoteok_scrap
from stackoverflow import stackoverflow_scrap
from weworkremotely import weworkremotely_scrap
from flask import Flask, render_template, request, redirect, send_file
from exporter import save_to_file


db = {}
save = []
app = Flask(__name__)

@app.route("/")
def home():
	try:
		previous_word=save
		if previous_word:
			previous_word=save
		else:
			previous_word=["Not yet"]
	except:
		previous_word = ["Not yet"]
	return render_template("main.html", previous_word=previous_word)

@app.route("/search")
def read():
	try:
		word = request.args.get("word")
		if db.get(word):
			result = db[word]
			number = len(result)
			if word not in save:
				save.append(word)
		else:
			a = stackoverflow_scrap(word)
			b = remoteok_scrap(word)
			c = weworkremotely_scrap(word)
			result = a+b+c
			number = len(result)
			db[word]=result
			if word not in save:
				save.append(word)
		return render_template("read.html",result=result,number=number,word=word)
	except:
		return redirect("/")
		
@app.route("/export")
def export():
	try:
		word = request.args.get("word")
		if not word:
			raise Exception()
		wow = db.get(word)
		if not wow:
			raise Exception()
		save_to_file(db=db,word=word)
		return send_file(f"{word}.csv")
	except:
		return redirect("/")

if __name__ == "__main__":
    app.run()
