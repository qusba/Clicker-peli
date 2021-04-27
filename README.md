# ot-harjoitustyö
Ohjelman perusidea on clicker-tyypin peli, jossa pisteitä kerätään hiiren painalluksilla. Pisteillä voi ostaa kaupasta päivityksiä,
jotka nopeuttavat pisteiden keräämistä.


## Dokumentaatio
[tuntikirjanpito](https://github.com/qusba/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[vaativuusmaarittely](https://github.com/qusba/ot-harjoitustyo/blob/master/dokumentaatio/vaativuusmaarittely.md)

[arkkitehtuuri](https://github.com/qusba/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus
1. Mene terminaalissa repositorion päähakemistoon ja asenna riippuvuudet komennolla poetry install
2. Ohjelman voi suorittaa komennolla poetry run invoke start

## Komentorivitoiminnot

### Ohjelman suorittamiseen: 
poetry run invoke start

### Testien suorittamiseen: 
poetry run invoke test

### Testikattavuuden gemerointi:
poetry run invoke coverage-report

### Pylint tarkistus:
poetry run invoke lint


