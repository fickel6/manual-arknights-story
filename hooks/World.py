# Object classes from AP core, to represent an entire MultiWorld and this individual World that's part of it
from typing import Any
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState, Item

# Object classes from Manual -- extending AP core -- representing items and locations that are used in generation
from ..Items import ManualItem
from ..Locations import ManualLocation

# Raw JSON data from the Manual apworld, respectively:
#          data/game.json, data/items.json, data/locations.json, data/regions.json
#
from ..Data import game_table, item_table, location_table, region_table

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value, format_state_prog_items_key, ProgItemsCat, remove_specific_item

# calling logging.info("message") anywhere below in this file will output the message to both console and log file
import logging

#gen random combination for operator choices
import itertools
########################################################################################
## Order of method calls when the world generates:
##    1. create_regions - Creates regions and locations
##    2. create_items - Creates the item pool
##    3. set_rules - Creates rules for accessing regions and locations
##    4. generate_basic - Runs any post item pool options, like place item/category
##    5. pre_fill - Creates the victory location
##
## The create_item method is used by plando and start_inventory settings to create an item from an item name.
## The fill_slot_data method will be used to send data to the Manual client for later use, like deathlink.
########################################################################################



# Use this function to change the valid filler items to be created to replace item links or starting items.
# Default value is the `filler_item_name` from game.json
def hook_get_filler_item_name(world: World, multiworld: MultiWorld, player: int) -> str | bool:
    return False

def before_generate_early(world: World, multiworld: MultiWorld, player: int) -> None:
    """
    This is the earliest hook called during generation, before anything else is done.
    Use it to check or modify incompatible options, or to set up variables for later use.
    """
    pass

# Called before regions and locations are created. Not clear why you'd want this, but it's here. Victory location is included, but Victory event is not placed yet.
def before_create_regions(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after regions and locations are created, in case you want to see or modify that information. Victory location is included.
def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to remove locations from the world
    locationNamesToRemove: list[str] = [] # List of location names
    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if location.name in locationNamesToRemove:
                    region.locations.remove(location)

# This hook allows you to access the item names & counts before the items are created. Use this to increase/decrease the amount of a specific item in the pool
# Valid item_config key/values:
# {"Item Name": 5} <- This will create qty 5 items using all the default settings
# {"Item Name": {"useful": 7}} <- This will create qty 7 items and force them to be classified as useful
# {"Item Name": {"progression": 2, "useful": 1}} <- This will create 3 items, with 2 classified as progression and 1 as useful
# {"Item Name": {0b0110: 5}} <- If you know the special flag for the item classes, you can also define non-standard options. This setup
#       will create 5 items that are the "useful trap" class
# {"Item Name": {ItemClassification.useful: 5}} <- You can also use the classification directly
def before_create_items_all(item_config: dict[str, int|dict], world: World, multiworld: MultiWorld, player: int) -> dict[str, int|dict]:
    return item_config

# The item pool before starting items are processed, in case you want to see the raw item pool at that stage
def before_create_items_starting(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# The item pool after starting items are processed but before filler is added, in case you want to see the raw item pool at that stage
def before_create_items_filler(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    # choose which is you start with
    # 0 = is2
    # 1 = is3
    # 2 = is4
    # 3 = is5
    # 4 = is6
    item = []
    starting_is = world.options.starting_region.value
    if starting_is == 0:
        item.append(next(i for i in item_pool if i.name == "is2 key"))
        if world.options.quick_start == True:
            item.append(next(i for i in item_pool if i.name == "floor2 key is2"))
        starting_is = "is2"
    elif starting_is == 1:
        item.append(next(i for i in item_pool if i.name == "is3 key"))
        if world.options.quick_start == True:
            item.append(next(i for i in item_pool if i.name == "floor2 key is3"))
        starting_is = "is3"
    elif starting_is == 2:
        item.append(next(i for i in item_pool if i.name == "is4 key"))
        if world.options.quick_start == True:
            item.append(next(i for i in item_pool if i.name == "floor2 key is4"))
        starting_is = "is4"
    elif starting_is == 3:
        item.append(next(i for i in item_pool if i.name == "is5 key"))
        if world.options.quick_start == True:
            item.append(next(i for i in item_pool if i.name == "floor2 key is5"))
        starting_is = "is5"
    elif starting_is == 4:
        item.append(next(i for i in item_pool if i.name == "is6 key"))
        if world.options.quick_start == True:
            item.append(next(i for i in item_pool if i.name == "floor2 key is6"))
        starting_is = "is6"
    else:
        raise Exception("not a valid starting is")
    for i in item:
        multiworld.push_precollected(i)
        item_pool.remove(i)
    # choose a starting squad, voucher (3 rand. ops is later)
    # added a random variable for future proofing 
    # later the amount of starting squads + starting_vouchers can be randomised with options (needed?)
    starting_items_choice = [
        {
            "item_categories": ["squad"],
            "random":1
        },
        {
            "item_categories": ["starting voucher"],
            "random":1
        }
    ]
    for starting in starting_items_choice:
        possible_item_names = []

        for category in starting["item_categories"]:
            possible_item_names.extend(
                [name for name, i in world.item_name_to_item.items() if category in i.get("category", []) and starting_is in i.get("category", [])] #accounts for the key not existing
            )

        possible_items = [
            i for i in item_pool if i.name in possible_item_names 
        ]
        for _ in range(starting["random"]): 
            random_starting_item = world.random.choice(possible_items)
            multiworld.push_precollected(random_starting_item)
            possible_items.remove(random_starting_item)
            item_pool.remove(random_starting_item)
            match random_starting_item:
                case "First Move Advantage":
                    starting_items = ["sniper", "specialist", "vanguard"]
                case "Slow and Steady Wins the Race":
                    starting_items = ["Caster", "Defender", "Sniper"] # bug where a 6 star specialist can be chosen
                case "Overcoming your Weaknesses":
                    starting_items = ["Guard", "Medic", "Supporter"]
                case "Flexible Deployment":
                    starting_items = ["Vanguard", "Supporter", "Specialist"]
                case "Indestructible":
                    starting_items = ["Defender", "Caster", "Medic"]
                case _: # it will default to 'First Move Advantage' voucher I.E. begin with sniper, specialist and vanguard 
                    starting_items = ["sniper", "specialist", "vanguard"]

    # now that the starting_voucher is chosen, the operators will be chosen
    # amount of 5 stars is is dependent, because they changed the hope requirement
    # the rest will be filled with 1 to 4 stars (not randomised)
    # also randomise 4 and 3 stars?
    if world.options.include_5_stars == 0:
        item_pool.remove(next(i for i in item_pool if i.name == "progressive 5 star"))
        item_pool.remove(next(i for i in item_pool if i.name == "progressive 5 star"))
    elif world.options.include_5_stars == 1:
        delete_character = []
        delete_character.extend([name for name, i in world.item_name_to_item.items() if "5 star" in i.get("category", [])])
        delete_character = [i for i in item_pool if i.name in delete_character]
        for name in delete_character:
            item_pool.remove(name)
    else:
        delete_all = []
        delete_all.extend([name for name, i in world.item_name_to_item.items() if "5 star" in i.get("category", [])])
        delete_all.extend([name for name, i in world.item_name_to_item.items() if "progressive 5 star" in i.get("category", [])])
        delete_all = [i for i in item_pool if i.name in delete_all]
        for name in delete_all:
            item_pool.remove(name)

    max_amount_operators = 3
    if starting_is == "is2" or "is3" or "is4":
        random_variation = world.random.choice([[1,0], [0,2], [0,1]])
    else: 
        random_variation = world.random.choice([[1,0], [0,3], [0,2], [0, 1]])
    # print("there are "+ str(random_variation[0])+" 6 stars and "+ str(random_variation[1]) + " 5 stars")
    # print("chosen voucher is: [%s]" % ','.join(map(str, starting_items)))
    if random_variation[0] >=1 and world.options.include_6_stars == True:
        type_operator = world.random.randrange(0, 2)
        possible_operators_choice = [name for name, i in world.item_name_to_item.items() if starting_items[type_operator] in i.get("category", []) and "6 star" in i.get("category", [])]
        possible_operators = [i for i in item_pool if i.name in possible_operators_choice]
        random_operator = world.random.choice(possible_operators)
        multiworld.push_precollected(random_operator)
        item_pool.remove(random_operator)
    #if no six star, how should the amount of vouchers be distributed?)
    elif random_variation[1] >1 and world.options.include_5_stars == 0:
        random_variation_5_star = [0,0,0]
        for i in range(len(starting_items)):
            if random_variation[1] >0:
                random_variation_5_star[i] = 1
                random_variation[1] -= 1
            else:
                random_variation_5_star[i] = 0
        
        random_variation_5_star = list(set(itertools.permutations(random_variation_5_star)))
        random_variation_5_star = world.random.choice(random_variation_5_star)
        starting_5_star = [
            {
                "item_categories": [starting_items[0]],
                "random": random_variation_5_star[0]
            },
            {
                "item_categories": [starting_items[1]],
                "random": random_variation_5_star[1]
            },
            {
                "item_categories": [starting_items[2]],
                "random": random_variation_5_star[2]
            },
        ]
        for starting in starting_5_star:
            possible_operators_choice = []
            for category in starting["item_categories"]:
                possible_operators_choice.extend(
                    [name for name, i in world.item_name_to_item.items() if category in i.get("category", []) and "5 star" in i.get("category", [])] #accounts for the key not existing
                )

            possible_operators = [
                i for i in item_pool if i.name in possible_operators_choice 
            ]
            # print("[%s]"%", ".join(map(str, possible_operators)))
            if starting["random"] == 1: 
                random_starting_operator = world.random.choice(possible_operators)
                # print("chosen 5 star: " + str(random_starting_operator))
                multiworld.push_precollected(random_starting_operator)
                item_pool.remove(random_starting_operator)
    # remove the amount of random unlockable items
    max_amount_random_unlock = 20
    for _ in range(max_amount_random_unlock - world.options.include_random_operators):
        item_pool.remove(next(i for i in item_pool if i.name == "random unit unlock"))

    return item_pool

    # Some other useful hook options:

    ## Place an item at a specific location
    # location = next(l for l in multiworld.get_unfilled_locations(player=player) if l.name == "Location Name")
    # item_to_place = next(i for i in item_pool if i.name == "Item Name")
    # location.place_locked_item(item_to_place)
    # remove_specific_item(item_pool, item_to_place)

# The complete item pool prior to being set for generation is provided here, in case you want to make changes to it
def after_create_items(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# Called before rules for accessing regions and locations are created. Not clear why you'd want this, but it's here.
def before_set_rules(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after rules for accessing regions and locations are created, in case you want to see or modify that information.
def after_set_rules(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to modify the access rules for a given location
    victory_name = next(
        iter([
            name for name, location in world.location_name_to_location.items() if location.get('victory') == True
        ])
    )
    victory_location = multiworld.get_location(victory_name, player)
    if victory_name == "act0 boss":
        end_boss_location = world.options.act_0_boss_clear
    elif victory_name == "act1 boss":
        end_boss_location = world.options.act_1_boss_clear
    elif victory_name == "act2 boss":
        end_boss_location = world.options.act_2_boss_clear
    elif victory_name == "act3 boss":
        end_boss_location = world.options.act_3_boss_clear
    elif victory_name == "beat x bosses":
        amount_bosses = world.options.amount_boss
        

    def Example_Rule(state: CollectionState) -> bool:
        # Calculated rules take a CollectionState object and return a boolean
        # True if the player can access the location
        # CollectionState is defined in BaseClasses
        return True

    ## Common functions:
    # location = world.get_location(location_name, player)
    # location.access_rule = Example_Rule

    ## Combine rules:
    # old_rule = location.access_rule
    # location.access_rule = lambda state: old_rule(state) and Example_Rule(state)
    # OR
    # location.access_rule = lambda state: old_rule(state) or Example_Rule(state)

# The item name to create is provided before the item is created, in case you want to make changes to it
def before_create_item(item_name: str, world: World, multiworld: MultiWorld, player: int) -> str:
    return item_name

# The item that was created is provided after creation, in case you want to modify the item
def after_create_item(item: ManualItem, world: World, multiworld: MultiWorld, player: int) -> ManualItem:
    return item

# This method is run towards the end of pre-generation, before the place_item options have been handled and before AP generation occurs
def before_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

# This method is run at the very end of pre-generation, once the place_item options have been handled and before AP generation occurs
def after_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

# This method is run every time an item is added to the state, can be used to modify the value of an item.
# IMPORTANT! Any changes made in this hook must be cancelled/undone in after_remove_item
def after_collect_item(world: World, state: CollectionState, Changed: bool, item: Item):
    # the following let you add to the Potato Item Value count
    # if item.name == "Cooked Potato":
    #     state.prog_items[item.player][format_state_prog_items_key(ProgItemsCat.VALUE, "Potato")] += 1
    pass

# This method is run every time an item is removed from the state, can be used to modify the value of an item.
# IMPORTANT! Any changes made in this hook must be first done in after_collect_item
def after_remove_item(world: World, state: CollectionState, Changed: bool, item: Item):
    # the following let you undo the addition to the Potato Item Value count
    # if item.name == "Cooked Potato":
    #     state.prog_items[item.player][format_state_prog_items_key(ProgItemsCat.VALUE, "Potato")] -= 1
    pass


# This is called before slot data is set and provides an empty dict ({}), in case you want to modify it before Manual does
def before_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called after slot data is set and provides the slot data at the time, in case you want to check and modify it after Manual is done with it
def after_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called right at the end, in case you want to write stuff to the spoiler log
def before_write_spoiler(world: World, multiworld: MultiWorld, spoiler_handle) -> None:
    pass

# This is called when you want to add information to the hint text
def before_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:

    ### Example way to use this hook:
    # if player not in hint_data:
    #     hint_data.update({player: {}})
    # for location in multiworld.get_locations(player):
    #     if not location.address:
    #         continue
    #
    #     use this section to calculate the hint string
    #
    #     hint_data[player][location.address] = hint_string

    pass

def after_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:
    pass

def hook_interpret_slot_data(world: World, player: int, slot_data: dict[str, Any]) -> dict[str, Any]:
    """
        Called when Universal Tracker wants to perform a fake generation
        Use this if you want to use or modify the slot_data for passed into re_gen_passthrough
    """
    return slot_data
