from typing import Optional, Any
from BaseClasses import MultiWorld


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    # Remove unwanted champions from the item pool
    from ..Helpers import get_option_value
    if "6 star" in item["category"]:
        enabled_6_star = get_option_value(multiworld, player, "listing_6_star")
        # print(enabled_6_star)
        if get_option_value(multiworld, player, "blacklist_or_whitelist_operators"):
            result = item["name"] in enabled_6_star # True if they're in the yaml, false if they're not, # 0 if not found
            if result == 0:
                #if the unit isn't found, just return true (saying the unit should be included) to guarantee that it gens. 
                print("can't find the option")
                return True 
            return result  # True if they're in the yaml, false if they're not
        else: 
            return not (item["name"] in enabled_6_star)
    if "5 star" in item["category"]:
        enabled_5_star = get_option_value(multiworld, player, "listing_5_star")
        if get_option_value(multiworld, player, "blacklist_or_whitelist_operators"):
            result = item["name"] in enabled_5_star # True if they're in the yaml, false if they're not, # 0 if not found
            if result == 0:
                #if the unit isn't found, just return true (saying the unit should be included) to guarantee that it gens. 
                print("can't find the option")
                return True 
            return result  # True if they're in the yaml, false if they're not
        else: 
            return not (item["name"] in enabled_5_star)
    if "4 star" in item["category"]:
        enabled_4_star = get_option_value(multiworld, player, "listing_4_star")
        if get_option_value(multiworld, player, "blacklist_or_whitelist_operators"):
            result = item["name"] in enabled_4_star # True if they're in the yaml, false if they're not, # 0 if not found
            if result == 0:
                #if the unit isn't found, just return true (saying the unit should be included) to guarantee that it gens. 
                print("can't find the option")
                return True 
            return result  # True if they're in the yaml, false if they're not
        else: 
            return not (item["name"] in enabled_4_star)
    if "3 star" in item["category"]:
        enabled_3_star = get_option_value(multiworld, player, "listing_3_star")
        if get_option_value(multiworld, player, "blacklist_or_whitelist_operators"):
            result = item["name"] in enabled_3_star # True if they're in the yaml, false if they're not, # 0 if not found
            if result == 0:
                #if the unit isn't found, just return true (saying the unit should be included) to guarantee that it gens. 
                print("can't find the option")
                return True 
            return result  # True if they're in the yaml, false if they're not
        else: 
            return not (item["name"] in enabled_3_star)
    if "low star" in item["category"]:
        enabled_low_star = get_option_value(multiworld, player, "listing_low_star")
        if get_option_value(multiworld, player, "blacklist_or_whitelist_operators"):
            result = item["name"] in enabled_low_star # True if they're in the yaml, false if they're not, # 0 if not found
            if result == 0:
                #if the unit isn't found, just return true (saying the unit should be included) to guarantee that it gens. 
                print("can't find the option")
                return True 
            return result  # True if they're in the yaml, false if they're not
        else: 
            return not (item["name"] in enabled_low_star)

    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    from ..Helpers import get_option_value
    #chapter 0 should be removed if 
    enabled_chapters = get_option_value(multiworld, player, "included_chapters")
    if enabled_chapters is dict:
        print(enabled_chapters)
        if "c0" in enabled_chapters:
            if "chapter 0" in location["category"]:
                return True
            else:
                return False
        elif "c1" in enabled_chapters:
            if "chapter 1" in location["category"]:
                return True
            else:
                return False
        elif "c2" in enabled_chapters:
            if "chapter 2" in location["category"]:
                return True
            else:
                return False
        elif "c3" in enabled_chapters:
            if "chapter 3" in location["category"]:
                return True
            else:
                return False
        elif "c4" in enabled_chapters:
            if "chapter 4" in location["category"]:
                return True
            else:
                return False
        elif "c5" in enabled_chapters:
            if "chapter 5" in location["category"]:
                return True
            else:
                return False
        elif "c6" in enabled_chapters:
            if "chapter 6" in location["category"]:
                return True
            else:
                return False
        elif "c7" in enabled_chapters:
            if "chapter 7" in location["category"]:
                return True
            else:
                return False
        elif "c8" in enabled_chapters:
            if "chapter 8" in location["category"]:
                return True
            else:
                return False
        elif "c9" in enabled_chapters:
            if "chapter 9" in location["category"]:
                return True
            else:
                return False
        elif "c10" in enabled_chapters:
            if "chapter 10" in location["category"]:
                return True
            else:
                return False
        elif "c11" in enabled_chapters:
            if "chapter 11" in location["category"]:
                return True
            else:
                return False
        elif "c12" in enabled_chapters:
            if "chapter 12" in location["category"]:
                return True
            else:
                return False
        elif "c13" in enabled_chapters:
            if "chapter 13" in location["category"]:
                return True
            else:
                return False
        elif "c14" in enabled_chapters:
            if "chapter 14" in location["category"]:
                return True
            else:
                return False
        elif "c15" in enabled_chapters:
            if "chapter 15" in location["category"]:
                return True
            else:
                return False
        elif "c16" in enabled_chapters:
            if "chapter 16" in location["category"]:
                return True
            else:
                return False
        else:
            return False
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
