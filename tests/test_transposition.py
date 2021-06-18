from pathlib import Path

import pytest

from transposition import encrypt, decrypt
from transposition_hacker import hack


@pytest.mark.parametrize(
    'message, key, expected',
    (
        ('Common sense is not so common.', 8, 'Cenoonommstmme oo snnio. s s c'),
        ('Then they trotted away for the wind grew high: One acorn they left,'
         ' and no more might you spy.',
         9,
         'T atg:renishtwhr nfogperaeeO t hynoy wnt,mt. t w eh o ttfih earyheoni'
         'ayneoedrdgc d uy   hol m '),
    )
)
def test_encrypt(message, key, expected):
    assert encrypt(key, message) == expected


@pytest.mark.parametrize(
    'message, key, expected',
    (
        ('Cenoonommstmme oo snnio. s s c', 8, 'Common sense is not so common.'),
        ('T atg:renishtwhr nfogperaeeO t hynoy wnt,mt. t w eh o ttfih earyheoni'
         'ayneoedrdgc d uy   hol m ',
         9,
         'Then they trotted away for the wind grew high: One acorn they left,'
         ' and no more might you spy.'),
    )
)
def test_decrypt(message, key, expected):
    assert decrypt(key, message) == expected


@pytest.mark.parametrize('filename', ('frankenstein.txt',
                                      'the_time_machine.txt'))
@pytest.mark.parametrize('key', (10, 645, 3507))
def test_file_roundtrip(filename, key):
    original = Path(filename).read_text()
    round_trip = decrypt(key, encrypt(key, original))
    assert original == round_trip


CIPHER_TEXT = ("AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n"
               " uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no"
               " euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb"
               "  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v"
               "  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa"
               "  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d"
               " ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu"
               " thllnrshicwsg etriebruaisss  d iorr.")

PLAIN_TEXT = ("Augusta Ada King-Noel, Countess of Lovelace (10 December 1815"
              " - 27 November 1852) was an English mathematician and writer,"
              " chiefly known for her work on Charles Babbage's early"
              " mechanical general-purpose computer, the Analytical Engine."
              " Her notes on the engine include what is recognised as the first"
              " algorithm intended to be carried out by a machine. As a result,"
              " she is often regarded as the first computer programmer.")


def test_hack():
    plain_text, key = hack(CIPHER_TEXT)
    assert plain_text == PLAIN_TEXT
    assert key == 6
