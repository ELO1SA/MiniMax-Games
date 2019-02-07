"""
A subclass of Game State
A class for to keep track of the state of the stone_henge game
"""
from typing import Any
from game_state import GameState
from map import Map

LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class StoneHengeState(GameState):
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
        >>> a = StoneHengeState(True, Map(2))
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

    def make_move(self, move: str) -> 'StoneHengeState':
        """
        move: Tuple(mover: int, move: str)
        Return the GameState that results from applying move to this GameState.
        """
        # string_of_state = deepcopy(self.map.henge)
        # dic_of_state = deepcopy(self.map.state)
        # for char in string_of_state:
        #     if char == move[1]:
        #         string_of_state = string_of_state.replace('char',
        #                                                   str(move[0]))
        # for key in dic_of_state:
        #     for lst in dic_of_state[key]:
        #         for i in range(len(lst)):
        #             if lst[i] == move[1]:
        #                 lst[i] = move[0]
        # # Up to now the d_o_s and d_o_s are already up to date
        # for key in dic_of_state:
        #     for lst in dic_of_state[key]:
        #         total = len(lst)
        #         count_1 = len([i for i in lst if i == '1'])
        #         count_2 = len([i for i in lst if i == '2'])
        #         claimer = '@'
        #         if count_1 >= total:
        #             claimer = '1'
        #         elif count_2 >= total:
        #             claimer = '2'
        #         lst[0] = claimer
        # # print(dic_of_state, string_of_state)
        # new_map = Map(self.map.side_length)
        # new_map.state = dic_of_state
        # new_map.henge = string_of_state
        # # print(new_map)
        if self.p1_turn is True:
            str_move = ('1', move)
        else:
            str_move = ('2', move)
        new_map = self.map.move_map(str_move)
        if self.p1_turn is True:
            return StoneHengeState(False, new_map)
        return StoneHengeState(True, new_map)

    def is_valid_move(self, move: Any) -> bool:
        """
        Return whether move is a valid move for this GameState.
        """
        if move is None:
            return False
        return move in self.get_possible_moves()

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).
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
            if len(state_.get_possible_moves()) == 0:
                return self.WIN
            # list_of_oponent_state = []
            for opnent_move in state_.get_possible_moves():
                oponent_state = state_.make_move(opnent_move)
                list_of_oponent_state.append(oponent_state)
        if all([(len(i.get_possible_moves()) == 0) for i in
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
            if len(new_state.get_possible_moves()) == 0:
                return self.WIN
            oponent_possible_moves = new_state.get_possible_moves()
            one_choice = []
            for move1 in oponent_possible_moves:
                oponent_state = new_state.make_move(move1)
                one_choice.append(oponent_state)
            list_of_oppnent_state.append(any([(len(i.get_possible_moves())
                                               == 0) for i in one_choice]))
        if all(list_of_oppnent_state):
            return self.LOSE
        return self.DRAW


if __name__ == '__main__':
    import doctest

    doctest.testmod()
