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
    victory_name = next(
        iter([
            name for name, location in world.location_name_to_location.items() if location.get('victory') == True
        ])
    )
    max_amount_bosses = 16
    if victory_name != "beat x bosses":
        for _ in range(max_amount_bosses - 1):
            item_pool.remove(next(i for i in item_pool if i.name == "defeated bosses"))
    else:
        for _ in range(max_amount_bosses - world.options.amount_boss):
            item_pool.remove(next(i for i in item_pool if i.name == "defeated bosses"))
    #remove all the excluded operators
    def remove_character(prog_item, item_name, amount_progressive, option):
        if option == 0:
            for _ in range(amount_progressive):
                item_pool.remove(next(i for i in item_pool if i.name == prog_item))
        elif option == 1:
            delete_character = []
            delete_character.extend([name for name, i in world.item_name_to_item.items() if item_name in i.get("category", [])])
            delete_character = [i for i in item_pool if i.name in delete_character]
            for name in delete_character:
                item_pool.remove(name)
        else:
            for _ in range(amount_progressive):
                item_pool.remove(next(i for i in item_pool if i.name == prog_item))
            delete_all = []
            delete_all.extend([name for name, i in world.item_name_to_item.items() if item_name in i.get("category", [])])
            delete_all = [i for i in item_pool if i.name in delete_all]
            for name in delete_all:
                item_pool.remove(name)

    remove_character("progressive 6 star", "6 star", 2, world.options.include_6_stars)
    remove_character("progressive 5 star", "5 star", 2, world.options.include_5_stars)
    remove_character("progressive 4 star", "4 star", 2, world.options.include_4_stars)
    remove_character("progressive 3 star", "3 star", 1, world.options.include_3_stars)
    remove_character("progressive low star", "low star", 1, world.options.include_1_and_2_stars)
    # remove the amount of random unlockable items
    max_amount_random_unlock = 20
    for _ in range(max_amount_random_unlock - world.options.include_random_operators):
        item_pool.remove(next(i for i in item_pool if i.name == "random unit unlock"))

    return item_pool

# The item pool after starting items are processed but before filler is added, in case you want to see the raw item pool at that stage
def before_create_items_filler(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:

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
    # actx bosses are done with 'defeat boss' item. 
    # this means that we only need to force this item to the correct boss
    # and we don't have to change the requirement
    victory_location = multiworld.get_location(victory_name, player)
    if victory_name != "beat x bosses":
        return None
    amount_bosses = world.options.amount_boss

    def check_boss_amount(state: CollectionState):
        #really simple. just check how many boss amount is collected
        return state.has_group("boss clear", player, amount_bosses)
    
    victory_location.access_rule = lambda state: check_boss_amount(state)

    # def Example_Rule(state: CollectionState) -> bool:
    #     # Calculated rules take a CollectionState object and return a boolean
    #     # True if the player can access the location
    #     # CollectionState is defined in BaseClasses
    #     return True

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
    victory_name = next(
        iter([
            name for name, location in world.location_name_to_location.items() if location.get('victory') == True
        ])
    )
    beat_boss = next(i for i in multiworld.get_items() if i.player == player and "defeated bosses" == i.name)
    print(beat_boss)
    boss_locations = []
    match victory_name:
        case "act0 boss":
            match world.options.act_0_boss_clear:
                case 0:
                    boss_locations.append("0-11 clear")
                case 1:
                    boss_locations.append("1-12 clear")
                case 2:
                    boss_locations.append("2-10 clear")
                case 3:
                    boss_locations.append("3-8 clear")
        case "act1 boss":
            match world.options.act_1_boss_clear:
                case 0:
                    boss_locations.append("4-10 clear")
                case 1:
                    boss_locations.append("5-11 clear")
                case 2:
                    boss_locations.append("6-18 clear")
                case 3:
                    boss_locations.append("7-20 clear")
                case 4:
                    boss_locations.append("JT8-3 clear")
        case "act2 boss":
            match world.options.act_2_boss_clear:
                case 0:
                    boss_locations.append("9-21 clear")
                case 1:
                    boss_locations.append("10-19 clear")
                case 2:
                    boss_locations.append("11-21 clear")
                case 3:
                    boss_locations.append("12-21 clear")
                case 4:
                    boss_locations.append("13-22 clear")
                case 5:
                    boss_locations.append("14-23 clear")
        case "act3 boss":
            match world.options.act_3_boss_clear:
                case 0:
                    boss_locations.append("15-21 clear")
        case "beat x bosses":
            boss_locations.extend([name for name, i in world.location_name_to_location.items() if "boss stage" in i.get("category", [])])

    # print("boss locations: " + boss_locations)
    #Force place the 'defeated boss' in the boss_locations just found.
    for location in boss_locations:
        placed_location = multiworld.get_location(location, player)
        placed_location.place_locked_item(beat_boss)
        multiworld.itempool.remove(beat_boss)

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
