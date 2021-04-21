import sys
from  PyQt5 import QtWidgets, uic, QtSql, QtCore
from PyQt5.QtSql import QSqlTableModel

import laporan

class pulsa(QtWidgets.QMainWindow):
    def __init__(self):
        super(pulsa, self).__init__()
        uic.loadUi('database_pulsa_new.ui',self)
        self.show()
        self.setWindowTitle('Tugas 2')
        self.textEdit_harga.setText('Rp. 7000,-')
        self.textEdit_harga_fix.setText('7000')
        self.textEdit_harga.setStyleSheet('font:25px')
        self.lineEdit_nohp.setText('087')
        
        self.openDB()
        self.model = QtSql.QSqlTableModel()
        self.displaytable('')

        self.combo_pulsa.currentIndexChanged.connect(self.setHarga)
        self.combo_sc.currentIndexChanged.connect(self.setLogo)
        
        self.pushButton.clicked.connect(self.save)
        self.pushButton_add.clicked.connect(self.addrowempty)
        self.pushButton_del.clicked.connect(self.remove)
        self.pushButton_search.clicked.connect(self.search)
        self.pushButton_ref.clicked.connect(self.refresh)
        self.pushButton_lihat.clicked.connect(self.lihat)

        self.textEdit_harga_fix.hide()
        self.label_axis.hide()
        self.label_telkomsel.hide()
        self.label_indosat.hide()
        self.label_smartfren.hide()

        self.label_2.setStyleSheet('color:#1c50a3;')
        self.label_3.setStyleSheet('color:#1c50a3;')
        self.label_5.setStyleSheet('color:#1c50a3;')
        self.label_7.setStyleSheet('color:#1c50a3;')
        self.label_8.setStyleSheet('color:#1c50a3;')
        self.label_6.setStyleSheet('color:#1c50a3;')
        self.lineEdit_nohp.setStyleSheet('color:#1c50a3; border:1px solid #1c50a3;')
        self.lineEdit_search.setStyleSheet('color:#1c50a3; border:1px solid #1c50a3;')
        self.combo_sc.setStyleSheet('color:#1c50a3; border:1px solid #1c50a3;')
        self.combo_pulsa.setStyleSheet('color:#1c50a3; border:1px solid #1c50a3;')
        self.textEdit_harga.setStyleSheet('color:#1c50a3; border:1px solid #1c50a3;')
        self.pushButton.setStyleSheet('border-radius:5px;background-color:#1c50a3;border:1px solid #55d1ed; color:white;')
        self.pushButton_add.setStyleSheet('border-radius:5px;background-color:#1c50a3;border:1px solid #55d1ed; color:white;')
        self.pushButton_ref.setStyleSheet('border-radius:5px;background-color:#1c50a3;border:1px solid #55d1ed; color:white;')
        self.pushButton_lihat.setStyleSheet('border-radius:5px;background-color:#1c50a3;border:1px solid #55d1ed; color:white;')
        self.pushButton_del.setStyleSheet('border-radius:5px;background-color:#1c50a3;border:1px solid #55d1ed; color:white;')
        self.pushButton_search.setStyleSheet('border-radius:5px;background-color:#55d1ed;border:1px solid #1c50a3; color:#1c50a3;')


        
    def openDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('contoh.db')

        if not db.open():
            return False
        else :
            return True

    def setHarga(self):
        comboindex = self.sender().currentIndex()
        if comboindex == 0: #5.000
            hrg = 7000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 1: #10.000
            hrg = 12000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 2: #15.000
            hrg = 12000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 3: #25.000
            hrg = 27000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 4: #50.000
            hrg = 52000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 5: #100.000
            hrg = 102000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 6: #15.000
            hrg = 152000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 7: #200.000
            hrg = 200000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 8: #300.000
            hrg = 300000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 9: #500.000
            hrg = 500000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 10: #1.000.000
            hrg = 1000000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))

    def setLogo(self):
        comboindex = self.sender().currentIndex()
        if comboindex == 0: #Simcard XL

            self.lineEdit_nohp.setText('087')

            self.combo_pulsa_Axis.hide()
            self.combo_pulsa_Telkomsel.hide()
            self.combo_pulsa_Indosat.hide()
            self.combo_pulsa_Smartfren.hide()
            
            self.label_xl.show()
            self.label_axis.hide()
            self.label_telkomsel.hide()
            self.label_indosat.hide()
            self.label_smartfren.hide()
        elif comboindex == 1: #Simcard Axis

            self.lineEdit_nohp.setText('083')
            
            self.label_xl.hide()
            self.label_axis.show()
            self.label_telkomsel.hide()
            self.label_indosat.hide()
            self.label_smartfren.hide()
        elif comboindex == 2: #Simcard Telkomsel

            self.lineEdit_nohp.setText('082')
            
            self.label_xl.hide()
            self.label_axis.hide()
            self.label_telkomsel.show()
            self.label_indosat.hide()
            self.label_smartfren.hide()
        elif comboindex == 3: #Simcard Indosat

            self.lineEdit_nohp.setText('085')
            
            self.label_xl.hide()
            self.label_axis.hide()
            self.label_telkomsel.hide()
            self.label_indosat.show()
            self.label_smartfren.hide()
        elif comboindex == 4: #Simcard Smartfren

            self.lineEdit_nohp.setText('088')
            
            self.label_xl.hide()
            self.label_axis.hide()
            self.label_telkomsel.hide()
            self.label_indosat.hide()
            self.label_smartfren.show()
        
    def displaytable(self,p_filter):
        if p_filter is "":
            self.model.setTable('pulsa')
        else:
            query = QtSql.QSqlQuery("select * from pulsa "
            "where NomerHP like '%"+
            p_filter + "%' ")
            self.model.setTable("")
            self.model.setQuery(query)
            
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.tableView.setModel(self.model)

    def save(self):
        nohp = str(self.lineEdit_nohp.text())
        sc = str(self.combo_sc.currentText())
        tgl = str(self.calendarWidget.selectedDate().toPyDate())
        pulsa = self.combo_pulsa.currentText()
        harga = self.textEdit_harga_fix.toPlainText()
        
        query = QtSql.QSqlQuery()
        query.exec_("insert into pulsa values (null,'"+nohp+"','"+sc+"','"+pulsa+"','"+harga+"','"+tgl+"')")
        self.displaytable('')

        self.lineEdit_nohp.setText('087')
        self.textEdit_harga.setText('Rp. 7000,-')
        self.combo_pulsa.setCurrentIndex(0)
        self.combo_sc.setCurrentIndex(0)

    def addrowempty(self):
        self.model.rowCount()
        ret = self.model.insertRows(self.model.rowCount(),1)
        ret

    def remove(self):
        self.model.removeRow(self.tableView.currentIndex().row())
        self.displaytable('')

    def search(self):
        nohp = self.lineEdit_search.text()
        self.displaytable(nohp)

    def refresh(self):
        self.displaytable('')
        self.lineEdit_search.setText('')
        self.lineEdit_nohp.setText('087')

    def lihat(self):
        self.menu = laporan.laporan()
        self.menu.show()
        self.hide()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = pulsa()
    app.exec_()
