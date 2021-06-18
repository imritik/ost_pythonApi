import re
from csv import writer
from slate3k import PDF

def extract(filename):
    emails = []
    phones = []
    file = open(filename, 'rb')
    text = str(PDF(file))
    file.close()
    emails += re.findall(r"[^(\\t\\n:)][a-z0-9\.+_]+@[a-z0-9\.+_]+\.[a-z]+", text)
    phones += re.findall(r'\+?[0-9]?[0-9]?[- ]?[0-9]{3}[- ]?[0-9]{3}[- ]?[0-9]{4}', text)
    return emails, phones

def updateCSV(row):
    file = open('contacts.csv', 'a')
    write = writer(file)
    write.writerow(row)
    file.close()