Nu am idee cum ar trebui sa folosesc makefile pentru python. 
Se ruleaza cu python Main.py
In cazul meu nu am nevoie de un fisier de iesire deoarece in descrierea exercitiului cerinta e ca sirurile sa se afiseze.

Programul ia din fisierul input.txt datele si creaza automatul.
Dupa, asteapta inputul de sir.
Dupa ce acesta este dat, afiseaza outputurile posibile. Nu afiseaza nimic daca nu exista niciun output.

Programul se incheie daca la intrare primeste caracterul #.

In fisierul input.txt automatul este de forma:

Linia 1:  MULTIMEA STARILOR

Linia 2:  STAREA INITIALA

Linia 3:  MULTIMEA STARILOR FINALE

Linia 4:  ALFABETUL DE INTRARE

LINIA 5:  ALFABETUL DE IESIRE

LINIA 6:  ALFABETUL STIVEI

LINIA 7:  SIMBOLUL INITIAL AL STIVEI

LINIA 8 - INCOLO : TRANZITIILE 

Forma tranzitiilor este:  Stare automatului -> caracter de intrare -> litera citita pe stiva ->
                          Starea destinatie -> Modificarea stivei -> Caracterul de iesire

Lambda e implicit cunoscut ca 'lambda' si nu trebuie specificat in alfabetul de intrare.
