# devop-security-scan
Permettre de faire un scanner de son infrastructure et détecter les failles de sécurités.

Tcp_scan : TCP connect scan (-sT) https://nmap.org/book/scan-methods-connect-scan.html

os_detection: https://nmap.org/book/man-os-detection.html

syn_scan: https://nmap.org/man/fr/man-port-scanning-techniques.html

version_detection: https://nmap.org/man/fr/man-version-detection.html

## nmap3scanner

A fin de asurer la sécurité du système et observer leurs vulnérabilités.

On utilise cet algorithme « nmap3scanner » pour faire un scanner et observer les ports ouvert dans une target d'adresse IP et pouvoir identifier par exemple: les protocoles, version, systèmes d’exploitation d’un ordinateur distant.

## Installation d’un environnement virtuel

``` sudo apt install python3 python3-venv ```

``` sudo apt install virtual env python3-virtualenv ```

## Création de l’environnement virtuel

``` python3 -m venv devop-security-scan ```

## Activation de l’environnement virtuel

``` source devop-security-scan/bin/activate ```

## Installation du microframework Flask

``` pip install flask ```

## Installation des paquets

C'est necessaire d'avoir installé: python3-nmap

``` pip install python3-nmap ```

nmap3scanner.py fonctionne en root.

``` pip install flask ```

``` sudo apt install sqlite3 ```

``` pip install flask_sqlalchemy ```






