# Arkkitehtuurikuvaus

## Luokka/pakkauskaavio
![luokka_pakkauskaavio](https://user-images.githubusercontent.com/81024277/116245463-a79a9180-a771-11eb-859d-23e7feae6cf1.jpg)

Peliä ylläpitää _GameLoop_-luokka, joka on rippuvainen kaikista muista luokista. Kaikki ui-luokat ovat riippuvasia _Colors_-luokasta. _GameLogic_-luokka on eriytetty, eikä se ole riippuvainen mistään muusta luokasta.

## Käyttöliittymä
Pelissä on neljä erillaista näkymää: aloitusnäkymä, pelinkäkymä, valikko- sekä kauppanäkymät. Pelinäkymää pyörittää _GameLoop_-luokan _start()_-metodi, joka huolehtii pelin pyörittämisestä, kaikilla muilla näkymillä on oma luokkansa. Pelin kaikki toiminnot toteutuvat käyttäjän hiirenpainalluksilla.

## Sovelluslogiikka
Pelin pisteytyksen sovelluslogiikasta vastaa täysin _GameLogic_-luokka. Metodia _click()_ kutsutaan aina kun käyttäjä painaa hiirellä näytöllä näkyvästä ympyrästä, tämä tuottaa pisteitä. Metodia _click_upgrade()_ kutsutaan kun käyttäjä ostaa kaupasta päivityksen "2X". Metodi _autoclicker()_ tuottaa käyttäjälle automaattisia klikkauksia, sitä kutsutaan kun vastaavan niminen päivitys ostetaan kaupasta. _autoclicker_click()_-metodi huolehtii siitä että autoclikkerit kutsuvat metodia _click()_ oikean verran; metodia kutsutaan pelin loopissa kerran sekunnissa. Luokan viimeinen metodi _autoclicker_upgrade()_ vaikuttaa autoclikkereiden klikkausnopeuteen per sekunti, sitä kutsutaan aina kun käyttäjä ostaa saman nimisen päivityksen kaupasta.

## Pelin tallentaminen
Pelitilanteen tallentamisesta huolehtii _SaveGame_-luokka, joka sijaitsee repositories kansiossa. Luokassa on kaksi metodia: _save_game_ ja _load_game_. _save_game_-metodia kutsutaan aina kun käyttäjä painaa valikko-/menu-näkymässä kohtaa "SAVE AND EXIT". Metodi tallentaa listaan kaikki _GameLogic_-luokan muuttujien arvot ja sen jälkeen käyttää pythonin kirjastoa _pickle_ luodakseen save.dat -nimisen tiedoston johon lista tallennetaan bitstreamina. Luokan _load_game_-metodia kutsutaan, jos aloitusnäkymässä käyttäjä painaa "Load game!" -painiketta. Myös tämä metodi käyttää _pickle_-kirjastoa lukeakseen save-dat -tiedoston ja uudelleenalustaa _GameLogic_-luokan muuttujat tietojen mukaisesti.


## Päätoiminnallisuudet 

### Scoren tuottaminen
![starting game state diagram](https://user-images.githubusercontent.com/81024277/116233987-afa00480-a764-11eb-8cd9-bfb6e08320ff.jpg)

Peli aloitetaan komennolla poetry run invoke start, joka kutsuu index.py:n _main_ funktiota, joka alustaa kaikki GameLoop-luokan tarvitsemat luokkamuuttujat (logic,display.colors,startview,event_queue,menu,shop sekä save). Tämän jälkeen main funktio luo GameLoop olion ja kutsuu sen metodia _start()_. GameLoop kutsuu _start()_-metodin sisällä omaa metodiaan _event_handler()_. Event-handler -metodi tunnistaa ohjelman olevan alussa "begin" muuttujan boolean arvosta ja kutsuu StartView luokan metodia _view()_, mikä piirtää aloitusnäytön palauttamatta mitään. Kun käyttäjä painaa "Start a new game!" vaihtuu muuttujan "begin" arvo Falseksi ja aloitusnäkymä poistuu näkyvistä. Kun käyttäjä klikkaa näytön keskeltä kutsutaan GameLogic luokan metodia _click()_. Metodi tuottaa scorea ja kontrolli palaa looppiin.
