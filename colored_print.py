#!/usr/bin/env python3
"""
Module for colored printing to the terminal.
Provides functions to print text with various colors and styles.
"""

class Colors:
    """ANSI color codes for terminal text formatting."""
    
    # Text colors
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BLACK = '\033[30m'
    
    # Bright colors
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    
    # Background colors
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSED = '\033[7m'
    
    # Reset formatting
    RESET = '\033[0m'


def colored_print(text, color=None, bg_color=None, style=None, end='\n'):
    """
    Print text with specified color and formatting.
    
    Args:
        text (str): The text to print
        color (str): Foreground color (e.g., 'red', 'green', 'blue')
        bg_color (str): Background color (e.g., 'bg_red', 'bg_green')
        style (str): Style (e.g., 'bold', 'underline', 'reversed')
        end (str): String appended after the last value, default is newline
    """
    color_code = ''
    
    # Map color names to ANSI codes
    color_map = {
        'red': Colors.RED,
        'green': Colors.GREEN,
        'yellow': Colors.YELLOW,
        'blue': Colors.BLUE,
        'magenta': Colors.MAGENTA,
        'cyan': Colors.CYAN,
        'white': Colors.WHITE,
        'black': Colors.BLACK,
        'bright_red': Colors.BRIGHT_RED,
        'bright_green': Colors.BRIGHT_GREEN,
        'bright_yellow': Colors.BRIGHT_YELLOW,
        'bright_blue': Colors.BRIGHT_BLUE,
        'bright_magenta': Colors.BRIGHT_MAGENTA,
        'bright_cyan': Colors.BRIGHT_CYAN,
    }
    
    # Map background color names to ANSI codes
    bg_color_map = {
        'bg_red': Colors.BG_RED,
        'bg_green': Colors.BG_GREEN,
        'bg_yellow': Colors.BG_YELLOW,
        'bg_blue': Colors.BG_BLUE,
        'bg_magenta': Colors.BG_MAGENTA,
        'bg_cyan': Colors.BG_CYAN,
        'bg_white': Colors.BG_WHITE,
    }
    
    # Map style names to ANSI codes
    style_map = {
        'bold': Colors.BOLD,
        'underline': Colors.UNDERLINE,
        'reversed': Colors.REVERSED,
    }
    
    # Apply color if specified
    if color and color.lower() in color_map:
        color_code += color_map[color.lower()]
    
    # Apply background color if specified
    if bg_color and bg_color.lower() in bg_color_map:
        color_code += bg_color_map[bg_color.lower()]
    
    # Apply style if specified
    if style and style.lower() in style_map:
        color_code += style_map[style.lower()]
    
    # Print the colored text
    print(f"{color_code}{text}{Colors.RESET}", end=end)


def cprint(text, color='white', bg_color=None, style=None, end='\n'):
    """
    Convenience function for colored printing.
    
    Args:
        text (str): The text to print
        color (str): Foreground color (default: white)
        bg_color (str): Background color
        style (str): Style (e.g., 'bold', 'underline')
        end (str): String appended after the last value, default is newline
    """
    colored_print(text, color=color, bg_color=bg_color, style=style, end=end)


# Example usage and demonstration
if __name__ == "__main__":
    print("Demonstration of colored printing:")
    
    # Basic colors
    cprint("Red text", 'red')
    cprint("Green text", 'green')
    cprint("Yellow text", 'yellow')
    cprint("Blue text", 'blue')
    cprint("Magenta text", 'magenta')
    cprint("Cyan text", 'cyan')
    cprint("White text", 'white')
    
    print()
    
    # Bright colors
    cprint("Bright red text", 'bright_red')
    cprint("Bright green text", 'bright_green')
    cprint("Bright yellow text", 'bright_yellow')
    cprint("Bright blue text", 'bright_blue')
    cprint("Bright magenta text", 'bright_magenta')
    cprint("Bright cyan text", 'bright_cyan')
    
    print()
    
    # With backgrounds
    cprint("Red text on yellow background", 'red', 'bg_yellow')
    cprint("White text on blue background", 'white', 'bg_blue')
    cprint("Black text on white background", 'black', 'bg_white')
    
    print()
    
    # With styles
    cprint("Bold red text", 'red', style='bold')
    cprint("Underlined blue text", 'blue', style='underline')
    cprint("Reversed text", 'white', 'bg_black', 'reversed')
    
    print()
    
    # Combined examples
    cprint("Bold yellow on red background", 'bright_yellow', 'bg_red', 'bold')
    cprint("Underlined cyan text", 'cyan', style='underline')