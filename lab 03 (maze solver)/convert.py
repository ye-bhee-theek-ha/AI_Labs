import sys


def convert_to_array(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        # mechanism to prevent adding three 0's or 1's when encounters "---" or "   "
        char_ignore = 0
        # to check if a character is skipped and then corrected
        corrected = False

        cur_row = 0
        cur_col = 0

        safe_houses = []
        player_pos = [0, 0]

        maze = []
        for line in file:
            tmp_row = []
            for char in line:
                if char_ignore == 0:
                    if char == "+" or char == "|":
                        tmp_row.append(1)
                    elif char == "-":
                        tmp_row.append(1)
                        char_ignore = 2
                    elif char == " ":
                        if tmp_row[-1] == 0 or corrected:  # checks if the previous block was also a path then skips 3 spaces and
                            char_ignore = 3                # adds 2 0's for the wall space (which is not here) and the next free tile
                            tmp_row.append(0)              # also if char appears in the skipped tile case is handled in the else statement below
                            tmp_row.append(0)              # and corrected variable is set to true so the previous is still considered as empty
                            corrected = False
                        else:
                            char_ignore = 2
                            tmp_row.append(0)
                    elif char == "\n":
                        pass
                    else:
                        add_char(char, player_pos, safe_houses, cur_row, cur_col)
                        tmp_row.append(char)
                else:
                    if char.isalpha():
                        tmp_row.pop()
                        tmp_row.append(char)
                        add_char(char, player_pos, safe_houses, cur_row, cur_col)
                        corrected = True

                    char_ignore -= 1
                cur_col += 1

            cur_row += 1
            cur_col = 0

            maze.append(tmp_row)

        return maze, player_pos, safe_houses


def add_char(char, player_pos, safe_houses, cur_row, cur_col):
    if char == "A":
        if player_pos[1] != 0 or player_pos[0] != 0:
            print("Cannot be more than 1 players")
            sys.exit()
        player_pos[0] = cur_row
        player_pos[1] = cur_col

    elif char == "S":
        safe_houses.append((cur_row, cur_col))
