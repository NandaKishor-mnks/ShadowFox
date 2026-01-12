#Initially
justice_league = ["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]
print("Initial Justice League:", justice_league)

# 1. Number of members
print("Number of members:", len(justice_league))

# 2. Batman recruits Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\nAfter adding Batgirl and Nightwing:", justice_league)

# 3. Make Wonder Woman the leader (move to beginning)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\nAfter making Wonder Woman the leader:", justice_league)

# 4. Separate Aquaman and Flash
# Choosing "Green Lantern" to place between them
justice_league.remove("Green Lantern")
flash_index=justice_league.index("Flash")
justice_league.insert(flash_index+1,"Green Lantern")
print("\nAfter separating Aquaman and Flash:", justice_league)

# 5. Replace the list with new members
justice_league = ["Cyborg","Shazam","Hawkgirl","Martian Manhunter","Green Arrow"]
print("\nNew Justice League team:", justice_league)

# 6. Sort alphabetically
justice_league.sort()
print("\nSorted Justice League:", justice_league)

# Bonus: New leader
print("\nNew leader (0th index):", justice_league[0])
