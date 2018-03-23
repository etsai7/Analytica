import os.path
from PreProcPDF import PreProcess
import PyPDF2
import codecs

directory = os.fsencode("./Data/PDF_Converted")

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


        else:
            continue



getDataDir(directory)