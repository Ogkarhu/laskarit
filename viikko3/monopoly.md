```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "4" Sattuma
    Ruutu "1" -- "4" Rautatie
    Ruutu "1" -- "1" Lähtöruutu
    Ruutu "1" -- "28" Kiinteistöt
    Ruutu "1" -- "1" Vankila
    Ruutu "1" -- "1" Mene_vankilaan
    Vankila "1" -- "1" Mene_vankilaan
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Pelaaja "1" -- "n" Rahat
    Pelaaja "1" -- "0-28" Kiinteistöt
```
