from PyQt5.QtSql import QSqlTableModel
from  PyQt5 import QtWidgets, uic, QtSql, QtCore
import sys

import database_pulsa

class laporan(QtWidgets.QMainWindow):
    def __init__(self):
        super(laporan,self).__init__()
        uic.loadUi('laporan.ui',self)
        self.show()

        self.openDB()
        self.model = QtSql.QSqlTableModel()
        self.displaytable()

        self.label_2.setStyleSheet('color:#1c50a3;')
        self.label_3.setStyleSheet('color:#1c50a3;')
        self.label.setStyleSheet('color:#1c50a3;')
        self.combo_laporan.setStyleSheet('color:#1c50a3; border:1px solid #1c50a3;')
        self.combo_simcard.setStyleSheet('color:#1c50a3; border:1px solid #1c50a3;')
        self.pushButton_back.setStyleSheet('border-radius:5px;background-color:#55d1ed;border:1px solid #1c50a3; color:#1c50a3;')

        self.combo_laporan.currentIndexChanged.connect(self.setLaporan)
        self.combo_simcard.currentIndexChanged.connect(self.setSimcard)

        self.pushButton_back.clicked.connect(self.back)


    def openDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('contoh.db')

        if not db.open():
            return False
        else :
            return True

    def displaytable(self):
        self.model.setTable('pulsa')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.tableView.setModel(self.model)

    def setLaporan(self):

        #ID || NomerHP || SimCard || Nominal || Tanggal
        
        index = self.sender().currentIndex()
        if index == 0:
            self.displaytable()
        elif index == 1: #Per Hari
            query = QtSql.QSqlQuery("select count(ID) jumlahNomor, sum(Harga) TotalHasil, Tanggal from pulsa "
                                    "group by Tanggal")
            self.combo_simcard.setCurrentIndex(0)
            self.model.setTable("")
            self.model.setQuery(query) 
        elif index == 2: #Per Bulan
            query = QtSql.QSqlQuery("select count(ID) jumlahNomor, sum(Harga) TotalCuan, MONTH(Tanggal) BulanKe from pulsa "
                                    "group by MONTH(Tanggal)")
            self.combo_simcard.setCurrentIndex(0)
            self.model.setTable("")
            self.model.setQuery(query)
        elif index == 3: #Per Tahun
            query = QtSql.QSqlQuery("select count(ID) jumlahNomor, sum(Harga) TotalCuan, Tanggal from pulsa "
                                    "group by YEAR(Tanggal)")
            self.combo_simcard.setCurrentIndex(0)
            self.model.setTable("")
            self.model.setQuery(query)



            

    def setSimcard(self):
        index = self.sender().currentIndex()
        if index == 0:
            self.displaytable()
        elif index == 1:
            query = QtSql.QSqlQuery(" select ID,Simcard, NomerHP, Nominal, Tanggal "
                                    " from pulsa where Simcard like '%XL%' ")
            self.combo_laporan.setCurrentIndex(0)
            self.model.setTable("")
            self.model.setQuery(query) 
        elif index == 2:
            query = QtSql.QSqlQuery(" select ID,Simcard, NomerHP, Nominal, Tanggal "
                                    " from pulsa where Simcard like '%Axis%' ")
            self.combo_laporan.setCurrentIndex(0)
            self.model.setTable("")
            self.model.setQuery(query)
        elif index == 3:
            query = QtSql.QSqlQuery(" select ID,Simcard, NomerHP, Nominal, Tanggal "
                                    " from pulsa where Simcard like '%Telkomsel%' ")
            self.combo_laporan.setCurrentIndex(0)
            self.model.setTable("")
            self.model.setQuery(query) 
        elif index == 4:
            query = QtSql.QSqlQuery(" select ID,Simcard, NomerHP, Nominal, Tanggal "
                                    " from pulsa where Simcard like '%Indosat%' ")
            self.combo_laporan.setCurrentIndex(0)
            self.model.setTable("")
            self.model.setQuery(query) 
        elif index == 5:
            query = QtSql.QSqlQuery(" select ID,Simcard, NomerHP, Nominal, Tanggal "
                                    " from pulsa where Simcard like '%Smartfren%' ")
            self.combo_laporan.setCurrentIndex(0)
            self.model.setTable("")
            self.model.setQuery(query)

    def back(self):
        self.menu = database_pulsa.pulsa()
        self.menu.show()
        self.hide()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = laporan()
    app.exec_()
