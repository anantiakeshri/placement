from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",
                 ["Pikachu", "Squartile", "Charmander", "Bellossom"])
table.add_column("Type", ["Electric", "Water", "Fire", "Grass"])
table.left_padding_width = 3
table.right_padding_width = 3
table.junction_char = "*"
print(table)
