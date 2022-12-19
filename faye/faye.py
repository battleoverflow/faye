"""
    Owner: Shinigamilib (https://github.com/shinigamilib)
    Project: Faye
    License: BSD 2-Clause
"""

class Faye:

    def log(self, msg: str = "Logger init", level: str = "INFO") -> str:
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

    def progress(self, total: int = 0, description: str = ""):
        """
        Progress bar built with tqdm

        total: The length of the progress bar
        description: Description of the progress bar
        """

        from tqdm import tqdm

        # Progress bar configuration
        for p in tqdm(range(total), desc=description):
            pass