from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)
        self.label1 = QLabel("Enter your IP:", self)
        self.ip = QLineEdit(self)
        self.ip.move(10, 30)
        
        self.label2 = QLabel("Api key:", self)
        self.api = QLineEdit(self)
        self.label2.move(10,80)
        self.api.move(10,100)
     
        self.label3 = QLabel("Hostname:", self)
        self.host = QLineEdit(self)
        self.label3.move(10,130)
        self.host.move(10,160)
      
        self.button = QPushButton("Send", self)
        self.button.move(10,190 )

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()


    
    def _create_url(self, res):
        openstreetmap_url = "https://www.openstreetmap.org/?mlat=%s&mlon=%s#map=12" % (res["Latitude"],res["Longitude"] )
        return openstreetmap_url

    def __query(self, hostname, ip, api):
        url = "http://%s/ip/%s?key=%s" % (hostname, ip, api)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()
    
    def on_click(self):
        hostname = self.host.text()
        api = self.api.text()
        ip = self.ip.text()

        if hostname == "" or ip =="" or api =="":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname,ip , api)
            if res:
                self.label2.setText("Hello")
                self.label2.adjustSize()
                self.show()
                Urls = main._create_url(res)
                QDesktopServices.openUrl(QUrl(Urls))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
   
    app.exec_()
   
    


