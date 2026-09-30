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
    # using this hook to make some global variables 
    global victory_name
    global included_chapters
    included_chapters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
    amount_chapters = world.options.included_random_chapters
    if amount_chapters >= len(included_chapters):
        return
    amount_chapters = len(included_chapters)-amount_chapters
    for _ in range(0, amount_chapters):
        remove_chapter = world.random.choice(included_chapters)
        match remove_chapter:
            case "0":
                    included_chapters.remove("0")
            case "1":
                    included_chapters.remove("1")
            case "2":
                    included_chapters.remove("2")
            case "3":
                    included_chapters.remove("3")
            case "4":
                    included_chapters.remove("4")
            case "5":
                    included_chapters.remove("5")
            case "6":
                    included_chapters.remove("6")
            case "7":
                    included_chapters.remove("7")
            case "8":
                    included_chapters.remove("8")
            case "9":
                    included_chapters.remove("9")
            case "10":
                    included_chapters.remove("10")
            case "11":
                    included_chapters.remove("11")
            case "12":
                    included_chapters.remove("12")
            case "13":
                    included_chapters.remove("13")
            case "14":
                    included_chapters.remove("14")
            case "15":
                    included_chapters.remove("15")
            case "16":
                while "progressive chapter 16" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 16"))
                    included_chapters.remove("16")
    pass

# Called before regions and locations are created. Not clear why you'd want this, but it's here. Victory location is included, but Victory event is not placed yet.
def before_create_regions(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after regions and locations are created, in case you want to see or modify that information. Victory location is included.
def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    locationNamesToRemove: list[str] = [] # List of location names
    all_chapters = get_option_value(multiworld, player, "included_chapters")
    if all_chapters is dict:
        #remove the amount of chapters not included
        for _ in range(0, 17 - world.options.included_random_chapters):
            chapter, _ = world.random.choice([all_chapters.keys()])
            locationNamesToRemove.extend(
                name for name, i in world.location_name_to_location.items() if chapter in i.get("category", [])
            )
                   
    pass
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
    victory_names = [name for name, location in world.location_name_to_location.items() if location.get('victory') == True]
    global victory_name, included_chapters
    victory_name = victory_names[world.options.goal]

    max_amount_bosses = 17
    if victory_name == "collect OP":
        for _ in range(100 - world.options.originium_prime_hunt.value):
            item_pool.remove(next(i for i in item_pool if i.name == "Originium Prime"))
        for _ in range(max_amount_bosses):
            item_pool.remove(next(i for i in item_pool if i.name == "defeated bosses"))
    elif victory_name != "beat x bosses":
        for _ in range(max_amount_bosses - 1):
            item_pool.remove(next(i for i in item_pool if i.name == "defeated bosses"))
        for _ in range(100):
            item_pool.remove(next(i for i in item_pool if i.name == "Originium Prime"))

    # remove the amount of random unlockable items
    max_amount_random_unlock = 20
    for _ in range(max_amount_random_unlock - world.options.include_random_operators):
        item_pool.remove(next(i for i in item_pool if i.name == "random unit unlock"))

    amount_chapters = world.options.included_random_chapters
    if amount_chapters >= len(included_chapters):
        return item_pool
    amount_chapters = len(included_chapters)-amount_chapters
    for _ in range(0, amount_chapters):
        remove_chapter = world.random.choice(included_chapters)
        match remove_chapter:
            case "0":
                while "progressive chapter 0" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 0"))
                    included_chapters.remove("0")
            case "1":
                while "progressive chapter 1" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 1"))
                    included_chapters.remove("1")
            case "2":
                while "progressive chapter 2" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 2"))
                    included_chapters.remove("2")
            case "3":
                while "progressive chapter 3" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 3"))
                    included_chapters.remove("3")
            case "4":
                while "progressive chapter 4" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 4"))
                    included_chapters.remove("4")
            case "5":
                while "progressive chapter 5" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 5"))
                    included_chapters.remove("5")
            case "6":
                while "progressive chapter 6" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 6"))
                    included_chapters.remove("6")
            case "7":
                while "progressive chapter 7" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 7"))
                    included_chapters.remove("7")
            case "8":
                while "progressive chapter 8 past" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 8 past"))
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 8 present"))
                #past and present are the same length. to be sure everything works, add a second while loop for removing extra present items
                    included_chapters.remove("8")
            case "9":
                while "progressive chapter 9" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 9"))
                    included_chapters.remove("9")
            case "10":
                while "progressive chapter 10" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 10"))
                    included_chapters.remove("10")
            case "11":
                while "progressive chapter 11" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 11"))
                    included_chapters.remove("11")
            case "12":
                while "progressive chapter 12" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 12"))
                    included_chapters.remove("12")
            case "13":
                while "progressive chapter 13" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 13"))
                    included_chapters.remove("13")
            case "14":
                while "progressive chapter 14" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 14"))
                    included_chapters.remove("14")
            case "15":
                while "progressive chapter 15" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 15"))
                    included_chapters.remove("15")
            case "16":
                while "progressive chapter 16" in item_pool:
                    item_pool.remove(next(i for i in item_pool if i.name == "progressive chapter 16"))
                    included_chapters.remove("16")
        
    logging.info("included chapters are:")
    for chapter in included_chapters:
        logging.info(f"chapter {chapter}")

    max_squad = 13
    if world.options.squad_size_sanity != 0:
        for i in range(max_squad - world.options.squad_size_sanity):
            item_pool.remove(next(i for i in item_pool if i.name == "progressive squad size"))
    
    return item_pool

# The item pool after starting items are processed but before filler is added, in case you want to see the raw item pool at that stage
def before_create_items_filler(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    #collect the first chapter unlock
    global included_chapters

    match world.random.choice(included_chapters):
        case 0:
            collect_chapter = next(i for i in item_pool if i.name == "progressive chapter 0")
        case 1:
            collect_chapter = next(i for i in item_pool if i.name == "progressive chapter 1")
        case 2:
            collect_chapter = next(i for i in item_pool if i.name == "progressive chapter 2")
        case 3:
            collect_chapter = next(i for i in item_pool if i.name == "progressive chapter 3")
        case 4:
            collect_chapter = next(i for i in item_pool if i.name == "progressive chapter 4")
        case 5:
            collect_chapter = next(i for i in item_pool if i.name == "progressive chapter 5")
        case 6:
            collect_chapter = next(i for i in item_pool if i.name == "progressive chapter 6")
        case 7:
            collect_chapter = next(i for i in item_pool if i.name == "progressive chapter 7")
        case 8:
            collect_chapter = next(i for i in item_pool if i.name == "progressive chapter 8 past")
        case 9:
            collect_chapter = next(i for i in item_pool if i.name == "progressive chapter 9")
        case 10:
            collect_chapter = next(i for i in item_pool if i.name == "progressive chapter 10")
        case 11:
            collect_chapter = next(i for i in item_pool if i.name == "progressive chapter 11")
        case 12:
            collect_chapter = next(i for i in item_pool if i.name == "progressive chapter 12")
        case 13:
            collect_chapter = next(i for i in item_pool if i.name == "progressive chapter 13")
        case 14:
            collect_chapter = next(i for i in item_pool if i.name == "progressive chapter 14")
        case 15:
            collect_chapter = next(i for i in item_pool if i.name == "progressive chapter 15")
        case 16:
            collect_chapter = next(i for i in item_pool if i.name == "progressive chapter 16")
        
    multiworld.push_precollected(collect_chapter)
    item_pool.remove(collect_chapter)
    
    possible_characters = []
    possible_characters.extend(
        name for name, i in world.item_name_to_item.items() if "character" in i.get("category", [])
    )
    possible_characters.extend(
        name for name, i in world.item_name_to_item.items() if "progressive characters" in i.get("category", [])
    )
    amount_operators = world.options.starting_squad_range
    #helper function. checks if the item is a rarity or progressive rarity.
    #returns true, false if it is a rarity; false, true if it is a progressive rarity; false, false if it is neither
    #true, true should never happen
    def rarity(name_i: str, rarity:str, prog_rarity: str) ->tuple[bool, bool]:
        try:
            next(
                name for name, i in world.item_name_to_item.items() if rarity in i.get("category", []) and name_i in i.get("name", [])
            )
        except:
            #its not a x star, so check if its a progressive item
            try:
                next(
                    name for name, i in world.item_name_to_item.items() if prog_rarity in i.get("category", [])
                )
            except:
                #its not a progressive character or a rarity, so it must be a excluded rarity or not this rarity
                return (False, False)
            else:
                #its a progressive character, so it must be a progressive character
                return (False, True)
        else:
            #it is this rarity
            return (True, False)

    #helper function. determine how many slots are already occupied.
    #higher rarity means more slots are occupied. 6 star = 4 slots, 5 star = 2 slots, 4 star and lower = 1 slot
    def remove_amount(name:str) ->int:
        amount_operators = 0
        detemined_rarity = rarity(name, "6 star", "progressive 6 star")
        #the rarity was 6 star. if not, we continue searching
        if detemined_rarity[0] == True or detemined_rarity[1] == True:
            return 4
        
        detemined_rarity = rarity(name, "5 star", "progressive 5 star")
        #the rarity was 6 star. if not, we continue searching
        if detemined_rarity[0] == True or detemined_rarity[1] == True:
            return 2
        
        detemined_rarity = rarity(name, "4 star", "progressive 4 star")
        #the rarity was 6 star. if not, we continue searching
        if detemined_rarity[0] == True or detemined_rarity[1] == True:
            return 1
        
        detemined_rarity = rarity(name, "low star", "progressive low star")
        #the rarity was 6 star. if not, we continue searching
        if detemined_rarity[0] == True or detemined_rarity[1] == True:
            return 1
        #if it didn't find anything, return 0
        return 0

    while amount_operators > 0:
        if len(possible_characters) <=0:
            #if the length of the possible characters (progressive or ops) smaller than 0
            #then we just break and don't continue, it won't gen even if we want to
            break
        random_character = world.random.choice(possible_characters)
        # print("found operator: " + random_character)
        try:
            remove_character = next(i for i in item_pool if i.name == random_character)
        except:
            #if it didn't find it in item_pool, it should be excluded by a earlier hook
            pass
        else:
            #if it did find in the itempool, we must collect and remove from the itempool
            #also need to determine the rarity to decrement our checked amount
            multiworld.push_precollected(remove_character)
            item_pool.remove(remove_character)
            amount_operators -= remove_amount(random_character)
        finally:
            possible_characters.remove(random_character)
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

    global victory_name 
    # actx bosses are done with 'defeat boss' item. 
    # this means that we only need to force this item to the correct boss
    # and we don't have to change the requirement
    # print("victory name: " + victory_name)
    victory_location = multiworld.get_location(victory_name, player)
    if victory_name != "beat x bosses":
        return None

    def check_boss_amount(state: CollectionState):
        #really simple. just check how many boss amount is collected
        return state.has_group("boss clear", player, world.options.amount_boss)
    def check_OP_amount(state: CollectionState):
        return state.has_group("Originium Prime", player, world.options.originium_prime_hunt)
    match victory_name:
        #really simple. just check how many items is collected
        #also made this a match case statement, because there are 2 different conditions need to be changed
        case "beat x bosses":
            victory_location.access_rule = lambda state: check_boss_amount(state)
        case "collect OP":
            victory_location.access_rule = lambda state: check_OP_amount(state)

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
    boss_locations = []
    placed_item = next(i for i in multiworld.get_items() if i.player == player and "beaten stage" == i.name)
    match victory_name:
        case "boss chapter cleared":
            match world.options.chapter_boss_clear.value:
                case 0:
                    boss_locations.append("0-11 clear")
                case 1:
                    boss_locations.append("1-12 clear")
                case 2:
                    boss_locations.append("2-10 clear")
                case 3:
                    boss_locations.append("3-8 clear")
                case 4:
                    boss_locations.append("4-10 clear")
                case 5:
                    boss_locations.append("5-10 clear")
                case 6:
                    boss_locations.append("6-16 clear")
                case 7:
                    boss_locations.append("7-18 clear")
                case 8:
                    boss_locations.append("JT8-3 clear")
                case 9:
                    boss_locations.append("9-19 clear")
                case 10:
                    boss_locations.append("10-17 clear")
                case 11:
                    boss_locations.append("11-20 clear")
                case 12:
                    boss_locations.append("12-20 clear")
                case 13:
                    boss_locations.append("13-21 clear")
                case 14:
                    boss_locations.append("14-21 clear")
                case 15:
                    boss_locations.append("15-20 clear")
                case 16:
                    boss_locations.append("16-16 clear")
        case "H-stages cleared":
            match world.options.H_stage_clear.value:
                case 5:
                    boss_locations.append("H5-4 clear")
                case 6:
                    boss_locations.append("H6-4 clear")
                case 7:
                    boss_locations.append("H7-4 clear")
                case 8:
                    boss_locations.append("H8-4 clear")
                case 9:
                    boss_locations.append("H9-6 clear")
                case 10:
                    boss_locations.append("H10-3 clear")
                case 11:
                    boss_locations.append("H11-4 clear")
                case 12:
                    boss_locations.append("H12-4 clear")
                case 13:
                    boss_locations.append("H13-4 clear")
                case 14:
                    boss_locations.append("H14-4 clear")
                case 15:
                    boss_locations.append("H15-4 clear")
                case 16:
                    boss_locations.append("H16-4 clear")
        case "beat multiple boss stages":
            placed_item = next(i for i in multiworld.get_items() if i.player == player and "defeated bosses" == i.name)
            boss_locations.extend([name for name, i in world.location_name_to_location.items() if "boss stage" in i.get("category", [])])
        case "collect OP":
            #no need to force place items in collect runs. only needs to remove items, which is done in a different hook (before_create_items_filler)
            return

    # print("boss locations: [%s]" % ", ".join(boss_locations))
    #Force place the 'defeated boss' in the boss_locations just found.
    for location in boss_locations:
        placed_item = next(i for i in multiworld.get_items() if i.player == player and "defeated bosses" == i.name)
        placed_location = multiworld.get_location(location, player)
        placed_location.place_locked_item(placed_item)
        multiworld.itempool.remove(placed_item)

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
