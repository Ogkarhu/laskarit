import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_saldo_kasvaa_oikein(self):
        self.maksukortti = Maksukortti(1000)
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 15)

    def test_saldo_vahenee_oikein(self):
        self.maksukortti = Maksukortti(1000)
        self.maksukortti.ota_rahaa(500)        
        self.assertEqual(self.maksukortti.saldo_euroina(), 5)

    def test_saldo_ei_mene_miinukselle(self):
        self.maksukortti = Maksukortti(1000)
        self.maksukortti.ota_rahaa(1200)        
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_kortti_palauttaa_true(self):
        self.maksukortti = Maksukortti(1000)
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)        

    def test_kortti_palauttaa_false(self):
        self.maksukortti = Maksukortti(1000)
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)  

    def test_tuloste_on_oikein(self):
        self.maksukortti = Maksukortti(1000)
        self.assertEqual(self.maksukortti.__str__(),"Kortilla on rahaa 10.00 euroa")  
