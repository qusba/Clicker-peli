import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti
class Testkassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    def test_lahtotilanne_oikein_raha(self):
        self.assertEqual(self.kassa.kassassa_rahaa,100000)
   
    def test_lahtotilanne_oikein_edulliset(self):
        self.assertEqual(self.kassa.edulliset,0)
   
    def test_lahtotilanne_oikein_maukkaat(self):
        self.assertEqual(self.kassa.maukkaat,0)

    def test_kateistosto_kun_on_riittavasti_rahaa(self):
        tulos = self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.kassassa_rahaa,100240)
        self.assertEqual(tulos,0)
        self.assertEqual(self.kassa.edulliset,1)
        tulos2 = self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.kassassa_rahaa,100640)
        self.assertEqual(tulos2,0)
        self.assertEqual(self.kassa.maukkaat,1)

    def test_kateisnosto_kun_ei_riittavasti_rahaa(self):
        tulos1 = self.kassa.syo_edullisesti_kateisella(200)
        tulos2 = self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(tulos1,200)
        self.assertEqual(tulos2,300)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)
        self.assertEqual(self.kassa.edulliset,0)
        self.assertEqual(self.kassa.maukkaat,0)
    
    def test_edullisen_osto_kun_kortilla_tarpeeksi_rahaa(self):
        tulos = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset,1)
        self.assertEqual(self.kortti.saldo,760)
        self.assertEqual(tulos,True)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)
    
    def test_edullisen_osto_kun_kortilla_ei_tarpeeksi_rahaa(self):
        self.kortti = Maksukortti(200)
        tulos = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset,0)
        self.assertEqual(self.kortti.saldo,200)
        self.assertEqual(tulos,False)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)
    
    def test_maukkaan_osto_kun_kortilla_tarpeeksi_rahaa(self):
        tulos = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat,1)
        self.assertEqual(self.kortti.saldo,600)
        self.assertEqual(tulos,True)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)
    
    def test_maukkaan_osto_kun_kortilla_ei_tarpeeksi_rahaa(self):
        self.kortti = Maksukortti(200)
        tulos = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat,0)
        self.assertEqual(self.kortti.saldo,200)
        self.assertEqual(tulos,False)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)

    def test_kortille_ladataan_rahaa_oikein(self):
        self.kassa.lataa_rahaa_kortille(self.kortti,300)
        self.assertEqual(self.kassa.kassassa_rahaa,100300)
        self.assertEqual(self.kortti.saldo,1300)
    def test_lataa_rahaa_kortille_vaarin(self):
        tulos = self.kassa.lataa_rahaa_kortille(self.kortti,-200)
        self.assertEqual(tulos, None)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)
    

    




