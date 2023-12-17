import sys,os
from PyQt5.QtWidgets import QApplication,QMainWindow,QTabWidget,QWidget
from PyQt5.Qt import QIcon
from PyQt5.QtMultimedia import QMediaPlayer
from UI.UI_MainWindow import Ui_MainWindow

#主窗口
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        if not os.path.exists('./db2temps'):
            os.mkdir('./db2temps')

        #设置工具栏按钮动作
        #退出程序
        self.ui.action_quit.triggered.connect(self.close)
        #关闭当前页面
        self.ui.action_close.triggered.connect(self.on_closeCurrentTab)
        #最小化界面
        self.ui.action_mini.triggered.connect(self.on_miniWidget)
        #打开对应的数据库
        self.ui.action_home.triggered.connect(self.on_openHome)
        self.ui.action_picture.triggered.connect(self.on_openPicture)
        self.ui.action_video.triggered.connect(self.on_openVideo)
        self.ui.action_history.triggered.connect(self.on_openHistory)
        self.ui.action_man.triggered.connect(self.on_openMan)

        #打开简介主页面
        # self.ui.action_home.triggered.connect(self.on_openHome)

        # 设置标签主显示页
        self.cenTab = QTabWidget()
        self.cenTab.setTabsClosable(True)
        self.cenTab.tabCloseRequested.connect(self.on_cenTab_close)
        self.cenTab.currentChanged.connect(self.on_cenTab_currentChange)
        self.setCentralWidget(self.cenTab)

        #简介主页面
        from IndexWidget import IndexWidget
        self.home = IndexWidget()


        from CakePictureWidget import CakePhotoWidget
        self.picture = CakePhotoWidget(self)

        from CakeVideoWidget import CakeVideoWidget
        self.video = CakeVideoWidget(self)

        from HistoryWidget import HistoryIndexWidget
        self.history = HistoryIndexWidget(self)

        from ManWidget import ManWidget
        self.man = ManWidget()

        self.ui.action_home.triggered.emit()

    #槽函数，关闭当前标签页
    def on_cenTab_close(self,index):
        if self.cenTab.currentWidget() == self.video:
            if self.video.player.state() == QMediaPlayer.PlayingState:
                self.video.player.stop()
        self.cenTab.removeTab(index)


    # 槽函数，关闭所有标签页
    def on_closeCurrentTab(self):
        while self.cenTab.count() > 0:
            self.cenTab.removeTab(self.cenTab.currentIndex())
        if self.video.player.state() == QMediaPlayer.PlayingState:
            self.video.player.pause()

    #槽函数，切换标签页面，处理视频播放停播
    def on_cenTab_currentChange(self):
        if self.video.player.state() == QMediaPlayer.PlayingState:
            self.video.player.pause()

    #槽函数，最小化窗口
    def on_miniWidget(self):
        if self.isFullScreen():
            self.showMinimized()
        else:
            self.showFullScreen()

    #槽，打开简介主页面
    def on_openHome(self):
        self.cenTab.insertTab(0,self.home,QIcon(":/img/img/主页.png"),"数据库简介")
        self.cenTab.setCurrentWidget(self.home)
    #槽，打开对应的数据库页
    def on_openPicture(self):
        pass
        self.cenTab.insertTab(0,self.picture,QIcon(":/img/img/图片.png"),"图片库",)
        self.cenTab.setCurrentWidget(self.picture)

    def on_openVideo(self):
        pass
        self.cenTab.insertTab(0, self.video, QIcon(":/img/img/视频.png"), "视频库", )
        self.cenTab.setCurrentWidget(self.video)

    def on_openHistory(self):
        self.cenTab.insertTab(0, self.history, QIcon(":/img/img/文档.png"), "文档库", )
        self.cenTab.setCurrentWidget(self.history)

    def on_openMan(self):
        self.cenTab.insertTab(0, self.man, QIcon(":/img/img/人物.png"), "非遗传承人", )
        self.cenTab.setCurrentWidget(self.man)




if __name__ == "__main__":
    mainApp = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showFullScreen()
    sys.exit(mainApp.exec_())