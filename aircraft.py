# class Aircraft:
#
#     def __init__(self, model, aircraft_id, rows, seats_in_row):
#         self._model = model
#         self._aircraft_id = aircraft_id
#         self._rows = rows
#         self._seats_in_row = seats_in_row
#
#     def model(self):
#         return self._model
#
#     def aircraft_id(self):
#         return self._aircraft_id
#
#     def possible_seats(self):
#         return self._rows * self._seats_in_row
#
#     def seating_plan(self):
#          return (range(1, self._rows + 1), 'ABCDEFGH'[:self._seats_in_row])


class Aircraft:

    def __init__(self, aircraft_id):
        self._aircraft_id = aircraft_id

    def aircraft_id(self):
        return self._aircraft_id

    def num_seats(self):
        rows, seats = self.seating_plan()
        return len(rows) * len(seats)


class AirBus319(Aircraft):

    def model(self):
        return 'AirBus 319'

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing747(Aircraft):

    def model(self):
        return 'AirBus 319'

    def seating_plan(self):
        return range(1, 35), "ABCDEFGH"

