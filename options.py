from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# Ui
from ui.ui_Options import Ui_Dialog as Ui



class Options(QDialog, Ui):
  def __init__(self, parent):
    super().__init__(parent)
    self.setupUi(self)
    self.setWindowFlag(Qt.WindowType.MSWindowsFixedSizeDialogHint, True)
