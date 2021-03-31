import unittest
from maksukortti import Maksukortti

class TestMaksumaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_maksukortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_laittaminen_toimii(self):
        self.maksukortti.lataa_rahaa(990)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahan_ottaminen_kun_on_tarpeeksi(self):
        self.maksukortti.lataa_rahaa(990)
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")
    
    def test_rahan_ottaminen_kun_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(300)
        self.assertEqual(str(self.maksukortti),"saldo: 0.1")
    
    def test_ottaminen_palauttaa_True_kun_on_tarpeeksi(self):
        self.maksukortti.lataa_rahaa(990)
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
    
    def test_ottaminen_palauttaa_False_kun_ei_ole_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), False)
