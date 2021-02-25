from flask import Flask, render_template, request, session, redirect, url_for, send_file
from functools import wraps
import time
import os
  
app = Flask(__name__)
app.secret_key = "Pick a secure key?? Nah!"

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/solve" , methods=["POST"])
def solve():
    f=open("kekw.osf",'w')
    j=0
    #Read form data, write to file in proper format.
    for i in request.form.keys():
        j+=1
        if (request.form[("000"+str(j))[-3:]]==""):
            print('0',end=' ',file=f)
        else:
            print(request.form[("000"+str(j))[-3:]],end=' ',file=f)
        if (j%9==0):
            print(file=f)
    f.close()
    #Call the sudoku solver on the file we made
    os.system("<compiled solver name> kekw.osf kekw.osf")
    #Read the solution into the output template
    f=open("kekw.osf",'r')
    j=dict()
    k=0
    for t in f.readlines():
        for i in t:
            if i.isnumeric():
                k+=1
                j[("0000"+str(k))[-3:]]=i
    f.close()
    return render_template("output.html",item=j)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)
 