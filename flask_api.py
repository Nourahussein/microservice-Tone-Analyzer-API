from flask import Flask,render_template, request
from elasticsearch import Elasticsearch
#from flask.templating import render_template
app = Flask(__name__, template_folder='template')

es= Elasticsearch

@app.route('/', methods=["GET", "POST"])
def index():
    q=  request.form.get("q")
    if q is not None:
        resp= es.search(index='hotels',  body={"query": {"match_all": {}}})
        print('Got %d hits:' %res['hits']['total'])

        return render_template("index.html", q=q, respnse= resp)
    return render_template('index.html')

app.run(debug=True, port=3000)
