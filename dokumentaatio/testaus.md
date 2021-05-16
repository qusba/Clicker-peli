# Testausdokumentti

Ohjelmalle on luotu automaattisia testejä, jotka toimivat yksikkö ja integraatiotasolla. Testit on luotu käyttäen unittestiä.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka
Sovelluslogiikkaa testataan _TestGameLogic_-luokalla. Luokka käyttää vain _GameLogic_-luokkaa ja testaa kaikkia logiikalle olennaisia toimintoja.

### Tallennus
Tietojen tallennusta testaa _TestSaveGame_-luokka. Luokka käyttää _SaveGame_-luokan toimintoja ja tallentaa _GameLogic_-luokan arvoja. Luokka testaa tallennusta, että lataamista.

### Pelin pääsilmukka
Peliä pyörittävää silmukkaa on myös testattu, tämä on toteutettu _TestGameLoop_-luokalla. Käytännössä testit testaavat käyttöliittymän toimivuutta, eli ne olisi voinut jättää kokonaan pois testauksesta. Testiluokka luo _GameLoop_-luokkaolion, mikä käyttää kaikkia muita luokkia hyväkseen.

### Testikattavuus
Testauksen haarautumakattavuus on 64%.
![testcoverage](https://user-images.githubusercontent.com/81024277/118395490-5d5f4e80-b653-11eb-91c6-b7f43d6fce43.png)

Kattavuutta laskee _GameLoop_-luokan testaus. Kohtasin ylitsepääsemättömän segmentaatio-ongelman, jonka vuoksi en voinnut tehdä enempää testejä luokalle.

### Asennus
Asennusta on testattu manuaalisesti käyttöohjeen ohjeistamalla tavalla.

### Toiminnallisuudet
Vaativuusmäärittelyn kaikki toiminnallisuudet on testattu manuaalisesti, sekä osittain automaatiotesteillä. 
