# Arkkitehtuurikuvaus

## Luokka/pakkauskaavio
![luokka_pakkauskaavio](https://user-images.githubusercontent.com/81024277/116245463-a79a9180-a771-11eb-859d-23e7feae6cf1.jpg)

Peliä ylläpitää GameLoop-luokka, joka on rippuvainen kaikista muista luokista. Kaikki ui-luokat ovat riippuvasia Colors-luokasta. GameLogic-luokka on eriytetty, eikä se ole riippuvainen mistään muusta luokasta.


## Päätoiminnallisuudet 

### Scoren tuottaminen
![starting game state diagram](https://user-images.githubusercontent.com/81024277/116233987-afa00480-a764-11eb-8cd9-bfb6e08320ff.jpg)

Peli aloitetaan komennolla poetry run invoke start, joka kutsuu index.py:n main funktiota, joka alustaa kaikki GameLoop-luokan tarvitsemat luokkamuuttujat (logic,display.colors,startview,event_queue,menu, sekä shop). Tämän jälkeen main funktio luo GameLoop olion ja kutsuu sen metodia start(). GameLoop kutsuu start() metodin sisällä omaa metodiaan event_handler(). Event-handler -metodi tunnistaa ohjelman olevan alussa "begin" muuttujan boolean arvosta ja kutsuu StartView luokan metodia view(), mikä piirtää aloitusnäytön palauttamatta mitään. Kun käyttäjä painaa "Start a new game!" vaihtuu muuttujan "begin" arvo Falseksi ja aloitusnäkymä poistuu näkyvistä. Kun käyttäjä klikkaa näytön keskeltä kutsutaan GameLogic luokan metodia click(). Metodi tuottaa scorea ja kontrolli palaa looppiin.
