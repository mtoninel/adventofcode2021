#!usr/bin/env python
from __future__ import annotations
from typing import NamedTuple

# PUZZLE 1

with open('./bingo_input.txt') as file:
    input = file.read()

# Input parsing, first line numbers represent extracted numbers while tables are single bingo tables, winning tables are represented by either fully complete rows or columns, no diagonals.

# Define a class for table object and a method to parse the tables.
class Table(NamedTuple):
    left: set[int] # keep track of the numbers left
    called: list[int] # keep track of the ones called, used to call winning boards

    @property
    def win_or_not(self) -> bool: # property to understand winning tables
        for i in range(5): # tables are 5x5
            for j in range(5):
                if self.called[i * 5 + j] in self.left: # offset within list
                    break
                else:
                    return True

            for j in range(5):
                if self.called[i + 5 * j] in self.left:
                    break
                else:
                    return True
        else:
            return False
                
        

    # Construct a method for parsing tables and append the set and list above
    @classmethod
    def parsing(cls, board: str) -> Table: #arrow is used to define metadata components and store them in a dict accessible with the .__annotations__ method
        ints = [int(s) for s in board.split()]
        n_left = set(ints)
        return cls(n_left, ints)

# Parse input
extracted_n, *tables = input.split('\n\n') # Python splits on both newlines and whitespaces equally
boards = [Table.parsing(table) for table in tables] # List of n bingo boards, each with 2 attributes, left and called.
numbers = [int(s) for s in extracted_n.split(',')] # List of extracted numbers

# Iterate through called numbers and boards to understand if a board wins
def winning_board() -> str:
    for number in numbers:
        for board in boards:
            board.left.discard(number) # Discard a number from a set if present in the called ones

        # Print the product between called numbers and not called ones in the winning board
        for board in boards:
            if board.win_or_not:
                return sum(board.left) * number


print(winning_board())
