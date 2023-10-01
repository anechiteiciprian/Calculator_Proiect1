# Importăm modulul argparse pentru a prelua argumentele din linia de comandă
import argparse

# Funcție pentru afișarea rezultatului și așteptarea unei noi operații
def afisare_si_asteptare(valoare_curenta):
    print(valoare_curenta)
    operatie = input("> ")
    return operatie

# Funcție pentru a verifica dacă o comandă este validă și a efectua operația corespunzătoare
def efectuare_operatie(valoare_curenta, operatie):
    if operatie.startswith('+'):
        try:
            numar = float(operatie[1:])
            valoare_curenta += numar
        except ValueError:
            print("Invalid operation", valoare_curenta)
    elif operatie.startswith('-'):
        try:
            numar = float(operatie[1:])
            valoare_curenta -= numar
        except ValueError:
            print("Invalid operation", valoare_curenta)
    elif operatie.startswith('*'):
        try:
            numar = float(operatie[1:])
            valoare_curenta *= numar
        except ValueError:
            print("Invalid operation", valoare_curenta)
    elif operatie.startswith('/'):
        try:
            numar = float(operatie[1:])
            if numar != 0:
                valoare_curenta /= numar
            else:
                print("Invalid operation", valoare_curenta)
        except ValueError:
            print("Invalid operation", valoare_curenta)
    elif operatie.startswith('='):
        try:
            numar = float(operatie[1:])
            valoare_curenta = numar
        except ValueError:
            print("Invalid operation", valoare_curenta)
    elif operatie == 'x':
        exit()
    else:
        print("Invalid operation", valoare_curenta)
    return valoare_curenta

# Funcție principală pentru calculatoare
def main():
    # Parsăm argumentele din linia de comandă
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--valoare', type=float, default=0.0, help='Valoarea inițială')
    args = parser.parse_args()

    valoare_curenta = args.valoare

    while True:
        valoare_curenta = efectuare_operatie(valoare_curenta, afisare_si_asteptare(valoare_curenta))

if __name__ == "__main__":
    main()