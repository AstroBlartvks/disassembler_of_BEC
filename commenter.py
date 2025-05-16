from table import Table


class Commenter:
    def __init__(self, hex_list: list[str]):
        self.hex: list[str] = hex_list
        self.comments: list[str] = []

    @staticmethod
    def comment_one(byte_command: str) -> str:
        command: str = Table.cmd_description.get(byte_command)

        if not(command is None): return command

        for key in Table.cmd_description.keys():
            if key.count("X") == 0: continue

            if byte_command[0:2] == key[0:2]:
                return Table.cmd_description.get(key)
            elif byte_command[0] == key[0]:
                return Commenter.handle_command_with_three_x(byte_command, key)
            
        return "Слово / Переменная"

    @staticmethod
    def handle_command_with_three_x(byte_command: str, key: str) -> str:
        command_example = Table.cmd_description.get(key) 
        address_type = byte_command[1]

        if byte_command[0] == "F":
            return Table.cmd_description.get(key) + " (прямая относительная)"

        if int(address_type, 16) < 8:
            return Table.cmd_description.get(key) + " (абсолютная адресация)"

        match address_type:
            case "E":
                return Table.cmd_description.get(key) + f" (прямая относительная)"
            case "8":
                return Table.cmd_description.get(key) + f" (косвенная относительная)"
            case "A":
                return Table.cmd_description.get(key) + f" (автоинкрементная адресация)+"
            case "B":
                return Table.cmd_description.get(key) + f" (автодекрементная адресация)-"
            case "C":
                return Table.cmd_description.get(key) + f" (относительно стека)"
            case "F":
                return Table.cmd_description.get(key) + f" (прямая загрузка)"
        return command_example

    def comment_all(self) -> None:
        for byte_command in self.hex:
            self.comments.append(self.comment_one(byte_command))

    def get_comments(self):
        return self.comments
    