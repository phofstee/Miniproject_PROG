__author__ = "Thomas Korevaar, Menno Noltes, Gijs van Ewijk, Larsse Vink and Pim Hofstee"
__version__ = 1.0
__status__ = 'Development'


# Programme modules
from register import register
from login import login


# Geeft menu opties weer
def menu():

    print('Menu: ')
    print('1 - Inloggen')
    print('2 - Registreren')
    print('')

    try:
        input_choice = int(input('Maak een keuze: '))
        if input_choice > 0 and input_choice < 3:
            if input_choice == 1:
                login()
            if input_choice == 2:
                # @todo: wachtwoord encrypten bij opslaan?
                register()
        else:
            print('Geen geldige invoer!')
    except:
        print('')
        print('Ongeldige waarde!')

    # Na dat de functie is uitgevoerd, moet het menu opnieuw worden gestart.
    menu()

# Roep menu aan bij opstarten script
menu()