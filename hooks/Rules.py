from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value, get_option_value, is_option_enabled
from BaseClasses import MultiWorld, CollectionState

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

#to speed things up, I'm making a look-up table for the progressive characters. 
#the functions requiresBlock and requiresranged will check this look-up table if its filled or not
#maybe fill this dictionary with squad limits?
#actually, yeah thats a lot better and faster than constantly calling functions, retype these comments to be more clear
progressive_operators_settings = dict() #could be replaced with curly braces, these ones{}, because its apparently faster
def fill_progressive_operator_dictionary(multiworld: MultiWorld, player: int):
    #forgot to delimit the get_option_value outputs! search how to do it
    for stars in range(1, 7):
        progressive_operators_settings[f"{stars} star"] = get_option_value(multiworld, player, f"include_{stars}_stars")
        progressive_operators_settings[f"amount {stars}"] = get_option_value(multiworld, player, f"amount_progressive_{stars}_stars")

    progressive_operators_settings["squad sanity"] = is_option_enabled(multiworld, player, "squad_size_sanity")

# if even 3 or 4 stars is excluded, then most basic levels should be beatable, so check if even these options are disabled or not. 
# 1 and 2 stars aren't included, because they are basically useless
def enabledOperators(world: World, player: int):
    six_stars = get_option_value(world.multiworld, player, "include 6 stars")
    five_stars = get_option_value(world.multiworld, player, "include 5 stars")
    four_stars = get_option_value(world.multiworld, player, "include 4 stars")
    three_stars = get_option_value(world.multiworld, player, "include 3 stars")
    if six_stars == 2 or five_stars == 2 or four_stars == 2 or three_stars == 2:
        return True

    return False
#hook for combining normal operators and progressive characters
def requiredOperators(multiworld: MultiWorld, state: CollectionState, player: int, blocked: str, ranged: str):
    if not bool(progressive_operators_settings):
        fill_progressive_operator_dictionary(multiworld, player)

    #check the squad size first. if this isn't bigger than the required amount of blocking and ranged units, then we can return false immediately
    print(progressive_operators_settings)
    #return early if minimum amount of block and ranged can't be taken with the unlocked squad size
    if progressive_operators_settings["squad size"]:
        total_block = int(blocked) + int(ranged)
        if total_block > 12 and state.count("increased squad size", player) <12:
            return False
        if state.count("increased squad size", player) < total_block:
            return False
    #check for the enabled operators. if the any category isn't enabled, they are using them, just not randomised, there for beatable (most of the time)
    if not enabledOperators(multiworld, player):
        return False
    
    standing_units = 0
    ranged_units = 0
    for item_name, amount in [("6 star", "amount 6 star"), ("5 star", "amount 5 star"), ("4 star", "amount 4 star"), ("3 star", "amount 3 star"), ("2 star", "amount 2 star"), ("1 star", "amount 1 star")]:
        #can I check per item group? that would save a lot of coding (and probably time)
        #first do only blocking units
        amount_progressive = state.count(f"progressive {item_name}", player)
        #if the included limit is smaller than 12, we need to calculate how many slots can be used.
        if progressive_operators_settings[item_name] == 1:
            amount_progressive = amount_progressive * 12/progressive_operators_settings[amount]
        standing_units += amount_progressive
        amount_operators += amount_progressive
        #if there are enough blocking units and ranged units, then we can return early
        if standing_units >= int(blocked) and ranged_units >= int(ranged):
            return True

    #to check the normal list, just use the normal ap approach with the || things. 
    return f"|@blocked:{int(blocked) - standing_units}| AND |@ranged:{int(ranged) - ranged_units}|"

#be sure that category name is a valid name!!
def checkAmountxStars(state: CollectionState, player: int, category_name: str, required: str):
    progressive_amount = state.count(f"progressive {category_name}", player)
    if progressive_operators_settings[category_name] == 1:
        progressive_amount = progressive_amount * 12/progressive_operators_settings[f"amount {category_name}"]

    return f"|@{category_name}:{required-progressive_amount}|" if progressive_amount < int(required) else False

def checkClassAmount(state: CollectionState, player: int, class_name: str, required: str):
    total = 0
    for item_group_name in ["6 star", "5 star", "4 star", "3 star", "2 star", "1 star"]:
        amount_progressive = state.count(f"progressive {item_group_name}", player)
        total += amount_progressive
        if total > int(required):
            return True
    return f"|@{class_name}: {required-total}|"

def totalOperators(state: CollectionState, player: int, amount_needed):
    total = 0
    for item_group_name in ["6 star", "5 star", "4 star", "3 star", "2 star", "1 star"]:
        total += state.count(f"progressive {item_group_name}", player)
        if total >= int(amount_needed):
            return True

    return f"|@character:{amount_needed-total}|"        

def OPAmount(multiworld: MultiWorld, state:CollectionState, player: int):
    total = get_option_value(multiworld, player, "originium_prime_hunt")
    needed = get_option_value(multiworld, player, "percentage_goal_amount")
    if isinstance(total, int) and isinstance(needed, int):
        if state.count ("Originium Prime") >= total*needed/100:
            return True
    # if the option isn't a int, then something else is wrong, so always return false just to be sure it doesn't work
    return False