import sys
from PyQt5 import QtWidgets

app=QtWidgets.QApplication(sys.argv)
widget=QtWidgets.QWidget()
widget.resize(500,500)
widget.setWindowTitle("显示一个窗口")
widget.show()
sys.exit(app.exec_())