from typing import Optional, Any
from BaseClasses import MultiWorld
# calling logging.info("message") anywhere below in this file will output the message to both console and log file
import logging

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    from .World import included_chapters
    from ..Helpers import get_option_value
    #seems like this function is only called for the locations. 
    enabled_chapters = get_option_value(multiworld, player, "enabled_chapters")
    if isinstance(enabled_chapters, (set, dict)):
        if category_name == "chapter 0" and "chapter 0" not in included_chapters:
            return False
        if category_name == "chapter 1" and "chapter 1" not in included_chapters:
            return False
        if category_name == "chapter 2" and "chapter 2" not in included_chapters:
            return False
        if category_name == "chapter 3" and "chapter 3" not in included_chapters:
            return False
        if category_name == "chapter 4" and "chapter 4" not in included_chapters:
            return False
        if category_name == "chapter 5" and "chapter 5" not in included_chapters:
            return False
        if category_name == "chapter 6" and "chapter 6" not in included_chapters:
            return False
        if category_name == "chapter 7" and "chapter 7" not in included_chapters:
            return False
        if category_name == "chapter 8" and "chapter 8" not in included_chapters:
            return False
        if category_name == "chapter 9" and "chapter 9" not in included_chapters:
            return False
        if category_name == "chapter 10" and "chapter 10" not in included_chapters:
            return False
        if category_name == "chapter 11" and "chapter 11" not in included_chapters:
            return False
        if category_name == "chapter 12" and "chapter 12" not in included_chapters:
            return False
        if category_name == "chapter 13" and "chapter 13" not in included_chapters:
            return False
        if category_name == "chapter 14" and "chapter 14" not in included_chapters:
            return False
        if category_name == "chapter 15" and "chapter 15" not in included_chapters:
            return False
        if category_name == "chapter 16" and "chapter 16" not in included_chapters:
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
    if "progressive 6 star" == item["name"] and get_option_value(multiworld, player, "include_6_stars") != 1:
        return False
    if "progressive 5 star" == item["name"] and get_option_value(multiworld, player, "include_5_stars") != 1:
        return False
    if "progressive 4 star" == item["name"] and get_option_value(multiworld, player, "include_4_stars") != 1:
        return False
    if "progressive 3 star" == item["name"] and get_option_value(multiworld, player, "include_3_stars") == 1:
        return False
    if "progressive 2 star" == item["name"] and get_option_value(multiworld, player, "include_2_stars") == 1:
        return False
    if "progressive 1 star" == item["name"] and get_option_value(multiworld, player, "include_1_stars") == 1:
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
    
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:

    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
