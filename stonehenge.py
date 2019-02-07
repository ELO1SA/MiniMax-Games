"""
A Subclass of Game
a class for the the Stone Henge Game
"""
from copy import deepcopy
from typing import Any
from game import Game
from game_state import GameState
from map import Map

LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class StonehengeGame(Game):
    """
    A sub class of Game, A class for the Stone Henge game.
    """

    def __init__(self, p1_starts: bool):
        side_length = int(input("Please enter a side lenth to start: "))
        map_ = Map(side_length)
        self.current_state = StonehengeState(p1_starts, map_)
        # if p1_starts:
        #     self.p1_turn = True
        # else:
        #     self.p1_turn = False
        self.p1_turn = p1_starts

    def get_instructions(self) -> str:
        """
        Return the Instrucsions for this game
        @rtype: str
        Doctest not provided since the __init__ of the class relies on input
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
        Doctest not provided since the __init__ of the class relies on input
        """
        if string not in LETTERS:
            string = input("Sorry, but invalid input, how'bout we try again: ")
        # if self.p1_turn:
        #     return (1, string.upper())
        return string.upper()

    def is_over(self, state: "StonehengeState") -> bool:
        """
        Return whether or not the game is over at state
        @param StoneHengeState state: the current state
        @rtype: bool
        Doctest not provided since the __init__ of the class relies on input
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
        Doctest not provided since the __init__ of the class relies on input
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


class StonehengeState(GameState):
    """
    The state of a game at a certain point in time.

    WIN - score if player is in a winning position
    LOSE - score if player is in a losing position
    DRAW - score if player is in a tied position
    p1_turn - whether it is p1's turn or not

    WIN: int = 1
    LOSE: int = -1
    DRAW: int = 0
    p1_turn: bool
    """
    WIN: int = 1
    LOSE: int = -1
    DRAW: int = 0
    p1_turn: bool

    def __init__(self, is_p1_turn: bool, map_: Map) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.

        """
        super().__init__(is_p1_turn)
        self.map = map_

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        >>> a = StonehengeState(True, Map(2))
        >>> a.__str__().startswith(' ')
        True
        """
        return self.map.__str__()
        # if self.p1_turn is True:
        #     return "The game is in p1's turn, and the battle state is " \
        #            "as follows: \n" + message
        # return "The game is in p2's turn, and the battle state is " \
        #        "as follows: \n" + message

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        >>> a = StonehengeState(True, Map(2))
        >>> a.get_possible_moves()
        ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        """
        map_ = self.map
        list_of_states = map_.extract_state()
        winning_count = 0.5 * len(list_of_states)
        count1 = 0
        count2 = 0
        for item in list_of_states:
            if item == '1':
                count1 += 1
            elif item == '2':
                count2 += 1
        if count1 >= winning_count or count2 >= winning_count:
            return []
        x = []
        large_str = self.map.__str__()
        for char in large_str:
            if char in LETTERS:
                x.append(str(char))
        return x

    # def get_current_player_name(self) -> str:
    #     """
    #     Return 'p1' if the current player is Player 1, and 'p2' if the current
    #     player is Player 2.
    #     """
    #     if self.p1_turn:
    #         return 'p1'
    #     return 'p2'

    def make_move(self, move: str) -> 'StonehengeState':
        """
        move: Tuple(mover: int, move: str)
        Return the GameState that results from applying move to this GameState.
        """
        if self.p1_turn is True:
            str_move = ('1', move)
        else:
            str_move = ('2', move)
        new_map = self.map.move_map(str_move)
        if self.p1_turn is True:
            return StonehengeState(False, new_map)
        return StonehengeState(True, new_map)

    def is_valid_move(self, move: Any) -> bool:
        """
        Return whether move is a valid move for this GameState.
        >>> a = StonehengeState(True, Map(2))
        >>> a.is_valid_move('Z')
        False
        """
        if move is None:
            return False
        return move in self.get_possible_moves()

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).
        This doctest is not provided due to the fact that it doesnt like spaces
        """
        return (self.get_current_player_name() + '\'s turn, '
                + self.map.__str__())

    def no_longer_in_use_ro(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        possible_moves = self.get_possible_moves()
        list_of_oponent_state = []
        for move in possible_moves:
            state_ = self.make_move(move)
            if state_.get_possible_moves() == []:
                return self.WIN
            # list_of_oponent_state = []
            for opnent_move in state_.get_possible_moves():
                oponent_state = state_.make_move(opnent_move)
                list_of_oponent_state.append(oponent_state)
        if all([(i.get_possible_moves() == []) for i in
                list_of_oponent_state]):
            return self.LOSE
        return self.DRAW

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        current_player_possible_moves = self.get_possible_moves()
        list_of_oppnent_state = []
        for move in current_player_possible_moves:
            new_state = self.make_move(move)
            if new_state.get_possible_moves() == []:
                return self.WIN
            oponent_possible_moves = new_state.get_possible_moves()
            one_choice = []
            for move1 in oponent_possible_moves:
                oponent_state = new_state.make_move(move1)
                one_choice.append(oponent_state)
            list_of_oppnent_state.append(any([(i.get_possible_moves()
                                               == []) for i in one_choice]))
        if all(list_of_oppnent_state):
            return self.LOSE
        return self.DRAW


if __name__ == '__main__':
    import doctest

    doctest.testmod()
