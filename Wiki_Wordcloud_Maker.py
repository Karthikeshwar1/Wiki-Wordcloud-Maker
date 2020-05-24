import sys
import bs4  # to extract data
import matplotlib.pyplot as plt
import requests  # to download html file
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from wordcloud import WordCloud, STOPWORDS  # to create our image
from appUi import Hdialog



class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Basic config
        self.setWindowTitle("Wordcloud Generator")
        self.resize(400, 250)
        self.setWindowIcon(QIcon('res/Wordcloud_maker_icon.png'))

        # Window config
        layout = QVBoxLayout()
        self.text_edit = QLineEdit()
        self.text_edit.setMaxLength(40)
        self.text_edit.setPlaceholderText('Enter the text')

        # Buttons and layout
        generate_button = QPushButton('Generate')
        generate_button.clicked.connect(self.do_wordcloud)

        save_button = QPushButton('Help')
        save_button.clicked.connect(self.help_dialog)

        layout.addWidget(self.text_edit)
        layout.addWidget(generate_button)
        layout.addWidget(save_button)
        widget = QWidget()
        widget.setLayout(layout)

        # Now add this layout to the MainWindow
        self.setCentralWidget(widget)

    # Dialog box to show errors/exceptions
    def error_dialog(self, error_text="Oops!", error_info="Some Error", error_details="Nothing to display"):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setText(error_text)
        msg.setInformativeText(error_info)
        msg.setWindowTitle("Error")
        msg.setDetailedText(error_details)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.button_click)
        msg.exec_()

    # Message box to inform when input is not given
    def no_input(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("Nothing is entered, so Wikipedia's article of the day will be showed")
        msg.setWindowTitle("Info")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.button_click)
        x = msg.exec_()

    # Button event handler
    def button_click(self):
        pass

    # The main part of the program
    # Creates a wordcloud based on the given input
    def do_wordcloud(self):
        text_to_search = self.text_edit.text()

        if text_to_search == "":
            self.no_input()

        try:
            res = requests.get('https://en.wikipedia.org/wiki/' + text_to_search)
            res.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            self.error_dialog(error_text="Looks like there is no article of that name!",
                            error_info="HTTP Error", error_details=str(errh))
            print("Http Error : ", errh)
            sys.exit(4)
        except requests.exceptions.ConnectionError as errc:
            self.error_dialog(error_text="We were unable to connect to the internet!",
                            error_info="Connection Error", error_details=errc)
            print("Connection Error : ", errc)
            sys.exit(4)
        except requests.exceptions.Timeout as errt:
            self.error_dialog(error_text="Your internet is as fast as a lazy sloth!",
                            error_info="Connection timed out", error_details=errt)
            print("Timeout Error : ", errt)
            sys.exit(4)
        except requests.exceptions.RequestException as err:
            self.error_dialog(error_text="Could not request the data from Wikipedia!",
                            error_info="Request Exception Error", error_details=err)
            print("Request Exception Error : ", err)
            sys.exit(4)
        except:
            self.error_dialog(error_text="Oops!",
                            error_info="Unknown error",
                            error_details="We truly don't know what happened. (smh)")
            print("Oops! Some unknown error occured!")
            sys.exit(4)


        print("Wikipedia article found on "+text_to_search)
        # Extract the data
        wiki_data = bs4.BeautifulSoup(res.text, 'lxml')
        wiki_data_elements = wiki_data.select('p')
        # Now print the content in <p> tags
        wiki_text = ""
        for i in range(len(wiki_data_elements)):
            print(wiki_data_elements[i].getText())
            wiki_text += wiki_data_elements[i].getText()

        stopwords = set(STOPWORDS)
        stopwords.update(["later", "page", "needed", "it", "this", "It", "the", "The"])
        wc = WordCloud(background_color="white", max_words=1000,
                       stopwords=stopwords, contour_width=2, contour_color='firebrick')

        # Generate a wordcloud
        wc.generate(wiki_text)
        # wc.to_file(text_to_search + " wordcloud.png")

        plt.figure(figsize=[11, 6])
        plt.imshow(wc, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    def help_dialog(self):
        self.window = QMainWindow()
        self.ui = Hdialog.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.ui.pushButton.clicked.connect(self.window.close)
        self.window.resize(500, 440)
        self.window.setWindowIcon(QIcon('res/information.png'))
        self.window.show()




# Initializing the app
app = QApplication(sys.argv)
app.setStyle('Fusion')

window = MainWindow()
window.show()

# Start the event loop.
app.exec_()