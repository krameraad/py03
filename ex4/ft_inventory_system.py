#!/usr/bin/env python3

X = "\033[0m"
R = "\033[91m"
G = "\033[92m"
B = "\033[94m"
C = "\033[96m"
M = "\033[95m"
Y = "\033[93m"
HY = "\033[1;93m"
D = "\033[2m"
H = "\033[1m"
HC = "\033[1;96m"
XH = "\033[0;1m"
E = "\033[3m"


alice = {
    "sword": {
        "type": "weapon",
        "rarity": "rare",
        "quantity": 1,
        "value": 500
    },
    "potion": {
        "type": "consumable",
        "rarity": "common",
        "quantity": 5,
        "value": 50
    },
    "shield": {
        "type": "armor",
        "rarity": "uncommon",
        "quantity": 1,
        "value": 200
    }
}

bob = {
    "mace": {
        "type": "weapon",
        "rarity": "uncommon",
        "quantity": 1,
        "value": 300
    },
    "magic_ring": {
        "type": "armor",
        "rarity": "rare",
        "quantity": 1,
        "value": 200
    }
}

players = {
    "Alice": alice,
    "Bob": bob
}


def get_total_value(inventory: dict) -> int:
    total_value = 0
    for item, info in inventory.items():
        total_value += info.get("quantity") * info.get("value")
    return total_value


def get_item_count(inventory: dict) -> int:
    count = 0
    for item, info in inventory.items():
        count += info.get("quantity")
    return count


def print_inventory(name: str, inventory: dict):
    """Print info on a player's inventory."""
    categories = {}

    print(f"{H}=== {name}'s Inventory ==={X}")
    for item, info in inventory.items():
        item_type = info.get("type")
        rarity = info.get("rarity")
        quantity = info.get("quantity")
        value = info.get("value")
        print(f"- {HY}{item}{X} ({item_type}, {rarity}):"
              f" {quantity}x @ {value} gold each"
              f" = {quantity * value} gold")
        if item_type in categories.keys():
            categories[item_type] += quantity
        else:
            categories.update({item_type: quantity})

    print(f"{HC}Net worth{X}\t: {get_total_value(inventory)} gold")
    print(f"{HC}Item count{X}\t: {get_item_count(inventory)} items")
    print(f"{HC}Categories{X}\t:", end="")
    for category, count in categories.items():
        print(f" {category}({count})", end="")
    print("\n")


def give_item(from_name: str,
              to_name: str,
              from_inv: dict,
              to_inv: dict,
              item: str,
              count: int):
    """Give up to `count` of `item` from `from_name` to `to_name`."""
    trade_item: dict = from_inv["potion"]

    print(f"{H}=== {from_name} gives {to_name} {count} {item}s ==={X}")
    if count > trade_item["quantity"]:
        count = trade_item["quantity"]
    trade_item["quantity"] -= count
    if trade_item["quantity"] < 1:
        from_inv.pop("potion")

    if item in to_inv.keys():
        to_inv[item] += count
    else:
        to_inv.update({item: dict(trade_item)})
        to_inv[item]["quantity"] = count
    print(f"{G}Transaction successful!{X}")

    print(f"{H}=== Updated inventories ==={X}")
    if from_inv.get("potion"):
        print(f"{HC}{from_name}'s {item}s{X}"
              f"\t: {from_inv.get("potion").get("quantity")}")
    else:
        print(f"{HC}{from_name}'s {item}s{X}\t: 0")
    print(f"{HC}{to_name}'s {item}s{X}"
          f"\t: {to_inv.get("potion").get("quantity")}\n")


def inventory_stats(players: dict):
    most_gold = ("", -1)
    most_items = ("", -1)
    rares = []
    for player in players:
        total_value = get_total_value(players[player])
        if total_value > most_gold[1]:
            most_gold = (player, total_value)
        item_count = get_item_count(players[player])
        if item_count > most_items[1]:
            most_items = (player, item_count)
        for item, info in players[player].items():
            if info.get("rarity") == "rare":
                rares += [item]
    print(f"{H}=== Inventory Analytics ==={X}\n")
    print(f"{HC}Most valuable player\t:{X} {most_gold[0]} ({most_gold[1]} gold)")
    print(f"{HC}Most items\t\t:{X} {most_items[0]} ({most_items[1]} items)")
    print(f"{HC}Rarest items\t\t:{X} {rares}")


print(f"{H}=== Player Inventory System ==={X}\n")
print_inventory("Alice", alice)
print_inventory("Bob", bob)
give_item("Alice", "Bob", alice, bob, "potion", 2)
print_inventory("Alice", alice)
print_inventory("Bob", bob)
inventory_stats(players)
