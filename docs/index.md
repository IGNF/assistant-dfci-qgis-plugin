# Plugin QGis Assistant DFCI

## Version 1.1.0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; IGN - DTSO 

| Version      | Date       | Auteur       |
|--------------|------------|--------------|
| **1.1.0**    | 23/01/2026 | IGN - DTSO   |

<div  style="text-align: left;"> 
	<img  src="Image0.jpg"  height = 110/> 
</div>

<hr style="border-color:  #98BF18; "/>

| Version | Date  | Modifié par | Commentaire |
|--|--|--|--|
| 0.1 | 10/01/2025 | Gérôme PECHEUR | Création du manuel utilisateur  |
| 1.0.0 | 08/07/2025 | Gérôme PECHEUR | Adaptation à la version 1.0.0 du plugin |
| 1.1.0 | 23/01/2026 | Philippe GALLEN | Adaptation à la version 1.1.0 du plugin |  


<hr style="border-color:  #98BF18; "/>

<div  style="background-color: white; border: 1px solid black; padding: 10px; text-align: justify;">
  <h2 style="color: #00ADC5">Sommaire</h2>
</div>

- [1. Prérequis](#1-prérequis)
- [2. Résumé](#2-résumé)
- [3. Installation](#3-installation)
- [4. Présentation](#4-présentation)
- [5. Mode de sélection](#5-mode-de-sélection)
  - [5.1 Sélection unique](#51-sélection-unique)
  - [5.2 Sélection multiple](#52-sélection-multiple)
- [6. Modification](#6-modification)
- [7. Extra](#7-extra)
  - [7.1 A propos de](#71-a-propos-de)  


  
<div  style="background-color: white; border: 1px solid black; padding: 10px; text-align: justify;">
  <h2 id="1-prérequis" style="color: #00ADC5" >1. Prérequis</h2>
</div>

Version de QGIS 3 : 3.28 ou supérieure.  
Ce plugin fonctionne en parallèle du plugin « IGN Espace collaboratif » version 4.2.2  
Ce plugin fonctionne uniquement avec des couches de la BDTopo, le nom de la couche route doit obligatoirement se nommer : « troncon_de_route » dans QGIS.  

Si le package « openpyxl » n’est pas installé sur le poste le message d’erreur ci-dessous apparaît lors d’une transaction.  

<div  style="text-align: center;"> 
	<img  src="Image1.png" /> 
</div>

Remède : installation du package.  
Ouvrir l’invite de commande, se placer dans le répertoire « bin » de l’installation de QGIS :  
Exemple :  
<div  style="text-align: center;"> 
	<img  src="Image2.png" /> 
</div>

Puis taper la commande : python-qgis-ltr.bat -m pip install openpyxl  
<div  style="text-align: center;"> 
	<img  src="Image3.png" /> 
</div>

Le package s’installe, vous n’avez plus qu’à relancer QGIS.  

<div  style="background-color: white; border: 1px solid black; padding: 10px; text-align: justify;">
  <h2 id="2-résumé" style="color: #00ADC5">2. Résumé</h2>
</div>
  
Ce plugin est une aide à la modification des attributs sémantiques des « complexes DFCI ».  
  
  
  
<div  style="background-color: white; border: 1px solid black; padding: 10px; text-align: justify;">
  <h2 id="3-installation" style="color: #00ADC5">3. Installation</h2>
</div>
  
Ouvrir QGIS.  
Allez dans Extensions/Installer/Gérer les extensions, cliquez sur Installer depuis un ZIP, sélectionner le fichier ZIP puis cliquez sur Installer le plugin.  

<div  style="text-align: center;"> 
	<img  src="Image4.png" /> 
</div>
  
<div  style="background-color: white; border: 1px solid black; padding: 10px; text-align: justify;">
  <h2 id="4-présentation" style="color: #00ADC5">4. Présentation</h2>
</div>
  
<div  style="text-align: center;"> 
	<img  src="Image5.png" /> 
</div>

Cette interface permet de modifier les attributs des champs DFCI des tronçons de routes  

Le bouton « ? » permet d’afficher le suivi des versions et permet également d’ouvrir la documentation du plugin  
Le bouton « log » permet d’afficher le rapport des modifications  
Le bouton ![Image6](Image6.png) permet d’annuler la dernière modification effective et uniquement la dernière.  
Le bouton ![Image7](Image7.png) permet de modifier la couleur des tronçons sélectionnés dans QGIS. Ça peut être utile suivant la symbologie appliquée pour les tronçons dans QGIS.  
Le bouton ![Image8](Image8.png) permet la sélection de toutes les entités comprises entre deux tronçons.  

Le bouton « Valider les modifications » valide les modifications dans QGIS, le plugin « espace collaboratif » se charge d’impacter les bases BDTopo de l’IGN.  

<div  style="text-align: left;"> 
	<img  src="Image9.jpg" /> 
</div>
A l’ouverture de l’outil il y a une vérification de la présence dans le projet des couches nécessaires. Afficher l’état du modèle permet de **vérifier les permissions sur chaque attribut.** Ces permissions sont définies dans le projet en fonction des guichets en saisie directe dans la BDTOPO.  
  
<div  style="background-color: white; border: 1px solid black; padding: 10px; text-align: justify;">
  <h2 id="5-mode-de-sélection" style="color: #00ADC5">5. Mode de sélection</h2>
</div>

### <span style="color: white; background-color: #00ADC5; padding: 2px 5px;">5.1 Sélection unique</span>
Les attributs affichés sont ceux du tronçon sélectionné.  
En vert lorsqu’ils sont différents de « NULL » ou de vide.  


### <span style="color: white; background-color: #00ADC5; padding: 2px 5px;">5.2 Sélection multiple</span>
- Sélection multiple avec l’outil de saisie. Dans QGIS on peut sélectionner manuellement un ensemble de tronçons  

- Sélection multiple de tronçons contigües, on sélectionne 2 tronçons, <mark>ces 2 tronçons doivent être visible à l’écran et être connectés.</mark>  
Ensuite on clique sur le bouton ![Image8](Image8.png) , le résultat est une sélection de tous les tronçons entre le premier et le deuxième sélectionnés respectant l’algorithme du chemin le plus court.  
Un contrôle visuel est toutefois nécessaire afin de vérifier si les tronçons sont bien ceux désirés.  


Seuls les attributs communs à tous les tronçons sont représentés en vert.  


<div  style="background-color: white; border: 1px solid black; padding: 10px; text-align: justify;">
  <h2 id="6-modification" style="color: #00ADC5">5. Modification</h2>
</div>
Une fois les tronçons sélectionnés il suffit de choisir le ou les attributs à modifier parmi les valeurs possibles ou éditables.  

 ![Image11](Image11.png) &nbsp;

Les valeurs en rose sont celles qui seront modifiées pour tous les tronçons sélectionnés.  

Les modifications sur le(s) tronçon(s) sélectionné(s) sont à valider avec le bouton ![Image12](Image12.png) 
Un message QGIS confirme la prise en compte des modifications.  
![Image13](Image13.png)  

![Image15](Image15.jpg)  


<div  style="background-color: white; border: 1px solid black; padding: 10px; text-align: justify;">
  <h2 id="5-mode-de-sélection" style="color: #00ADC5">7. Extra</h2>
</div>

### <span style="color: white; background-color: #00ADC5; padding: 2px 5px;">7.1 A propos de</span>

Accessible via le bouton ![Image16](Image16.png)  

![Image17](Image17.png)  

Cette boite permet de suivre l’historique des différentes versions ainsi que d’afficher la documentation.  