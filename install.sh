#!/bin/bash
cd ~
rm -rf LOGGER-G.O.D
mkdir LOGGER-G.O.D && cd LOGGER-G.O.D
pkg install python wget -y
# Ici on imagine que tu as mis les fichiers sur ton nouveau GitHub
wget https://raw.githubusercontent.com/TON_NOUVEAU_PSEUDO/LOGGER-G.O.D/main/server.py
wget https://raw.githubusercontent.com/TON_NOUVEAU_PSEUDO/LOGGER-G.O.D/main/index.html
python server.py
