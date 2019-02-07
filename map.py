"""
A class to keep the map of the stone henge game
"""
from copy import deepcopy


class Map:
    """
    Map class
    """

    def __init__(self, side_length: int):
        """
        Initialization...
        >>> a = Map(1)
        >>> a.__str__().startswith(' ')
        True
        """
        self.side_length = side_length
        if side_length == 1:
            self.henge = """\
      {3}   {4}
     /   /
{1} - A - B
     \\ / \\
  {2} - C   {6}
       \\
        {5}"""

            self.state = {'ho': [['@', 'A', 'B'], ['@', 'C']],
                          'rl': [['@', 'A'], ['@', 'B', 'C']],
                          'lr': [['@', 'A', 'C'], ['@', 'B']]}

        elif side_length == 2:
            self.henge = """\
        {4}   {5}
       /   /
  {1} - A - B   {6}
     / \\ / \\ /
{2} - C - D - E
     \\ / \\ / \\
  {3} - F - G   {9}
       \\   \\
        {7}   {8}"""

            self.state = {'ho': [['@', 'A', 'B'], ['@', 'C', 'D', 'E'],
                                 ['@', 'F', 'G']],
                          'rl': [['@', 'A', 'C'], ['@', 'B', 'D', 'F'],
                                 ['@', 'E', 'G']],
                          'lr': [['@', 'C', 'F'], ['@', 'A', 'D', 'G'],
                                 ['@', 'B', 'E']]}
        elif side_length == 3:
            self.henge = """\
          {5}   {6}
         /   / 
    {1} - A - B   {7}
       / \\ / \\ /
  {2} - C - D - E   {8}
     / \\ / \\ / \\ /
{3} - F - G - H - I
     \\ / \\ / \\ / \\
  {4} - J - K - L   {12}
       \\   \\   \\
        {9}   {10}   {11}"""

            self.state = {'ho': [['@', 'A', 'B'], ['@', 'C', 'D', 'E'],
                                 ['@', 'F', 'G', 'H', 'I'],
                                 ['@', 'J', 'K', 'L']],
                          'rl': [['@', 'A', 'C', 'F'],
                                 ['@', 'B', 'D', 'G', 'J'],
                                 ['@', 'E', 'H', 'K'], ['@', 'I', 'L']],
                          'lr': [['@', 'F', 'J'], ['@', 'C', 'G', 'K'],
                                 ['@', 'A', 'D', 'H', 'L'],
                                 ['@', 'B', 'E', 'I']]}
        elif side_length == 4:
            self.henge = """\
            {6}   {7}
           /   / 
      {1} - A - B   {8}
         / \\ / \\ /
    {2} - C - D - E   {9}
       / \\ / \\ / \\ /
  {3} - F - G - H - I   {10}
     / \\ / \\ / \\ / \\ /
{4} - J - K - L - M - N
     \\ / \\ / \\ / \\ / \\
  {5} - O - P - Q - R   {15}
       \\   \\   \\   \\
        {11}   {12}   {13}   {14}"""
            self.state = {'ho': [['@', 'A', 'B'], ['@', 'C', 'D', 'E'],
                                 ['@', 'F', 'G', 'H', 'I'],
                                 ['@', 'J', 'K', 'L', 'M', 'N'],
                                 ['@', 'O', 'P', 'Q', 'R']],
                          'rl': [['@', 'A', 'C', 'F', 'J'],
                                 ['@', 'B', 'D', 'G', 'K', 'O'],
                                 ['@', 'E', 'H', 'L', 'P'],
                                 ['@', 'I', 'M', 'Q'], ['@', 'N', 'R']],
                          'lr': [['@', 'J', 'O'], ['@', 'F', 'K', 'P'],
                                 ['@', 'C', 'G', 'L', 'Q'],
                                 ['@', 'A', 'D', 'H', 'M', 'R'],
                                 ['@', 'B', 'E', 'I', 'N']]}
        elif side_length == 5:
            self.henge = """\
              {7}   {8}
             /   / 
        {1} - A - B   {9}
           / \\ / \\ /
      {2} - C - D - E   {10}
         / \\ / \\ / \\ /
    {3} - F - G - H - I   {11}
       / \\ / \\ / \\ / \\ /
  {4} - J - K - L - M - N   {12}
     / \\ / \\ / \\ / \\ / \\ /
{5} - O - P - Q - R - S - T
     \\ / \\ / \\ / \\ / \\ / \\
  {6} - U - V - W - X - Y   {18}
       \\   \\   \\   \\   \\
        {13}   {14}   {15}   {16}   {17}"""
            self.state = {'ho': [['@', 'A', 'B'], ['@', 'C', 'D', 'E'],
                                 ['@', 'F', 'G', 'H', 'I'],
                                 ['@', 'J', 'K', 'L', 'M', 'N'],
                                 ['@', 'O', 'P', 'Q', 'R', 'S', 'T'],
                                 ['@', 'U', 'V', 'W', 'X', 'Y']],
                          'rl': [['@', 'A', 'C', 'F', 'J', 'O'],
                                 ['@', 'B', 'D', 'G', 'K', 'P', 'U'],
                                 ['@', 'E', 'H', 'L', 'Q', 'V'],
                                 ['@', 'I', 'M', 'R', 'W'],
                                 ['@', 'N', 'S', 'X'], ['@', 'T', 'Y']],
                          'lr': [['@', 'O', 'U'], ['@', 'J', 'P', 'V'],
                                 ['@', 'F', 'K', 'Q', 'W'],
                                 ['@', 'C', 'G', 'L', 'R', 'X'],
                                 ['@', 'A', 'D', 'H', 'M', 'S', 'Y'],
                                 ['@', 'B', 'E', 'I', 'N', 'T']]}
        else:
            raise Exception('Orz. Not yet supported.')

    def extract_state(self) -> list:
        """
        Return the extracted states
        @rtype: list, of states. One of '@', '1', '2'
        >>> a = Map(1)
        >>> a.extract_state()
        ['@', '@', '@', '@', '@', '@']
        """
        x = []
        for key in self.state:
            for lst in self.state[key]:
                x.append(lst[0])
        return x

    def move_map(self, move: tuple) -> "Map":
        """
        Return the new Map after appling the move
        @param str move: The move
        @rtype: "Map"
        >>> a = Map(1)
        >>> b = a.move_map(('1', 'A'))
        >>> b.extract_state()
        ['1', '@', '1', '@', '1', '@']
        """
        player = move[0]
        the_move = move[1]
        new_state = deepcopy(self.state)
        new_henge = deepcopy(self.henge)
        new_henge = new_henge.replace(the_move, player)
        # The string repr_ have been replaced up to now
        for key in new_state:
            nested_blocks_help(new_state, key, player, the_move)
            # for lst in new_state[key]:
            #     for i in range(len(lst)):
            #         if lst[i] == the_move:
            #             lst[i] = player
        for key in new_state:
            for lst in new_state[key]:
                total = len(lst) - 1
                count_1 = len([i for i in lst[1:] if i == '1'])
                count_2 = len([i for i in lst[1:] if i == '2'])
                # claimer = '@'
                if lst[0] == '@' and count_1 >= 0.5 * total:
                    lst[0] = '1'
                elif lst[0] == '@' and count_2 >= 0.5 * total:
                    lst[0] = '2'
                # lst[0] = claimer
                # if lst[0] == '@':
                #     claimer = '@'
                #     if count_1 >= 0.5 * total:
                #         claimer = '1'
                #     elif count_2 >= 0.5 * total:
                #         claimer = '2'
                #     lst[0] = claimer
        new_map = Map(self.side_length)
        new_map.state = new_state
        new_map.henge = new_henge
        return new_map

    def __str__(self) -> str:
        """
        Return the str repr__
        @rtype: str
        """
        states = self.extract_state()
        henge = self.henge
        for i in range(1, len(states) + 1):
            formatter = '{' + '{}'.format(i) + '}'
            # print(formatter)
            henge = henge.replace(formatter, states[i - 1])
            # print(henge)
        return henge

    def __eq__(self, other: "Map") -> bool:
        """
        A special method __eq__
        >>> a = Map(2)
        >>> b = Map(2)
        >>> c = Map(2)
        >>> d = b.move_map(('1', 'A'))
        >>> a == c
        True
        >>> a == d
        False
        """
        return (type(self) == type(other)) and \
               (self.__str__() == other.__str__())


def nested_blocks_help(new_state, key, player, the_move) -> None:
    """
    Okay, here is a helper func...
    """
    for lst in new_state[key]:
        for i in range(len(lst)):
            if lst[i] == the_move:
                lst[i] = player


if __name__ == '__main__':
    import doctest

    doctest.testmod()
