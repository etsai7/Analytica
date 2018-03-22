import sys
import os.path
import PyPDF2
directory = os.fsencode("./Data")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".pdf") or filename.endswith(".py"):
        print(os.path.join(directory, file).decode("utf-8"))
        # print(file)
        continue
    else:
        continue