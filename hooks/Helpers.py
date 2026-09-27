from typing import Optional, Any
from BaseClasses import MultiWorld


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    from ..Helpers import get_option_value
    #chapter 0 should be removed if 
    enabled_chapters = get_option_value(multiworld, player, "included_chapters")
    if enabled_chapters is dict:
        print(enabled_chapters)
        if "c0" in enabled_chapters and category_name == "chapter 0":
            return True
        elif "c1" in enabled_chapters and category_name == "chapter 1":
            return True
        elif "c2" in enabled_chapters and category_name == "chapter 2":
            return True
        elif "c3" in enabled_chapters and category_name == "chapter 3":
            return True
        elif "c4" in enabled_chapters and category_name == "chapter 4":
            return True
        elif "c5" in enabled_chapters and category_name == "chapter 5":
            return True
        elif "c6" in enabled_chapters and category_name == "chapter 6":
            return True
        elif "c7" in enabled_chapters and category_name == "chapter 7":
            return True
        elif "c8" in enabled_chapters and category_name == "chapter 8":
            return True
        elif "c9" in enabled_chapters and category_name == "chapter 9":
            return True
        elif "c10" in enabled_chapters and category_name == "chapter 10":
            return True
        elif "c11" in enabled_chapters and category_name == "chapter 11":
            return True
        elif "c12" in enabled_chapters and category_name == "chapter 12":
            return True
        elif "c13" in enabled_chapters and category_name == "chapter 13":
            return True
        elif "c14" in enabled_chapters and category_name == "chapter 14":
            return True
        elif "c15" in enabled_chapters and category_name == "chapter 15":
            return True
        elif "c16" in enabled_chapters and category_name == "chapter 16":
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
        enabled_6_star = get_option_value(multiworld, player, "listing_6_star")
        # print(enabled_6_star)
        return item["name"] in enabled_6_star if get_option_value(multiworld, player, "blacklist_or_whitelist_operators") else not item["name"] in enabled_6_star
    if "5 star" in item["category"]:
        enabled_5_star = get_option_value(multiworld, player, "listing_5_star")
        return item["name"] in enabled_5_star if get_option_value(multiworld, player, "blacklist_or_whitelist_operators") else not item["name"] in enabled_5_star
    if "4 star" in item["category"]:
        enabled_4_star = get_option_value(multiworld, player, "listing_4_star")
        return item["name"] in enabled_4_star if get_option_value(multiworld, player, "blacklist_or_whitelist_operators") else not item["name"] in enabled_4_star
    if "3 star" in item["category"]:
        enabled_3_star = get_option_value(multiworld, player, "listing_3_star")
        return item["name"] in enabled_3_star if get_option_value(multiworld, player, "blacklist_or_whitelist_operators") else not item["name"] in enabled_3_star
    if "2 star" in item["category"]:
        enabled_low_star = get_option_value(multiworld, player, "listing_low_star")
        return item["name"] in enabled_low_star if get_option_value(multiworld, player, "blacklist_or_whitelist_operators") else not item["name"] in enabled_low_star
    
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:

    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
