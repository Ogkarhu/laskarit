import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()


    def test_rahamaara_ja_lounaat_tasmaavat(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myydyt_lounaat_tasmaavat(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kateisosto_toimii(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(400), 160)

    def test_maukas_kateisosto_toimii(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450), 50)

    def test_edullinen_liian_vahan_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_maukas_liian_vahan_rahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_edulliset_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaat_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(600)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edulliset_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_korttiosto_toimii(self):
        kortti = Maksukortti(400)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti),True)
        self.assertEqual(kortti.saldo,160)

    def test_maukkaasti_korttiosto_toimii(self):
        kortti = Maksukortti(450)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti),True)
        self.assertEqual(kortti.saldo,50)

    def test_edulliset_kasvaa_kortilla(self):
        kortti = Maksukortti(400)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti),True)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaat_kasvaa_kortilla(self):
        kortti = Maksukortti(450)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti),True)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_ei_saldoa(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti),False)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_ei_saldoa(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti),False)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_saldon_lataaminen_onnistuu(self):
        kortti = Maksukortti(0)
        kortti.lataa_rahaa(500)
        self.assertEqual(kortti.saldo,500)

    #def test_saldon_lataaminen_ei_negatiivisilla(self):
    #    kortti = Maksukortti(0)
    #    kortti.lataa_rahaa(-500)
    #    self.assertEqual(kortti.saldo,0)

    def test_kassassa_euroja(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000)

    def test_lataa_rahaa_kortille(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti,100)
        self.assertEqual(kortti.saldo_euroina(),1)

    def test_lataa_rahaa_kortille_fail(self):
        kortti = Maksukortti(0)
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(kortti,-100),None)
        self.assertEqual(kortti.saldo_euroina(),0)
