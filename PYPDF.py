import pyttsx3
from PyPDF2 import PdfReader 

#Load the PDF
book = open('A_Very_Short_Story_by_E_Hemingway.pdf', 'rb')
pdfReader = PdfReader(book)  #class usage
pages = len(pdfReader.pages)  # get number of pages
print(f"Total pages: {pages}")

#Initialize text-to-speech
tts = pyttsx3.init()

#Read each page
for page_num in range(pages):
    text = pdfReader.pages[page_num].extract_text()
    if text:  #  Check if there's text on the page
        tts.say(text)

#Speak it
tts.runAndWait()





