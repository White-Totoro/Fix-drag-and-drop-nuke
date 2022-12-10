# Fix-drag-and-drop-nuke
Correction of a strange “feature” in the nuke, that when you have a node selected and you throw something into the nuke with a drag drop, then you switch the connection to the new file or node.

The essence is simple, as soon as the cursor leaves the nuke window, the selection is removed from all nodes so that there is no reconnect.

How this install?
Put the .nuke file in the folder where you have access to Init.py and just write import leave_selected_false in the main menu.py
