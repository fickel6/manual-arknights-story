from typing import Optional, Any
from BaseClasses import MultiWorld

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    from .World import included_chapters
    from ..Helpers import get_option_value
    #chapter 0 should be removed if 
    enabled_chapters = get_option_value(multiworld, player, "included_chapters")
    if enabled_chapters is dict:
        print(enabled_chapters)
        if category_name == "chapter 0" and "c0" in enabled_chapters and "0" in included_chapters:
            return True
        elif category_name == "chapter 1" and "c1" in enabled_chapters and "1" in included_chapters:
            return True
        elif category_name == "chapter 2" and "c2" in enabled_chapters and "2" in included_chapters:
            return True
        elif category_name == "chapter 3" and "c3" in enabled_chapters and "3" in included_chapters:
            return True
        elif category_name == "chapter 4" and "c4" in enabled_chapters and "4" in included_chapters:
            return True
        elif category_name == "chapter 5" and "c5" in enabled_chapters and "5" in included_chapters:
            return True
        elif category_name == "chapter 6" and "c6" in enabled_chapters and "6" in included_chapters:
            return True
        elif category_name == "chapter 7" and "c7" in enabled_chapters and "7" in included_chapters:
            return True
        elif category_name == "chapter 8" and "c8" in enabled_chapters and "8" in included_chapters:
            return True
        elif category_name == "chapter 9" and "c9" in enabled_chapters and "9" in included_chapters:
            return True
        elif category_name == "chapter 10" and "c10" in enabled_chapters and "10" in included_chapters:
            return True
        elif category_name == "chapter 11" and "c11" in enabled_chapters and "11" in included_chapters:
            return True
        elif category_name == "chapter 12" and "c12" in enabled_chapters and "12" in included_chapters:
            return True
        elif category_name == "chapter 13" and "c13" in enabled_chapters and "13" in included_chapters:
            return True
        elif category_name == "chapter 14" and "c14" in enabled_chapters and "14" in included_chapters:
            return True
        elif category_name == "chapter 15" and "c15" in enabled_chapters and "15" in included_chapters:
            return True
        elif category_name == "chapter 16" and "c16" in enabled_chapters and "16" in included_chapters:
            return True
    elif "6 star" == category_name and get_option_value(multiworld, player, "include_6_stars") != 0:
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
    elif "defeated bosses" == category_name:
        if get_option_value(multiworld, player, "The End Objective") == 2:
            return True
        else:
            return False
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
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
        # print(list_6_star)
        return item["name"] in list_6_star if get_option_value(multiworld, player, "blacklist_or_whitelist_operators") else not item["name"] in list_6_star
    if "5 star" in item["category"]:
        list_5_star = get_option_value(multiworld, player, "list_5_star")
        return item["name"] in list_5_star if get_option_value(multiworld, player, "blacklist_or_whitelist_operators") else not item["name"] in list_5_star
    if "4 star" in item["category"]:
        list_4_star = get_option_value(multiworld, player, "list_4_star")
        return item["name"] in list_4_star if get_option_value(multiworld, player, "blacklist_or_whitelist_operators") else not item["name"] in list_4_star
    if "3 star" in item["category"]:
        list_3_star = get_option_value(multiworld, player, "list_3_star")
        return item["name"] in list_3_star if get_option_value(multiworld, player, "blacklist_or_whitelist_operators") else not item["name"] in list_3_star
    if "2 star" in item["category"]:
        list_2_star = get_option_value(multiworld, player, "list_2_star")
        return item["name"] in list_2_star if get_option_value(multiworld, player, "blacklist_or_whitelist_operators") else not item["name"] in list_2_star
    if "1 star" in item["category"]:
        list_1_star = get_option_value(multiworld, player, "list_1_star")
        return item["name"] in list_1_star if get_option_value(multiworld, player, "blacklist_or_whitelist_operators") else not item["name"] in list_1_star
    
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:

    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
