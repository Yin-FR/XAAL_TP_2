# Développement d'un Capteur de la qualité de l'Air et une Gateway sur Protocol de XAAL
## Introduction
Le fichier contient deux sections de TP, Qualité de l'air et ESPHome. Le projet est implémenté par le SDK Python du protocole XAAL.
## Installation et Lancement
1. Téléchargez d'abord le code source du projet :
```
git clone https://github.com/YinTAN-Stan/XAAL_TP.git
```
2. Installez l'environnement virtuel et la bibliothèque python de XAAL en suivant les instructions sur https://redmine.telecom-bretagne.eu/svn/xaal/code/Python/branches/0.7/README.html
3. Exécutez le Terminal (ou CMD) dans le répertoire racine du projet, activez l'environnement virtuel avec la bibliothèque XAAL installée, puis exécutez la commande pour lancer les code: 
dans le fichier `air_quality`
```
python dev.py
```
dans le fichier `esp` 
```
python sample.py
```
## Explication
1. **Qualité de l'air**: En utilisant les données de Airbreizh, nous avons développé un device qui retourne l'indice de qualité de l'air à Brest. Vous pouvez le verifier et voir les données de cette device dans la liste des devices.
2. **ESPHome**: Nous avons développé d'une Gateway xAAL. ESPHome est un firmware opensource utilisé pour piloter bon nombre d'équipements domotiques bon marché, comme les Sonoff-Dual. En utilisant le protocole natif utilisé par ESPHome, nous pouvons contrôler le Sonoff-Dual sur notre propre Gateway. Vous pouvez utiliser `xaal-isalive` pour verifier les états des devices, inclu 2 relays, 1 sensor. Après changer le numéro du port dans le fichier `xaal.ini`, vous pouvez exécuter la commande pour controller les relays directement dans le dashboard.
```
python -m xaal.dashboard
```



