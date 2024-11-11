testo = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eu sapien vitae lacus porta tempor. Fusce id lectus vitae ex laoreet consequat eu eget sem. Sed euismod neque vel pulvinar volutpat. Sed et rhoncus erat. Integer euismod accumsan lobortis. Vestibulum eu maximus sem. Sed quis arcu quis eros iaculis suscipit at sit amet dui. Integer dictum finibus nisi, et gravida purus cursus vel. Praesent aliquam consectetur tellus, maximus aliquam felis dictum a. Ut sollicitudin vehicula odio, in luctus magna pharetra id.

Maecenas et sapien quis ipsum aliquet tincidunt sed at nisl. Suspendisse potenti. Curabitur faucibus nisl velit, quis vulputate dolor blandit id. Donec ultricies diam et consectetur imperdiet. Sed porta non enim sit amet tempor. Maecenas quis lacus euismod, eleifend urna vel, mollis nulla. Suspendisse in erat enim. Cras ullamcorper eget dui nec consectetur.

Donec in molestie sapien, nec pulvinar mi. Etiam dignissim est metus, at blandit elit rhoncus nec. In eleifend sit amet nunc vitae tincidunt. Cras et dignissim felis, sed luctus nulla. Proin eu erat a eros venenatis consequat. Praesent vehicula auctor elit, a volutpat augue bibendum id. Nam aliquam augue at neque rhoncus, aliquam efficitur elit efficitur. Aliquam posuere, nisi non lobortis molestie, nulla urna maximus arcu, a hendrerit magna magna at tortor. Etiam sem dui, ultricies id mi ac, tempus mollis quam. Phasellus nec odio elit.

Nunc laoreet massa nec lacus dapibus, sed ultricies magna fringilla. Suspendisse efficitur quam ut venenatis auctor. Praesent tincidunt interdum eros, at molestie orci. Nunc luctus dui in libero luctus pellentesque ac quis elit. Vestibulum rhoncus eget lacus sed rutrum. Sed metus ex, elementum quis pulvinar sit amet, finibus eget urna. Fusce accumsan velit metus, a convallis nunc bibendum vitae. Cras iaculis mi eget magna tempor dapibus. Sed efficitur semper iaculis. Vestibulum ullamcorper rhoncus massa, at aliquet orci ultricies non.

Sed ut feugiat felis. Duis facilisis mi ut eros congue convallis. Aenean rutrum vehicula arcu et dapibus. Donec pharetra augue ac orci pulvinar dapibus. Ut volutpat metus id metus dictum rhoncus vitae ac metus. Ut dapibus est nibh, nec sodales magna tempor et. Morbi ullamcorper facilisis ullamcorper. Vestibulum purus est, pretium et consectetur et, feugiat a sapien.
'''

with open("lorem.txt", "w") as file:

    file.write(testo)

with open("lorem.txt", "r") as file:

    testo_letto = file.read()

def controlla(testo_letto):

    if len(testo_letto)>0:

        return True

    else:

        return False


paragrafi = list(filter(controlla, testo_letto.split("\n")))

print(f"Il numero di paragrafi è {len(paragrafi)}")

numero_parole= 0
caratteri = 0

for paragrafo in paragrafi:

    parole = list(filter(controlla, paragrafo.split(" ")))
    numero_parole += len(parole)

    for parola in parole:

        caratteri += len(parola)





print(f"Il numero di parole è {numero_parole}")

print(f"Il numero di caratteri è {caratteri}")


