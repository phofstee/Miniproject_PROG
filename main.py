__author__ = "Thomas Korevaar, Menno Noltes, Gijs van Ewijk, Larsse Vink and Pim Hofstee"
__version__ = 1.0
__status__ = 'Development'

# Programma modules
import register
import login
import retrieve
import information
from menu import menu
import park

# Geeft menu opties weer
def loginmenu():

    print('Menu: ')
    print('1 - Inloggen')
    print('2 - Registreren')
    print('3 - Uitleg')
    print('')

    input_choice = int(input('Maak een keuze: '))
    if input_choice > 0 and input_choice < 4:
        if input_choice == 1:
            # Pim, Thomas
            success, useruuid = login.login()
            #useruuid bevat de uuid voor volgende queries

            while success:
                action = menu()

                for k,v in action.items():
                    if v == "park":
                        park.park(useruuid)
                    if v == "retrieve":
                        retrieve.retrieve(useruuid)
                        #tbi fiets ophalen
                    if v == "info":
                        information.menu(useruuid)
                        #tbi informatie over fiets/stalling
                    if v == "logout":
                        success = False
                        useruuid = None
                        loginmenu()

        if input_choice == 2:
            # Pim
            register.register()
        if input_choice == 3:
            # Menno
            print('Kies optie 1 om in te loggen als u al een account heeft.')
            print('Kies optie 2 om een nieuw account te maken.')
    else:
        print('Geen geldige invoer!')

    loginmenu()

# Roep menu aan bij opstarten script
loginmenu()
