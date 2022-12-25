"""
    Owner: Hifumi1337 (https://github.com/hifumi1337)
    Project: Faye
    License: BSD 2-Clause
"""

class Faye:

    def log(self, msg: str = "Logger init", level: str = "INFO") -> str:
        """
        Generic logging method that allows the user to set a message and log level.

        @params
        
        msg (str): Log message
        
        level (str): Level string

        @rtype: str
        """

        # Checks for empty string parameters
        if level != "" and msg != "":
            return f"[{level}] => {msg}"
        else:
            raise NameError

    def progress(self, total: int = 0, description: str = ""):
        """
        Simple progress bar built with tqdm to allow quick terminal visualization.

        @params

        total (int): The length of the progress bar

        description (str): Description to display beside the progress bar

        @rtype: None
        """

        from tqdm import tqdm

        # Progress bar configuration
        for p in tqdm(range(total), desc=description):
            pass