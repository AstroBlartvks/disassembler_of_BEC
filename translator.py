from table import Table

class Translator:
    def __init__(self, hex_list: list[str]):
        self.hex: list[str] = hex_list
        self.translated: list[str] = []
    
    def translate_one_line(self, byte_command: str) -> str:
        command: str = Table.opcode_dict.get(byte_command)

        if not(command is None):
            return command
            

        for key in Table.opcode_dict.keys():
            if key.count("X") == 0:
                continue
            if byte_command[0:2] == key[0:2]:
                if key[0] == "F":
                    return self.handle_jump_command(byte_command, key)
                else:
                    return self.handle_command_with_two_x(key)
        
        for key in Table.opcode_dict.keys():
            if key.count("X") == 0:
                continue
            elif byte_command[0] == key[0]:
                return self.handle_command_with_three_x(byte_command, key)
            
        print(f"Ошибка в команде {byte_command}, не найдена, замена на WORD 0x{byte_command}!")
        return f"WORD 0x{byte_command}"

    @staticmethod
    def handle_jump_command(byte_command: str, key: str) -> str:
        command_example = Table.opcode_dict.get(key) 
        return command_example.split(" ")[0] + f" {Translator.hex_to_signed_byte(byte_command[2:])}"

    @staticmethod
    def hex_to_signed_byte(hex_str: str) -> str:
        value = int(hex_str, 16)
        if value >= 128:
            return str(value - 256)
        return "+" + str(value)

    @staticmethod
    def handle_command_with_two_x(key: str) -> str:
        return Table.opcode_dict.get(key)

    def handle_command_with_three_x(self, byte_command: str, key: str) -> str:
        command_example = Table.opcode_dict.get(key) 
        address_type = byte_command[1]

        if int(address_type, 16) < 8:
            return command_example.split(" ")[0] + " 0x0" + byte_command[1:]

        match address_type:
            case "E":
                return command_example.split(" ")[0] + f" (IP{self.hex_to_signed_byte(byte_command[2:])})"
            case "8":
                return command_example.split(" ")[0] + f" $(IP{self.hex_to_signed_byte(byte_command[2:])})"
            case "A":
                return command_example.split(" ")[0] + f" (IP{self.hex_to_signed_byte(byte_command[2:])})+"
            case "B":
                return command_example.split(" ")[0] + f" (IP{self.hex_to_signed_byte(byte_command[2:])})-"
            case "C":
                return command_example.split(" ")[0] + f" (SP{self.hex_to_signed_byte(byte_command[2:])})"
            case "F":
                return command_example.split(" ")[0] + f" #0x{byte_command[2:]}"
        return command_example
    
    def translate_all(self) -> None:
        for byte_command in self.hex:
            self.translated.append(self.translate_one_line(byte_command))

    def get_translated(self):
        return self.translated

