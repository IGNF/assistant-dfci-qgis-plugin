from qgis.PyQt.QtWidgets import QMessageBox
from qgis.PyQt.QtCore import Qt

from .constante import *
import webbrowser

def afficheDoc():
    webbrowser.open("https://ignf.github.io/assistant-dfci-qgis-plugin/")

def afficheerreur(text, titre=TITRE):
    msg = QMessageBox()
    msg.setIcon(Warning)
    msg.setWindowTitle(titre)
    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg.setText(text)
    msg.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
    msg.setFixedSize(msg.size())
    msg.exec()


def affichemessageAvertissement(text, titre):
    msg = QMessageBox()
    msg.setIcon(Warning)
    msg.setWindowTitle(titre)
    msg.setText(text)
    btnAnnuler = msg.addButton("Annuler", QMessageBox.ButtonRole.YesRole)
    btnAnnuler.setStyleSheet("color:red ; font-weight: bold")
    btnValider = msg.addButton("valider les modifications", QMessageBox.ButtonRole.AcceptRole)
    btnValider.setStyleSheet("color:green ; font-weight: bold")
    msg.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
    msg.exec()

    if msg.clickedButton() == btnAnnuler:
        return False
    if msg.clickedButton() == btnValider:
        return True
    return None

