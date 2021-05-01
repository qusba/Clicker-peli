# Käyttöohje
Lataa projektin viimeisin versio repositorion etusivulta.

## Alkutoimet
Mene terminaalissa repositorion päähakemistoon ja asenna riippuvuudet komennolla: 
_poetry install_

Tämän jälkeen ohjelman voi käynnistää komennolla:
_poetry run invoke start_

## Aloitusnäkymä
Peli alkaa aloitusnäkymästä, jossa on kaksi painiketta:
_Start a new game!_ sekä _Load game_

_Start a new game!_ painikkeesta voit aloittaa uuden pelin.
_Load game_ painike lataa viimeisimmän tallennetun pelin, jos sellaista ei ole, painike aloittaa uuden pelin.

## Pelinäkymä
Pelinäkymässä pelaaja saa pistetä painamalla näytön keskellä olevaa _click-painiketta_. Pelinäkymän oikeassa yläkulmassa on myös _menu-painike_, josta pelaaja voi avata menu-valikon.

## Menu
Menu-valikossa on kaksi painiketta: _SHOP_ ja _SAVE AND EXIT_. _Shop-painikkeella_ pelaaja saa kauppanäkymän esiin. _Save and
 exit -painikkeella_ pelaaja voi tallentaa ja poistua pelistä.
 ### Tallentaminen
 _SAVE AND EXIT_  painike kutsuu SaveGame-luokan save-metodia, joka luo save.dat tiedoston samaan kansioon, jossa save_game.py tiedosto itse sijaitsee, eli repositories kansioon. save.dat tiedostoon metodi tallentaa pelilogiikan tärkeiden muuttujien arvot.
 
 ## Shop
 Kauppanäkymässä on kolme painiketta: _2X, Autoclicker, sekä Autoclicker upgrade_. _2X-painike_ ostaa pelaajalle päivityksen, mikä tuplaa klikkauksen tuottaman pistemäärän. _Autoclicker-painike_ ostaa pelaajalle koneen, mikä klikkaa automaattisesti kerran sekunnissa. _Autoclicker upgrade -painike_ tuplaa autoklikkaajien tehon.
 
 ## Pelin sulkeminen
 Peli on mahdollista lopettaa tallentaen _SAVE AND EXIT -painikkeella_ tai tallentamatta sulkemalla pygamen tuottaman näytön.

