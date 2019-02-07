"""
A module for strategies.
"""
from typing import Any


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


def recursive_minimax_strategy(game: Any) -> Any:
    """
    Return a move throuth the MINIMAX algorithum, done recursively
    @param Any game: A game to be played
    @rtype: Any
    """
    copied_game = game
    possible_moves = game.current_state.get_possible_moves()
    possible_states = []
    for i in possible_moves:
        bt = copied_game.current_state.make_move(i)
        possible_states.append(bt)
    lst = [-1 * get_score(x) for x in possible_states]
    max_ = max(lst)
    index = lst.index(max_)
    return possible_moves[index]


def iterative_minimax_strategy(game) -> Any:
    """
    Return a move for the game, with MM strategy, done iteratively
    @param "Game" game: A game to be played
    @rtype: Any
    """
    current_possible_moves = game.current_state.get_possible_moves()
    state = game.current_state
    stack = Stack()
    tree_root = Tree(state)
    stack.add(tree_root)
    while not stack.is_empty():
        top = stack.remove()
        if top.value.get_possible_moves() == []:
            top.score = 1
        elif top.children == []:
            new_possible_moves = top.value.get_possible_moves()
            for i in new_possible_moves:
                top.children.append(Tree(top.value.make_move(i)))
            stack.add(top)
            for child in top.children:
                stack.add(child)
        elif top.children != []:
            top.score = -1 * max([i.score for i in top.children])
    x = []
    for item in tree_root.children:
        x.append(item.score)
    index = x.index(max(x))
    return current_possible_moves[index]


def get_score(state):
    """
    @param state:
    @type state:
    @return:
    @rtype:
    """
    copied_state = state
    if copied_state.get_possible_moves() == []:
        # if copied_state.get_current_player_name() == player:
        # return 1
        # if copied_state.get_current_player_name() != player:
        return -1
        # return 0
    return max([-1 * get_score(copied_state.make_move(x)) for x
                in copied_state.get_possible_moves()])


class Tree:
    """
    A somewhat useful tree class...
    """

    def __init__(self, value=None, score: int = -2, children=None):
        self.value = value
        self.score = score
        self.children = children if children else []


class Stack:
    """
    A somewhat useful Stack class...
    """

    def __init__(self):
        """
        Initialization
        """
        self.item_ = []

    def add(self, item):
        """
        Well, add the item
        >>> a = Stack()
        >>> a.add(111)
        >>> a.item_[0] == 111
        True
        """
        self.item_.append(item)

    def remove(self):
        """
        Well, we remove the last item in the stack
        @rtype:
        >>> s = Stack()
        >>> s.add(111)
        >>> s.add(222)
        >>> s.remove()
        222
        """
        a = self.item_.pop()
        return a

    def is_empty(self) -> bool:
        """
        Well, returns true iff the Stack is empty
        @rtype: bool
        >>> a = Stack()
        >>> a.is_empty()
        True
        """
        return self.item_ == []
