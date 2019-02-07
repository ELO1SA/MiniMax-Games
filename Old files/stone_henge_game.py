"""
A Subclass of Game
a class for the the Stone Henge Game
"""
from typing import Any
from copy import deepcopy
from game import Game
from stone_henge_state import StoneHengeState
from map import Map

LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class StoneHengeGame(Game):
    """
    A sub class of Game, A class for the Stone Henge game.
    """

    def __init__(self, p1_starts: bool):
        side_length = int(input("Please enter a side lenth to start: "))
        map_ = Map(side_length)
        self.current_state = StoneHengeState(p1_starts, map_)
        # if p1_starts:
        #     self.p1_turn = True
        # else:
        #     self.p1_turn = False
        self.p1_turn = p1_starts

    def get_instructions(self) -> str:
        """
        Return the Instrucsions for this game
        @rtype: str
        """
        ins = "This game allows two players. Each player takes turn to " \
              "claim the cells in a stone henge map, one claiming at least " \
              "half of the number of cells in a ley-line claims that row and " \
              "in the same manner, the player first to claim at least half " \
              "of all the lines is the winner of the game!"
        return ins

    def str_to_move(self, string: str) -> Any:
        """
        Return a recognizable str input...
        @param str string: String input
        @rtype: Any
        """
        if string not in LETTERS:
            string = input("Sorry, but invalid input, try again: ")
        # if self.p1_turn:
        #     return (1, string.upper())
        return string.upper()

    def is_over(self, state: StoneHengeState) -> bool:
        """
        Return whether or not the game is over at state
        @param StoneHengeState state: the current state
        @rtype: bool
        """
        list_of_states = deepcopy(state.map.extract_state())
        winning_count = 0.5 * len(list_of_states)
        count1 = 0
        count2 = 0
        for item in list_of_states:
            if item == '1':
                count1 += 1
            elif item == '2':
                count2 += 1
        return count1 >= winning_count or count2 >= winning_count

        # winning = 0
        # if state.map.side_length == 2:
        #     winning = 5
        # elif state.map.side_length == 3:
        #     winning = 6
        # los = state.map.get_list_repr()
        # player1 = 0
        # player2 = 0
        # for string in los:
        #     line = string.strip()
        #     if line.startswith('1'):
        #         player1 += 1
        #     if line.endswith('1'):
        #         player1 += 1
        #     if line.startswith('2'):
        #         player2 += 1
        #     if line.endswith('2'):
        #         player2 += 1
        # if player1 >= winning or player2 >= winning:
        #     return True
        # return False

    def is_winner(self, player: str) -> bool:
        """
        Return True iff player is the winner of the game
        @param str player: The player, either 'p1' or 'p2'
        @rtype: bool
        """
        # winning = 0
        # if self.current_state.map.side_length == 2:
        #     winning = 5
        # elif self.current_state.map.side_length == 3:
        #     winning = 6
        # los = self.current_state.map.get_list_repr()
        # player1 = 0
        # player2 = 0
        # for string in los:
        #     line = string.strip()
        #     if line.startswith('1'):
        #         player1 += 1
        #     if line.endswith('1'):
        #         player1 += 1
        #     if line.startswith('2'):
        #         player2 += 1
        #     if line.endswith('2'):
        #         player2 += 1
        # if player == 'p1' and player1 >= winning:
        #     return True
        # elif player == 'p2' and player2 >= winning:
        #     return True
        # return False
        list_of_states = deepcopy(self.current_state.map.extract_state())
        winning_count = 0.5 * len(list_of_states)
        count1 = 0
        count2 = 0
        for item in list_of_states:
            if item == '1':
                count1 += 1
            elif item == '2':
                count2 += 1
        if count1 >= winning_count and player == 'p1':
            return True
        elif count2 >= winning_count and player == 'p2':
            return True
        return False
        # return count1 >= winning_count or count2 >= winning_count


if __name__ == '__main__':
    import doctest

    doctest.testmod()
