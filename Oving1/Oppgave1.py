from sys import stdin


class Kubbe:
    vekt = None
    neste = None
    def __init__(self, vekt):
        self.vekt = vekt
        self.neste = None


def spor(kubbe):
    biggest = kubbe.vekt
    while kubbe:
        if kubbe.neste.vekt > biggest:
            biggest = kubbe.neste.vekt
        kubbe = kubbe.neste
    return biggest

# Oppretter en lenket liste
forste = None
siste = None
for linje in stdin:
    forrige_siste = siste
    siste = Kubbe(int(linje))
    if forste == None:
        forste = siste
    else:
        forrige_siste.neste = siste

#Kaller losningsfunksjonen og skriver ut resultatet
print spor(forste)