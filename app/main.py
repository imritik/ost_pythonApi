from flask import Flask, render_template, request
import os
import extract

#For testing purposes only
from time import time
from statistics import mean

app = Flask(__name__)
folder_path = os.getcwd() + '/CVs'
os.system("mkdir CVs")

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template('index.html', data=None)
    
    if request.method == "POST":
        t0 = time()
        t3 = time()
        convert_times = list()
        extract_times = list()
        for f in request.files.getlist('files'):
            t1 = time()
            #Obtain, Save and convert given CV
            f.save(folder_path+'/'+f.filename)
            filename = folder_path+'/'+f.filename
            if f.content_type != "application/pdf":
                name, ext = os.path.splitext(filename)
                os.system("py toPDF.py {} {}".format(filename, name+".pdf"))
                os.remove(filename)
                filename = name+".pdf"
            t2 = time()
            convert_times.append(t2-t1)
            #Email and Phone Number Extraction
            emails, phones = extract.extract(filename)
            row = ["\t".join(emails), "\t".join(phones), filename]
            extract.updateCSV(row)
            t3 = time()
            extract_times.append(t3-t2)
        
        print("\nTotal time to complete request = {}".format(t3-t0))
        print("Average time for conversion = {}".format(mean(convert_times)))
        print("Average time for data extraction = {}".format(mean(extract_times)))


        return render_template('index.html', data = {"message": True})
