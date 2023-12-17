from PyQt5.QtWidgets import QWidget,QAbstractItemView
from PyQt5.QtCore import Qt,QIODevice,QUrl,QEvent
from PyQt5.QtGui import QIcon
from UI.UI_VideoWidget import Ui_PhotoWidget
from CakeDollMaker import MainWindow
from CreateDBConnect import SingleDBConnect
from PyQt5.QtSql import QSqlQuery,QSqlQueryModel
from PyQt5.QtMultimedia import QMediaContent,QMediaPlayer
import os

class CakeVideoWidget(QWidget):

    def __init__(self,mainWin=MainWindow):
        super().__init__()
        self.mainWin = mainWin
        self.ui = Ui_PhotoWidget()
        self.ui.setupUi(self)

        self.sqlQuery = QSqlQuery(SingleDBConnect().DB)
        self.query = QSqlQuery(SingleDBConnect().DB)
        self.qryModel = QSqlQueryModel(self)

        self.ui.tbvVideo.setModel(self.qryModel)
        self.qryModel.setQuery("select TITLE , SOURCE , SUMMARY , MD5 FROM VIDEO")
        self.initTableView()

        self.ui.tbvVideo.clicked.connect(self.on_tbvVideoClicked)

        # 创建视频播放器
        self.player = QMediaPlayer(self)
        self.player.setNotifyInterval(1000)
        # 设置显示组件
        self.player.setVideoOutput(self.ui.videoWidget)
        #显示组件事件过滤器
        #self.ui.videoWidget.installEventFilter(self)
        self._duration = ''
        self._curPos = ''

        self.player.stateChanged.connect(self.do_stateChanged)
        self.player.positionChanged.connect(self.do_positionChanged)
        self.player.durationChanged.connect(self.do_durationChanged)

        self.ui.pbtnPlay.clicked.connect(self.on_btnPlay_clicked)
        self.ui.pbtnPause.clicked.connect(self.on_btnPause_clicked)
        self.ui.pbtnStop.clicked.connect(self.on_btnStop_clicked)
        self.ui.pbtnSound.clicked.connect(self.on_pbtnSound_clicked)

        self.ui.sliderVolumn.valueChanged.connect(self.on_sliderVolumn_valueChange)
        self.ui.sliderVolumn.setValue(30)
        self.ui.sliderPosition.valueChanged.connect(self.on_sliderPosition_valueChange)

    def initTableView(self):
        self.ui.tbvVideo.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionModel(QAbstractItemView.SingleSelection)
        self.ui.tbvVideo.setAlternatingRowColors(True)
        # 设置默认行高
        self.ui.tbvVideo.verticalHeader().setDefaultSectionSize(60)
        self.ui.tbvVideo.setColumnWidth(0, 320)
        self.ui.tbvVideo.setColumnWidth(1, 220)
        self.qryModel.setHeaderData(0, Qt.Horizontal, "视频名称")
        self.qryModel.setHeaderData(1, Qt.Horizontal, "来源")
        self.ui.tbvVideo.setColumnHidden(2, True)
        self.ui.tbvVideo.setColumnHidden(3, True)


    #槽，选中表格某行响应
    def on_tbvVideoClicked(self,index):
        if self.player.PlayingState:
            self.player.stop()
        curRec = self.qryModel.record(index.row())
        MD5 = curRec.value("MD5")
        SUMMARY = curRec.value("SUMMARY")
        self.ui.txEditSummary.setText(SUMMARY)
        data = self.getVideoStream(MD5)
        NAME = os.getcwd()+'\\db2temps\\'+MD5
        if os.path.exists(NAME):
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(NAME)))
            self.player.play()
            self.player.pause()
        else:

            with open(NAME, 'wb') as file:
                file.write(data)
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(NAME)))
            self.player.play()
            self.player.pause()

    def on_btnPlay_clicked(self):
        self.player.play()

    def on_btnPause_clicked(self):
        self.player.pause()

    def on_btnStop_clicked(self):
        self.player.stop()
    #槽函数,播放状态改变，调整按钮
    def do_stateChanged(self,state):
        isPlaying = (state == QMediaPlayer.PlayingState)
        self.ui.pbtnPlay.setEnabled(not isPlaying)
        self.ui.pbtnPause.setEnabled(isPlaying)
        self.ui.pbtnStop.setEnabled(isPlaying)

    #槽，响应实时播放进度
    def do_positionChanged(self,position):
        if (self.ui.sliderPosition.isSliderDown()):
            return
        self.ui.sliderPosition.setSliderPosition(position)
        secs = position/1000
        mins = secs/60
        secs = secs%60
        self._curPos = "%d:%d"%(mins,secs)
        self.ui.labRatio.setText(self._curPos + "/" +self._duration)

    #槽，响应获取总播放时长
    def do_durationChanged(self,duration):
        self.ui.sliderPosition.setMaximum(duration)
        secs = duration / 1000
        mins = secs / 60
        secs = secs % 60
        self._duration = "%d:%d" % (mins, secs)
        self.ui.labRatio.setText(self._curPos + "/" + self._duration)

    #槽，音量调节
    def on_sliderVolumn_valueChange(self,value):
        self.player.setVolume(value)

    #槽，进度调整
    def on_sliderPosition_valueChange(self,value):
        self.player.setPosition(value)

    #槽，静音按钮
    def on_pbtnSound_clicked(self):
        mute = self.player.isMuted()
        self.player.setMuted(not mute)
        if mute:
            self.ui.pbtnSound.setIcon(QIcon(":/img/img/出音.png"))
        else:
            self.ui.pbtnSound.setIcon(QIcon(":/img/img/静音.png"))

    #获取视频源文件，字节串
    def getVideoStream(self, MD5):
        sqQuery = "select ID,VIDEOBINNARY from VIDEOFILE where MD5=?"
        self.query.prepare(sqQuery)
        self.query.bindValue(0, MD5)
        self.query.exec()
        self.query.last()
        return self.query.value("VIDEOBINNARY")

