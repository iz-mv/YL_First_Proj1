from PyQt5 import QtCore, QtGui, QtWidgets
import sys
# Импорт библиотеки
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow

# Подключение к БД
con = sqlite3.connect("proj.db")

# Создание курсора
cur = con.cursor()


def bigmak():
    result = cur.execute("""SELECT products FROM burgers
        WHERE id = 1""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def bigmak_p():
    result = cur.execute("""SELECT price FROM burgers
        WHERE id = 1""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def makchicken():
    result = cur.execute("""SELECT products FROM burgers
        WHERE id = 2""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def makchicken_p():
    result = cur.execute("""SELECT price FROM burgers
        WHERE id = 2""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def dv_fileofish():
    result = cur.execute("""SELECT products FROM burgers
        WHERE id = 3""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def dv_fileofish_p():
    result = cur.execute("""SELECT price FROM burgers
        WHERE id = 3""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def dv_royal():
    result = cur.execute("""SELECT products FROM burgers
        WHERE id = 4""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def dv_royal_p():
    result = cur.execute("""SELECT price FROM burgers
        WHERE id = 4""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def gamburger():
    result = cur.execute("""SELECT products FROM burgers
        WHERE id = 5""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def gamburger_p():
    result = cur.execute("""SELECT price FROM burgers
        WHERE id = 5""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def chickenburger():
    result = cur.execute("""SELECT products FROM burgers
        WHERE id = 6""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def chickenburger_p():
    result = cur.execute("""SELECT price FROM burgers
        WHERE id = 6""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def fileofish():
    result = cur.execute("""SELECT products FROM burgers
        WHERE id = 7""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def fileofish_p():
    result = cur.execute("""SELECT price FROM burgers
        WHERE id = 7""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def bigtasty():
    result = cur.execute("""SELECT products FROM burgers
        WHERE id = 8""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def bigtasty_p():
    result = cur.execute("""SELECT price FROM burgers
        WHERE id = 8""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def french_fries():
    result = cur.execute("""SELECT products FROM snacks
        WHERE id = 1""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def frensh_fries_p():
    result = cur.execute("""SELECT price FROM snacks
        WHERE id = 1""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def chicken_wings():
    result = cur.execute("""SELECT products FROM snacks
        WHERE id = 2""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def chicken_wings_p():
    result = cur.execute("""SELECT price FROM snacks
        WHERE id = 2""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def nuggets():
    result = cur.execute("""SELECT products FROM snacks
        WHERE id = 3""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def nuggets_p():
    result = cur.execute("""SELECT price FROM snacks
        WHERE id = 3""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def strips():
    result = cur.execute("""SELECT products FROM snacks
        WHERE id = 4""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def strips_p():
    result = cur.execute("""SELECT price FROM snacks
        WHERE id = 4""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def rustic_potatoes():
    result = cur.execute("""SELECT products FROM snacks
        WHERE id = 5""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def rustic_potatoes_p():
    result = cur.execute("""SELECT price FROM snacks
        WHERE id = 5""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def shrimps():
    result = cur.execute("""SELECT products FROM snacks
        WHERE id = 6""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def shrimps_p():
    result = cur.execute("""SELECT price FROM snacks
        WHERE id = 6""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def cheese_sticks():
    result = cur.execute("""SELECT products FROM snacks
        WHERE id = 7""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def cheese_sticks_p():
    result = cur.execute("""SELECT price FROM snacks
        WHERE id = 7""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def salad():
    result = cur.execute("""SELECT products FROM snacks
        WHERE id = 8""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def salad_p():
    result = cur.execute("""SELECT price FROM snacks
        WHERE id = 8""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def cappuccino():
    result = cur.execute("""SELECT products FROM drinks
        WHERE id = 1""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def cappuccino_p():
    result = cur.execute("""SELECT price FROM drinks
        WHERE id = 1""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def latte():
    result = cur.execute("""SELECT products FROM drinks
        WHERE id = 2""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def latte_p():
    result = cur.execute("""SELECT price FROM drinks
        WHERE id = 2""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def americano():
    result = cur.execute("""SELECT products FROM drinks
        WHERE id = 3""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def americano_p():
    result = cur.execute("""SELECT price FROM drinks
        WHERE id = 3""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def black_tea():
    result = cur.execute("""SELECT products FROM drinks
        WHERE id = 4""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def black_tea_p():
    result = cur.execute("""SELECT price FROM drinks
        WHERE id = 4""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def cola():
    result = cur.execute("""SELECT products FROM drinks
        WHERE id = 5""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def cola_p():
    result = cur.execute("""SELECT price FROM drinks
        WHERE id = 5""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def fanta():
    result = cur.execute("""SELECT products FROM drinks
        WHERE id = 6""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def fanta_p():
    result = cur.execute("""SELECT price FROM drinks
        WHERE id = 6""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def sprite():
    result = cur.execute("""SELECT products FROM drinks
        WHERE id = 7""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def sprite_p():
    result = cur.execute("""SELECT price FROM drinks
        WHERE id = 7""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def cocktail():
    result = cur.execute("""SELECT products FROM drinks
        WHERE id = 8""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def cocktail_p():
    result = cur.execute("""SELECT price FROM drinks
        WHERE id = 8""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def s_1():
    result = cur.execute("""SELECT products FROM sauces
        WHERE id = 1""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def s_1_p():
    result = cur.execute("""SELECT price FROM sauces
        WHERE id = 1""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def s_2():
    result = cur.execute("""SELECT products FROM sauces
        WHERE id = 2""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def s_2_p():
    result = cur.execute("""SELECT price FROM sauces
        WHERE id = 2""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def s_3():
    result = cur.execute("""SELECT products FROM sauces
        WHERE id = 3""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def s_3_p():
    result = cur.execute("""SELECT price FROM sauces
        WHERE id = 3""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def s_4():
    result = cur.execute("""SELECT products FROM sauces
        WHERE id = 4""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def s_4_p():
    result = cur.execute("""SELECT price FROM sauces
        WHERE id = 4""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def s_5():
    result = cur.execute("""SELECT products FROM sauces
        WHERE id = 5""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def s_5_p():
    result = cur.execute("""SELECT price FROM sauces
        WHERE id = 5""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def s_6():
    result = cur.execute("""SELECT products FROM sauces
        WHERE id = 6""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def s_6_p():
    result = cur.execute("""SELECT price FROM sauces
        WHERE id = 6""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def s_7():
    result = cur.execute("""SELECT products FROM sauces
        WHERE id = 7""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def s_7_p():
    result = cur.execute("""SELECT price FROM sauces
        WHERE id = 7""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def s_8():
    result = cur.execute("""SELECT products FROM sauces
        WHERE id = 8""")
    for elem in result:
        z = str(elem)[2:-3]
        return z


def s_8_p():
    result = cur.execute("""SELECT price FROM sauces
        WHERE id = 8""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


def fp_beg():
    result = cur.execute("""SELECT fp FROM final_price
        WHERE id = 1""")
    for elem in result:
        z = str(elem)[1:-2]
        return z


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("McDonald's_Golden_Arches.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.m = QtWidgets.QTabWidget(self.centralwidget)
        self.m.setEnabled(True)
        self.m.setGeometry(QtCore.QRect(-10, 0, 1280, 720))
        self.m.setMinimumSize(QtCore.QSize(1280, 720))
        self.m.setMaximumSize(QtCore.QSize(1280, 720))
        self.m.setBaseSize(QtCore.QSize(1000, 750))
        self.m.setStyleSheet("background-color: rgb(220, 251, 255);\n"
                             "background-color: rgb(229, 229, 229);")
        self.m.setObjectName("m")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.frame_1_1 = QtWidgets.QFrame(self.tab_1)
        self.frame_1_1.setGeometry(QtCore.QRect(50, 40, 250, 300))
        self.frame_1_1.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_1_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1_1.setObjectName("frame_1_1")
        self.photo_1_1 = QtWidgets.QLabel(self.frame_1_1)
        self.photo_1_1.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_1_1.setText("")
        self.photo_1_1.setPixmap(QtGui.QPixmap("emojis/mac/BigMac.webp"))
        self.photo_1_1.setScaledContents(True)
        self.photo_1_1.setObjectName("photo_1_1")
        self.name_1_1 = QtWidgets.QLabel(self.frame_1_1)
        self.name_1_1.setGeometry(QtCore.QRect(85, 215, 80, 30))
        self.name_1_1.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_1_1.setObjectName("name_1_1")
        self.ButtonPlus_1_1 = QtWidgets.QPushButton(self.frame_1_1)
        self.ButtonPlus_1_1.setGeometry(QtCore.QRect(145, 255, 30, 30))
        self.ButtonPlus_1_1.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_1_1.setObjectName("ButtonPlus_1_1")
        self.price_1_1 = QtWidgets.QLabel(self.frame_1_1)
        self.price_1_1.setGeometry(QtCore.QRect(75, 255, 60, 30))
        self.price_1_1.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_1_1.setObjectName("price_1_1")
        self.frame_1_6 = QtWidgets.QFrame(self.tab_1)
        self.frame_1_6.setGeometry(QtCore.QRect(360, 370, 250, 300))
        self.frame_1_6.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_1_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1_6.setObjectName("frame_1_6")
        self.photo_1_6 = QtWidgets.QLabel(self.frame_1_6)
        self.photo_1_6.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_1_6.setText("")
        self.photo_1_6.setPixmap(QtGui.QPixmap("emojis/mac/Chickenburger.webp"))
        self.photo_1_6.setScaledContents(True)
        self.photo_1_6.setObjectName("photo_1_6")
        self.name_1_6 = QtWidgets.QLabel(self.frame_1_6)
        self.name_1_6.setGeometry(QtCore.QRect(70, 215, 110, 30))
        self.name_1_6.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_1_6.setObjectName("name_1_6")
        self.ButtonPlus_1_6 = QtWidgets.QPushButton(self.frame_1_6)
        self.ButtonPlus_1_6.setGeometry(QtCore.QRect(140, 255, 30, 30))
        self.ButtonPlus_1_6.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_1_6.setObjectName("ButtonPlus_1_6")
        self.price_1_ = QtWidgets.QLabel(self.frame_1_6)
        self.price_1_.setGeometry(QtCore.QRect(80, 255, 50, 30))
        self.price_1_.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.price_1_.setObjectName("price_1_")
        self.frame_1_3 = QtWidgets.QFrame(self.tab_1)
        self.frame_1_3.setGeometry(QtCore.QRect(670, 40, 250, 300))
        self.frame_1_3.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_1_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1_3.setObjectName("frame_1_3")
        self.photo_1_3 = QtWidgets.QLabel(self.frame_1_3)
        self.photo_1_3.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_1_3.setText("")
        self.photo_1_3.setPixmap(QtGui.QPixmap("emojis/mac/Double_Filet_o_Fish.webp"))
        self.photo_1_3.setScaledContents(True)
        self.photo_1_3.setObjectName("photo_1_3")
        self.name_1_3 = QtWidgets.QLabel(self.frame_1_3)
        self.name_1_3.setGeometry(QtCore.QRect(35, 215, 180, 30))
        self.name_1_3.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_1_3.setObjectName("name_1_3")
        self.ButtonPlus_1_3 = QtWidgets.QPushButton(self.frame_1_3)
        self.ButtonPlus_1_3.setGeometry(QtCore.QRect(145, 255, 30, 30))
        self.ButtonPlus_1_3.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_1_3.setObjectName("ButtonPlus_1_3")
        self.price_1_3 = QtWidgets.QLabel(self.frame_1_3)
        self.price_1_3.setGeometry(QtCore.QRect(75, 255, 60, 30))
        self.price_1_3.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_1_3.setObjectName("price_1_3")
        self.frame_1_7 = QtWidgets.QFrame(self.tab_1)
        self.frame_1_7.setGeometry(QtCore.QRect(670, 370, 250, 300))
        self.frame_1_7.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_1_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1_7.setObjectName("frame_1_7")
        self.photo_1_7 = QtWidgets.QLabel(self.frame_1_7)
        self.photo_1_7.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_1_7.setText("")
        self.photo_1_7.setPixmap(QtGui.QPixmap("emojis/mac/Filet_o_Fish.webp"))
        self.photo_1_7.setScaledContents(True)
        self.photo_1_7.setObjectName("photo_1_7")
        self.name_1_7 = QtWidgets.QLabel(self.frame_1_7)
        self.name_1_7.setGeometry(QtCore.QRect(70, 215, 110, 30))
        self.name_1_7.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_1_7.setObjectName("name_1_7")
        self.ButtonPlus_1_7 = QtWidgets.QPushButton(self.frame_1_7)
        self.ButtonPlus_1_7.setGeometry(QtCore.QRect(145, 255, 30, 30))
        self.ButtonPlus_1_7.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_1_7.setObjectName("ButtonPlus_1_7")
        self.price_1_7 = QtWidgets.QLabel(self.frame_1_7)
        self.price_1_7.setGeometry(QtCore.QRect(75, 255, 60, 30))
        self.price_1_7.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_1_7.setObjectName("price_1_7")
        self.frame_1_2 = QtWidgets.QFrame(self.tab_1)
        self.frame_1_2.setGeometry(QtCore.QRect(360, 40, 250, 300))
        self.frame_1_2.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1_2.setObjectName("frame_1_2")
        self.photo_1_2 = QtWidgets.QLabel(self.frame_1_2)
        self.photo_1_2.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_1_2.setText("")
        self.photo_1_2.setPixmap(QtGui.QPixmap("emojis/mac/McChicken.webp"))
        self.photo_1_2.setScaledContents(True)
        self.photo_1_2.setObjectName("photo_1_2")
        self.name_1_2 = QtWidgets.QLabel(self.frame_1_2)
        self.name_1_2.setGeometry(QtCore.QRect(80, 215, 90, 30))
        self.name_1_2.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_1_2.setObjectName("name_1_2")
        self.ButtonPlus_1_2 = QtWidgets.QPushButton(self.frame_1_2)
        self.ButtonPlus_1_2.setGeometry(QtCore.QRect(145, 255, 30, 30))
        self.ButtonPlus_1_2.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_1_2.setObjectName("ButtonPlus_1_2")
        self.price_1_2 = QtWidgets.QLabel(self.frame_1_2)
        self.price_1_2.setGeometry(QtCore.QRect(75, 255, 60, 30))
        self.price_1_2.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_1_2.setObjectName("price_1_2")
        self.frame_1_5 = QtWidgets.QFrame(self.tab_1)
        self.frame_1_5.setGeometry(QtCore.QRect(50, 370, 250, 300))
        self.frame_1_5.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_1_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1_5.setObjectName("frame_1_5")
        self.photo_1_5 = QtWidgets.QLabel(self.frame_1_5)
        self.photo_1_5.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_1_5.setText("")
        self.photo_1_5.setPixmap(QtGui.QPixmap("emojis/mac/Hamburger.webp"))
        self.photo_1_5.setScaledContents(True)
        self.photo_1_5.setObjectName("photo_1_5")
        self.name_1_5 = QtWidgets.QLabel(self.frame_1_5)
        self.name_1_5.setGeometry(QtCore.QRect(75, 215, 100, 30))
        self.name_1_5.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_1_5.setObjectName("name_1_5")
        self.ButtonPlus_1_5 = QtWidgets.QPushButton(self.frame_1_5)
        self.ButtonPlus_1_5.setGeometry(QtCore.QRect(140, 255, 30, 30))
        self.ButtonPlus_1_5.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_1_5.setObjectName("ButtonPlus_1_5")
        self.price_1_5 = QtWidgets.QLabel(self.frame_1_5)
        self.price_1_5.setGeometry(QtCore.QRect(80, 255, 50, 30))
        self.price_1_5.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_1_5.setObjectName("price_1_5")
        self.frame_1_4 = QtWidgets.QFrame(self.tab_1)
        self.frame_1_4.setGeometry(QtCore.QRect(980, 40, 250, 300))
        self.frame_1_4.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_1_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1_4.setObjectName("frame_1_4")
        self.photo_1_4 = QtWidgets.QLabel(self.frame_1_4)
        self.photo_1_4.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_1_4.setText("")
        self.photo_1_4.setPixmap(QtGui.QPixmap("emojis/mac/DblRoyal.webp"))
        self.photo_1_4.setScaledContents(True)
        self.photo_1_4.setObjectName("photo_1_4")
        self.name_1_4 = QtWidgets.QLabel(self.frame_1_4)
        self.name_1_4.setGeometry(QtCore.QRect(65, 215, 120, 30))
        self.name_1_4.setAutoFillBackground(False)
        self.name_1_4.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_1_4.setObjectName("name_1_4")
        self.ButtonPlus_1_4 = QtWidgets.QPushButton(self.frame_1_4)
        self.ButtonPlus_1_4.setGeometry(QtCore.QRect(145, 255, 30, 30))
        self.ButtonPlus_1_4.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_1_4.setObjectName("ButtonPlus_1_4")
        self.price_1_4 = QtWidgets.QLabel(self.frame_1_4)
        self.price_1_4.setGeometry(QtCore.QRect(75, 255, 60, 30))
        self.price_1_4.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_1_4.setObjectName("price_1_4")
        self.frame_1_8 = QtWidgets.QFrame(self.tab_1)
        self.frame_1_8.setGeometry(QtCore.QRect(980, 370, 250, 300))
        self.frame_1_8.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_1_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1_8.setObjectName("frame_1_8")
        self.photo_1_8 = QtWidgets.QLabel(self.frame_1_8)
        self.photo_1_8.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_1_8.setText("")
        self.photo_1_8.setPixmap(QtGui.QPixmap("emojis/mac/BigTasty.webp"))
        self.photo_1_8.setScaledContents(True)
        self.photo_1_8.setObjectName("photo_1_8")
        self.name_1_8 = QtWidgets.QLabel(self.frame_1_8)
        self.name_1_8.setGeometry(QtCore.QRect(75, 215, 100, 30))
        self.name_1_8.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_1_8.setObjectName("name_1_8")
        self.ButtonPlus_1_8 = QtWidgets.QPushButton(self.frame_1_8)
        self.ButtonPlus_1_8.setGeometry(QtCore.QRect(145, 255, 30, 30))
        self.ButtonPlus_1_8.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_1_8.setObjectName("ButtonPlus_1_8")
        self.price_1_8 = QtWidgets.QLabel(self.frame_1_8)
        self.price_1_8.setGeometry(QtCore.QRect(75, 255, 60, 30))
        self.price_1_8.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_1_8.setObjectName("price_1_8")
        self.m.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_2_7 = QtWidgets.QFrame(self.tab_2)
        self.frame_2_7.setGeometry(QtCore.QRect(670, 370, 250, 300))
        self.frame_2_7.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_2_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2_7.setObjectName("frame_2_7")
        self.name_2_7 = QtWidgets.QLabel(self.frame_2_7)
        self.name_2_7.setGeometry(QtCore.QRect(50, 215, 150, 30))
        self.name_2_7.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_2_7.setObjectName("name_2_7")
        self.ButtonPlus_2_7 = QtWidgets.QPushButton(self.frame_2_7)
        self.ButtonPlus_2_7.setGeometry(QtCore.QRect(145, 255, 30, 30))
        self.ButtonPlus_2_7.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_2_7.setObjectName("ButtonPlus_2_7")
        self.photo_2_7 = QtWidgets.QLabel(self.frame_2_7)
        self.photo_2_7.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_2_7.setText("")
        self.photo_2_7.setPixmap(QtGui.QPixmap("emojis/mac/ItalianWeeks_Cheese.webp"))
        self.photo_2_7.setScaledContents(True)
        self.photo_2_7.setObjectName("photo_2_7")
        self.price_2_7 = QtWidgets.QLabel(self.frame_2_7)
        self.price_2_7.setGeometry(QtCore.QRect(75, 255, 60, 30))
        self.price_2_7.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_2_7.setObjectName("price_2_7")
        self.frame_2_8 = QtWidgets.QFrame(self.tab_2)
        self.frame_2_8.setGeometry(QtCore.QRect(980, 370, 250, 300))
        self.frame_2_8.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_2_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2_8.setObjectName("frame_2_8")
        self.photo_2_8 = QtWidgets.QLabel(self.frame_2_8)
        self.photo_2_8.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_2_8.setText("")
        self.photo_2_8.setPixmap(QtGui.QPixmap("emojis/mac/Salad_Vegetable.webp"))
        self.photo_2_8.setScaledContents(True)
        self.photo_2_8.setObjectName("photo_2_8")
        self.name_2_8 = QtWidgets.QLabel(self.frame_2_8)
        self.name_2_8.setGeometry(QtCore.QRect(60, 215, 130, 30))
        self.name_2_8.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_2_8.setObjectName("name_2_8")
        self.ButtonPlus_2_8 = QtWidgets.QPushButton(self.frame_2_8)
        self.ButtonPlus_2_8.setGeometry(QtCore.QRect(145, 255, 30, 30))
        self.ButtonPlus_2_8.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_2_8.setObjectName("ButtonPlus_2_8")
        self.price_2_8 = QtWidgets.QLabel(self.frame_2_8)
        self.price_2_8.setGeometry(QtCore.QRect(75, 255, 60, 30))
        self.price_2_8.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_2_8.setObjectName("price_2_8")
        self.frame_2_4 = QtWidgets.QFrame(self.tab_2)
        self.frame_2_4.setGeometry(QtCore.QRect(980, 40, 250, 300))
        self.frame_2_4.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_2_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2_4.setObjectName("frame_2_4")
        self.photo_2_4 = QtWidgets.QLabel(self.frame_2_4)
        self.photo_2_4.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_2_4.setText("")
        self.photo_2_4.setPixmap(QtGui.QPixmap("emojis/mac/Strips.webp"))
        self.photo_2_4.setScaledContents(True)
        self.photo_2_4.setObjectName("photo_2_4")
        self.name_2_4 = QtWidgets.QLabel(self.frame_2_4)
        self.name_2_4.setGeometry(QtCore.QRect(85, 215, 80, 30))
        self.name_2_4.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_2_4.setObjectName("name_2_4")
        self.ButtonPlus_2_4 = QtWidgets.QPushButton(self.frame_2_4)
        self.ButtonPlus_2_4.setGeometry(QtCore.QRect(145, 255, 30, 30))
        self.ButtonPlus_2_4.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_2_4.setObjectName("ButtonPlus_2_4")
        self.price_2_4 = QtWidgets.QLabel(self.frame_2_4)
        self.price_2_4.setGeometry(QtCore.QRect(75, 255, 60, 30))
        self.price_2_4.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_2_4.setObjectName("price_2_4")
        self.frame_2_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2_2.setGeometry(QtCore.QRect(360, 40, 250, 300))
        self.frame_2_2.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_2_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2_2.setObjectName("frame_2_2")
        self.photo_2_2 = QtWidgets.QLabel(self.frame_2_2)
        self.photo_2_2.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_2_2.setText("")
        self.photo_2_2.setPixmap(QtGui.QPixmap("emojis/mac/Chicken_wings.webp"))
        self.photo_2_2.setScaledContents(True)
        self.photo_2_2.setObjectName("photo_2_2")
        self.name_2_2 = QtWidgets.QLabel(self.frame_2_2)
        self.name_2_2.setGeometry(QtCore.QRect(45, 215, 160, 30))
        self.name_2_2.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_2_2.setObjectName("name_2_2")
        self.ButtonPlus_2_2 = QtWidgets.QPushButton(self.frame_2_2)
        self.ButtonPlus_2_2.setGeometry(QtCore.QRect(145, 255, 30, 30))
        self.ButtonPlus_2_2.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_2_2.setObjectName("ButtonPlus_2_2")
        self.price_2_2 = QtWidgets.QLabel(self.frame_2_2)
        self.price_2_2.setGeometry(QtCore.QRect(75, 255, 60, 30))
        self.price_2_2.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_2_2.setObjectName("price_2_2")
        self.frame_2_6 = QtWidgets.QFrame(self.tab_2)
        self.frame_2_6.setGeometry(QtCore.QRect(360, 370, 250, 300))
        self.frame_2_6.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_2_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2_6.setObjectName("frame_2_6")
        self.photo_2_6 = QtWidgets.QLabel(self.frame_2_6)
        self.photo_2_6.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_2_6.setText("")
        self.photo_2_6.setPixmap(QtGui.QPixmap("emojis/mac/krevetki.webp"))
        self.photo_2_6.setScaledContents(True)
        self.photo_2_6.setObjectName("photo_2_6")
        self.name_2_6 = QtWidgets.QLabel(self.frame_2_6)
        self.name_2_6.setGeometry(QtCore.QRect(85, 215, 80, 30))
        self.name_2_6.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_2_6.setObjectName("name_2_6")
        self.ButtonPlus_2_6 = QtWidgets.QPushButton(self.frame_2_6)
        self.ButtonPlus_2_6.setGeometry(QtCore.QRect(145, 255, 30, 30))
        self.ButtonPlus_2_6.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_2_6.setObjectName("ButtonPlus_2_6")
        self.price_2_6 = QtWidgets.QLabel(self.frame_2_6)
        self.price_2_6.setGeometry(QtCore.QRect(75, 255, 60, 30))
        self.price_2_6.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_2_6.setObjectName("price_2_6")
        self.frame_2_3 = QtWidgets.QFrame(self.tab_2)
        self.frame_2_3.setGeometry(QtCore.QRect(670, 40, 250, 300))
        self.frame_2_3.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_2_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2_3.setObjectName("frame_2_3")
        self.photo_2_3 = QtWidgets.QLabel(self.frame_2_3)
        self.photo_2_3.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_2_3.setText("")
        self.photo_2_3.setPixmap(QtGui.QPixmap("emojis/mac/Nuggets.webp"))
        self.photo_2_3.setScaledContents(True)
        self.photo_2_3.setObjectName("photo_2_3")
        self.name_2_3 = QtWidgets.QLabel(self.frame_2_3)
        self.name_2_3.setGeometry(QtCore.QRect(50, 215, 150, 30))
        self.name_2_3.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_2_3.setObjectName("name_2_3")
        self.ButtonPlus_2_3 = QtWidgets.QPushButton(self.frame_2_3)
        self.ButtonPlus_2_3.setGeometry(QtCore.QRect(145, 255, 30, 30))
        self.ButtonPlus_2_3.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_2_3.setObjectName("ButtonPlus_2_3")
        self.price_2_3 = QtWidgets.QLabel(self.frame_2_3)
        self.price_2_3.setGeometry(QtCore.QRect(75, 255, 60, 30))
        self.price_2_3.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_2_3.setObjectName("price_2_3")
        self.frame_2_1 = QtWidgets.QFrame(self.tab_2)
        self.frame_2_1.setGeometry(QtCore.QRect(50, 40, 250, 300))
        self.frame_2_1.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_2_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2_1.setObjectName("frame_2_1")
        self.photo_2_1 = QtWidgets.QLabel(self.frame_2_1)
        self.photo_2_1.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_2_1.setText("")
        self.photo_2_1.setPixmap(QtGui.QPixmap("emojis/mac/Fries.webp"))
        self.photo_2_1.setScaledContents(True)
        self.photo_2_1.setObjectName("photo_2_1")
        self.name_2_1 = QtWidgets.QLabel(self.frame_2_1)
        self.name_2_1.setGeometry(QtCore.QRect(60, 215, 130, 30))
        self.name_2_1.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_2_1.setObjectName("name_2_1")
        self.ButtonPlus_2_1 = QtWidgets.QPushButton(self.frame_2_1)
        self.ButtonPlus_2_1.setGeometry(QtCore.QRect(140, 255, 30, 30))
        self.ButtonPlus_2_1.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_2_1.setObjectName("ButtonPlus_2_1")
        self.price_2_1 = QtWidgets.QLabel(self.frame_2_1)
        self.price_2_1.setGeometry(QtCore.QRect(80, 255, 50, 30))
        self.price_2_1.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_2_1.setObjectName("price_2_1")
        self.frame_2_5 = QtWidgets.QFrame(self.tab_2)
        self.frame_2_5.setGeometry(QtCore.QRect(50, 370, 250, 300))
        self.frame_2_5.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_2_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2_5.setObjectName("frame_2_5")
        self.photo_2_5 = QtWidgets.QLabel(self.frame_2_5)
        self.photo_2_5.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_2_5.setText("")
        self.photo_2_5.setPixmap(QtGui.QPixmap("emojis/mac/Potat_Wedges.webp"))
        self.photo_2_5.setScaledContents(True)
        self.photo_2_5.setObjectName("photo_2_5")
        self.name_2_5 = QtWidgets.QLabel(self.frame_2_5)
        self.name_2_5.setGeometry(QtCore.QRect(20, 215, 210, 30))
        self.name_2_5.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_2_5.setObjectName("name_2_5")
        self.ButtonPlus_2_5 = QtWidgets.QPushButton(self.frame_2_5)
        self.ButtonPlus_2_5.setGeometry(QtCore.QRect(145, 255, 30, 30))
        self.ButtonPlus_2_5.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_2_5.setObjectName("ButtonPlus_2_5")
        self.price_2_5 = QtWidgets.QLabel(self.frame_2_5)
        self.price_2_5.setGeometry(QtCore.QRect(75, 255, 60, 30))
        self.price_2_5.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_2_5.setObjectName("price_2_5")
        self.m.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame_3_1 = QtWidgets.QFrame(self.tab_3)
        self.frame_3_1.setGeometry(QtCore.QRect(50, 40, 250, 300))
        self.frame_3_1.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_3_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3_1.setObjectName("frame_3_1")
        self.photo_3_1 = QtWidgets.QLabel(self.frame_3_1)
        self.photo_3_1.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_3_1.setText("")
        self.photo_3_1.setPixmap(QtGui.QPixmap("emojis/mac/cappucino.webp"))
        self.photo_3_1.setScaledContents(True)
        self.photo_3_1.setObjectName("photo_3_1")
        self.name_3_1 = QtWidgets.QLabel(self.frame_3_1)
        self.name_3_1.setGeometry(QtCore.QRect(80, 215, 90, 30))
        self.name_3_1.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_3_1.setObjectName("name_3_1")
        self.ButtonPlus_3_1 = QtWidgets.QPushButton(self.frame_3_1)
        self.ButtonPlus_3_1.setGeometry(QtCore.QRect(145, 255, 30, 30))
        self.ButtonPlus_3_1.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_3_1.setObjectName("ButtonPlus_3_1")
        self.price_3_1 = QtWidgets.QLabel(self.frame_3_1)
        self.price_3_1.setGeometry(QtCore.QRect(75, 255, 60, 30))
        self.price_3_1.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_3_1.setObjectName("price_3_1")
        self.frame_3_2 = QtWidgets.QFrame(self.tab_3)
        self.frame_3_2.setGeometry(QtCore.QRect(360, 40, 250, 300))
        self.frame_3_2.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_3_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3_2.setObjectName("frame_3_2")
        self.photo_3_2 = QtWidgets.QLabel(self.frame_3_2)
        self.photo_3_2.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_3_2.setText("")
        self.photo_3_2.setPixmap(QtGui.QPixmap("emojis/mac/latte.webp"))
        self.photo_3_2.setScaledContents(True)
        self.photo_3_2.setObjectName("photo_3_2")
        self.name_3_2 = QtWidgets.QLabel(self.frame_3_2)
        self.name_3_2.setGeometry(QtCore.QRect(95, 215, 60, 30))
        self.name_3_2.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_3_2.setObjectName("name_3_2")
        self.ButtonPlus_3_2 = QtWidgets.QPushButton(self.frame_3_2)
        self.ButtonPlus_3_2.setGeometry(QtCore.QRect(145, 255, 30, 30))
        self.ButtonPlus_3_2.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_3_2.setObjectName("ButtonPlus_3_2")
        self.price_3_2 = QtWidgets.QLabel(self.frame_3_2)
        self.price_3_2.setGeometry(QtCore.QRect(75, 255, 60, 30))
        self.price_3_2.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_3_2.setObjectName("price_3_2")
        self.frame_3_3 = QtWidgets.QFrame(self.tab_3)
        self.frame_3_3.setGeometry(QtCore.QRect(670, 40, 250, 300))
        self.frame_3_3.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_3_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3_3.setObjectName("frame_3_3")
        self.photo_3_3 = QtWidgets.QLabel(self.frame_3_3)
        self.photo_3_3.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_3_3.setText("")
        self.photo_3_3.setPixmap(QtGui.QPixmap("emojis/mac/Americano.webp"))
        self.photo_3_3.setScaledContents(True)
        self.photo_3_3.setObjectName("photo_3_3")
        self.name_3_3 = QtWidgets.QLabel(self.frame_3_3)
        self.name_3_3.setGeometry(QtCore.QRect(75, 215, 100, 30))
        self.name_3_3.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_3_3.setObjectName("name_3_3")
        self.ButtonPlus_3_3 = QtWidgets.QPushButton(self.frame_3_3)
        self.ButtonPlus_3_3.setGeometry(QtCore.QRect(140, 255, 30, 30))
        self.ButtonPlus_3_3.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_3_3.setObjectName("ButtonPlus_3_3")
        self.price_3_3 = QtWidgets.QLabel(self.frame_3_3)
        self.price_3_3.setGeometry(QtCore.QRect(80, 255, 50, 30))
        self.price_3_3.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_3_3.setObjectName("price_3_3")
        self.frame_3_4 = QtWidgets.QFrame(self.tab_3)
        self.frame_3_4.setGeometry(QtCore.QRect(980, 40, 250, 300))
        self.frame_3_4.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_3_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3_4.setObjectName("frame_3_4")
        self.photo_3_4 = QtWidgets.QLabel(self.frame_3_4)
        self.photo_3_4.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_3_4.setText("")
        self.photo_3_4.setPixmap(QtGui.QPixmap("emojis/mac/Ceylon.webp"))
        self.photo_3_4.setScaledContents(True)
        self.photo_3_4.setObjectName("photo_3_4")
        self.name_3_4 = QtWidgets.QLabel(self.frame_3_4)
        self.name_3_4.setGeometry(QtCore.QRect(70, 215, 110, 30))
        self.name_3_4.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_3_4.setObjectName("name_3_4")
        self.ButtonPlus_3_4 = QtWidgets.QPushButton(self.frame_3_4)
        self.ButtonPlus_3_4.setGeometry(QtCore.QRect(140, 255, 30, 30))
        self.ButtonPlus_3_4.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_3_4.setObjectName("ButtonPlus_3_4")
        self.price_3_4 = QtWidgets.QLabel(self.frame_3_4)
        self.price_3_4.setGeometry(QtCore.QRect(80, 255, 50, 30))
        self.price_3_4.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_3_4.setObjectName("price_3_4")
        self.frame_3_5 = QtWidgets.QFrame(self.tab_3)
        self.frame_3_5.setGeometry(QtCore.QRect(50, 370, 250, 300))
        self.frame_3_5.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_3_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3_5.setObjectName("frame_3_5")
        self.photo_3_5 = QtWidgets.QLabel(self.frame_3_5)
        self.photo_3_5.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_3_5.setText("")
        self.photo_3_5.setPixmap(QtGui.QPixmap("emojis/mac/cola.webp"))
        self.photo_3_5.setScaledContents(True)
        self.photo_3_5.setObjectName("photo_3_5")
        self.name_3_5 = QtWidgets.QLabel(self.frame_3_5)
        self.name_3_5.setGeometry(QtCore.QRect(80, 215, 90, 30))
        self.name_3_5.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_3_5.setObjectName("name_3_5")
        self.ButtonPlus_3_5 = QtWidgets.QPushButton(self.frame_3_5)
        self.ButtonPlus_3_5.setGeometry(QtCore.QRect(140, 255, 30, 30))
        self.ButtonPlus_3_5.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_3_5.setObjectName("ButtonPlus_3_5")
        self.price_3_5 = QtWidgets.QLabel(self.frame_3_5)
        self.price_3_5.setGeometry(QtCore.QRect(80, 255, 50, 30))
        self.price_3_5.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_3_5.setObjectName("price_3_5")
        self.frame_3_6 = QtWidgets.QFrame(self.tab_3)
        self.frame_3_6.setGeometry(QtCore.QRect(360, 370, 250, 300))
        self.frame_3_6.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_3_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3_6.setObjectName("frame_3_6")
        self.photo_3_6 = QtWidgets.QLabel(self.frame_3_6)
        self.photo_3_6.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_3_6.setText("")
        self.photo_3_6.setPixmap(QtGui.QPixmap("emojis/mac/fanta.webp"))
        self.photo_3_6.setScaledContents(True)
        self.photo_3_6.setObjectName("photo_3_6")
        self.name_3_6 = QtWidgets.QLabel(self.frame_3_6)
        self.name_3_6.setGeometry(QtCore.QRect(95, 215, 60, 30))
        self.name_3_6.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_3_6.setObjectName("name_3_6")
        self.ButtonPlus_3_6 = QtWidgets.QPushButton(self.frame_3_6)
        self.ButtonPlus_3_6.setGeometry(QtCore.QRect(140, 255, 30, 30))
        self.ButtonPlus_3_6.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_3_6.setObjectName("ButtonPlus_3_6")
        self.price_3_6 = QtWidgets.QLabel(self.frame_3_6)
        self.price_3_6.setGeometry(QtCore.QRect(80, 255, 50, 30))
        self.price_3_6.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_3_6.setObjectName("price_3_6")
        self.frame_3_7 = QtWidgets.QFrame(self.tab_3)
        self.frame_3_7.setGeometry(QtCore.QRect(670, 370, 250, 300))
        self.frame_3_7.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_3_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3_7.setObjectName("frame_3_7")
        self.photo_3_7 = QtWidgets.QLabel(self.frame_3_7)
        self.photo_3_7.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_3_7.setText("")
        self.photo_3_7.setPixmap(QtGui.QPixmap("emojis/mac/sprite.webp"))
        self.photo_3_7.setScaledContents(True)
        self.photo_3_7.setObjectName("photo_3_7")
        self.name_3_7 = QtWidgets.QLabel(self.frame_3_7)
        self.name_3_7.setGeometry(QtCore.QRect(90, 215, 70, 30))
        self.name_3_7.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_3_7.setObjectName("name_3_7")
        self.ButtonPlus_3_7 = QtWidgets.QPushButton(self.frame_3_7)
        self.ButtonPlus_3_7.setGeometry(QtCore.QRect(140, 255, 30, 30))
        self.ButtonPlus_3_7.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_3_7.setObjectName("ButtonPlus_3_7")
        self.price_3_7 = QtWidgets.QLabel(self.frame_3_7)
        self.price_3_7.setGeometry(QtCore.QRect(80, 255, 50, 30))
        self.price_3_7.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_3_7.setObjectName("price_3_7")
        self.frame_3_8 = QtWidgets.QFrame(self.tab_3)
        self.frame_3_8.setGeometry(QtCore.QRect(980, 370, 250, 300))
        self.frame_3_8.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_3_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3_8.setObjectName("frame_3_8")
        self.photo_3_8 = QtWidgets.QLabel(self.frame_3_8)
        self.photo_3_8.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_3_8.setText("")
        self.photo_3_8.setPixmap(QtGui.QPixmap("emojis/mac/milkshake.webp"))
        self.photo_3_8.setScaledContents(True)
        self.photo_3_8.setObjectName("photo_3_8")
        self.name_3_8 = QtWidgets.QLabel(self.frame_3_8)
        self.name_3_8.setGeometry(QtCore.QRect(45, 215, 160, 30))
        self.name_3_8.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_3_8.setObjectName("name_3_8")
        self.ButtonPlus_1_16 = QtWidgets.QPushButton(self.frame_3_8)
        self.ButtonPlus_1_16.setGeometry(QtCore.QRect(140, 255, 30, 30))
        self.ButtonPlus_1_16.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                           "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_1_16.setObjectName("ButtonPlus_1_16")
        self.price_3_8 = QtWidgets.QLabel(self.frame_3_8)
        self.price_3_8.setGeometry(QtCore.QRect(80, 255, 50, 30))
        self.price_3_8.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_3_8.setObjectName("price_3_8")
        self.m.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.frame_4_1 = QtWidgets.QFrame(self.tab_4)
        self.frame_4_1.setGeometry(QtCore.QRect(50, 40, 250, 300))
        self.frame_4_1.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_4_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4_1.setObjectName("frame_4_1")
        self.photo_4_1 = QtWidgets.QLabel(self.frame_4_1)
        self.photo_4_1.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_4_1.setText("")
        self.photo_4_1.setPixmap(QtGui.QPixmap("emojis/mac/Sauce_Cheese.webp"))
        self.photo_4_1.setScaledContents(True)
        self.photo_4_1.setObjectName("photo_4_1")
        self.name_4_1 = QtWidgets.QLabel(self.frame_4_1)
        self.name_4_1.setGeometry(QtCore.QRect(65, 215, 120, 30))
        self.name_4_1.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_4_1.setObjectName("name_4_1")
        self.ButtonPlus_4_1 = QtWidgets.QPushButton(self.frame_4_1)
        self.ButtonPlus_4_1.setGeometry(QtCore.QRect(140, 255, 30, 30))
        self.ButtonPlus_4_1.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_4_1.setObjectName("ButtonPlus_4_1")
        self.price_4_1 = QtWidgets.QLabel(self.frame_4_1)
        self.price_4_1.setGeometry(QtCore.QRect(80, 255, 50, 30))
        self.price_4_1.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_4_1.setObjectName("price_4_1")
        self.frame_4_2 = QtWidgets.QFrame(self.tab_4)
        self.frame_4_2.setGeometry(QtCore.QRect(360, 40, 250, 300))
        self.frame_4_2.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_4_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4_2.setObjectName("frame_4_2")
        self.photo_4_2 = QtWidgets.QLabel(self.frame_4_2)
        self.photo_4_2.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_4_2.setText("")
        self.photo_4_2.setPixmap(QtGui.QPixmap("emojis/mac/Ketchup.webp"))
        self.photo_4_2.setScaledContents(True)
        self.photo_4_2.setObjectName("photo_4_2")
        self.name_4_2 = QtWidgets.QLabel(self.frame_4_2)
        self.name_4_2.setGeometry(QtCore.QRect(90, 215, 70, 30))
        self.name_4_2.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_4_2.setObjectName("name_4_2")
        self.ButtonPlus_4_2 = QtWidgets.QPushButton(self.frame_4_2)
        self.ButtonPlus_4_2.setGeometry(QtCore.QRect(140, 255, 30, 30))
        self.ButtonPlus_4_2.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_4_2.setObjectName("ButtonPlus_4_2")
        self.price_4_2 = QtWidgets.QLabel(self.frame_4_2)
        self.price_4_2.setGeometry(QtCore.QRect(80, 255, 50, 30))
        self.price_4_2.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_4_2.setObjectName("price_4_2")
        self.frame_4_3 = QtWidgets.QFrame(self.tab_4)
        self.frame_4_3.setGeometry(QtCore.QRect(670, 40, 250, 300))
        self.frame_4_3.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_4_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4_3.setObjectName("frame_4_3")
        self.photo_4_3 = QtWidgets.QLabel(self.frame_4_3)
        self.photo_4_3.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_4_3.setText("")
        self.photo_4_3.setPixmap(QtGui.QPixmap("emojis/mac/teriyaki_sauce.webp"))
        self.photo_4_3.setScaledContents(True)
        self.photo_4_3.setObjectName("photo_4_3")
        self.name_4_3 = QtWidgets.QLabel(self.frame_4_3)
        self.name_4_3.setGeometry(QtCore.QRect(65, 215, 120, 30))
        self.name_4_3.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_4_3.setObjectName("name_4_3")
        self.ButtonPlus_4_3 = QtWidgets.QPushButton(self.frame_4_3)
        self.ButtonPlus_4_3.setGeometry(QtCore.QRect(140, 255, 30, 30))
        self.ButtonPlus_4_3.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_4_3.setObjectName("ButtonPlus_4_3")
        self.price_4_3 = QtWidgets.QLabel(self.frame_4_3)
        self.price_4_3.setGeometry(QtCore.QRect(80, 255, 50, 30))
        self.price_4_3.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_4_3.setObjectName("price_4_3")
        self.frame_4_4 = QtWidgets.QFrame(self.tab_4)
        self.frame_4_4.setGeometry(QtCore.QRect(980, 40, 250, 300))
        self.frame_4_4.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_4_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4_4.setObjectName("frame_4_4")
        self.photo_4_4 = QtWidgets.QLabel(self.frame_4_4)
        self.photo_4_4.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_4_4.setText("")
        self.photo_4_4.setPixmap(QtGui.QPixmap("emojis/mac/Sous_Kislo_sladkiy.webp"))
        self.photo_4_4.setScaledContents(True)
        self.photo_4_4.setObjectName("photo_4_4")
        self.name_4_4 = QtWidgets.QLabel(self.frame_4_4)
        self.name_4_4.setGeometry(QtCore.QRect(40, 215, 170, 30))
        self.name_4_4.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_4_4.setObjectName("name_4_4")
        self.ButtonPlus_4_4 = QtWidgets.QPushButton(self.frame_4_4)
        self.ButtonPlus_4_4.setGeometry(QtCore.QRect(140, 255, 30, 30))
        self.ButtonPlus_4_4.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_4_4.setObjectName("ButtonPlus_4_4")
        self.price_4_4 = QtWidgets.QLabel(self.frame_4_4)
        self.price_4_4.setGeometry(QtCore.QRect(80, 255, 50, 30))
        self.price_4_4.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_4_4.setObjectName("price_4_4")
        self.frame_1_13 = QtWidgets.QFrame(self.tab_4)
        self.frame_1_13.setGeometry(QtCore.QRect(50, 370, 250, 300))
        self.frame_1_13.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_1_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1_13.setObjectName("frame_1_13")
        self.photo_4_5 = QtWidgets.QLabel(self.frame_1_13)
        self.photo_4_5.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_4_5.setText("")
        self.photo_4_5.setPixmap(QtGui.QPixmap("emojis/mac/Sous_CHesnochnyy.webp"))
        self.photo_4_5.setScaledContents(True)
        self.photo_4_5.setObjectName("photo_4_5")
        self.name_4_5 = QtWidgets.QLabel(self.frame_1_13)
        self.name_4_5.setGeometry(QtCore.QRect(50, 215, 150, 30))
        self.name_4_5.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_4_5.setObjectName("name_4_5")
        self.ButtonPlus_4_5 = QtWidgets.QPushButton(self.frame_1_13)
        self.ButtonPlus_4_5.setGeometry(QtCore.QRect(140, 255, 30, 30))
        self.ButtonPlus_4_5.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_4_5.setObjectName("ButtonPlus_4_5")
        self.price_4_5 = QtWidgets.QLabel(self.frame_1_13)
        self.price_4_5.setGeometry(QtCore.QRect(80, 255, 50, 30))
        self.price_4_5.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_4_5.setObjectName("price_4_5")
        self.frame_4_6 = QtWidgets.QFrame(self.tab_4)
        self.frame_4_6.setGeometry(QtCore.QRect(360, 370, 250, 300))
        self.frame_4_6.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_4_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4_6.setObjectName("frame_4_6")
        self.photo_4_6 = QtWidgets.QLabel(self.frame_4_6)
        self.photo_4_6.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_4_6.setText("")
        self.photo_4_6.setPixmap(QtGui.QPixmap("emojis/mac/Sous-Sladkiy-CHili.webp"))
        self.photo_4_6.setScaledContents(True)
        self.photo_4_6.setObjectName("photo_4_6")
        self.name_4_6 = QtWidgets.QLabel(self.frame_4_6)
        self.name_4_6.setGeometry(QtCore.QRect(40, 215, 170, 30))
        self.name_4_6.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_4_6.setObjectName("name_4_6")
        self.ButtonPlus_4_6 = QtWidgets.QPushButton(self.frame_4_6)
        self.ButtonPlus_4_6.setGeometry(QtCore.QRect(140, 255, 30, 30))
        self.ButtonPlus_4_6.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_4_6.setObjectName("ButtonPlus_4_6")
        self.price_4_6 = QtWidgets.QLabel(self.frame_4_6)
        self.price_4_6.setGeometry(QtCore.QRect(80, 255, 50, 30))
        self.price_4_6.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_4_6.setObjectName("price_4_6")
        self.frame_4_7 = QtWidgets.QFrame(self.tab_4)
        self.frame_4_7.setGeometry(QtCore.QRect(670, 370, 250, 300))
        self.frame_4_7.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_4_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4_7.setObjectName("frame_4_7")
        self.photo_4_7 = QtWidgets.QLabel(self.frame_4_7)
        self.photo_4_7.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_4_7.setText("")
        self.photo_4_7.setPixmap(QtGui.QPixmap("emojis/mac/Sous_Barbekyu.webp"))
        self.photo_4_7.setScaledContents(True)
        self.photo_4_7.setObjectName("photo_4_7")
        self.name_4_7 = QtWidgets.QLabel(self.frame_4_7)
        self.name_4_7.setGeometry(QtCore.QRect(65, 215, 120, 30))
        self.name_4_7.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_4_7.setObjectName("name_4_7")
        self.ButtonPlus_4_7 = QtWidgets.QPushButton(self.frame_4_7)
        self.ButtonPlus_4_7.setGeometry(QtCore.QRect(140, 255, 30, 30))
        self.ButtonPlus_4_7.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_4_7.setObjectName("ButtonPlus_4_7")
        self.price_4_7 = QtWidgets.QLabel(self.frame_4_7)
        self.price_4_7.setGeometry(QtCore.QRect(80, 255, 50, 30))
        self.price_4_7.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_4_7.setObjectName("price_4_7")
        self.frame_4_8 = QtWidgets.QFrame(self.tab_4)
        self.frame_4_8.setGeometry(QtCore.QRect(980, 370, 250, 300))
        self.frame_4_8.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame_4_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4_8.setObjectName("frame_4_8")
        self.photo_4_8 = QtWidgets.QLabel(self.frame_4_8)
        self.photo_4_8.setGeometry(QtCore.QRect(25, 10, 200, 200))
        self.photo_4_8.setText("")
        self.photo_4_8.setPixmap(QtGui.QPixmap("emojis/mac/Sous_Gorchichnyy.webp"))
        self.photo_4_8.setScaledContents(True)
        self.photo_4_8.setObjectName("photo_4_8")
        self.name_4_8 = QtWidgets.QLabel(self.frame_4_8)
        self.name_4_8.setGeometry(QtCore.QRect(55, 215, 140, 30))
        self.name_4_8.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.name_4_8.setObjectName("name_4_8")
        self.ButtonPlus_4_8 = QtWidgets.QPushButton(self.frame_4_8)
        self.ButtonPlus_4_8.setGeometry(QtCore.QRect(140, 255, 30, 30))
        self.ButtonPlus_4_8.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                          "background-color: rgb(172, 172, 172);")
        self.ButtonPlus_4_8.setObjectName("ButtonPlus_4_8")
        self.price_4_8 = QtWidgets.QLabel(self.frame_4_8)
        self.price_4_8.setGeometry(QtCore.QRect(80, 255, 50, 30))
        self.price_4_8.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.price_4_8.setObjectName("price_4_8")
        self.m.addTab(self.tab_4, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.summ = QtWidgets.QLabel(self.tab_6)
        self.summ.setGeometry(QtCore.QRect(420, 50, 271, 111))
        self.summ.setToolTipDuration(1)
        self.summ.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                "font: 87 14pt \"Arial Black\";")
        self.summ.setObjectName("summ")
        self.summ_rub = QtWidgets.QLabel(self.tab_6)
        self.summ_rub.setGeometry(QtCore.QRect(690, 50, 121, 111))
        self.summ_rub.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                    "font: 87 10pt \"Arial Black\";")
        self.summ_rub.setText(f"  {fp_beg()} ")
        self.summ_rub.setObjectName("summ_rub")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_6)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(210, 210, 881, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.verticalLayoutWidget)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.verticalLayout.addWidget(self.verticalScrollBar)
        self.pushButton = QtWidgets.QPushButton(self.tab_6)
        self.pushButton.setGeometry(QtCore.QRect(1000, 620, 251, 61))
        self.pushButton.setStyleSheet("background-color: rgb(172, 172, 172);\n"
                                      "font: 87 16pt \"Arial Black\";")
        self.pushButton.setObjectName("pushButton")
        self.photo = QtWidgets.QLabel(self.tab_6)
        self.photo.setGeometry(QtCore.QRect(1070, 30, 151, 131))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("photos/McDonald\'s_Golden_Arches.svg.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.m.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.m.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Заказ"))
        self.name_1_1.setText(_translate("MainWindow", (f"  {bigmak()} ")))
        self.ButtonPlus_1_1.setText(_translate("MainWindow", "+"))
        self.price_1_1.setText(_translate("MainWindow", (f"  {bigmak_p()} ₽")))
        self.name_1_6.setText(_translate("MainWindow", (f"  {chickenburger()} ")))
        self.ButtonPlus_1_6.setText(_translate("MainWindow", "+"))
        self.price_1_.setText(_translate("MainWindow", (f"  {chickenburger_p()} ₽")))
        self.name_1_3.setText(_translate("MainWindow", (f"  {dv_fileofish()} ")))
        self.ButtonPlus_1_3.setText(_translate("MainWindow", "+"))
        self.price_1_3.setText(_translate("MainWindow", (f"  {dv_fileofish_p()} ₽")))
        self.name_1_7.setText(_translate("MainWindow", (f"  {fileofish()} ")))
        self.ButtonPlus_1_7.setText(_translate("MainWindow", "+"))
        self.price_1_7.setText(_translate("MainWindow", (f"  {fileofish_p()} ₽")))
        self.name_1_2.setText(_translate("MainWindow", (f"  {makchicken()} ")))
        self.ButtonPlus_1_2.setText(_translate("MainWindow", "+"))
        self.price_1_2.setText(_translate("MainWindow", (f"  {makchicken_p()} ₽")))
        self.name_1_5.setText(_translate("MainWindow", (f"  {gamburger()} ")))
        self.ButtonPlus_1_5.setText(_translate("MainWindow", "+"))
        self.price_1_5.setText(_translate("MainWindow", (f"  {gamburger_p()} ₽")))
        self.name_1_4.setText(_translate("MainWindow", (f"  {dv_royal()} ")))
        self.ButtonPlus_1_4.setText(_translate("MainWindow", "+"))
        self.price_1_4.setText(_translate("MainWindow", (f"  {dv_royal_p()} ₽")))
        self.name_1_8.setText(_translate("MainWindow", (f"  {bigtasty()} ")))
        self.ButtonPlus_1_8.setText(_translate("MainWindow", "+"))
        self.price_1_8.setText(_translate("MainWindow", (f"  {bigtasty_p()} ₽")))
        self.m.setTabText(self.m.indexOf(self.tab_1), _translate("MainWindow", "Бургеры"))
        self.name_2_7.setText(_translate("MainWindow", (f"  {cheese_sticks()} ")))
        self.ButtonPlus_2_7.setText(_translate("MainWindow", "+"))
        self.price_2_7.setText(_translate("MainWindow", (f"  {cheese_sticks_p()} ₽")))
        self.name_2_8.setText(_translate("MainWindow", (f"  {salad()} ")))
        self.ButtonPlus_2_8.setText(_translate("MainWindow", "+"))
        self.price_2_8.setText(_translate("MainWindow", (f"  {salad_p()} ₽")))
        self.name_2_4.setText(_translate("MainWindow", (f"  {strips()} ")))
        self.ButtonPlus_2_4.setText(_translate("MainWindow", "+"))
        self.price_2_4.setText(_translate("MainWindow", (f"  {strips_p()} ₽")))
        self.name_2_2.setText(_translate("MainWindow", (f"  {chicken_wings()} ")))
        self.ButtonPlus_2_2.setText(_translate("MainWindow", "+"))
        self.price_2_2.setText(_translate("MainWindow", (f"  {chicken_wings_p()} ₽")))
        self.name_2_6.setText(_translate("MainWindow", (f"  {shrimps()} ")))
        self.ButtonPlus_2_6.setText(_translate("MainWindow", "+"))
        self.price_2_6.setText(_translate("MainWindow", (f"  {shrimps_p()} ₽")))
        self.name_2_3.setText(_translate("MainWindow", (f"  {nuggets()} ")))
        self.ButtonPlus_2_3.setText(_translate("MainWindow", "+"))
        self.price_2_3.setText(_translate("MainWindow", (f"  {nuggets_p()} ₽")))
        self.name_2_1.setText(_translate("MainWindow", (f"  {french_fries()} ")))
        self.ButtonPlus_2_1.setText(_translate("MainWindow", "+"))
        self.price_2_1.setText(_translate("MainWindow", (f"  {frensh_fries_p()} ₽")))
        self.name_2_5.setText(_translate("MainWindow", (f"  {rustic_potatoes()} ")))
        self.ButtonPlus_2_5.setText(_translate("MainWindow", "+"))
        self.price_2_5.setText(_translate("MainWindow", (f"  {rustic_potatoes_p()} ₽")))
        self.m.setTabText(self.m.indexOf(self.tab_2), _translate("MainWindow", "Закуски"))
        self.name_3_1.setText(_translate("MainWindow", (f"  {cappuccino()} ")))
        self.ButtonPlus_3_1.setText(_translate("MainWindow", "+"))
        self.price_3_1.setText(_translate("MainWindow", (f"  {cappuccino_p()} ₽")))
        self.name_3_2.setText(_translate("MainWindow", (f"  {latte()} ")))
        self.ButtonPlus_3_2.setText(_translate("MainWindow", "+"))
        self.price_3_2.setText(_translate("MainWindow", (f"  {latte_p()} ₽")))
        self.name_3_3.setText(_translate("MainWindow", (f"  {americano()} ")))
        self.ButtonPlus_3_3.setText(_translate("MainWindow", "+"))
        self.price_3_3.setText(_translate("MainWindow", (f"  {americano_p()} ₽")))
        self.name_3_4.setText(_translate("MainWindow", (f"  {black_tea()} ")))
        self.ButtonPlus_3_4.setText(_translate("MainWindow", "+"))
        self.price_3_4.setText(_translate("MainWindow", (f"  {black_tea_p()} ₽")))

        self.name_3_5.setText(_translate("MainWindow", (f"  {cola()} ")))
        self.ButtonPlus_3_5.setText(_translate("MainWindow", "+"))

        self.price_3_5.setText(_translate("MainWindow", (f"  {cola_p()} ₽")))

        self.name_3_6.setText(_translate("MainWindow", (f"  {fanta()} ")))
        self.ButtonPlus_3_6.setText(_translate("MainWindow", "+"))

        self.price_3_6.setText(_translate("MainWindow", (f"  {fanta_p()} ₽")))

        self.name_3_7.setText(_translate("MainWindow", (f"  {sprite()} ")))
        self.ButtonPlus_3_7.setText(_translate("MainWindow", "+"))

        self.price_3_7.setText(_translate("MainWindow", (f"  {sprite_p()} ₽")))

        self.name_3_8.setText(_translate("MainWindow", (f"  {cocktail()} ")))
        self.ButtonPlus_1_16.setText(_translate("MainWindow", "+"))

        self.price_3_8.setText(_translate("MainWindow", (f"  {cocktail_p()} ₽")))
        self.m.setTabText(self.m.indexOf(self.tab_3), _translate("MainWindow", "Напитки"))

        self.name_4_1.setText(_translate("MainWindow", (f"  {s_1()} ")))
        self.ButtonPlus_4_1.setText(_translate("MainWindow", "+"))

        self.price_4_1.setText(_translate("MainWindow", (f"  {s_1_p()} ₽")))

        self.name_4_2.setText(_translate("MainWindow", (f"  {s_2()} ")))
        self.ButtonPlus_4_2.setText(_translate("MainWindow", "+"))

        self.price_4_2.setText(_translate("MainWindow", (f"  {s_2_p()} ₽")))

        self.name_4_3.setText(_translate("MainWindow", (f"  {s_3()} ")))
        self.ButtonPlus_4_3.setText(_translate("MainWindow", "+"))

        self.price_4_3.setText(_translate("MainWindow", (f"  {s_3_p()} ₽")))

        self.name_4_4.setText(_translate("MainWindow", (f"  {s_4()} ")))
        self.ButtonPlus_4_4.setText(_translate("MainWindow", "+"))
        self.price_4_4.setText(_translate("MainWindow", (f"  {s_4_p()} ₽")))
        self.name_4_5.setText(_translate("MainWindow", (f"  {s_5()} ")))
        self.ButtonPlus_4_5.setText(_translate("MainWindow", "+"))
        self.price_4_5.setText(_translate("MainWindow", (f"  {s_5_p()} ₽")))
        self.name_4_6.setText(_translate("MainWindow", (f"  {s_6()} ")))
        self.ButtonPlus_4_6.setText(_translate("MainWindow", "+"))
        self.price_4_6.setText(_translate("MainWindow", (f"  {s_6_p()} ₽")))
        self.name_4_7.setText(_translate("MainWindow", (f"  {s_7()} ")))
        self.ButtonPlus_4_7.setText(_translate("MainWindow", "+"))
        self.price_4_7.setText(_translate("MainWindow", (f"  {s_7_p()} ₽")))
        self.name_4_8.setText(_translate("MainWindow", (f"  {s_8()} ")))
        self.ButtonPlus_4_8.setText(_translate("MainWindow", "+"))
        self.price_4_8.setText(_translate("MainWindow", (f"  {s_8_p()} ₽")))
        self.m.setTabText(self.m.indexOf(self.tab_4), _translate("MainWindow", "Соусы"))
        self.summ.setText(_translate("MainWindow", "    Общая стоимость:"))
        self.pushButton.setText(_translate("MainWindow", "Заказать"))
        self.m.setTabText(self.m.indexOf(self.tab_6), _translate("MainWindow", "Корзина"))


a = 0
t = 0


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.t1_1()
        self.t1_2()
        self.t1_3()
        self.t1_4()
        self.t1_5()
        self.t1_6()
        self.t1_7()
        self.t1_8()

        self.t2_1()
        self.t2_2()
        self.t2_3()
        self.t2_4()
        self.t2_5()
        self.t2_6()
        self.t2_7()
        self.t2_8()

        self.t3_1()
        self.t3_2()
        self.t3_3()
        self.t3_4()
        self.t3_5()
        self.t3_6()
        self.t3_7()
        self.t3_8()

        self.t4_1()
        self.t4_2()
        self.t4_3()
        self.t4_4()
        self.t4_5()
        self.t4_6()
        self.t4_7()
        self.t4_8()

        self.fp()

    def t1_1(self):
        self.ButtonPlus_1_1.clicked.connect(self.run1_1)

    def run1_1(self):
        global t
        a = (int(self.price_1_1.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t1_2(self):
        self.ButtonPlus_1_2.clicked.connect(self.run1_2)

    def run1_2(self):
        global t
        a = (int(self.price_1_2.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t1_3(self):
        self.ButtonPlus_1_3.clicked.connect(self.run1_3)

    def run1_3(self):
        global t
        a = (int(self.price_1_3.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t1_4(self):
        self.ButtonPlus_1_4.clicked.connect(self.run1_4)

    def run1_4(self):
        global t
        a = (int(self.price_1_4.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t1_5(self):
        self.ButtonPlus_1_5.clicked.connect(self.run1_5)

    def run1_5(self):
        global t
        a = (int(self.price_1_5.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t1_6(self):
        self.ButtonPlus_1_6.clicked.connect(self.run1_6)

    def run1_6(self):
        global t
        a = (int(self.price_1_.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t1_7(self):
        self.ButtonPlus_1_7.clicked.connect(self.run1_7)

    def run1_7(self):
        global t
        a = (int(self.price_1_7.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t1_8(self):
        self.ButtonPlus_1_8.clicked.connect(self.run1_8)

    def run1_8(self):
        global t
        a = (int(self.price_1_8.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###
    ###

    def t2_1(self):
        self.ButtonPlus_2_1.clicked.connect(self.run2_1)

    def run2_1(self):
        global t
        a = (int(self.price_2_1.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t2_2(self):
        self.ButtonPlus_2_2.clicked.connect(self.run2_2)

    def run2_2(self):
        global t
        a = (int(self.price_2_2.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t2_3(self):
        self.ButtonPlus_2_3.clicked.connect(self.run2_3)

    def run2_3(self):
        global t
        a = (int(self.price_2_3.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t2_4(self):
        self.ButtonPlus_2_4.clicked.connect(self.run2_4)

    def run2_4(self):
        global t
        a = (int(self.price_2_4.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t2_5(self):
        self.ButtonPlus_2_5.clicked.connect(self.run2_5)

    def run2_5(self):
        global t
        a = (int(self.price_2_5.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t2_6(self):
        self.ButtonPlus_2_6.clicked.connect(self.run2_6)

    def run2_6(self):
        global t
        a = (int(self.price_2_6.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t2_7(self):
        self.ButtonPlus_2_7.clicked.connect(self.run2_7)

    def run2_7(self):
        global t
        a = (int(self.price_2_7.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t2_8(self):
        self.ButtonPlus_2_8.clicked.connect(self.run2_8)

    def run2_8(self):
        global t
        a = (int(self.price_2_8.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###
    ###

    def t3_1(self):
        self.ButtonPlus_3_1.clicked.connect(self.run3_1)

    def run3_1(self):
        global t
        a = (int(self.price_3_1.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t3_2(self):
        self.ButtonPlus_3_2.clicked.connect(self.run3_2)

    def run3_2(self):
        global t
        a = (int(self.price_3_2.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t3_3(self):
        self.ButtonPlus_3_3.clicked.connect(self.run3_3)

    def run3_3(self):
        global t
        a = (int(self.price_3_3.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t3_4(self):
        self.ButtonPlus_3_4.clicked.connect(self.run3_4)

    def run3_4(self):
        global t
        a = (int(self.price_3_4.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t3_5(self):
        self.ButtonPlus_3_5.clicked.connect(self.run3_5)

    def run3_5(self):
        global t
        a = (int(self.price_3_5.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t3_6(self):
        self.ButtonPlus_3_6.clicked.connect(self.run3_6)

    def run3_6(self):
        global t
        a = (int(self.price_3_6.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t3_7(self):
        self.ButtonPlus_3_7.clicked.connect(self.run3_7)

    def run3_7(self):
        global t
        a = (int(self.price_3_7.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t3_8(self):
        self.ButtonPlus_1_16.clicked.connect(self.run3_8)

    def run3_8(self):
        global t
        a = (int(self.price_3_8.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###
    ###

    def t4_1(self):
        self.ButtonPlus_4_1.clicked.connect(self.run4_1)

    def run4_1(self):
        global t
        a = (int(self.price_4_1.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t4_2(self):
        self.ButtonPlus_4_2.clicked.connect(self.run4_2)

    def run4_2(self):
        global t
        a = (int(self.price_4_2.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t4_3(self):
        self.ButtonPlus_4_3.clicked.connect(self.run4_3)

    def run4_3(self):
        global t
        a = (int(self.price_4_3.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t4_4(self):
        self.ButtonPlus_4_4.clicked.connect(self.run4_4)

    def run4_4(self):
        global t
        a = (int(self.price_4_4.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t4_5(self):
        self.ButtonPlus_4_5.clicked.connect(self.run4_5)

    def run4_5(self):
        global t
        a = (int(self.price_4_5.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t4_6(self):
        self.ButtonPlus_4_6.clicked.connect(self.run4_6)

    def run4_6(self):
        global t
        a = (int(self.price_4_6.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t4_7(self):
        self.ButtonPlus_4_7.clicked.connect(self.run4_7)

    def run4_7(self):
        global t
        a = (int(self.price_4_7.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    ###

    def t4_8(self):
        self.ButtonPlus_4_8.clicked.connect(self.run4_8)

    def run4_8(self):
        global t
        a = (int(self.price_4_8.text()[2:-2]))
        print(a)
        t = a + t
        self.summ_rub.setText(str(t))
        update_final_price(1, t)

    def fp(self):
        self.pushButton.clicked.connect(self.run_fp)

    def run_fp(self):
        self.summ_rub.setText('0')
        global t
        t = 0
        update_final_price(1, 0)


def update_final_price(dev_id, fp):
    sql_update_query = """Update final_price set fp = ? where id = ?"""
    data = (fp, dev_id)
    cur.execute(sql_update_query, data)
    con.commit()
    print("Запись успешно обновлена")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
