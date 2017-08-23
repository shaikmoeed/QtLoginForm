from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import time

from ui import css_ui


class Beautiful(QDialog, css_ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        systray_img = QIcon("systray.jpg")
        systray = QSystemTrayIcon(systray_img, self)

        menu = QMenu()
        restore = QAction("Restore", self)
        exit = QAction("Close", self)

        menu.addActions([restore, exit])
        systray.setContextMenu(menu)
        systray.show()
        
        systray.showMessage("Beautiful", "This is a notification "
                                         "visible in system tray", QSystemTrayIcon.Warning)

        restore.triggered.connect(self.reset)
        exit.triggered.connect(self.close)

    def reset(self):
        print("Restore is working!!")


app = QApplication(sys.argv)
dialog = Beautiful()

splash_image = QPixmap("systray.jpg")
splash = QSplashScreen(splash_image)
splash.show()

time.sleep(1)

dialog.show()
splash.finish(dialog)
app.exec_()
