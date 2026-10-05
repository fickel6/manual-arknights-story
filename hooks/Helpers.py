from typing import Optional, Any
from BaseClasses import MultiWorld
# calling logging.info("message") anywhere below in this file will output the message to both console and log file
import logging

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    from .World import included_chapters
    from ..Helpers import get_option_value
    #chapter 0 should be removed if 
    # enabled_chapters = get_option_value(multiworld, player, "enabled_chapters")
    # if enabled_chapters is not int:
    #     # logging.info(enabled_chapters)
    #     if category_name == "chapter 0" and "chapter 0" in enabled_chapters and "chapter 0" in included_chapters:
    #         logging.info(f"chapter 0 is included")
    #         return True
    #     elif category_name == "chapter 1" and "chapter 1" in enabled_chapters and "chapter 1" in included_chapters:
    #         logging.info(f"chapter 1 is included")
    #         return True
    #     elif category_name == "chapter 2" and "chapter 2" in enabled_chapters and "chapter 2" in included_chapters:
    #         logging.info(f"chapter 2 is included")
    #         return True
    #     elif category_name == "chapter 3" and "chapter 3" in enabled_chapters and "chapter 3" in included_chapters:
    #         logging.info(f"chapter 3 is included")
    #         return True
    #     elif category_name == "chapter 4" and "chapter 4" in enabled_chapters and "chapter 4" in included_chapters:
    #         logging.info(f"chapter 4 is included")
    #         return True
    #     elif category_name == "chapter 5" and "chapter 5" in enabled_chapters and "chapter 5" in included_chapters:
    #         logging.info(f"chapter 5 is included")
    #         return True
    #     elif category_name == "chapter 6" and "chapter 6" in enabled_chapters and "chapter 6" in included_chapters:
    #         logging.info(f"chapter 6 is included")
    #         return True
    #     elif category_name == "chapter 7" and "chapter 7" in enabled_chapters and "chapter 7" in included_chapters:
    #         logging.info(f"chapter 7 is included")
    #         return True
    #     elif category_name == "chapter 8" and "chapter 8" in enabled_chapters and "chapter 8" in included_chapters:
    #         logging.info(f"chapter 8 is included")
    #         return True
    #     elif category_name == "chapter 9" and "chapter 9" in enabled_chapters and "chapter 9" in included_chapters:
    #         logging.info(f"chapter 9 is included")
    #         return True
    #     elif category_name == "chapter 10" and "chapter 10" in enabled_chapters and "chapter 10" in included_chapters:
    #         logging.info(f"chapter 10 is included")
    #         return True
    #     elif category_name == "chapter 11" and "chapter 11" in enabled_chapters and "chapter 11" in included_chapters:
    #         logging.info(f"chapter 11 is included")
    #         return True
    #     elif category_name == "chapter 12" and "chapter 12" in enabled_chapters and "chapter 12" in included_chapters:
    #         logging.info(f"chapter 12 is included")
    #         return True
    #     elif category_name == "chapter 13" and "chapter 13" in enabled_chapters and "chapter 13" in included_chapters:
    #         logging.info(f"chapter 13 is included")
    #         return True
    #     elif category_name == "chapter 14" and "chapter 14" in enabled_chapters and "chapter 14" in included_chapters:
    #         logging.info(f"chapter 14 is included")
    #         return True
    #     elif category_name == "chapter 15" and "chapter 15" in enabled_chapters and "chapter 15" in included_chapters:
    #         logging.info(f"chapter 15 is included")
    #         return True
    #     elif category_name == "chapter 16" and "chapter 16" in enabled_chapters and "chapter 16" in included_chapters:
    #         logging.info(f"chapter 16 is included")
    #         return True
    # elif "6 star" == category_name and get_option_value(multiworld, player, "include_6_stars") != 0:
    if "6 star" == category_name and get_option_value(multiworld, player, "include_6_stars") != 0:
        return False
    elif "5 star" == category_name and get_option_value(multiworld, player, "include_5_stars") != 0:
        return False
    elif "4 star" == category_name and get_option_value(multiworld, player, "include_4_stars") != 0:
        return False
    elif "3 star" == category_name and get_option_value(multiworld, player, "include_3_stars") != 0:
        return False
    elif "2 star" == category_name and get_option_value(multiworld, player, "include_6_stars") != 0:
        return False
    elif "1 star" == category_name and get_option_value(multiworld, player, "include_6_stars") != 0:
        return False
    elif "progressive squad size" == category_name:
        if get_option_value(multiworld, player, "squad_size_sanity") == 0:
            return False
        else:
            return True
    elif "OP hunt" == category_name:
        if get_option_value(multiworld, player, "The End Objective") == 3:
            return True
        else:
            return False
    elif "stage clear" == category_name:
        if get_option_value(multiworld, player, "The End Objective") in (0, 1):
            return True
        else:
            return False
    elif "defeated bosses goal" == category_name:
        print("removed boss items")
        if get_option_value(multiworld, player, "The End Objective") == 2:
            return True
        else:
            return False
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    # from .World import included_chapters
    # logging.info(included_chapters)
    # Remove unwanted champions from the item pool
    from ..Helpers import get_option_value
    if "progressive 6 star" == item["name"]:
        if get_option_value(multiworld, player, "include_6_stars") == 1:
            return True
        return False
    if "progressive 5 star" == item["name"]:
        if get_option_value(multiworld, player, "include_5_stars") == 1:
            return True
        return False
    if "progressive 4 star" == item["name"]:
        if get_option_value(multiworld, player, "include_4_stars") == 1:
            return True
        return False
    if "progressive 3 star" == item["name"]:
        if get_option_value(multiworld, player, "include_3_stars") == 1:
            return True
        return False
    if "progressive 2 star" == item["name"]:
        if get_option_value(multiworld, player, "include_2_stars") == 1:
            return True
        return False
    if "progressive 1 star" == item["name"]:
        if get_option_value(multiworld, player, "include_1_stars") == 1:
            return True
        return False

    #remove the operator
    if "6 star" in item["category"]:
        list_6_star = get_option_value(multiworld, player, "list_6_star")
        return item["name"] in list_6_star if get_option_value(multiworld, player, "black_or_white") else not item["name"] in list_6_star
    if "5 star" in item["category"]:
        list_5_star = get_option_value(multiworld, player, "list_5_star")
        return item["name"] in list_5_star if get_option_value(multiworld, player, "black_or_white") else not item["name"] in list_5_star
    if "4 star" in item["category"]:
        list_4_star = get_option_value(multiworld, player, "list_4_star")
        return item["name"] in list_4_star if get_option_value(multiworld, player, "black_or_white") else not item["name"] in list_4_star
    if "3 star" in item["category"]:
        list_3_star = get_option_value(multiworld, player, "list_3_star")
        return item["name"] in list_3_star if get_option_value(multiworld, player, "black_or_white") else not item["name"] in list_3_star
    if "2 star" in item["category"]:
        list_2_star = get_option_value(multiworld, player, "list_2_star")
        return item["name"] in list_2_star if get_option_value(multiworld, player, "black_or_white") else not item["name"] in list_2_star
    if "1 star" in item["category"]:
        list_1_star = get_option_value(multiworld, player, "list_1_star")
        return item["name"] in list_1_star if get_option_value(multiworld, player, "black_or_white") else not item["name"] in list_1_star
    
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    from .World import included_chapters
    if "chapter 0" in location["category"] and "chapter 0" not in included_chapters:
        return False
    elif "chapter 1" in location["category"] and "chapter 1" not in included_chapters:
        return False
    elif "chapter 2" in location["category"] and "chapter 2" not in included_chapters:
        return False
    elif "chapter 3" in location["category"] and "chapter 3" not in included_chapters:
        return False
    elif "chapter 4" in location["category"] and "chapter 4" not in included_chapters:
        return False
    elif "chapter 5" in location["category"] and "chapter 5" not in included_chapters:
        return False
    elif "chapter 6" in location["category"] and "chapter 6" not in included_chapters:
        return False
    elif "chapter 7" in location["category"] and "chapter 7" not in included_chapters:
        return False
    elif "chapter 8" in location["category"] and "chapter 8" not in included_chapters:
        return False
    elif "chapter 9" in location["category"] and "chapter 9" not in included_chapters:
        return False
    elif "chapter 10" in location["category"] and "chapter 10" not in included_chapters:
        return False
    elif "chapter 11" in location["category"] and "chapter 11" not in included_chapters:
        return False
    elif "chapter 12" in location["category"] and "chapter 12" not in included_chapters:
        return False
    elif "chapter 13" in location["category"] and "chapter 13" not in included_chapters:
        return False
    elif "chapter 14" in location["category"] and "chapter 14" not in included_chapters:
        return False
    elif "chapter 15" in location["category"] and "chapter 15" not in included_chapters:
        return False
    elif "chapter 16" in location["category"] and "chapter 16" not in included_chapters:
        return False
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
