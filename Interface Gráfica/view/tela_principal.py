# -*- coding: utf-8 -*-
import random

################################################################################
## Form generated from reading UI file 'aposta.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
                               QLabel, QLineEdit, QMainWindow, QPushButton,
                               QRadioButton, QSizePolicy, QSpacerItem, QTableWidget,
                               QTableWidgetItem, QVBoxLayout, QWidget, QMessageBox, QAbstractItemView)

from infra.entities.aposta import Aposta
from infra.repository.aposta_repository import ApostaRepository
from infra.configs.connection import DBConnectionHandler


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 737)
        conn = DBConnectionHandler()
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(850, 700))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 871, 721))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(150, 70, 529, 191))
        self.lbl_valor_aposta = QLabel(self.widget_4)
        self.lbl_valor_aposta.setObjectName(u"lbl_valor_aposta")
        self.lbl_valor_aposta.setGeometry(QRect(9, 84, 88, 16))
        self.lbl_nome = QLabel(self.widget_4)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setGeometry(QRect(9, 9, 111, 16))
        self.lbl_vencedor = QLabel(self.widget_4)
        self.lbl_vencedor.setObjectName(u"lbl_vencedor")
        self.lbl_vencedor.setGeometry(QRect(10, 31, 53, 16))
        self.txt_nome = QLineEdit(self.widget_4)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(126, 9, 191, 20))
        self.txt_valor_aposta = QLineEdit(self.widget_4)
        self.txt_valor_aposta.setObjectName(u"txt_valor_aposta")
        self.txt_valor_aposta.setGeometry(QRect(126, 84, 51, 20))
        self.lbl_placar = QLabel(self.widget_4)
        self.lbl_placar.setObjectName(u"lbl_placar")
        self.lbl_placar.setGeometry(QRect(9, 58, 35, 16))
        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(178, 58, 16, 16))
        self.txt_casa = QLineEdit(self.widget_4)
        self.txt_casa.setObjectName(u"txt_casa")
        self.txt_casa.setGeometry(QRect(151, 58, 21, 20))
        self.lbl_casa = QLabel(self.widget_4)
        self.lbl_casa.setObjectName(u"lbl_casa")
        self.lbl_casa.setGeometry(QRect(120, 60, 27, 16))
        self.txt_visitante = QLineEdit(self.widget_4)
        self.txt_visitante.setObjectName(u"txt_visitante")
        self.txt_visitante.setGeometry(QRect(191, 58, 21, 20))
        self.lbl_visitante = QLabel(self.widget_4)
        self.lbl_visitante.setObjectName(u"lbl_visitante")
        self.lbl_visitante.setGeometry(QRect(220, 60, 50, 16))
        self.layoutWidget = QWidget(self.widget_4)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(130, 30, 119, 19))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.rb_casa = QRadioButton(self.layoutWidget)
        self.rb_casa.setObjectName(u"rb_casa")
        self.rb_casa.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_4.addWidget(self.rb_casa)

        self.rb_visitante = QRadioButton(self.layoutWidget)
        self.rb_visitante.setObjectName(u"rb_visitante")
        self.rb_visitante.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_4.addWidget(self.rb_visitante)

        self.layoutWidget_2 = QWidget(self.widget_4)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(190, 160, 169, 25))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.btn_apostar = QPushButton(self.layoutWidget_2)
        self.btn_apostar.setObjectName(u"btn_apostar")
        self.btn_apostar.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_5.addWidget(self.btn_apostar)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.lbl_apostas = QLabel(self.widget_4)
        self.lbl_apostas.setObjectName(u"lbl_apostas")
        self.lbl_apostas.setGeometry(QRect(10, 120, 151, 16))
        self.lbl_qtd_apostas = QLabel(self.widget_4)
        self.lbl_qtd_apostas.setObjectName(u"lbl_qtd_apostas")
        self.lbl_qtd_apostas.setGeometry(QRect(160, 120, 21, 20))
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(170, 310, 521, 321))
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tb_resultado = QTableWidget(self.widget_2)
        if (self.tb_resultado.columnCount() < 3):
            self.tb_resultado.setColumnCount(3)
        tb_nome = QTableWidgetItem()
        self.tb_resultado.setHorizontalHeaderItem(0, tb_nome)
        tb_aposta = QTableWidgetItem()
        self.tb_resultado.setHorizontalHeaderItem(1, tb_aposta)
        tb_valor_ganho = QTableWidgetItem()
        self.tb_resultado.setHorizontalHeaderItem(2, tb_valor_ganho)
        self.tb_resultado.setObjectName(u"tb_resultado")
        self.tb_resultado.setMinimumSize(QSize(401, 0))
        self.tb_resultado.setContextMenuPolicy(Qt.NoContextMenu)
        self.tb_resultado.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout.addWidget(self.tb_resultado)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(37, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_resultado = QPushButton(self.widget_2)
        self.btn_resultado.setObjectName(u"btn_resultado")
        self.btn_resultado.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.btn_resultado)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(252, 270, 371, 38))
        self.txt_result_casa = QLineEdit(self.widget_3)
        self.txt_result_casa.setObjectName(u"txt_result_casa")
        self.txt_result_casa.setGeometry(QRect(131, 8, 21, 20))
        self.txt_result_visitante = QLineEdit(self.widget_3)
        self.txt_result_visitante.setObjectName(u"txt_result_visitante")
        self.txt_result_visitante.setGeometry(QRect(171, 8, 21, 20))
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(158, 8, 16, 16))
        self.lbl_result_casa = QLabel(self.widget_3)
        self.lbl_result_casa.setObjectName(u"lbl_result_casa")
        self.lbl_result_casa.setGeometry(QRect(100, 10, 27, 16))
        self.lbl_result_visitante = QLabel(self.widget_3)
        self.lbl_result_visitante.setObjectName(u"lbl_result_visitante")
        self.lbl_result_visitante.setGeometry(QRect(200, 10, 50, 16))
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(320, 30, 186, 22))
        self.horizontalLayout_6 = QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.lbl_logo = QLabel(self.widget1)
        self.lbl_logo.setObjectName(u"lbl_logo")

        self.horizontalLayout_6.addWidget(self.lbl_logo)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.horizontalLayout_3.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.lbl_qtd_apostas = 0
    # setupUi

        self.btn_apostar.clicked.connect(self.salvar_aposta)
        self.btn_apostar.clicked.connect(self.adicionar_apostador)

        self.btn_resultado.clicked.connect(self.gerar_placar)

        self.tb_resultado.setSelectionMode(QAbstractItemView.NoSelection)
        self.tb_resultado.setEditTriggers(QAbstractItemView.NoEditTriggers)






    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_valor_aposta.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Valor da aposta</span></p></body></html>", None))
        self.lbl_nome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">Nome do Apostador</span></p></body></html>", None))
        self.lbl_vencedor.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">Vencedor</span></p></body></html>", None))
        self.txt_nome.setInputMask("")
        self.lbl_placar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Placar</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">X</span></p></body></html>", None))
        self.lbl_casa.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Casa</span></p></body></html>", None))
        self.lbl_visitante.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Visitante</span></p></body></html>", None))
        self.rb_casa.setText(QCoreApplication.translate("MainWindow", u"Casa", None))
        self.rb_visitante.setText(QCoreApplication.translate("MainWindow", u"Visitante", None))
        self.btn_apostar.setText(QCoreApplication.translate("MainWindow", u"Apostar", None))
        self.lbl_apostas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Quantidade de apostas</span></p></body></html>", None))
        self.lbl_qtd_apostas.setText("")
        ___qtablewidgetitem = self.tb_resultado.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome do Apostador", None));
        ___qtablewidgetitem1 = self.tb_resultado.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Aposta", None));
        ___qtablewidgetitem2 = self.tb_resultado.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Valor ganho", None));
        self.btn_resultado.setText(QCoreApplication.translate("MainWindow", u"Resultado", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">X</span></p></body></html>", None))
        self.lbl_result_casa.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Casa</span></p></body></html>", None))
        self.lbl_result_visitante.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Visitante</span></p></body></html>", None))
        self.lbl_logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Brazino</span><span style=\" font-size:12pt; font-weight:600; color:#005500;\">666</span></p></body></html>", None))
    # retranslateUi



    def salvar_aposta(self):

        if self.validar_aposta():
            db = ApostaRepository()
            aposta = Aposta(nome_apostador=self.txt_nome.text(),
                                 vencedor=None, time_casa = int(self.txt_casa.text()),
                                 time_visitante = int(self.txt_visitante.text()),
                                 valor_aposta = int(self.txt_valor_aposta.text())
                                 )

            if (self.rb_casa.isChecked()):
                aposta.vencedor = 'C'
                retorno = db.insert(aposta)

                if retorno == 'Ok':
                    msg = QMessageBox()
                    msg.setWindowTitle('Aposta realizada')
                    msg.setText('Aposta realizada com sucesso')
                    msg.exec()
            else:
                aposta.vencedor = 'V'
                retorno = db.insert(aposta)
                if retorno == 'Ok':
                    msg = QMessageBox()
                    msg.setWindowTitle('Aposta realizada')
                    msg.setText('Aposta realizada com sucesso')
                    msg.exec()
        else:
            print("Aposta invávila")

        self.popular_tabela()

    def adicionar_apostador(self):
        self.lbl_qtd_apostas += 1

    def gerar_placar(self):
        gols_casa = random.randint(0, 5)
        gols_vistante = random.randint(0, 5)

        self.txt_result_casa.setText(str(gols_casa))
        self.txt_result_visitante.setText(str(gols_vistante))

    def validar_vencedor(self):
        vencedor = None
        if self.txt_result_visitante > self.txt_result_casa:
            vencedor = 'visita'
        elif self.txt_result_visitante < self.txt_result_casa:
            vencedor = 'casa'
        else:
            vencedor = 'empate'

    def validar_ganhador(self):
        if self.rb_casa.isChecked() and self.txt_casa == self.txt_result_casa and self.txt_visitante == self.txt_result_visitante:
            self.txt_valor_aposta = float(self.txt_valor_aposta) * 2
        elif self.rb_visitante.isChecked() and self.txt_casa == self.txt_result_casa and self.txt_visitante == self.txt_result_visitante:
            self.txt_valor_aposta = float(self.txt_valor_aposta) * 2
        elif self.rb_casa.isChecked() and self.txt_casa != self.txt_result_casa and self.txt_visitante != self.txt_result_visitante:
            self.txt_valor_aposta = float(self.txt_valor_aposta) * 0.5
        elif self.rb_visitante.isChecked() and self.txt_casa != self.txt_result_casa and self.txt_visitante != self.txt_result_visitante:
            self.txt_valor_aposta = float(self.txt_valor_aposta) * 0.5
        else:
            self.txt_valor_aposta = 0


    def validar_aposta(self):
        if self.rb_casa.isChecked() and int(self.txt_casa.text()) > int(self.txt_visitante.text()):
            return True
        elif self.rb_visitante.isChecked() and int(self.txt_visitante.text()) > int(self.txt_casa.text()):
            return True
        else:
            return False


    def popular_tabela(self):
        self.tb_resultado.setRowCount(0)
        db = ApostaRepository()
        lista_aposta  = db.select_all()
        self.tb_resultado.setRowCount(len(lista_aposta))

        linha = 0
        for aposta in lista_aposta:

            valores = [aposta.nome_apostador, aposta.vencedor, aposta.time_casa, aposta.time_visitante, aposta.valor_aposta]

            for valor in valores:
                item = QTableWidgetItem(str(valor))
                self.tb_resultado.setItem(linha, valores.index(valor), item)
                self.tb_resultado.item(linha, valores.index(valor))
            linha += 1





