from convert import convert_to_array

filename = "maze.txt"

# fix corrected bool problem

maze, player_pos, safe_house = convert_to_array(filename)

for line in maze:
    print(line)
print(player_pos)
print(safe_house)
