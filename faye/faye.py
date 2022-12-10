class Faye:

    def log(msg: str = "Logger init", level: str = "INFO") -> str:
        if level != "" and msg != "":
            return f"[{level}] => {msg}"
        else:
            raise NameError

    def progress(total: int = 0, description: str = ""):
        from tqdm import tqdm

        for p in tqdm(range(total), desc=description):
            pass