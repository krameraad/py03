#!/usr/bin/env python3

X = "\033[0m"
R = "\033[91m"
G = "\033[92m"
B = "\033[94m"
C = "\033[96m"
M = "\033[95m"
Y = "\033[93m"
D = "\033[2m"
H = "\033[1m"
HC = "\033[1;96m"
XH = "\033[0;1m"
E = "\033[3m"

alice = set(["first_kill",
             "level_10",
             "treasure_hunter",
             "speed_demon"])
bob = set(["first_kill",
           "level_10",
           "boss_slayer",
           "collector"])
charlie = set(["level_10",
               "treasure_hunter",
               "boss_slayer",
               "speed_demon",
               "perfectionist"])
print(f"{H}=== Achievement Tracker System ==={X}\n")
print(f"{HC}Alice{XH}'s achievements:{X}")
print(alice, "\n")
print(f"{HC}Bob{XH}'s achievements:{X}")
print(bob, "\n")
print(f"{HC}Charlie{XH}'s achievements:{X}")
print(charlie, "\n")

print(f"{H}=== Achievement Analytics ==={X}\n")
print(f"{H}All unique achievements:{X}")
all = alice.union(bob, charlie)
print(all)
print(f"{H}Total unique achievements: {Y}{len(all)}{X}\n")

print(f"{H}Common to all players:{X} {alice.intersection(bob, charlie)}")
alice_dif = alice.difference(bob, charlie)
bob_dif = bob.difference(alice, charlie)
charlie_dif = charlie.difference(alice, bob)
print(f"{H}Rare achievements (1 player):{X}"
      f" {alice_dif.union(bob_dif, charlie_dif)}\n")

print(f"{HC}Alice{XH} vs {C}Bob{XH} common:{X} "
      f"{alice.intersection(bob)}")
print(f"{H}- {C}Alice{XH} unique:{X} {alice.difference(bob)}")
print(f"{H}- {C}Bob{XH} unique:{X} {bob.difference(alice)}")
