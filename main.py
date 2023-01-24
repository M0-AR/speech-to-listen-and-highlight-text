from PyPDF2 import PdfReader
from PyQt5.QtGui import QTextCursor, QTextCharFormat
from gtts import gTTS

from pdfminer.high_level import extract_text

# with open("book.pdf", "rb") as file:
#     text = extract_text(file)
#     tts = gTTS(text)
#     tts.save("book.mp3")


# import sounddevice as sd
# import soundfile as sf
# data, fs = sf.read("book.mp3")
# sd.play(data, fs)
# status = sd.wait()


# import fitz
# pdf_document = fitz.open("book.pdf")
# page = pdf_document[0]
# highlight = page.add_highlight((10, 10, 50, 50))
#

# Read page by page's number [5] page number five
# from PyPDF2 import PdfReader
# pdf = PdfReader(open('book.pdf', 'rb'))
# page = pdf.pages[5]
# highlight = page.extract_text()
# print(highlight)


from PyQt5.QtCore import Qt, QTextStream, QFile, QIODevice, QThread
from PyQt5.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QDialog
import sys
import pyttsx3


class MyDialog(QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)

        self.engine = pyttsx3.init()
        from PyPDF2 import PdfReader
        # load pdf file
        pdf = PdfReader(open('book.pdf', 'rb'))
        # extract text from specific page number
        text = pdf.pages[5].extract_text()

        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit.setText(text)

        layout = QVBoxLayout(self)
        layout.addWidget(self.textEdit)

        self.play_button = QPushButton("Play", self)
        self.play_button.clicked.connect(self.play_audio)
        layout.addWidget(self.play_button)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop_audio)
        layout.addWidget(self.stop_button)

        self.highlight_button = QPushButton("Highlight", self)
        self.highlight_button.clicked.connect(self.highlight)
        layout.addWidget(self.highlight_button)

        self.setWindowTitle("PDF Reader")

    def play_audio(self):
        self.engine.say(self.textEdit.toPlainText())
        self.engine.runAndWait()

    def stop_audio(self):
        self.engine.stop()

    def highlight(self):
        cursor = self.textEdit.textCursor()
        cursor.select(QTextCursor.LineUnderCursor)
        cursor.setCharFormat(QTextCharFormat().setBackground(Qt.yellow))


app = QApplication(sys.argv)
dialog = MyDialog()
dialog.show()
sys.exit(app.exec_())
