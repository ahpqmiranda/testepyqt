from main_window import Ui_MainWindow
import sys
import time
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QProgressBar, QListWidget
from PyQt6.QtCore import QRunnable, QObject, QThreadPool, pyqtSignal as Signal, pyqtSlot as Slot


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()




        # self.setWindowTitle("My App")
        # button = QPushButton("Press Me!")
        #
        # self.setCentralWidget(button)
        # self.setFixedSize(QSize(400, 300))
        #
        # # self.maximumSize(QSize(600, 500))
        #
        # button.clicked.connect(self.the_button_was_clicked)
    #
    # def the_button_was_clicked(self):
    #     print("Clicked!")
    #     self.setWindowTitle("Clicked!")


    def closeEvent(self, event):
        print("Closing")
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
