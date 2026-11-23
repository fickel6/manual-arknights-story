from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value, get_option_value, is_option_enabled
from BaseClasses import MultiWorld, CollectionState

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.

# import logging

def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# if even 3 or 4 stars is excluded, then most basic levels should be beatable, so check if even these options are disabled or not. 
# 1 and 2 stars aren't included, because they are basically useless
def enabledOperators(multiworld: MultiWorld, player: int):
    six_stars = get_option_value(multiworld, player, "include_6_stars")
    five_stars = get_option_value(multiworld, player, "include_5_stars")
    four_stars = get_option_value(multiworld, player, "include_4_stars")
    three_stars = get_option_value(multiworld, player, "include_3_stars")
    if six_stars == 2 or five_stars == 2 or four_stars == 2 or three_stars == 2:
        return True

    return False

#hook for combining normal operators and progressive characters
def requiredOperators(multiworld: MultiWorld, state: CollectionState, player: int, block: str, range: str):

    #check the squad size first. if this isn't bigger than the required amount of blocking and range units, then we can return false immediately
    #return early if minimum amount of block and range can't be taken with the unlocked squad size
    if is_option_enabled(multiworld, player, "squad_size_sanity"):
        total_block = int(block) + int(range)
        if total_block > 12:
            # logging.info("invalid block count")
            return False
        if state.count("progressive squad size", player) < total_block:
            # logging.info("squad size isn't big enough")
            return False
    #check for the enabled operators. if the any category isn't enabled, they are using them, just not randomised, there for beatable (most of the time)
    if enabledOperators(multiworld, player): 
            # logging.info("enough operators are not enabled for this run")
            return True
    
    standing_units = 0
    rangers = 0
    for item_name, amount in [(get_option_value(multiworld, player, "include_6_stars"), get_option_value(multiworld, player, "amount_progressive_6_stars")), 
                              (get_option_value(multiworld, player, "include_5_stars"), get_option_value(multiworld, player, "amount_progressive_5_stars")), 
                              (get_option_value(multiworld, player, "include_4_stars"), get_option_value(multiworld, player, "amount_progressive_4_stars")), 
                              (get_option_value(multiworld, player, "include_3_stars"), get_option_value(multiworld, player, "amount_progressive_3_stars")), 
                              (get_option_value(multiworld, player, "include_2_stars"), get_option_value(multiworld, player, "amount_progressive_2_stars")), 
                              (get_option_value(multiworld, player, "include_1_stars"), get_option_value(multiworld, player, "amount_progressive_1_stars"))]:
        #can I check per item group? that would save a lot of coding (and probably time)
        #first do only blocking units
        amount_progressive = state.count(f"progressive {item_name}", player)
        #if the included limit is smaller than 12, we need to calculate how many slots can be used.
        if item_name == 1:
            amount_progressive = amount_progressive * 12//amount
        standing_units += amount_progressive
        rangers += amount_progressive
        #if there are enough blocking units and range units, then we can return early
        if standing_units >= int(block) and rangers >= int(range):
            # logging.info("progressive characters are enough")
            return True
    #to check the normal list, just use the normal ap approach with the || things. 
    # logging.info("returning a normal require block")
    return f"|@block:{int(block) - standing_units}| AND |@range:{int(range) - rangers}|"

#be sure that category name is a valid name!!
def checkAmountxStars(multiworld: MultiWorld, state: CollectionState, player: int, category_name: str, required: str):
    progressive_amount = state.count(f"progressive {category_name}", player)
    # to determine the rarity, We can just check the first character. max rarity is 6 (less than 10) and always at the beginning
    rarity = int(category_name[0])
    if get_option_value(multiworld, player, f"include_{rarity}_stars") == 1:
        progressive_amount = progressive_amount * 12//get_option_value(multiworld, player, f"amount_progressive_{rarity}_stars")

    return f"|@{category_name}:{int(required)-progressive_amount}|" if progressive_amount < int(required) else False

def checkClassAmount(state: CollectionState, player: int, class_name: str, required: str):
    # logging.info("checking class amount")
    total = 0
    for item_group_name in ["6 star", "5 star", "4 star", "3 star", "2 star", "1 star"]:
        amount_progressive = state.count(f"progressive {item_group_name}", player)
        total += amount_progressive
        if total > int(required):
            return True
    return f"|@{class_name}: {int(required)-total}|"

def totalOperators(state: CollectionState, player: int, amount_needed):
    total = 0
    # logging.info("checking total amount")
    for item_group_name in ["6 star", "5 star", "4 star", "3 star", "2 star", "1 star"]:
        total += state.count(f"progressive {item_group_name}", player)
        if total >= int(amount_needed):
            return True

    return f"|@character:{int(amount_needed)-total}|"        

def OPAmount(multiworld: MultiWorld, player: int, state:CollectionState):
    total = get_option_value(multiworld, player, "originium_prime_hunt")
    needed = get_option_value(multiworld, player, "percentage_goal_amount")
    if isinstance(total, int) and isinstance(needed, int):
        if state.count ("Originium Prime") >= total*needed/100:
            return True
    #return false also if one of the options doesn't return an int (which should never happen).
    return False