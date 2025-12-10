#!/usr/bin/env python3
"""
Example usage of the colored printing module.
"""

from colored_print import cprint, colored_print

# Basic usage examples
print("=== Basic Color Examples ===")
cprint("This is red text", 'red')
cprint("This is green text", 'green')
cprint("This is blue text", 'blue')

print("\n=== Background Color Examples ===")
cprint("White text with red background", 'white', 'bg_red')
cprint("Black text with yellow background", 'black', 'bg_yellow')

print("\n=== Style Examples ===")
cprint("Bold text", 'yellow', style='bold')
cprint("Underlined text", 'cyan', style='underline')
cprint("Reversed text", 'white', 'bg_black', 'reversed')

print("\n=== Combined Examples ===")
cprint("Error message", 'bright_red', style='bold')
cprint("Success message", 'bright_green', style='bold')
cprint("Warning message", 'bright_yellow', style='bold')
cprint("Info message", 'bright_blue', style='bold')

print("\n=== Direct Function Usage ===")
colored_print("Using the main function directly", color='magenta', style='underline')