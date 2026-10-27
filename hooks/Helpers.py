from typing import Optional, Any
from BaseClasses import MultiWorld
# calling logging.info("message") anywhere below in this file will output the message to both console and log file
import logging

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    from .World import included_chapters
    
    #seems like this function is only called for the locations. 
    if category_name == "chapter 0" and "chapter 0" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "chapter 1" and "chapter 1" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "chapter 2" and "chapter 2" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "chapter 3" and "chapter 3" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "chapter 4" and "chapter 4" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "chapter 5" and "chapter 5" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "chapter 6" and "chapter 6" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "chapter 7" and "chapter 7" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "chapter 8" and "chapter 8" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "chapter 9" and "chapter 9" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "chapter 10" and "chapter 10" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "chapter 11" and "chapter 11" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "chapter 12" and "chapter 12" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "chapter 13" and "chapter 13" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "chapter 14" and "chapter 14" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "chapter 15" and "chapter 15" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "chapter 16" and "chapter 16" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Darknights memoir" and "Darknights memoir" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "A Walk in the Dust" and "A Walk in the Dust" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Babel" and "Babel" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Ending a Grand Overture" and "Ending a Grand Overture" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Guide Ahead" and "Guide Ahead" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Hortus de Escapismo" and "Hortus de Escapismo" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Break the Ice" and "Break the Ice" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "The Rides to Lake Silberneherze" and "The Rides to Lake Silberneherze" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Il Siracusan" and "Il Siracusan" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Maria Nearl" and "Maria Nearl" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Near Light" and "Near Light" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Who is Real" and "Who is Real" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Invitation to Wine" and "Invitation to Wine" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Where the Vernal Winds Will Never Blow" and "Where the Vernal Winds Will Never Blow" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Here a People Sows" and "Here a People Sows" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Such is the Joy of Our Reunion" and "Such is the Joy of Our Reunion" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Mansfield Break" and "Mansfield Break" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Dorothy's Vision" and "Dorothy's Vision" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Lonetrail" and "Lonetrail" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Grani And The Knights' Treasure" and "Grani And The Knights' Treasure" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Under Tides" and "Under Tides" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Stultifera Navis" and "Stultifera Navis" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Path of Life" and "Path of Life" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Exodus From the Pale Sea" and "Exodus From the Pale Sea" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Twilight of Wolumonde" and "Twilight of Wolumonde" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Lingering Echoes" and "Lingering Echoes" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Zwillingstürme im Herbst" and "Zwillingstürme im Herbst" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "When the Fireflights Casts" and "When the Fireflights Casts" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "When Elegies Are Ashes" and "When Elegies Are Ashes" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Heart of Surging Flame" and "Heart of Surging Flame" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Gavial the Great Chief Returns" and "Gavial the Great Chief Returns" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Dossoles Holiday" and "Dossoles Holiday" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Ideal City" and "Ideal City" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "So long Adele" and "So long Adele" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    if category_name == "Adventure That Cannot Wait for the Sun" and "Adventure That Cannot Wait for the Sun" not in included_chapters:
        logging.info(f"{category_name} is being removed")
        return False
    # items can't be removed from this hook
    # if "6 star" == category_name and get_option_value(multiworld, player, "include_6_stars") != 0:
    #     return False
    # if "5 star" == category_name and get_option_value(multiworld, player, "include_5_stars") != 0:
    #     return False
    # if "4 star" == category_name and get_option_value(multiworld, player, "include_4_stars") != 0:
    #     return False
    # if "3 star" == category_name and get_option_value(multiworld, player, "include_3_stars") != 0:
    #     return False
    # if "2 star" == category_name and get_option_value(multiworld, player, "include_2_stars") != 0:
    #     return False
    # if "1 star" == category_name and get_option_value(multiworld, player, "include_1_stars") != 0:
    #     return False
    # if "OP hunt" == category_name and get_option_value(multiworld, player, "goal") != 3:
    #     return False
    # if "stage clear" == category_name and get_option_value(multiworld, player, "goal") not in (0, 1):
    #     return False
    # if "defeated bosses goal" == category_name and get_option_value(multiworld, player, "goal") != 2:
    #     return False
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    # from .World import included_chapters
    # logging.info(included_chapters)
    # Remove unwanted champions from the item pool
    from ..Helpers import get_option_value
    from .World import included_chapters
    if "chapter 0" == item["category"] and "chapter 0" not in included_chapters:
        return False
    if "chapter 1" == item["category"] and "chapter 1" not in included_chapters:
        return False
    if "chapter 2" == item["category"] and "chapter 2" not in included_chapters:
        return False
    if "chapter 3" == item["category"] and "chapter 3" not in included_chapters:
        return False
    if "chapter 4" == item["category"] and "chapter 4" not in included_chapters:
        return False
    if "chapter 5" == item["category"] and "chapter 5" not in included_chapters:
        return False
    if "chapter 6" == item["category"] and "chapter 6" not in included_chapters:
        return False
    if "chapter 7" == item["category"] and "chapter 7" not in included_chapters:
        return False
    if "chapter 8" == item["category"] and "chapter 8" not in included_chapters:
        return False
    if "chapter 9" == item["category"] and "chapter 9" not in included_chapters:
        return False
    if "chapter 10" == item["category"] and "chapter 10" not in included_chapters:
        return False
    if "chapter 11" == item["category"] and "chapter 11" not in included_chapters:
        return False
    if "chapter 12" == item["category"] and "chapter 12" not in included_chapters:
        return False
    if "chapter 13" == item["category"] and "chapter 13" not in included_chapters:
        return False
    if "chapter 14" == item["category"] and "chapter 14" not in included_chapters:
        return False
    if "chapter 15" == item["category"] and "chapter 15" not in included_chapters:
        return False
    if "chapter 16" == item["category"] and "chapter 16" not in included_chapters:
        return False
    if "Darknights memoir"  == item["category"]and "Darknights memoir" not in included_chapters:
        return False
    if "A Walk in the Dust" == item["category"] and "A Walk in the Dust" not in included_chapters:
        return False
    if "Babel" == item["category"] and "Babel" not in included_chapters:
        return False
    if "Ending a Grand Overture" == item["category"] and "Ending a Grand Overture" not in included_chapters:
        return False
    if "Guide Ahead" == item["category"] and "Guide Ahead" not in included_chapters:
        return False
    if "Hortus de Escapismo" == item["category"] and "Hortus de Escapismo" not in included_chapters:
        return False
    if "Break the Ice" == item["category"] and "Break the Ice" not in included_chapters:
        return False
    if "The Rides to Lake Silberneherze" == item["category"] and "The Rides to Lake Silberneherze" not in included_chapters:
        return False
    if "Il Siracusan" == item["category"] and "Il Siracusan" not in included_chapters:
        return False
    if "Maria Nearl" == item["category"] and "Maria Nearl" not in included_chapters:
        return False
    if "Near Light" == item["category"] and "Near Light" not in included_chapters:
        return False
    if "Who is Real" == item["category"] and "Who is Real" not in included_chapters:
        return False
    if "Invitation to Wine" == item["category"] and "Invitation to Wine" not in included_chapters:
        return False
    if "Where the Vernal Winds Will Never Blow" == item["category"] and "Where the Vernal Winds Will Never Blow" not in included_chapters:
        return False
    if "Here a People Sows" and "Here a People Sows" == item["category"] not in included_chapters:
        return False
    if "Such is the Joy of Our Reunion" == item["category"] and "Such is the Joy of Our Reunion" not in included_chapters:
        return False
    if "Mansfield Break" == item["category"] and "Mansfield Break" not in included_chapters:
        return False
    if "Dorothy's Vision" == item["category"] and "Dorothy's Vision" not in included_chapters:
        return False
    if "Lonetrail" == item["category"] and "Lonetrail" not in included_chapters:
        return False
    if "Grani And The Knights' Treasure" == item["category"] and "Grani And The Knights' Treasure" not in included_chapters:
        return False
    if "Under Tides" == item["category"] and "Under Tides" not in included_chapters:
        return False
    if "Stultifera Navis" == item["category"] and "Stultifera Navis" not in included_chapters:
        return False
    if "Path of Life" == item["category"] and "Path of Life" not in included_chapters:
        return False
    if "Exodus From the Pale Sea" == item["category"] and "Exodus From the Pale Sea" not in included_chapters:
        return False
    if "Twilight of Wolumonde" == item["category"] and "Twilight of Wolumonde" not in included_chapters:
        return False
    if "Lingering Echoes" == item["category"] and "Lingering Echoes" not in included_chapters:
        return False
    if "Zwillingstürme im Herbst" == item["category"] and "Zwillingstürme im Herbst" not in included_chapters:
        return False
    if "When the Fireflights Casts"  == item["category"] and "When the Fireflights Casts" not in included_chapters:
        return False
    if "When Elegies Are Ashes" == item["category"] and "When Elegies Are Ashes" not in included_chapters:
        return False
    if "Heart of Surging Flame" == item["category"] and "Heart of Surging Flame" not in included_chapters:
        return False
    if "Gavial the Great Chief Returns" == item["category"] and "Gavial the Great Chief Returns" not in included_chapters:
        return False
    if "Dossoles Holiday" == item["category"] and "Dossoles Holiday" not in included_chapters:
        return False
    if "Ideal City" == item["category"] and "Ideal City" not in included_chapters:
        return False
    if "So long Adele" == item["category"] and "So long Adele" not in included_chapters:
        return False
    if "Adventure That Cannot Wait for the Sun" == item["category"] and "Adventure That Cannot Wait for the Sun" not in included_chapters:
        return False

    if "defeated bosses" == item["name"] and get_option_value(multiworld, player, "goal") not in (0, 1, 4, 5):
        return False
    if "beaten stage" == item["category"] and get_option_value(multiworld, player, "goal") != 2:
        return False
    if "OP hunt" == item["category"] and get_option_value(multiworld, player, "goal") != 3:
        return False

    #remove the operator
    if "6 star" in item["category"]:
        if get_option_value(multiworld, player, "include_6_stars") != 0:
            return False
        list_6_star = get_option_value(multiworld, player, "list_6_star")
        return item["name"] in list_6_star if get_option_value(multiworld, player, "black_or_whitelist") else not item["name"] in list_6_star
    if "5 star" in item["category"]:
        if get_option_value(multiworld, player, "include_5_stars") != 0:
            return False
        list_5_star = get_option_value(multiworld, player, "list_5_star")
        return item["name"] in list_5_star if get_option_value(multiworld, player, "black_or_whitelist") else not item["name"] in list_5_star
    if "4 star" in item["category"]:
        if get_option_value(multiworld, player, "include_4_stars") != 0:
            return False
        list_4_star = get_option_value(multiworld, player, "list_4_star")
        return item["name"] in list_4_star if get_option_value(multiworld, player, "black_or_whitelist") else not item["name"] in list_4_star
    if "3 star" in item["category"]:
        if get_option_value(multiworld, player, "include_3_stars") != 0:
            return False
        list_3_star = get_option_value(multiworld, player, "list_3_star")
        return item["name"] in list_3_star if get_option_value(multiworld, player, "black_or_whitelist") else not item["name"] in list_3_star
    if "2 star" in item["category"]:
        if get_option_value(multiworld, player, "include_2_stars") != 0:
            return False
        list_2_star = get_option_value(multiworld, player, "list_2_star")
        return item["name"] in list_2_star if get_option_value(multiworld, player, "black_or_whitelist") else not item["name"] in list_2_star
    if "1 star" in item["category"]:
        if get_option_value(multiworld, player, "include_1_stars") != 0:
            return False
        list_1_star = get_option_value(multiworld, player, "list_1_star")
        return item["name"] in list_1_star if get_option_value(multiworld, player, "black_or_whitelist") else not item["name"] in list_1_star
    if "progressive 6 star" == item["name"] and get_option_value(multiworld, player, "include_6_stars") != 1:
        return False
    if "progressive 5 star" == item["name"] and get_option_value(multiworld, player, "include_5_stars") != 1:
        return False
    if "progressive 4 star" == item["name"] and get_option_value(multiworld, player, "include_4_stars") != 1:
        return False
    if "progressive 3 star" == item["name"] and get_option_value(multiworld, player, "include_3_stars") != 1:
        return False
    if "progressive 2 star" == item["name"] and get_option_value(multiworld, player, "include_2_stars") != 1:
        return False
    if "progressive 1 star" == item["name"] and get_option_value(multiworld, player, "include_1_stars") != 1:
        return False
    if "Originium Prime" == item["name"] and get_option_value(multiworld, player, "goal") != 3:
        return False
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:

    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
