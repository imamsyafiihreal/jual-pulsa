import sys
from  PyQt5 import QtWidgets, uic, QtSql, QtCore
from PyQt5.QtSql import QSqlTableModel

import laporan

class pulsa(QtWidgets.QMainWindow):
    def __init__(self):
        super(pulsa, self).__init__()
        uic.loadUi('database_pulsa.ui',self)
        self.show()
        self.setWindowTitle('Tugas 2')
        self.textEdit_harga.setText('Rp. 7000,-')
        self.textEdit_harga_fix.setText('7000')
        self.textEdit_harga.setStyleSheet('font:25px')
        self.lineEdit_nohp.setText('087')
        self.label_msg.hide()
        
        self.openDB()
        self.model = QtSql.QSqlTableModel()
        self.displaytable('')

        self.combo_pulsaXL.currentIndexChanged.connect(self.setHargaXL)#-
        self.combo_pulsaAxis.currentIndexChanged.connect(self.setHargaAxis)
        self.combo_pulsaTelkomsel.currentIndexChanged.connect(self.setHargaTelkomsel)
        self.combo_pulsaIndosat.currentIndexChanged.connect(self.setHargaIndosat)
        self.combo_pulsaSmartfren.currentIndexChanged.connect(self.setHargaSmartfren)

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
        self.combo_pulsaAxis.hide()#-
        self.combo_pulsaTelkomsel.hide()
        self.combo_pulsaIndosat.hide()
        self.combo_pulsaSmartfren.hide()

        self.label_2.setStyleSheet('color:#1c50a3;')
        self.label_3.setStyleSheet('color:#1c50a3;')
        self.label_5.setStyleSheet('color:#1c50a3;')
        self.label_7.setStyleSheet('color:#1c50a3;')
        self.label_8.setStyleSheet('color:#1c50a3;')
        self.label_6.setStyleSheet('color:#1c50a3;')
        self.lineEdit_nohp.setStyleSheet('color:#1c50a3; border:1px solid #1c50a3;')
        self.lineEdit_search.setStyleSheet('color:#1c50a3; border:1px solid #1c50a3;')
        self.combo_sc.setStyleSheet('color:#1c50a3; border:1px solid #1c50a3;')
        self.combo_pulsaXL.setStyleSheet('color:#1c50a3; border:1px solid #1c50a3;')
        self.combo_pulsaAxis.setStyleSheet('color:#1c50a3; border:1px solid #1c50a3;')
        self.combo_pulsaTelkomsel.setStyleSheet('color:#1c50a3; border:1px solid #1c50a3;')
        self.combo_pulsaIndosat.setStyleSheet('color:#1c50a3; border:1px solid #1c50a3;')
        self.combo_pulsaSmartfren.setStyleSheet('color:#1c50a3; border:1px solid #1c50a3;')
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

    def setLogo(self):
        comboindex = self.sender().currentIndex()
        if comboindex == 0: #Simcard XL
            self.lineEdit_nohp.setText('087')
            self.textEdit_harga.setText('Rp. 7000,-')
            self.textEdit_harga_fix.setText('7000')
            self.combo_pulsaXL.show()#-combo
            self.combo_pulsaAxis.hide()
            self.combo_pulsaTelkomsel.hide()
            self.combo_pulsaIndosat.hide()
            self.combo_pulsaSmartfren.hide()
            self.label_xl.show()#-label
            self.label_axis.hide()
            self.label_telkomsel.hide()
            self.label_indosat.hide()
            self.label_smartfren.hide()

            
        elif comboindex == 1: #Simcard Axis
            self.lineEdit_nohp.setText('083')
            self.textEdit_harga.setText('Rp. 7000,-')
            self.textEdit_harga_fix.setText('7000')
            self.combo_pulsaXL.hide()#-combo
            self.combo_pulsaAxis.show()
            self.combo_pulsaTelkomsel.hide()
            self.combo_pulsaIndosat.hide()
            self.combo_pulsaSmartfren.hide()
            self.label_xl.hide()#-label
            self.label_axis.show()
            self.label_telkomsel.hide()
            self.label_indosat.hide()
            self.label_smartfren.hide()
            
        elif comboindex == 2: #Simcard Telkomsel
            self.lineEdit_nohp.setText('082')
            self.textEdit_harga.setText('Rp. 18000,-')
            self.textEdit_harga_fix.setText('18000')
            self.combo_pulsaXL.hide()#-combo
            self.combo_pulsaAxis.hide()
            self.combo_pulsaTelkomsel.show()
            self.combo_pulsaIndosat.hide()
            self.combo_pulsaSmartfren.hide()
            self.label_xl.hide()
            self.label_axis.hide()
            self.label_telkomsel.show()
            self.label_indosat.hide()
            self.label_smartfren.hide()
            
        elif comboindex == 3: #Simcard Indosat
            self.lineEdit_nohp.setText('085')
            self.textEdit_harga.setText('Rp. 7000,-')
            self.textEdit_harga_fix.setText('7000')
            self.combo_pulsaXL.hide()#-combo
            self.combo_pulsaAxis.hide()
            self.combo_pulsaTelkomsel.hide()
            self.combo_pulsaIndosat.show()
            self.combo_pulsaSmartfren.hide()
            self.label_xl.hide()#-label
            self.label_axis.hide()
            self.label_telkomsel.hide()
            self.label_indosat.show()
            self.label_smartfren.hide()
            
        elif comboindex == 4: #Simcard Smartfren
            self.lineEdit_nohp.setText('088')
            self.textEdit_harga.setText('Rp. 7000,-')
            self.textEdit_harga_fix.setText('7000')
            self.label_msg.show()
            self.combo_pulsaXL.hide()#-combo
            self.combo_pulsaAxis.hide()
            self.combo_pulsaTelkomsel.hide()
            self.combo_pulsaIndosat.hide()
            self.combo_pulsaSmartfren.show()
            self.label_xl.hide()#-label
            self.label_axis.hide()
            self.label_telkomsel.hide()
            self.label_indosat.hide()
            self.label_smartfren.show()

    def setHargaXL(self): #=========== HARGA XL ==========#
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
            hrg = 18000
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

    def setHargaAxis(self): #=========== HARGA AXIS ==========#
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
            hrg = 18000
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
    def setHargaTelkomsel(self): #=========== HARGA TELKOMSEL ==========#
        comboindex = self.sender().currentIndex()
        if comboindex == 0: #15.000
            hrg = 18000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 1: #20.000
            hrg = 22000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 2: #25.000
            hrg = 27000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 3: #30.000
            hrg = 30000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 4: #40.000
            hrg = 40000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 5: #50.000
            hrg = 52000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
    def setHargaIndosat(self): #=========== HARGA INDOSAT ==========#
        comboindex = self.sender().currentIndex()
        if comboindex == 0: #5.000
            hrg = 7000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 1: #10.000
            hrg = 12000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 2: #20.000
            hrg = 22000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 3: #25.000
            hrg = 27000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 4: #30.000
            hrg = 30000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 5: #50.000
            hrg = 50000
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
    def setHargaSmartfren(self): #=========== HARGA SMARTFREN ==========#
        comboindex = self.sender().currentIndex()
        if comboindex == 0: #5.000
            hrg = 7000
            self.label_msg.show()
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 1: #20.000
            hrg = 22000
            self.label_msg.hide()
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
        elif comboindex == 1: #50.000
            hrg = 50000
            self.label_msg.hide()
            self.textEdit_harga.setText("Rp. "+str(hrg)+",-")
            self.textEdit_harga_fix.setText(str(hrg))
    
            
        
    def displaytable(self,p_filter):
        if p_filter == "":
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
        pulsa = self.combo_pulsaXL.currentText() or self.combo_pulsaAxis.currentText() or self.combo_pulsaTelkomsel.currentText() or self.combo_pulsaIndosat.currentText() or self.combo_pulsaSmartfren.currentText()
        harga = self.textEdit_harga_fix.toPlainText()
        
        query = QtSql.QSqlQuery()
        query.exec_("insert into pulsa values (null,'"+nohp+"','"+sc+"','"+pulsa+"','"+harga+"','"+tgl+"')")
        self.displaytable('')

        self.lineEdit_nohp.setText('087')
        self.textEdit_harga.setText('Rp. 7000,-')
        self.combo_pulsaXL.setCurrentIndex(0)
        self.combo_pulsaAxis.setCurrentIndex(0)
        self.combo_pulsaTelkomsel.setCurrentIndex(0)
        self.combo_pulsaIndosat.setCurrentIndex(0)
        self.combo_pulsaSmartfren.setCurrentIndex(0)
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
