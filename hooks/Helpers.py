from typing import Optional, Any
from BaseClasses import MultiWorld


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    from ..Helpers import get_option_value
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    from ..Helpers import get_option_value
    #chapter 0 should be removed if 
    enabled_chapters = get_option_value(multiworld, player, "included_chapters")
    if enabled_chapters == "c0":
        if "chapter 0" in location["category"]:
            return True
        else:
            return False
    if enabled_chapters == "c0":
        if "chapter 0" in location["category"]:
            return True
        else:
            return False
    if enabled_chapters == "c0":
        if "chapter 0" in location["category"]:
            return True
        else:
            return False
    if enabled_chapters == "c0":
        if "chapter 0" in location["category"]:
            return True
        else:
            return False
    if enabled_chapters == "c0":
        if "chapter 0" in location["category"]:
            return True
        else:
            return False
    if enabled_chapters == "c0":
        if "chapter 0" in location["category"]:
            return True
        else:
            return False
    if enabled_chapters == "c0":
        if "chapter 0" in location["category"]:
            return True
        else:
            return False
    if enabled_chapters == "c0":
        if "chapter 0" in location["category"]:
            return True
        else:
            return False
    if enabled_chapters == "c0":
        if "chapter 0" in location["category"]:
            return True
        else:
            return False
    if enabled_chapters == "c0":
        if "chapter 0" in location["category"]:
            return True
        else:
            return False
    if enabled_chapters == "c0":
        if "chapter 0" in location["category"]:
            return True
        else:
            return False
    if enabled_chapters == "c0":
        if "chapter 0" in location["category"]:
            return True
        else:
            return False
    if enabled_chapters == "c0":
        if "chapter 0" in location["category"]:
            return True
        else:
            return False
    if enabled_chapters == "c0":
        if "chapter 0" in location["category"]:
            return True
        else:
            return False
    if enabled_chapters == "c0":
        if "chapter 0" in location["category"]:
            return True
        else:
            return False
    if enabled_chapters == "c0":
        if "chapter 0" in location["category"]:
            return True
        else:
            return False
    if enabled_chapters == "c0":
        if "chapter 0" in location["category"]:
            return True
        else:
            return False
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
