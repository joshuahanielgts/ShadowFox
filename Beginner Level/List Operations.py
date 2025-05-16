print("\nList Section")
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial team:", justice_league)

print("Total members:", len(justice_league))

justice_league.extend(["Batgirl", "Nightwing"])
print("After adding Batgirl & Nightwing:", justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Wonder Woman as leader:", justice_league)

justice_league.remove("Superman")
justice_league.insert(justice_league.index("Flash"), "Superman")
print("Separated Aquaman and Flash with Superman:", justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New team:", justice_league)

justice_league.sort()
print("Sorted team:", justice_league)
print("New leader:", justice_league[0])
