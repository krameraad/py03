#!/usr/bin/env python3

X = "\033[0m"
C = "\033[96m"
Y = "\033[93m"
H = "\033[1m"
HC = "\033[1;96m"
XH = "\033[0;1m"

alice = {"first_kill",
         "level_10",
         "treasure_hunter",
         "speed_demon"}
bob = {"first_kill",
       "level_10",
       "boss_slayer",
       "collector"}
charlie = {"level_10",
           "treasure_hunter",
           "boss_slayer",
           "speed_demon",
           "perfectionist"}


print(f"{H}\n=== Achievement Tracker System ==={X}")
print(f"{HC}Alice{XH}'s achievements:{X}")
print(alice, "\n")
print(f"{HC}Bob{XH}'s achievements:{X}")
print(bob, "\n")
print(f"{HC}Charlie{XH}'s achievements:{X}")
print(charlie)

print(f"{H}\n=== Achievement Analytics ==={X}")
all = alice | bob | charlie
# all = alice.union(bob, charlie)
print(f"{H}All unique achievements:{X} {all}")
print(f"{H}Total unique achievements: {Y}{len(all)}{X}\n")

print(f"{H}Common to all players:{X} {alice & bob & charlie}")
# print(f"{H}Common to all players:{X} {alice.intersection(bob, charlie)}")
alice_dif = alice - bob - charlie
bob_dif = bob - alice - charlie
charlie_dif = charlie - alice - bob
# alice_dif = alice.difference(bob, charlie)
# bob_dif = bob.difference(alice, charlie)
# charlie_dif = charlie.difference(alice, bob)
print(f"{H}Rare achievements (1 player):{X}"
      f" {alice_dif | bob_dif | charlie_dif}\n")
# print(f"{H}Rare achievements (1 player):{X}"
#       f" {alice_dif.union(bob_dif, charlie_dif)}\n")

print(f"{HC}Alice{XH} vs {C}Bob{XH} common:{X} "
      f"{alice & bob}")
print(f"{H}- {C}Alice{XH} unique:{X} {alice - bob}")
print(f"{H}- {C}Bob{XH} unique:{X} {bob - alice}")
# print(f"{H}- {C}Alice{XH} unique:{X} {alice.difference(bob)}")
# print(f"{H}- {C}Bob{XH} unique:{X} {bob.difference(alice)}")
