import sys

class Reader:
    def __init__(self, filepath: str):
        self.filepath: str = filepath
        self.hex: list[str] = []

    @staticmethod
    def __prepare(text: str) -> str:
        text = text.replace("А", "A")
        text = text.replace("С", "C")
        text = text.replace("Е", "E")
        return text

    def read(self) -> None:
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                text = file.read()
                text = self.__prepare(text)
            self.hex = list([x.strip() for x in text.strip().split("\n")])
        except Exception as e:
            print(f"Ошибка при чтении: {e}")
            sys.exit(-1)

    def get_hex_lines(self) -> list[str]:
        return self.hex
    