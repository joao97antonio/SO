import multiprocessing as mp
import time
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
import psutil as cp
import cpuinfo as ci

def pi_calc_MC (q, min, max):
    pi = 0
    for i in range(min, max):
        numerador =  (-1)**i
        denominador = 2*i + 1
        pi += numerador/denominador
    q.put(pi*4)


def pi_calc(num_interacoes):
    pi = 0
    t1 = time.time()
    for i in range(num_interacoes):
        numerador =  (-1)**i
        denominador = 2*i + 1
        pi += numerador/denominador
    t2 = time.time()
    pi = pi*4
    return (t2 - t1)

def multicore(num_interacoes,nthreads):
    resul = 0
    tmp1 = time.time()
    tp = mp.Queue()
    for i in range(nthreads):
        min = int (i*num_interacoes / nthreads)
        max = int ( (i+1)*num_interacoes / nthreads)
        procs = mp.Process(target=pi_calc_MC, args=(tp, min, max))
        procs.start()

    
    for i in range(nthreads):
        resul += tp.get()
    tmp2 = time.time()
    return (tmp2 - tmp1)
class Ui_MainWindow(object):
    ts = []
    tm = []
    ctrl = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 398)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 601, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.it_num = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.it_num.setObjectName("it_num")
        self.gridLayout_2.addWidget(self.it_num, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.rep_num = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.rep_num.setObjectName("rep_num")
        self.gridLayout_2.addWidget(self.rep_num, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 2, 1, 1)
        self.threadnum = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.threadnum.setObjectName("threadnum")
        self.gridLayout_2.addWidget(self.threadnum, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.sc_media = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.sc_media.setObjectName("sc_media")
        self.gridLayout.addWidget(self.sc_media, 0, 1, 1, 1)
        self.mc_media = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.mc_media.setObjectName("mc_media")
        self.gridLayout.addWidget(self.mc_media, 1, 1, 1, 1)
        self.effc = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.effc.setObjectName("effc")
        self.gridLayout.addWidget(self.effc, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 210, 461, 111))
        self.frame.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(222, 221, 218);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 441, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.process = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.process.setObjectName("process")
        self.horizontalLayout_2.addWidget(self.process)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.nnucleos = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.nnucleos.setObjectName("nnucleos")
        self.horizontalLayout_3.addWidget(self.nnucleos)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.ram_size = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.ram_size.setObjectName("ram_size")
        self.horizontalLayout_3.addWidget(self.ram_size)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(480, 210, 131, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.iniciar_bt = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.iniciar_bt.setObjectName("iniciar_bt")
        self.gridLayout_3.addWidget(self.iniciar_bt, 0, 0, 1, 1)
        self.iniciar_bt_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.iniciar_bt_2.setObjectName("iniciar_bt_2")
        self.gridLayout_3.addWidget(self.iniciar_bt_2, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(17, 330, 591, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Numero de Iteraçoes"))
        self.label_2.setText(_translate("MainWindow", " Numero de Threads"))
        self.label_8.setText(_translate("MainWindow", "Numero de Repeticoes"))
        self.label_4.setText(_translate("MainWindow", "Média Multi-Core"))
        self.label.setText(_translate("MainWindow", "Média Single-Core"))
        self.label_5.setText(_translate("MainWindow", "Eficiencia"))
        self.label_10.setText(_translate("MainWindow", "Processador:"))
        self.label_3.setText(_translate("MainWindow", " Numero de Nucleos: "))
        self.label_11.setText(_translate("MainWindow", "Ram"))
        self.iniciar_bt.setText(_translate("MainWindow", "Iniciar"))
        self.iniciar_bt_2.setText(_translate("MainWindow", "Gerar Gráficos"))
    def pc_info(self):
        cpu = ci.get_cpu_info()
        ram = cp.virtual_memory()
        txt = "{:.2f} GB".format(ram.total/1024/1024/1024)
        self.process.setText(cpu['brand'])
        self.nnucleos.setText(str(cpu['count']))
        self.ram_size.setText(txt)
    def set_fields(self):
        
        media_mc = 0
        media_sc = 0

        for i in range(int(self.rep_num.text())):
            self.ts.append(pi_calc(int(self.it_num.text())))
            self.tm.append(multicore(int(self.it_num.text()),int(self.threadnum.text())))
            self.progressBar.setValue(int((i+1)/int(self.rep_num.text())*100))
            if self.progressBar.value() == 100:
                self.iniciar_bt_2.setEnabled(True)
            else:
                self.iniciar_bt_2.setEnabled(False)
        media_mc = sum(self.tm)/int(self.rep_num.text())
        media_sc = sum(self.ts)/int(self.rep_num.text())
        frmt_mc = "{:.2f} s".format(media_mc)
        frmt_sc = "{:.2f} s".format(media_sc)
        self.sc_media.setText(frmt_sc)
        self.mc_media.setText(frmt_mc)
        self.effc.setText("{:.2f} %".format(media_mc/media_sc*100) )
    def set_enables(self):
        self.mc_media.setEnabled(False)
        self.sc_media.setEnabled(False)
        self.effc.setEnabled(False)
        self.mc_media.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
        self.sc_media.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
        self.effc.setStyleSheet("   color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
        self.iniciar_bt_2.setEnabled(False)
    def gerar_graficos(self):
        x = range(1, int(self.rep_num.text())+1)
        plt.plot(x, self.ts, label = "Single-Core")
        plt.plot(x,self.tm, label = "Multi-Core")
        plt.legend()
        plt.xlabel("Repetições")
        plt.ylabel("Tempo (s)")
        plt.show(),
        self.ts.clear()
        self.tm.clear()

    def acionar(self):
        self.ts.clear()
        self.tm.clear()
        self.progressBar.setValue(0)
        self.iniciar_bt.clicked.connect(self.set_fields)
        self.iniciar_bt_2.clicked.connect(self.gerar_graficos)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.set_enables()
    ui.acionar()
    ui.pc_info()
    MainWindow.show()
    sys.exit(app.exec_())
