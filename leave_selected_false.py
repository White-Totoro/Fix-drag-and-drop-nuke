# --------------------------------------------------------------
#  leave_selected_false.py
#  Version: 1.1.0
#  Author: Alexander Marchenko
#
#  Last Modified by: Alexander Marchenko
#  Last Updated: December 11th, 2022
# -------------------------------------------------------------

import nuke
import time

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

nuke_app = QApplication.instance()


class eventFilterWindowClass(QObject):
    def __init__(self):
        super().__init__()

        self.selected_nodes = []

    def eventFilter(self, obj, ev):
        """Check evene leave mouse outside the window

        Args:
            obj (Widget): Widget
            ev (QEvent): Event type

        Returns:
            False:
        """

        if ev.type() == QEvent.WindowDeactivate:
            selected_nodes = nuke.selectedNodes()
            if selected_nodes:
                self.selected_nodes = selected_nodes
                for n in self.selected_nodes:
                    n.knob('selected').setValue(False)
        if ev.type() == QEvent.WindowActivate:
            selected_nodes = nuke.selectedNodes()
            if not selected_nodes:
                for n in self.selected_nodes:
                    n.knob('selected').setValue(True)
                self.selected_nodes.clear()
        return False


def get_main_window():
    """This function get UI

    Returns:
        QtWidgets.QWidget: Nuke Main  
    """
    for widget in nuke_app.topLevelWidgets():
        if widget.metaObject().className() == 'Foundry::UI::LinkedView':
            return widget


# Install eventFilterWindowClass
main_window = get_main_window()
ev = eventFilterWindowClass()
main_window.installEventFilter(ev)
