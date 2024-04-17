"""
    Project: Faye (https://github.com/battleoverflow/faye)
    Author: battleoverflow (https://github.com/battleoverflow)
    License: BSD 2-Clause
"""

class Faye:
    def log(msg = "Logger init", level = None, color = False):
        """
        Generic logging method that allows the user to set a message and log level.
        
        msg (str): Log message
        
        level (str): Allows for a custom level, but a set list with colors are also available

        Levels:

        - TRACE (0)
        - DEBUG (1)
        - INFO (2)
        - WARNING (3)
        - ERROR (4)
        - CRITICAL (5)

        @rtype: str
        """

        level_db = [
            "TRACE",
            "DEBUG",
            "INFO",
            "WARNING",
            "ERROR",
            "CRITICAL"
        ]

        # Checks for empty string parameters
        if msg != "":
            if level in level_db or level in [0, 1, 2, 3, 4, 5]:
                # Sets color defaults
                if color:
                    from colorama import Fore, Style
                    
                    if level in ["ERROR", "CRITICAL", 4, 5]:
                        if level == 4:
                            level = "ERROR"
                        elif level == 5:
                            level = "CRITICAL"
                        
                        color_choice = Fore.RED
                    elif level in ["INFO", 2]:
                        if level == 2:
                            level = "INFO"

                        color_choice = Fore.GREEN
                    elif level in ["WARNING", 3]:
                        if level == 3:
                            level = "WARNING"

                        color_choice = Fore.YELLOW
                    elif level in ["DEBUG", "TRACE", 0, 1]:
                        if level == 0:
                            level = "DEBUG"
                        elif level == 1:
                            level = "TRACE"

                        color_choice = Fore.BLUE

                    try:
                        return  f"[{color_choice + level + Style.RESET_ALL}] => {msg}"
                    except UnboundLocalError:
                        return f"[{level}] => {msg}"
                else:
                    return f"[{level}] => {msg}"
            else:
                return f"[{level}] => {msg}"
        else:
            raise NameError

    def progress(total = 0, description = ""):
        """
        Simple progress bar built with tqdm to allow quick terminal visualization.

        total (int): The total length of the progress bar

        description (str): Description to display aside the progress bar

        @rtype: None
        """

        from tqdm import tqdm

        # Progress bar configuration
        for _ in tqdm(range(total), desc=description):
            pass
