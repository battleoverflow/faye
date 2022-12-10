"""
    Owner: Stience (https://github.com/stience)
    Project: Faye (https://github.com/stience/faye)

    Author(s): Hifumi1337
"""

class Faye:

    def log(msg: str = "Logger init", level: str = "INFO") -> str:
        """
        Generic logging method

        msg: Logging message
        level: Level message

        rtype: str
        """

        # Checks for empty string parameters
        if level != "" and msg != "":
            return f"[{level}] => {msg}"
        else:
            raise NameError

    def progress(total: int = 0, description: str = ""):
        """
        Progress bar built with tqdm

        total: The length of the progress bar
        description: Description of the progress bar
        """

        from tqdm import tqdm

        # Progress bar configuration
        for p in tqdm(range(total), desc=description):
            pass