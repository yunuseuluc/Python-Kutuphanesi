from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Ad", "Yaş", "Meslek"] 

table.add_row(["Ali", 26, "Mühendis"])
table.add_row(["Mehmet", 48, "Oyuncakcı"])
table.add_row(["Yunus", 7, "Öğrenci"])

print(table)