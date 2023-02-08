from aircraft import *
from flight import *


def make_flights():

    ## for old version with only class Aircraft you need to change AirBus319 into Aircraft class
    ## Aircraft class got more variables to input
    f = Flight('AS0504', AirBus319('ID 666'))
    f.allocate_passenger('18E', 'Piotras Dragon')
    f.allocate_passenger('15A', 'Piotras ZDragon')
    f.allocate_passenger('18D', 'Piotras ADragon')
    f.allocate_passenger('18C', 'Piotras BDragon')
    f.allocate_passenger('18B', 'Piotras CDragon')
    f.allocate_passenger('18A', 'Piotras DDragon')

    g = Flight('AS0505', Boeing747('ID 667'))
    g.allocate_passenger('1E', 'Piotras EDragon')
    g.allocate_passenger('1D', 'Piotras FDragon')
    g.allocate_passenger('1C', 'Piotras GDragon')
    g.allocate_passenger('1B', 'Piotras HDragon')
    g.allocate_passenger('1A', 'Piotras IDragon')

    return f, g


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f"| Name: {passenger}"     \
             f" Flight: {flight_number}"\
             f" Seat: {seat}"           \
             f" Aircrat: {aircraft}"    \
             f" |"
    banner = "+" + "-" * (len(output) -2) + "+"
    border = "|" + " " * (len(output) -2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()
