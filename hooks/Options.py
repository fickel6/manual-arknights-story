# Object classes from AP that represent different types of options that you can create
from Options import Option, OptionSet, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any
from ..Items import item_name_groups

####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class TotalCharactersToWinWith(Range):
    """Instead of having to beat the game with all characters, you can limit locations to a subset of character victory locations."""
    display_name = "Number of characters to beat the game with before victory"
    range_start = 10
    range_end = 50
    default = 50

class chapters(OptionSet):
    """list for enabling/disabling chapters"""  # Description of the yaml option in the template
    display_name = "included chapters"           # Name of the option in the spoiler
    valid_keys = {  #define my own list to choose included chapters
        "chapter 0": "c0", "chapter 1": "c1", "chapter 2": "c2", "chapter 3": "c3", "chapter 4": "c4", 
        "chapter 5": "c5", "chapter 6": "c6", "chapter 7": "c7", "chapter 8": "c8", "chapter 9": "c9",
        "chapter 10": "c10", "chapter 11": "c11", "chapter 12": "c12", "chapter 13": "c13",
        "chapter 14": "c14", "chapter 15": "c15", "chapter 16": "c16",
    } # This is the bit that matters.  Our yaml option wants you to pick names of items in the Champion category
    default = frozenset(valid_keys)              # This makes the default value list all of them.  It's easier for a player to delete ones they don't have than it is to guess what should be added.
class events(OptionSet):
    """list for enabling/disabling chapters"""  # Description of the yaml option in the template
    display_name = "included chapters"           # Name of the option in the spoiler
    valid_keys = {  #define my own list to choose included chapters
        "chapter 0": "c0", "chapter 1": "c1", "chapter 2": "c2", "chapter 3": "c3", "chapter 4": "c4", 
        "chapter 5": "c5", "chapter 6": "c6", "chapter 7": "c7", "chapter 8": "c8", "chapter 9": "c9",
        "chapter 10": "c10", "chapter 11": "c11", "chapter 12": "c12", "chapter 13": "c13",
        "chapter 14": "c14", "chapter 15": "c15", "chapter 16": "c16",
    } # This is the bit that matters.  Our yaml option wants you to pick names of items in the Champion category
    default = frozenset(valid_keys)              # This makes the default value list all of them.  It's easier for a player to delete ones they don't have than it is to guess what should be added.

class Enabled6Star(OptionSet):
    """enabled 6 star in the manual. only works when 6 star are individual items"""  # Description of the yaml option in the template
    display_name = "Enabled 6 Star Operators"           # Name of the option in the spoiler
    valid_keys = item_name_groups["6 star"]    # This is the bit that matters.  Our yaml option wants you to pick names of items in the Champion category
    default = frozenset(valid_keys)              # This makes the default value list all of them.  It's easier for a player to delete ones they don't have than it is to guess what should be added.

class Enabled5Star(OptionSet):
    """enabled 5 star in the manual. only works when 5 star are individual items"""  # Description of the yaml option in the template
    display_name = "Enabled 5 Star Operators"           # Name of the option in the spoiler
    valid_keys = item_name_groups["5 star"]    # This is the bit that matters.  Our yaml option wants you to pick names of items in the Champion category
    default = frozenset(valid_keys)              # This makes the default value list all of them.  It's easier for a player to delete ones they don't have than it is to guess what should be added.

class Enabled4Star(OptionSet):
    """enabled 4 star in the manual. only works when 4 star are individual items"""  # Description of the yaml option in the template
    display_name = "Enabled 4 Star Operators"           # Name of the option in the spoiler
    valid_keys = item_name_groups["4 star"]    # This is the bit that matters.  Our yaml option wants you to pick names of items in the Champion category
    default = frozenset(valid_keys)              # This makes the default value list all of them.  It's easier for a player to delete ones they don't have than it is to guess what should be added.

class Enabled3Star(OptionSet):
    """enabled 3 star in the manual. only works when 3 star are individual items"""  # Description of the yaml option in the template
    display_name = "Enabled 3 Star Operators"           # Name of the option in the spoiler
    valid_keys = item_name_groups["3 star"]    # This is the bit that matters.  Our yaml option wants you to pick names of items in the Champion category
    default = frozenset(valid_keys)              # This makes the default value list all of them.  It's easier for a player to delete ones they don't have than it is to guess what should be added.

class Enabled2Star(OptionSet):
    """enabled 2 star in the manual. only works when 2 stars are individual items"""  # Description of the yaml option in the template
    display_name = "Enabled 2 Star Operators"           # Name of the option in the spoiler
    valid_keys = item_name_groups["2 star"]    # This is the bit that matters.  Our yaml option wants you to pick names of items in the Champion category
    default = frozenset(valid_keys)              # This makes the default value list all of them.  It's easier for a player to delete ones they don't have than it is to guess what should be added.

class Enabled1Star(OptionSet):
    """enabled 1 star in the manual. only works when 1 stars are individual items"""  # Description of the yaml option in the template
    display_name = "Enabled 1 Star Operators"           # Name of the option in the spoiler
    valid_keys = item_name_groups["1 star"]    # This is the bit that matters.  Our yaml option wants you to pick names of items in the Champion category
    default = frozenset(valid_keys)              # This makes the default value list all of them.  It's easier for a player to delete ones they don't have than it is to guess what should be added.

class randomChapters(Range):
    """amount of chapters will be used for randomization. 
    0 means that all the chapters will be randomized."""
    display_name = "Amount of random chapters"
    range_start = 0
    range_end = 16


# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["included_chapters"] = chapters
    options["included_random_chapters"] = randomChapters

    options["list_6_star"] = Enabled6Star  # This registers the yaml option as `listing_6_star`
    options["list_5_star"] = Enabled5Star  # This registers the yaml option as `listing_5_star`
    options["list_4_star"] = Enabled4Star  # This registers the yaml option as `listing_4_star`
    options["list_3_star"] = Enabled3Star  # This registers the yaml option as `listing_3_star`
    options["list_2_star"] = Enabled2Star  # This registers the yaml option as `listing_4_star`
    options["list_1_star"] = Enabled1Star  # This registers the yaml option as `listing_3_star`
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    # groupname must be different then the options in the json file.
    groups["chapter selection"] = [chapters, randomChapters]
    groups["operator lists"] = [Enabled6Star, Enabled5Star, Enabled4Star, Enabled3Star, Enabled2Star, Enabled1Star]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    # groups.append(OptionGroup("goal options", chapters))
    return groups
