import pyttsx3
import PyPDF3
from tkinter.filedialog import *

book = askopenfilename()
pdfReader = PyPDF3.PdfFileReader(book)
pages = pdfReader.numPages
print("Nombre de pages:",pages)
speaker = pyttsx3.init()
for num in range(1, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    print(num)
    speaker.runAndWait()