import pyttsx3
import PyPDF2

book = open('psyco.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(22, pages):
    page = pdfReader.getPage(22)
    text = page.extractText()
    speaker.say(text)
    # speaker.say('Hi Nani')
    speaker.runAndWait()