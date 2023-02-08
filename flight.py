class Flight:
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f'First two signs should be letters')
        if not number[:2].isupper():
            raise ValueError('First two letter should be Capital Letters')
        if not len(number) == 6:
            raise ValueError('number is represented by two Capital Letters and four digits')
        if not number[2:].isnumeric():
            raise ValueError('Only two first signs are letters, the rest should be digits')

        self._airline = number[:2]
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_passenger(self, seat, passenger):
        '''
        Allocate a seat to a passenger

        :param seat:
        number from rows, letter from seats
        :param passenger:
        string -> name and vorname

        set passenger to right place
        self._seating[number from rows][letter from seats] = passenger

        :return:
        pass
        '''

        row, letter = self._parse_seat(seat)
        if self._seating[row][letter] is not None:
            raise ValueError(f'Seat {seat} already occupied')
        self._seating[row][letter] = passenger

    def _parse_seat(self, seat):
        row_text = seat[:-1]
        letter = seat[-1]
        rows, seats = self._aircraft.seating_plan()
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid seat row {row_text}')

        if row not in rows:
            raise ValueError(f'Invalid seat row {row}')

        if letter not in seats:
            raise ValueError(f'Invalid seat {letter}')
        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        '''

        :param from_seat:
        use parse to get row_from and letter from. Check if seat from is occupied.
        :param to_seat:
        use parse to get row_to and letter to. Check if seat to is occupied.
        :return:
        return pass
        if from_seat and to_seat are available, then relocate passenger from_seat to to_seat
        '''
        row_from, letter_from = self._parse_seat(from_seat)
        row_to, letter_to = self._parse_seat(to_seat)
        if self._seating[row_from][letter_from] is None:
            raise ValueError('from seat is None')
        if self._seating[row_to][letter_to] is not None:
            raise ValueError('to seat is occupied')
        self._seating[row_to][letter_to] = self._seating[row_from][letter_from]
        self._seating[row_from][letter_from] = None

    def num_available_seats(self):
        return sum(sum(1 for letter in row.values() if letter is None)
                   for row in self._seating if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in self._passenger_seats():
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        '''An iterable series of passenger seating locations.'''
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield passenger, f"{row}{letter}"
