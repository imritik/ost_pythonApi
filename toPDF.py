import sys
import os
import win32com.client

wdFormatPDF = 17

in_file = os.path.abspath(sys.argv[1])
out_file = os.path.abspath(sys.argv[2])

word = win32com.client.Dispatch('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()