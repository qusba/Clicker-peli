
![luokkakaavio](https://user-images.githubusercontent.com/81024277/115441616-ba651180-a219-11eb-93a6-34efbf23daea.png)

## Päätoiminnallisuudet 

### Scoren tuottaminen
![starting game state diagram](https://user-images.githubusercontent.com/81024277/116233987-afa00480-a764-11eb-8cd9-bfb6e08320ff.jpg)

Peli aloitetaan komennolla poetry run invoke start, joka kutsuu index.py:n main funktiota, joka alustaa kaikki GameLoop-luokan tarvitsemat luokkamuuttujat (logic,display.colors,startview,event_queue,menu, sekä shop). Tämän jälkeen main funktio luo GameLoop olion ja kutsuu sen metodia start(). GameLoop kutsuu start() metodin sisällä omaa metodiaan event_handler(). Event-handler -metodi tunnistaa ohjelman olevan alussa "begin" muuttujan boolean arvosta ja kutsuu StartView luokan metodia view(), mikä piirtää aloitusnäytön palauttamatta mitään. Kun käyttäjä painaa "Start a new game!" vaihtuu muuttujan "begin" arvo Falseksi ja aloitusnäkymä poistuu näkyvistä. Kun käyttäjä klikkaa näytön keskeltä kutsutaan GameLogic luokan metodia click(). Metodi tuottaa scorea ja kontrolli palaa looppiin.
