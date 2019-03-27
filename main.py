from flask import Flask, render_template
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="password",
	  database="flaskapp"
	)

mycursor = mydb.cursor()

df = pd.read_sql('SELECT * FROM BettingData WHERE Time >= NOW() - INTERVAL 8 HOUR', con=mydb)
df = df[["HT_Name", "AT_Name", "HT_Score", "AT_Score", "MatchTime", "HT_Wins", "Draw", "AT_Wins"]]
df = df.iterrows()

#mycursor.execute("SELECT * FROM BettingData WHERE Time >= NOW() - INTERVAL 4 HOUR")

#myresult = mycursor.fetchall()
#print (myresult, type(myresult))
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html", data=df)
@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(debug=True)