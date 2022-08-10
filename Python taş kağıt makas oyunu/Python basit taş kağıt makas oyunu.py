import random

secenek = ['tas' , 'kagit' , 'makas']

bilgisayar_puani = 0
kullanici_puani = 0

while True:
    bilgisayar_secimi = random.choice(secenek)
    kullanici_secimi = input('Yapmak istedğiniz hamleyi yapınız(tas,kagit,makas):')
    print(f'Bilgisayar:{bilgisayar_secimi} Siz:{kullanici_secimi}')
   
    if bilgisayar_secimi == kullanici_secimi:
        print('Berabere')
        
    elif bilgisayar_secimi == 'tas' and kullanici_secimi == 'kagit':
        kullanici_puani += 1
        print(f'Bilgisayar:{bilgisayar_puani} VS Siz:{kullanici_puani}')

    elif bilgisayar_secimi == 'kagit' and kullanici_secimi == 'makas':
        kullanici_puani += 1
        print(f'Bilgisayar:{bilgisayar_puani} VS Siz:{kullanici_puani}')

    elif bilgisayar_secimi == 'makas' and kullanici_secimi == 'tas':
        kullanici_puani += 1
        print(f'Bilgisayar:{bilgisayar_puani} VS Siz:{kullanici_puani}')

    else:
        bilgisayar_puani += 1
        print(f'Bilgisayar:{bilgisayar_puani} VS Siz:{kullanici_puani}')

    if bilgisayar_puani == 3 or kullanici_puani == 3:
            break

if bilgisayar_puani < kullanici_puani:
    print('Kazandınız')
    print('SİÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜ')
else:
    print('Kaybettiniz')
   