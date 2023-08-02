import operator

class GameState():

    def __init__(self):
        self.player_1 = {"name": "Player 1", "piece": "o"}
        self.player_2 = {"name": "Player 2", "piece": "x"}
        self.current_player = self.player_1
        self.target = None
        self.game_over = False
        self.validation_reference = "'[o]', '[o]', '[o]', '[o]'"
        self.grid = [
            ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
        ]

    def print_grid(self):
        key = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 "]
        for row in self.grid:
            print(*row)
        print(*key)

    def set_target_column(self):
        self.target = None
        player_input = input(f"{self.current_player['name']}, select a column: ")
        while self.target == None:
            if player_input.isdigit() == False:
                player_input = input("Invalid move! Please select another column: ")
            else:
                player_input = int(player_input)
            if player_input not in range(1, 8):
                player_input = input("Invalid move! Please select another column: ")
            else:
                self.target = player_input - 1

    def check_grid(self):
        reverse_grid = list(reversed(self.grid))
        while reverse_grid == list(reversed(self.grid)):
            if self.grid[0][self.target] == '[o]' or self.grid[0][self.target] == '[x]':
                self.target = int(input("Invalid move! Please select another column: ")) -1
            else:
                for row in reverse_grid:
                    if row[self.target] == "[ ]":
                        row[self.target] = f"[{self.current_player['piece']}]"
                        self.grid = list(reversed(reverse_grid))
                        return

    def validator(self):
        self.__row_validator()
        self.__column_validator()
        self.__diagonal_validator()
        if self.game_over == True:
            return self.game_over
        else:
            self.__swap_player()
            return self.game_over


    def __row_validator(self):
        for row in self.grid:
            row_str = str(row)
            if self.validation_reference in row_str:
                self.game_over = True
                return

    def __column_validator(self):
        for column in range(0, 7):
            column_list = []
            for row in self.grid:
                column_list.append(row[column])
            column_str = str(column_list)
            if self.validation_reference in column_str:
                self.game_over = True
                return

    def __diagonal_validator(self):
        row_count = -1
        column_count = -1
        for row in self.grid:
            row_count += 1
            for _ in row:
                if column_count == 6:
                    column_count = 0
                else:
                    column_count += 1
                for add_or_sub in [operator.add, operator.sub]:
                    if add_or_sub(column_count, 3) in range(0, 7) and (row_count - 3) in range(0, 6):
                        test_list = []
                        for target in range(0, 4):
                            test_list.append(self.grid[row_count - target][add_or_sub(column_count, target)])
                            if self.validation_reference in str(test_list):
                                self.game_over = True
                                return

    def __swap_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
            self.validation_reference = "'[x]', '[x]', '[x]', '[x]'"
        else:
            self.current_player = self.player_1
            self.validation_reference = "'[o]', '[o]', '[o]', '[o]'"
