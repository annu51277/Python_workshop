from prettytable import PrettyTable
table = PrettyTable()
# table.add_column('Family',['ans',0,0])
# table.add_column("Variables",['Ansar',"Arshia","Zaidan"])
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(['Adelaide', 1295, 1158259, 600.5],)
table.add_row(["Brisbane", 5905, 1857594, 1146.9])
table.add_column("location", ["India", "USA"])
# print(table.align)
table.align = "r"
# print(table.align)

print(table)
print(table.get_string(sortby="Annual Rainfall", reversesort=True))
#
