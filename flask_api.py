from flask import Flask,render_template, request
from elasticsearch import Elasticsearch
#from flask.templating import render_template
app = Flask(__name__, template_folder='template')

es= Elasticsearch
doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': '19-10-2019',
}
@app.route('/', methods=["GET", "POST"])
def index():
    q=  request.form.get("q")
    if q is not None:
        resp= es.search(index='hotels', doc_type='hotel', body={"query": {"match_all": {}}})
        return render_template("index.html", q=q, respnse= resp)
    return render_template('index.html')

app.run(debug=True, port=3000)
