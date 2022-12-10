# --------------------------------------------------------------
#  leave_selected_false.py
#  Version: 1.0.1
#  Author: Alexander Marchenko
#
#  Last Modified by: Alexander Marchenko
#  Last Updated: December 10th, 2022
# -------------------------------------------------------------

import nuke

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

nuke_app = QApplication.instance()

class eventFilterWindowClass(QObject):
    def eventFilter(self, obj, ev):
        """Check evene leave mouse outside the windoW """
        
        if ev.type() == QEvent.Leave:
            for n in nuke.allNodes():
                n.knob('selected').setValue(False)
        return False

def get_main_window():
    """This function get UI

    Returns:
        Object: get access to the main window 
    """
    for widget in nuke_app.topLevelWidgets():
        if widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return widget

#Install eventFilterWindowClass
main_window = get_main_window()
ev = eventFilterWindowClass()
main_window.installEventFilter(ev)
