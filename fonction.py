

from .constante import *
from .mapping_version import *
import webbrowser

def afficheDoc():
    webbrowser.open("https://ignf.github.io/assistant-dfci-qgis-plugin/")

def afficheerreur(text, titre=TITRE):
    msg = QMessageBox()
    msg.setIcon(Warning)
    msg.setWindowTitle(titre)
    msg.setStandardButtons(Ok)
    msg.setText(text)
    msg.setWindowFlags(WindowStaysOnTopHint)
    msg.setFixedSize(msg.size())
    msg.exec()


def affichemessageAvertissement(text, titre):
    msg = QMessageBox()
    msg.setIcon(Warning)
    msg.setWindowTitle(titre)
    msg.setText(text)
    btnAnnuler = msg.addButton("Annuler", YesRole)
    btnAnnuler.setStyleSheet("color:red ; font-weight: bold")
    btnValider = msg.addButton("valider les modifications", AcceptRole)
    btnValider.setStyleSheet("color:green ; font-weight: bold")
    msg.setWindowFlags(WindowStaysOnTopHint)
    msg.exec()

    if msg.clickedButton() == btnAnnuler:
        return False
    if msg.clickedButton() == btnValider:
        return True

