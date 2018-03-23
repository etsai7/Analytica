import os.path
import PyPDF2
import codecs
import plotly.plotly as py
from PIL import Image
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from re import sub
from decimal import Decimal

directory = os.fsencode("./Data/PDF_Converted")
yearly_total = {}


def getDataDir(directory):
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".pdf"):

            pdffilename = './Data/PDF_Converted/' + str(filename)
            o = open(pdffilename, 'rb')
            pdfFileReader = PyPDF2.PdfFileReader(o)
            fname = './Data/Text/Pre/' + filename.rstrip("_pdf.pdf") + '_proc.txt'
            file = filename.rstrip(".pdf") + '_proc.txt'
            f = codecs.open(fname, 'w',"ISO-8859-1")

            for x in range(0, 2): # Only need 1st 2 pages
                text = pdfFileReader.getPage(x)
                textp = text.extractText()
                f.write(textp)
            f.close()
            fileSave = PreProcess(fname, file)

            # Summary
            print("File Name: " + filename)
            print("\t%s has %d pages." % (filename, pdfFileReader.getNumPages()))
            print("\tPDF File Dir     : " + pdffilename)
            print("\tPreProc File Dir : " + fname)
            print("\tPostProc File Dir: " + fileSave + "\n")

            DataExtract(fileSave, file)

        else:
            continue

def PreProcess(filedir, file):
    fileSave = "./Data/Text/Post/"+ file
    with open(filedir, 'rb') as infile, open( fileSave, 'w') as outfile:
        for line in infile:
            if not line.strip(): continue  # skip the empty line
            outfile.write(line.decode("ISO-8859-1").rstrip("\r\n"))  # non-empty line. Write it to output''''''
            outfile.write("\n")
    return fileSave

def DataExtract(fileSave,fileName):
    file = open(fileSave, 'r')
    for line in file:
        if "Total spent" in line:
            year = fileName[0:4]
            money = next(file).rstrip("\n")
            total = Decimal(sub(r'[^\d.]', '', money))

            print(line.rstrip("\n") + " " + str(total) + " in " + year + "\n")
            yearly_total[year] = (total)

getDataDir(directory)
print(yearly_total)

year = []
val = []
for key in yearly_total:
    year.append(key)
    val.append(yearly_total[key])

print(year)
print(val)
# data = [go.Bar(
#             x = year,
#             y = val,
#             text=val,
#             textposition = 'auto',
#             marker=dict(
#                 color='rgb(158,202,225)',
#                 line=dict(
#                     color='rgb(8,48,107)',
#                     width=1.5),
#             ),
#             opacity=0.6
#     )]
#
# py.iplot(data, filename='Analytica-bar')

fig = py.get_figure('https://plot.ly/~etsai7/2')
py.image.save_as(fig,'etsai7.png')

img = mpimg.imread('etsai7.png')
plt.imshow(img)
plt.show()