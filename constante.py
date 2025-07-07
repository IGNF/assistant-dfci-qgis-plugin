
import os

TITRE = "Assisstant DFCI"
PATH_REP = f"{os.path.dirname(__file__)}"

LAYER_ESPACE_CO = ["troncon_de_route","route_numerotee_ou_nommee"]

LIEN_VERS_RTE_NOMMEE = "liens_vers_route_nommee"

TYPE_ROUTE = "type_de_route"
TYPE_ROUTE_DFCI = "Piste DFCI"
CLEABS = "cleabs"
GESTIONNAIRE ="gestionnaire"
NUMERO = "numero"
TOPONYME = "toponyme"


# 0 : bouton clické → fond vert
# 1 : valeur de l'objet → fond rose
# 2 : pas de fond
# 3 : bouton valider
# 4 : label
CUSTOM_WIDGETS = ("background-color: #2ab51a ;font-weight: bold",
                  "background-color: #ff8080 ;font-weight: bold",
                  "background-color: None",
                  "background-color: #df920d ;font-weight: bold",
                  "background-color: #dcdcdc"
                  )







