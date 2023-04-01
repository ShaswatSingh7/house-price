import pandas as pd
from flask import Flask,render_template
app=Flask(__name__)
data=pd.read_csv('cleaneddata.csv')
@app.route("/")
def ind():
    locations=sorted(data['location'].unique())
    return render_template('index.html',locations=locations)
if __name__ == '__main__':
    app.run(debug=True,port=http://127.0.0.1:5500/)
