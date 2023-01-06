from dataclasses import dataclass

from Entities.constants import RED


@dataclass
class Piece:
    def __init__(self, column, row, color):
        self.__column = column
        self.__row = row
        self.__color = color

    def __str__(self):
        return f"{'1' if self.__color == RED else '2'}"

    def __repr__(self):
        return f"{'1' if self.__color == RED else '2'}"

    @property
    def column(self):
        return self.__column

    @property
    def row(self):
        return self.__row

    @property
    def color(self):
        return self.__color





