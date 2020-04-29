# Program care simuleaza functionarea unui translator stiva nedeterminist cu lambda-tranzitii.
# Programul citeste dintr-un fisier elementele unui translator stiva nedeterminist cu lambda-tranzitii oarecare
# (starile, starea initiala, starile finale, alfabetul de intrare, alfabetul de iesire, alfabetul stivei, simbolul
# initial al stivei, tranzitiile).
# Programul permite citirea unui nr. oarecare de siruri peste alfabetul de intrare al translatorului.
# Pentru fiecare astfel de sir se afiseaza toate iesirile (siruri peste alfabetul de iesire) corespunzatoare
# (Atentie! pot exista 0, 1 sau mai multe iesiri pt acelasi sir de intrare).

class Automat:
    def __init__(self):
        self.stari = []
        self.starea_initiala = 0
        self.stari_finale = []
        self.alfabet_intrare = ['lambda']
        self.alfabet_iesire = []
        self.alfabet_stiva = []
        self.simbol_initial = ''
        self.tranzitii = []


def main():
    automat = Automat()

    with open('input3.txt') as f:
        # Preiau starile
        automat.stari = f.readline().split()

        # Preiau indexul starii initiale
        automat.starea_initiala = automat.stari.index(f.readline()[:-1])

        # Preiau indexurile starilor finale
        automat.stari_finale = f.readline().split()
        for i in range(len(automat.stari_finale)):
            automat.stari_finale[i] = automat.stari.index(automat.stari_finale[i])

        # Preiau alfabetul de intrare
        automat.alfabet_intrare = f.readline().split()

        # Preiau alfabetul de iesire
        automat.alfabet_iesire = f.readline().split()

        # Preiau alfabetul stivei
        automat.alfabet_stiva = f.readline().split()

        # Preiau simbolul initial al stivei
        automat.simbol_initial = f.readline()[:-1]

        # Preiau tranzitiile
        for line in f:
            # Starea de pornire -> Litera citita -> Simbolul de stiva citit -> Starea destinatie -> Modificarea stivei
            # -> Output
            tranzitie = line.split()
            automat.tranzitii.append(tranzitie)

    # Loop pentru input de siruri pana cand sirul de intrare este #
    g = 0

    while g == 0:
        # Astept alfabetul de intrare:
        sir_intrare = input("Sir de intrare: ")
        if sir_intrare == "#":
            g = 1
        else:
            get_outputs(automat, sir_intrare, automat.starea_initiala, [automat.simbol_initial], [])


def get_outputs(automat, sir_intrare, stare_curenta, stiva, output):
    # Daca prezinta conditiile de acceptare ale unui APD, afisez output.
    if len(sir_intrare) == 0:
        if stare_curenta in automat.stari_finale or len(stiva) == 0:
            print(''.join(output))
        else:
            cauta_lambda(automat, sir_intrare, stare_curenta, stiva, output)
    else:
        # Daca am ajuns sa golesc stiva nu e prea bine
        if len(stiva) == 0:
            print("whoops")

        # Altfel, caut o urmatoare stare pe care sa o parcurg.
        else:
            # Iau toate tranzitiile la rand
            for index_tranzitii in range(len(automat.tranzitii)):
                # Daca tranzitia e din starea in care sunt in alta stare e posibila o tranzitie
                if automat.stari.index(automat.tranzitii[index_tranzitii][0]) == stare_curenta:
                    # Daca litera citita de tranzitie e cea dorita sau e lambda
                    # Si daca ce citesc pe stiva e ce doresc sau e lambda
                    if (automat.tranzitii[index_tranzitii][1] == sir_intrare[0]
                        or automat.tranzitii[index_tranzitii][1] == 'lambda') \
                            and \
                            (automat.tranzitii[index_tranzitii][2] == stiva[-1]
                            or automat.tranzitii[index_tranzitii][2] == 'lambda'):
                        # Modific stiva
                        stiva_new = modifica_stiva(stiva, automat.tranzitii[index_tranzitii][4],
                                                       automat.alfabet_stiva)
                        if automat.tranzitii[index_tranzitii][5] != 'lambda':
                        # Daca output e lambda, nu adaug nimic la output
                            output_new = output + [automat.tranzitii[index_tranzitii][5]]
                        else:
                            # Altfel bag output
                            output_new = output
                        # Repet
                        if automat.tranzitii[index_tranzitii][1] == 'labmda':
                            get_outputs(automat,
                                        sir_intrare,
                                        automat.stari.index(automat.tranzitii[index_tranzitii][3]),
                                        stiva_new,
                                        output_new)
                        else:
                            get_outputs(automat,
                                        sir_intrare[1:],
                                        automat.stari.index(automat.tranzitii[index_tranzitii][3]),
                                        stiva_new,
                                        output_new)

def cauta_lambda(automat, sir_intrare, stare_curenta, stiva, output):
    for i in range(len(automat.tranzitii)):
        for index_tranzitii in range(len(automat.tranzitii)):
            # Daca tranzitia e din starea in care sunt in alta stare e posibila o tranzitie
            if automat.stari.index(automat.tranzitii[index_tranzitii][0]) == stare_curenta:
                # Daca litera citita de tranzitie e cea dorita sau e lambda
                # Si daca ce citesc pe stiva e ce doresc sau e lambda
                if (automat.tranzitii[index_tranzitii][1] == 'lambda') \
                        and \
                        (automat.tranzitii[index_tranzitii][2] == stiva[-1]
                         or automat.tranzitii[index_tranzitii][2] == 'lambda'):
                    # Modific stiva
                    stiva_new = modifica_stiva(stiva, automat.tranzitii[index_tranzitii][4],
                                               automat.alfabet_stiva)
                    if automat.tranzitii[index_tranzitii][5] != 'lambda':
                        # Daca output e lambda, nu adaug nimic la output
                        output_new = output + [automat.tranzitii[index_tranzitii][5]]
                    else:
                        # Altfel bag output
                        output_new = output
                    # Repet
                        get_outputs(automat,
                                    sir_intrare,
                                    automat.stari.index(automat.tranzitii[index_tranzitii][3]),
                                    stiva_new,
                                    output_new)

def modifica_stiva(stiva, input, alfabet_stiva):
    if stiva[-1] == input:
        return stiva
    else:
        if input == 'lambda':
            return stiva[:-1]
        else:
            stiva_noua = stiva.copy()
            # Separ inputul in elemente din alfabetul stivei
            i = 0
            j = 0
            while j <= len(input):
                if input[i:j] in alfabet_stiva:
                    if i == 0 and input[i:j] == stiva[-1]:
                        i = j
                    else:
                        stiva_noua += [input[i:j]]
                        i = j
                j += 1
            return stiva_noua



main()
