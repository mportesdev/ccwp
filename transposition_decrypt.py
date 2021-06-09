# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import math


def main():
    my_message = 'Cenoonommstmme oo snnio. s s c'
    my_key = 8

    plaintext = decrypt_message(my_key, my_message)

    print(f'{plaintext!r}')


def decrypt_message(key, message):
    num_of_columns = math.ceil(len(message) / key)
    num_of_rows = key
    shaded_boxes = num_of_columns * num_of_rows - len(message)

    plaintext = [''] * num_of_columns

    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        if column == num_of_columns or (column == num_of_columns - 1 and
                                        row >= num_of_rows - shaded_boxes):
            column = 0
            row += 1

    return ''.join(plaintext)


if __name__ == '__main__':
    main()

    print(repr(decrypt_message(9, 'Uhot  on ahoamdakef pe  r harhtesunnur'
                                  ' wgyegewie,aeean t  sec')))
    print(repr(decrypt_message(9, 'Tteeshiefheydtaplaad  :telst ct    t arh'
                                  'Fwaf.gsueoanur n rsdlutcm   lnhhatrf ')))
    print(repr(decrypt_message(9, 'T atg:renishtwhr nfogperaeeO t hynoy wnt,'
                                  'mt. t w eh o ttfih earyheoniayneoedrdgc d'
                                  ' uy   hol m ')))

    print(repr(decrypt_message(9, 'H cb  irhdeuousBdi   prrtyevdgp nir  '
                                  'eerit eatoreechadihf paken ge b te dih aoa.'
                                  'da tts tn')))
    print(repr(decrypt_message(9, 'A b  drottthawa nwar eci t nlel ktShw leec,'
                                  'hheat .na  e soogmah a  ateniAcgakh'
                                  ' dmnor  ')))
    print(repr(decrypt_message(9, "Bmmsrl dpnaua!toeboo'ktn uknrwos. yaregonr w"
                                  " nd,tu  oiady hgtRwt   A hhanhhasthtev  e"
                                  " t e  eo")))
