# Use a dictionary to remove dulicates from a list and maintain order

names = ["John", "Daisy", "Bob", "Lilly", "Bob", "Daisy"]
uniques_names = list({name: name for name in names}.values())
print(uniques_names)