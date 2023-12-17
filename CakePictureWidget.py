from PyQt5.QtWidgets import QWidget,QMessageBox
from UI.UI_PhotoWidget import Ui_PhotoWidget
from CakeDollMaker import MainWindow
from CreateDBConnect import SingleDBConnect
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtGui import QPixmap

class CakePhotoWidget(QWidget):

    def __init__(self,mainWin=MainWindow):
        super().__init__()
        self.mainWin = mainWin
        self.ui = Ui_PhotoWidget()
        self.ui.setupUi(self)
        # 目录打开
        self.ui.twPhoto.expandAll()
        self.ui.twPhoto.clicked.connect(self.on_photoClassChange)
        #初始化数据库查询
        self.sqlQuery = QSqlQuery(SingleDBConnect().DB)
        self.query = 'select * from PICTURE'

        self.currentPage = 0
        self.pages = 0

        self.ui.pbtnNext.clicked.connect(self.on_pbtnNextPicture)
        self.ui.pbtnPre.clicked.connect(self.on_pbtnPrePicture)
        self.ui.pbtnSearch.clicked.connect(self.on_pbtnSearch)
        self.ui.lineEditKeyword.returnPressed.connect(self.on_pbtnSearch)


    #槽函数，响应照片分类切换
    def on_photoClassChange(self):
        item = self.ui.twPhoto.currentItem().text(0)
        condition = " WHERE CLASS LIKE \'%%%s%%\' " % (item)
        SqlTotoalQuery = self.query + condition
        try:
            self.sqlQuery.exec(SqlTotoalQuery)
            self.sqlQuery.last()
            count = self.sqlQuery.at() + 1
            self.pages = count
            self.ui.labPages.setText(str(count))
            self.sqlQuery.first()
            self.ui.labCurrentPage.setText('1')
            self.currentPage = 1
            self.ui.labInfo.setText(self.sqlQuery.value('TITLE'))
            MD5 = self.sqlQuery.value('MD5')
            data = self.getPictureBinnary(MD5)
            if data is None:
                self.ui.labPhoto.clear()
                return
            else:
                pic = QPixmap()
                pic.loadFromData(data)
                h = self.ui.labPhoto.size().height()
                self.ui.labPhoto.setPixmap(pic.scaledToHeight(h))
        except Exception:
            print(Exception.__str__())

    #槽函数,向前翻一张照片
    def on_pbtnPrePicture(self):
        if self.currentPage == 1:
            return
        else:
            self.sqlQuery.previous()
            self.currentPage = self.currentPage - 1
            self.ui.labCurrentPage.setText(str(self.currentPage))
            self.ui.labInfo.setText(self.sqlQuery.value('TITLE'))
            MD5 = self.sqlQuery.value('MD5')
            data = self.getPictureBinnary(MD5)
            if data is None:
                self.ui.labPhoto.clear()
                return
            else:
                pic = QPixmap()
                pic.loadFromData(data)
                h = self.ui.labPhoto.size().height()
                self.ui.labPhoto.setPixmap(pic.scaledToHeight(h))

    #槽函数，向后翻一张照片
    def on_pbtnNextPicture(self):
        if self.currentPage == self.pages:
            return
        else:
            self.sqlQuery.next()
            self.currentPage = self.currentPage + 1
            self.ui.labCurrentPage.setText(str(self.currentPage))
            self.ui.labInfo.setText(self.sqlQuery.value('TITLE'))
            MD5 = self.sqlQuery.value('MD5')
            data = self.getPictureBinnary(MD5)
            if data is None:
                self.ui.labPhoto.clear()
                return
            else:
                pic = QPixmap()
                pic.loadFromData(data)
                h = self.ui.labPhoto.size().height()
                self.ui.labPhoto.setPixmap(pic.scaledToHeight(h))

    def getPictureBinnary(self,md5):
        condition = "select PICTUREBINNARY FROM PICTUREFILE WHERE MD5 LIKE \'%%%s%%\' " % (md5)
        sql = QSqlQuery(SingleDBConnect().DB)
        sql.exec(condition)
        sql.first()
        return sql.value('PICTUREBINNARY')


    def on_pbtnSearch(self):
        keyword = self.ui.lineEditKeyword.text()
        if keyword == '':
            QMessageBox.information(self,"提示","请输入查询关键字！",QMessageBox.Yes,QMessageBox.Yes)
            self.ui.lineEditKeyword.clear()
            return
        else:
            query = "select * from PICTURE WHERE CLASS LIKE \'%%%s%%\' OR TITLE LIKE \'%%%s%%\'" % (keyword, keyword)
            try:
                self.sqlQuery.exec(query)
                self.sqlQuery.last()
                count = self.sqlQuery.at() + 1
                if count <= 0:
                    QMessageBox.information(self, "提示", "查无相关信息照片", QMessageBox.Yes, QMessageBox.Yes)
                    item = '雷远洲'
                    condition = " WHERE CLASS LIKE \'%%%s%%\' " % (item)
                    SqlTotoalQuery = self.query + condition
                    self.sqlQuery.exec(SqlTotoalQuery)
                    self.sqlQuery.last()
                    count = self.sqlQuery.at() + 1
                    self.pages = count
                    self.ui.labPages.setText(str(count))
                    self.sqlQuery.first()
                    self.ui.labCurrentPage.setText('1')
                    self.currentPage = 1
                    self.ui.labInfo.setText(self.sqlQuery.value('TITLE'))
                    MD5 = self.sqlQuery.value('MD5')
                    data = self.getPictureBinnary(MD5)
                    if data is None:
                        self.ui.labPhoto.clear()
                        return
                    else:
                        pic = QPixmap()
                        pic.loadFromData(data)
                        h = self.ui.labPhoto.size().height()
                        self.ui.labPhoto.setPixmap(pic.scaledToHeight(h))
                else:
                    QMessageBox.information(self, "提示", "查到相关信息照片"+str(count)+'张', QMessageBox.Yes, QMessageBox.Yes)
                    self.pages = count
                    self.ui.labPages.setText(str(count))
                    self.sqlQuery.first()
                    self.ui.labCurrentPage.setText('1')
                    self.currentPage = 1
                    self.ui.labInfo.setText(self.sqlQuery.value('TITLE'))
                    MD5 = self.sqlQuery.value('MD5')
                    data = self.getPictureBinnary(MD5)
                    if data is None:
                        self.ui.labPhoto.clear()
                        return
                    else:
                        pic = QPixmap()
                        pic.loadFromData(data)
                        h = self.ui.labPhoto.size().height()
                        self.ui.labPhoto.setPixmap(pic.scaledToHeight(h))
            except Exception:
                print(Exception.__str__())





