from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value, get_option_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"

#to speed things up, I'm making a look-up table for the progressive characters. 
#the functions requiresBlock and requiresranged will check this look-up table if its filled or not
#maybe fill this dictionary with squad limits?
#actually, yeah thats a lot better and faster than constantly calling functions, retype these comments to be more clear
progressive_operators_settings = dict() #could be replaced with curly braces, these ones{}, because its apparently faster
def fill_progressive_operator_dictionary(multiworld: MultiWorld, player: int):
    #forgot to delimit the get_option_value outputs! search how to do it
    for stars in range(1, 7):
        settings = get_option_value(multiworld, player, f"amount progressive {stars} stars")
        progressive_operators_settings[f"{stars} star"] = settings

    settings = get_option_value(multiworld, player, "squad_size")
    if settings != 0:
        progressive_operators_settings["squad size"] = settings

#function for checking if 3 and 4 is excluded or not
# if it is excluded, it should return true. This way, if someone excluded 3 and 4 stars, all the stages will always be open
# 1 and 2 stars aren't included, because they are basically useless (sorry not sorry)
def enabledOperators(world: World, player: int):
    four_stars = get_option_value(world.multiworld, player, "include 4 stars")
    three_stars = get_option_value(world.multiworld, player, "include 3 stars")
    if four_stars == 2 and three_stars == 2:
        return True

    return False
#hook for combining normal operators and progressive characters
def requiredOperators(world: World, state: CollectionState, player: int, blocked: str, ranged: str):
    if not bool(progressive_operators_settings):
        fill_progressive_operator_dictionary(world.multiworld, player)

    #check the squad size first. if this isn't bigger than the required amount of blocking and ranged units, then we can return false immediately
    if progressive_operators_settings["squad size"] != 0 and progressive_operators_settings["squad size"] < state.count("increased squad size", player):
        return False
    #also check for the enabled operators. if this 3 and 4 stars aren't enabled, they are using them, just not randomised
    if not enabledOperators(world, player):
        return False
    
    standing_units = 0;
    ranged_units = 0;
    for item_group_name in ["6 star", "5 star", "4 star", "3 star", "2 star", "1 star"]:
        if standing_units >= int(blocked) and ranged_units >= int(ranged):
            return True
        
        #can I check per item group? that would save a lot of coding (and probably time)
        #first do only blocking units
        amount_progresive = state.count(f"progressive {item_group_name}", player)
        #if the included limit is smaller than 12, we need to calculate how many slots can be used. 
        progressive_limit = progressive_operators_settings[item_group_name] 
        if progressive_operators_settings[item_group_name] <12:
            amount_progressive = int(amount_progressive * (12/progressive_limit))
            
        standing_units += amount_progresive + state.count(f"{item_group_name}", player) #this must count the amount of x stars collected, see if there is a known function to do this, otherwise I will need to make a function for it
        standing_units += amount_operators
        #now we do ranged units
        amount_operators += amount_progresive + state.count(f"{item_group_name}", player) #this must count the amount of x stars collected, see if there is a known function to do this, otherwise I will need to make a function for it
    return False
