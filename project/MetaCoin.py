# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/tmp/MetaCoinn11308.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from cobra_contract import Contract
from cobra_hdwallet import HDWallet

# MetaCoin artifact path!
metacoin_artifact = "/home/meheret/PycharmProjects/metacoin-example/build/contracts/MetaCoin.json"


class UIMetaCoin(object):

    def __init__(self):
        self.instance = None
        self.web3 = None
        self.eth = None
        self.metacoin()

    def setupUi(self, MetaCoin):
        MetaCoin.setObjectName("MetaCoin")
        MetaCoin.resize(442, 627)
        MetaCoin.setMinimumSize(QtCore.QSize(442, 627))
        MetaCoin.setMaximumSize(QtCore.QSize(442, 627))
        MetaCoin.setStyleSheet("background: #1e2833;")
        self.widgetGetInfoForm = QtWidgets.QWidget(MetaCoin)
        self.widgetGetInfoForm.setGeometry(QtCore.QRect(0, 80, 441, 201))
        self.widgetGetInfoForm.setObjectName("widgetGetInfoForm")
        self.lineGetInfoFive = QtWidgets.QFrame(self.widgetGetInfoForm)
        self.lineGetInfoFive.setGeometry(QtCore.QRect(10, 120, 421, 20))
        self.lineGetInfoFive.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineGetInfoFive.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineGetInfoFive.setObjectName("lineGetInfoFive")
        self.lineGetInfoFour = QtWidgets.QFrame(self.widgetGetInfoForm)
        self.lineGetInfoFour.setGeometry(QtCore.QRect(10, 0, 421, 20))
        self.lineGetInfoFour.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineGetInfoFour.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineGetInfoFour.setObjectName("lineGetInfoFour")
        self.labelAccount = QtWidgets.QLabel(self.widgetGetInfoForm)
        self.labelAccount.setGeometry(QtCore.QRect(10, 80, 111, 41))
        self.labelAccount.setStyleSheet("color: gold;\n"
                                        "font: 20pt \"Sawasdee\";")
        self.labelAccount.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAccount.setObjectName("labelAccount")
        self.lineEditAccount = QtWidgets.QLineEdit(self.widgetGetInfoForm)
        self.lineEditAccount.setGeometry(QtCore.QRect(140, 80, 281, 41))
        self.lineEditAccount.setStyleSheet("border: none; \n"
                                           "color: gold;\n"
                                           "font: 18pt \"Sawasdee\";")
        self.lineEditAccount.setObjectName("lineEditAccount")
        self.lineGetInfoThree = QtWidgets.QFrame(self.widgetGetInfoForm)
        self.lineGetInfoThree.setGeometry(QtCore.QRect(10, 190, 421, 20))
        self.lineGetInfoThree.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineGetInfoThree.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineGetInfoThree.setObjectName("lineGetInfoThree")
        self.pushButtonGetInfo = QtWidgets.QPushButton(self.widgetGetInfoForm)
        self.pushButtonGetInfo.setGeometry(QtCore.QRect(10, 140, 421, 51))
        self.pushButtonGetInfo.setStyleSheet("QPushButton {\n"
                                             "  font: 20pt \"Sawasdee\"; \n"
                                             "  background: gold;\n"
                                             "  border: none;\n"
                                             "  border-radius: 4px;\n"
                                             "  outline: 0;\n"
                                             "  color: #1e2833;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover {\n"
                                             "  background:rgb(255, 215, 0);\n"
                                             "  outline: 0;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:active {\n"
                                             "  background: gold;\n"
                                             "  outline: 0;\n"
                                             "}")
        self.pushButtonGetInfo.setObjectName("pushButtonGetInfo")
        self.labelGetMetaCoinInfo = QtWidgets.QLabel(self.widgetGetInfoForm)
        self.labelGetMetaCoinInfo.setGeometry(QtCore.QRect(10, 20, 421, 41))
        self.labelGetMetaCoinInfo.setStyleSheet("color: gold;\n"
                                                "font: 20pt \"Sawasdee\";")
        self.labelGetMetaCoinInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelGetMetaCoinInfo.setObjectName("labelGetMetaCoinInfo")
        self.lineGetInfoTwo = QtWidgets.QFrame(self.widgetGetInfoForm)
        self.lineGetInfoTwo.setGeometry(QtCore.QRect(10, 60, 421, 20))
        self.lineGetInfoTwo.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineGetInfoTwo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineGetInfoTwo.setObjectName("lineGetInfoTwo")
        self.lineGetInfoOne = QtWidgets.QFrame(self.widgetGetInfoForm)
        self.lineGetInfoOne.setGeometry(QtCore.QRect(120, 80, 16, 41))
        self.lineGetInfoOne.setFrameShape(QtWidgets.QFrame.VLine)
        self.lineGetInfoOne.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineGetInfoOne.setObjectName("lineGetInfoOne")
        self.widgetSendForm = QtWidgets.QWidget(MetaCoin)
        self.widgetSendForm.setGeometry(QtCore.QRect(0, 350, 441, 241))
        self.widgetSendForm.setObjectName("widgetSendForm")
        self.labelBalanceTwo = QtWidgets.QLabel(self.widgetSendForm)
        self.labelBalanceTwo.setGeometry(QtCore.QRect(10, 60, 111, 41))
        self.labelBalanceTwo.setStyleSheet("color: gold;\n"
                                           "font: 20pt \"Sawasdee\";")
        self.labelBalanceTwo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBalanceTwo.setObjectName("labelBalanceTwo")
        self.lineSendTwo = QtWidgets.QFrame(self.widgetSendForm)
        self.lineSendTwo.setGeometry(QtCore.QRect(120, 60, 16, 101))
        self.lineSendTwo.setFrameShape(QtWidgets.QFrame.VLine)
        self.lineSendTwo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSendTwo.setObjectName("lineSendTwo")
        self.lineSendSix = QtWidgets.QFrame(self.widgetSendForm)
        self.lineSendSix.setGeometry(QtCore.QRect(140, 100, 291, 16))
        self.lineSendSix.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSendSix.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSendSix.setObjectName("lineSendSix")
        self.lineSendThree = QtWidgets.QFrame(self.widgetSendForm)
        self.lineSendThree.setGeometry(QtCore.QRect(10, 40, 421, 20))
        self.lineSendThree.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSendThree.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSendThree.setObjectName("lineSendThree")
        self.labelTo = QtWidgets.QLabel(self.widgetSendForm)
        self.labelTo.setGeometry(QtCore.QRect(10, 120, 111, 41))
        self.labelTo.setStyleSheet("color: gold;\n"
                                   "font: 20pt \"Sawasdee\";")
        self.labelTo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTo.setObjectName("labelTo")
        self.lineSendFour = QtWidgets.QFrame(self.widgetSendForm)
        self.lineSendFour.setGeometry(QtCore.QRect(10, 100, 111, 16))
        self.lineSendFour.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSendFour.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSendFour.setObjectName("lineSendFour")
        self.lineEditAddress = QtWidgets.QLineEdit(self.widgetSendForm)
        self.lineEditAddress.setGeometry(QtCore.QRect(140, 120, 291, 41))
        self.lineEditAddress.setStyleSheet("border: none; \n"
                                           "color: gold;\n"
                                           "font: 18pt \"Sawasdee\";")
        self.lineEditAddress.setObjectName("lineEditAddress")
        self.lineEditBalance = QtWidgets.QLineEdit(self.widgetSendForm)
        self.lineEditBalance.setGeometry(QtCore.QRect(140, 60, 291, 41))
        self.lineEditBalance.setStyleSheet("border: none; \n"
                                           "color: gold;\n"
                                           "font: 18pt \"Sawasdee\";")
        self.lineEditBalance.setInputMask("")
        self.lineEditBalance.setObjectName("lineEditBalance")
        self.lineSendOne = QtWidgets.QFrame(self.widgetSendForm)
        self.lineSendOne.setGeometry(QtCore.QRect(10, 230, 421, 20))
        self.lineSendOne.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSendOne.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSendOne.setObjectName("lineSendOne")
        self.pushButtonSend = QtWidgets.QPushButton(self.widgetSendForm)
        self.pushButtonSend.setGeometry(QtCore.QRect(10, 180, 421, 51))
        self.pushButtonSend.setStyleSheet("QPushButton {\n"
                                          "  font: 20pt \"Sawasdee\"; \n"
                                          "  background: gold;\n"
                                          "  border: none;\n"
                                          "  border-radius: 4px;\n"
                                          "  outline: 0;\n"
                                          "  color: #1e2833;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "  background: gold;\n"
                                          "  outline: 0;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:active {\n"
                                          "  background: gold;\n"
                                          "  outline: 0;\n"
                                          "}")
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.labelSendMetaCoin = QtWidgets.QLabel(self.widgetSendForm)
        self.labelSendMetaCoin.setGeometry(QtCore.QRect(10, 0, 421, 41))
        self.labelSendMetaCoin.setStyleSheet("color: gold;\n"
                                             "font: 20pt \"Sawasdee\";")
        self.labelSendMetaCoin.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSendMetaCoin.setObjectName("labelSendMetaCoin")
        self.lineSendFive = QtWidgets.QFrame(self.widgetSendForm)
        self.lineSendFive.setGeometry(QtCore.QRect(10, 160, 421, 20))
        self.lineSendFive.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSendFive.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSendFive.setObjectName("lineSendFive")
        self.labelMeheretTefsaye = QtWidgets.QLabel(MetaCoin)
        self.labelMeheretTefsaye.setGeometry(QtCore.QRect(10, 590, 421, 31))
        self.labelMeheretTefsaye.setStyleSheet("color: rgb(176, 176, 176);\n"
                                               "font: 12px \"Sawasdee\";")
        self.labelMeheretTefsaye.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMeheretTefsaye.setObjectName("labelMeheretTefsaye")
        self.widgetAddress = QtWidgets.QWidget(MetaCoin)
        self.widgetAddress.setGeometry(QtCore.QRect(10, 290, 421, 61))
        self.widgetAddress.setObjectName("widgetAddress")
        self.lineAddressOme = QtWidgets.QFrame(self.widgetAddress)
        self.lineAddressOme.setGeometry(QtCore.QRect(0, 50, 421, 20))
        self.lineAddressOme.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineAddressOme.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineAddressOme.setObjectName("lineAddressOme")
        self.labelYoursAddress = QtWidgets.QLabel(self.widgetAddress)
        self.labelYoursAddress.setGeometry(QtCore.QRect(0, -10, 421, 31))
        self.labelYoursAddress.setStyleSheet("color: gold;\n"
                                             "font: 16px \"Sawasdee\";")
        self.labelYoursAddress.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYoursAddress.setObjectName("labelYoursAddress")
        self.labelAccountAddress = QtWidgets.QLabel(self.widgetAddress)
        self.labelAccountAddress.setGeometry(QtCore.QRect(0, 20, 421, 31))
        self.labelAccountAddress.setStyleSheet("color: red;\n"
                                               "font: 18pt \"Sawasdee\";")
        self.labelAccountAddress.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAccountAddress.setObjectName("labelAccountAddress")
        self.widgetHeader = QtWidgets.QWidget(MetaCoin)
        self.widgetHeader.setGeometry(QtCore.QRect(10, 0, 421, 81))
        self.widgetHeader.setObjectName("widgetHeader")
        self.labelMetaCoin = QtWidgets.QLabel(self.widgetHeader)
        self.labelMetaCoin.setGeometry(QtCore.QRect(10, 0, 141, 81))
        self.labelMetaCoin.setStyleSheet("color: gold;\n"
                                         "font: 75 24pt \"Sawasdee\";")
        self.labelMetaCoin.setObjectName("labelMetaCoin")
        self.labelBalanceOne = QtWidgets.QLabel(self.widgetHeader)
        self.labelBalanceOne.setGeometry(QtCore.QRect(150, 0, 201, 81))
        self.labelBalanceOne.setStyleSheet("color: gold;\n"
                                           "margin-right: 0.5;\n"
                                           "font: 20pt \"Sawasdee\";")
        self.labelBalanceOne.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelBalanceOne.setObjectName("labelBalanceOne")
        self.labelCoin = QtWidgets.QLabel(self.widgetHeader)
        self.labelCoin.setGeometry(QtCore.QRect(350, 0, 61, 81))
        self.labelCoin.setStyleSheet("color: gold;\n"
                                     "font: 20pt \"Sawasdee\";")
        self.labelCoin.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelCoin.setObjectName("labelCoin")

        self.retranslateUi(MetaCoin)
        QtCore.QMetaObject.connectSlotsByName(MetaCoin)

    def retranslateUi(self, MetaCoin):
        _translate = QtCore.QCoreApplication.translate
        MetaCoin.setWindowTitle(_translate("MetaCoin", "MetaCoin"))
        self.labelAccount.setText(_translate("MetaCoin", "Account"))
        self.lineEditAccount.setPlaceholderText(_translate("MetaCoin", "0xAddress/Private key"))
        self.pushButtonGetInfo.setText(_translate("MetaCoin", "Get Information"))
        self.labelGetMetaCoinInfo.setText(_translate("MetaCoin", "Get MetaCoin Information"))
        self.labelBalanceTwo.setText(_translate("MetaCoin", "Balance"))
        self.labelTo.setText(_translate("MetaCoin", "To"))
        self.lineEditAddress.setPlaceholderText(_translate("MetaCoin", "0xAddress"))
        self.lineEditBalance.setPlaceholderText(_translate("MetaCoin", "1234"))
        self.pushButtonSend.setText(_translate("MetaCoin", "Send"))
        self.labelSendMetaCoin.setText(_translate("MetaCoin", "Send MetaCoin"))
        self.labelMeheretTefsaye.setText(_translate("MetaCoin", "@2019, Auther Meheret Tesfaye"))
        self.labelYoursAddress.setText(_translate("MetaCoin", "Your\'s Address"))
        self.labelAccountAddress.setText(_translate("MetaCoin", "No 0xAddress"))
        self.labelMetaCoin.setText(_translate("MetaCoin", "MetaCoin"))
        self.labelBalanceOne.setText(_translate("MetaCoin", "No"))
        self.labelCoin.setText(_translate("MetaCoin", "Coin"))

        self.pushButtonGetInfo.clicked.connect(self.getInfo)
        self.pushButtonSend.clicked.connect(self.sendMetaCoin)

    def metacoin(self):
        # initializing contract by MetaCoin artifact
        # And set provider in localhost or other
        contract = Contract(metacoin_artifact).setProvider({"HTTPProvider": "http://localhost:8545"})
        # Checking contract is connected
        if contract.isConnected():
            # Get web3 and eth from contract
            self.web3 = contract.getWeb3()
            self.eth = contract.getEth()
            # It is getting contract instance from Etheruem blockchain
            self.instance = contract.deploy()
        else:
            sys.exit()

    def getInfo(self):
        # Get account from client
        account = self.lineEditAccount.text()
        # Checking account
        if self.web3.isAddress(account):
            # To check sum address
            address = self.web3.toChecksumAddress(account)
            # Getting MetaCoin balance by address form instance of MetaCoin
            getBalance = self.instance.getBalance(address)
            self.labelBalanceOne.setText(str(getBalance))
            self.labelBalanceOne.setStyleSheet("color: green;\n"
                                               "margin-top: 3px;\n"
                                               "font: 16pt \"Sawasdee\";")
            # Setting your's address
            self.labelAccountAddress.setText(address)
            self.labelAccountAddress.setStyleSheet("color: green;\n"
                                                   "font: 12pt \"Sawasdee\";")
        elif len(account) == 64:
            # init HDWallet
            hdWallet = HDWallet()
            # Get HDWallet from private key
            pvHDWallet = hdWallet.hdwallet_from_private(account)
            # To check sum address
            address = pvHDWallet['address']
            # Getting MetaCoin balance by address form instance of MetaCoin
            getBalance = self.instance.getBalance(address)
            self.labelBalanceOne.setText(str(getBalance))
            self.labelBalanceOne.setStyleSheet("color: green;\n"
                                               "margin-top: 3px;\n"
                                               "font: 16pt \"Sawasdee\";")
            # Setting your's address
            self.labelAccountAddress.setText(address)
            self.labelAccountAddress.setStyleSheet("color: green;\n"
                                                   "font: 12pt \"Sawasdee\";")
        else:
            self.labelBalanceOne.setText("No")
            self.labelBalanceOne.setStyleSheet("color: red;\n"
                                               "margin-top: 0.5;\n"
                                               "font: 20pt \"Sawasdee\";")
            self.labelAccountAddress.setText("Wrong Account!")
            self.labelAccountAddress.setStyleSheet("color: red;\n"
                                                   "font: 18pt \"Sawasdee\";")

    def sendMetaCoin(self):
        # Get the balance
        balance = int(self.lineEditBalance.text())
        # Get address to send MetaCoin
        toAddress = self.lineEditAddress.text()
        # Sending MetaCoin from address
        fromAccount = self.lineEditAccount.text()
        if len(fromAccount):
            # init HDWallet
            hdWallet = HDWallet()
            # Get HDWallet from private key
            pvHDWallet = hdWallet.hdwallet_from_private(fromAccount)
            # To check sum address
            fromAddress = pvHDWallet['address']
        else:
            fromAddress = fromAccount
        # Validation ..
        if isinstance(balance, int) and self.web3.isAddress(toAddress)\
                and self.web3.isAddress(fromAddress):
            # To check sum address
            toAddress = self.web3.toChecksumAddress(toAddress)
            fromAddress = self.web3.toChecksumAddress(fromAddress)
            # Sending MetaCoin
            self.instance.sendCoin(toAddress, balance, transact={"from": fromAddress})
            # Refreshing account
            self.getInfo()
        else:
            sys.exit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MetaCoin = QtWidgets.QDialog()
    ui = UIMetaCoin()
    ui.setupUi(MetaCoin)
    MetaCoin.show()
    sys.exit(app.exec_())
