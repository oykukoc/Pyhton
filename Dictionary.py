# a collection of {key:value} pairs

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia":"Moscow"}

print(capitals.get("USA"))
print(capitals.get("Russia"))

capitals.update({"Germany":"Berlin"})
capitals.update({"Turkey": "Ankara"})
capitals.update({"USA":"Detroit"})
capitals.pop("China") # it deletes from the table
# capitals.clear()

for capital in capitals.values():
    print(capital,end=", ")