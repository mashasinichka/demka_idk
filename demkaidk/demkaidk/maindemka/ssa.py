from PyQt5 import QtWidgets
import avtoriz, table, regi, deli
import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS dannie(name TEXT , last_name TEXT,login TEXT,password TEXT)
''')


class Authorization(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = avtoriz.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.reg_form)
        self.ui.pushButton.clicked.connect(self.auto)
        self.ui.lineEdit.setPlaceholderText('Enter your login')
        self.ui.lineEdit_2.setPlaceholderText('Enter your password')

    def reg_form(self):
        auto.close()
        reg.show()

    def auto(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute(f'SELECT name,last_name FROM dannie WHERE login = "{name}"and password = "{passw}"')
        result = cursor.fetchone()

        if result is None:
            # self.ui.label_2.setText("Такого пользователя нет!")
            QtWidgets.QMessageBox.information(None, "Ошибка", "Такого пользователя нет. Повторите попытку",
                                              buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.Ok)

        else:
            auto.close()
            table.show()
            # table.ui.label.setText(str(result[0]))
            # table.ui.label_2.setText(str(result[1]))


class Registration(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = regi.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.zareg)
        self.ui.pushButton_2.clicked.connect(self.back)

    def zareg(self):
        db = sqlite3.connect("users.db")
        cursor = db.cursor()
        #######################

        # self.ui.lineEdit.setPlaceholderText('Имя')
        # self.ui.lineEdit_2.setPlaceholderText('Фамилия')
        # self.ui.lineEdit_3.setPlaceholderText('Логин')
        # self.ui.lineEdit_4.setPlaceholderText('Пароль')
        #######################
        name = self.ui.lineEdit.text()
        last_name = self.ui.lineEdit_2.text()
        login = self.ui.lineEdit_4.text()
        password = self.ui.lineEdit_3.text()

        if name == "" or last_name == "" or login == "" or password == "":
            QtWidgets.QMessageBox.information(None, "Ошибка", "Неверные данные", buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            row = (name, last_name, login, password)
            command = "INSERT INTO dannie (name, last_name, login, password) VALUES (?, ?, ?, ?)"
            cursor.execute('SELECT login FROM dannie WHERE login = ?', (login,))

            result = cursor.fetchall()
            if result:
                msgbox = QtWidgets.QMessageBox()
                msgbox.setText("Логин уже занят")
                msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msgbox.exec()
            else:
                cursor.execute(command, row)
                msgbox = QtWidgets.QMessageBox()
                msgbox.setText("Регистрация прошла успешно.")
                msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgbox.exec()

        db.commit()
        # QtWidgets.QMessageBox.information(None, "Регистрация", "Вы успешно зарегистрировались",buttons = QtWidgets.QMessageBox.Ok,defaultButton = QtWidgets.QMessageBox.Ok)
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_4.setText("")

        reg.close()
        auto.show()

    def back(self):
        reg.close()
        auto.show()


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = table.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add)
        self.ui.pushButton_2.clicked.connect(self.delete)
        self.ui.pushButton_3.clicked.connect(self.updata)
        #######################
        db = sqlite3.connect("users.db")
        cursor = db.cursor()
        command = "SELECT * FROM dannie"
        result = cursor.execute(command)

        self.ui.tableWidget.setRowCount(0)
        for stroka, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(stroka)
            for stolb, data in enumerate(row_data):
                self.ui.tableWidget.setItem(stroka, stolb, QtWidgets.QTableWidgetItem(str(data)))
        #########################

    def add(self):
        reg.show()

    def updata(self):
        db = sqlite3.connect("users.db")
        cursor = db.cursor()
        command = "SELECT * FROM dannie"
        result = cursor.execute(command)

        self.ui.tableWidget.setRowCount(0)
        for stroka, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(stroka)
            for stolb, data in enumerate(row_data):
                self.ui.tableWidget.setItem(stroka, stolb, QtWidgets.QTableWidgetItem(str(data)))

    def delete(self):
        dit.delete2()


class DelForm(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = deli.Ui_Form()
        self.ui.setupUi(self)
        # self.buttonBox.accepted.connect(self.delete2)
        self.ui.pushButton_3.clicked.connect(self.delete2)

    def delete2(self):
        text, ok = QtWidgets.QInputDialog.getText(None, "Кого удалим?", "Удалить:", echo=0)
        if ok:
            db = sqlite3.connect("users.db")
            cursor = db.cursor()
            command = "DELETE FROM dannie WHERE login =?"
            cursor.execute(command, (text,))
            db.commit()
            table.updata()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    auto = Authorization()
    auto.show()
    reg = Registration()
    table = MainWindow()
    dit = DelForm()
    sys.exit(app.exec_())

