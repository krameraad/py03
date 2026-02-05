#!/usr/bin/env python3

X = "\033[0m"
R = "\033[91m"
G = "\033[92m"
D = "\033[2m"
H = "\033[1m"
HC = "\033[1;96m"
HY = "\033[1;93m"


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


def get_total_value(inventory: dict[str, dict]) -> int:
    total_value = 0
    for v in inventory.values():
        total_value += v.get("quantity") * v.get("value")
    return total_value


def get_item_count(inventory: dict[str, dict]) -> int:
    count = 0
    for v in inventory.values():
        count += v.get("quantity")
    return count


def print_inventory(name: str, inventory: dict[str, dict]):
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
              from_inv: dict[str, dict],
              to_inv: dict[str, dict],
              item: str,
              count: int):
    """Give up to `count` of `item` from `from_name` to `to_name`."""
    print(f"{H}=== {from_name} tries to give {to_name} {count} {item}s ==={X}")

    trade_item = from_inv.get(item)
    if not trade_item or trade_item["quantity"] < 1:
        print(f"{R}Transaction failed!{X}")
        return

    if count > trade_item["quantity"]:
        count = trade_item["quantity"]
    trade_item["quantity"] -= count
    if trade_item["quantity"] < 1:
        from_inv.pop(item)

    if item in to_inv.keys():
        to_inv[item] += count
    else:
        to_inv.update({item: dict(trade_item)})
        to_inv[item]["quantity"] = count
    print(f"{G}Transaction successful!{X}")

    print(f"{H}=== Updated inventories ==={X}")
    if from_inv.get(item):
        print(f"{HC}{from_name}'s {item}s{X}"
              f"\t: {from_inv.get(item).get("quantity")}")
    else:
        print(f"{HC}{from_name}'s {item}s{X}\t: 0")
    print(f"{HC}{to_name}'s {item}s{X}"
          f"\t: {to_inv.get(item).get("quantity")}\n")


def inventory_stats(players: dict):
    """Print statistics on all players' inventories."""
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

    print(f"{H}=== Inventory Analytics ==={X}")
    print(f"{HC}Most valuable player{X}\t:"
          f" {most_gold[0]} ({most_gold[1]} gold)")
    print(f"{HC}Most items{X}\t\t: {most_items[0]} ({most_items[1]} items)")
    print(f"{HC}Rarest items{X}\t\t: {", ".join(rares)}")


print(f"{H}=== Player Inventory System ==={X}\n")
print_inventory("Alice", alice)
print_inventory("Bob", bob)
give_item("Alice", "Bob", alice, bob, "potion", 2)
print_inventory("Alice", alice)
print_inventory("Bob", bob)
inventory_stats(players)
