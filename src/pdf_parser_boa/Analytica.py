import os.path
import PyPDF2
import codecs
import plotly.plotly as py
from plotly.graph_objs import *
from PIL import Image
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from re import sub
from decimal import Decimal

directory = os.fsencode("../../Data/PDF_Converted")
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
        elif "Summary of Transactions" in line:
            print("Found summary of transactions")
            Categories = []
            while("Page" not in line):
                line = next(file)
                print(line)

def Yearly_Total_Bar():

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
    # py.sign_in('username', 'api_key')
    year = []
    val = []
    for key in yearly_total:
        year.append(key)
        val.append(yearly_total[key])

    print(year)
    print(val)
    trace1 = {
        "x": year,
        "y": val,
        "hoverinfo": "x+y+text",
        "marker": {
            "color": "rgb(85, 185, 237)",
            "line": {
                "color": "rgb(8,48,107)",
                "width": 2
            }
        },
        "opacity": 0.7,
        "orientation": "v",
        "text": val,
        "textposition": "auto",
        "textsrc": "etsai7:3:d9b6a5",
        "type": "bar",
        "uid": "550fd3",
        "xsrc": "etsai7:3:af110a",
        "ysrc": "etsai7:3:84691f"
    }
    data = Data([trace1])
    layout = {
        "autosize": True,
        "paper_bgcolor": "rgb(255, 255, 255)",
        "plot_bgcolor": "rgb(56, 50, 50)",
        "title": "Year Total",
        "xaxis": {
            "autorange": False,
            "gridcolor": "rgb(25, 24, 24)",
            "linecolor": "rgb(234, 57, 57)",
            "range": [2013, 2018],
            "showgrid": False,
            "showline": False,
            "title": "Year<br>",
            "type": "linear"
        },
        "yaxis": {
            "autorange": True,
            "gridcolor": "rgb(141, 136, 136)",
            "range": [0, 11140.2526316],
            "title": "Total Spent ($)",
            "type": "linear"
        }
    }
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig)

    py.iplot(data, filename='Analytica-bar')

getDataDir(directory)
print(yearly_total)

# Uncomment to save figure to plotly the yearly total
# Yearly_Total_Bar()



# This is to show the image
fig = py.get_figure('https://plot.ly/~etsai7/2')
py.image.save_as(fig,'etsai7.png')

img = mpimg.imread('etsai7.png')
plt.imshow(img)
plt.show()