from openpyxl import Workbook

class Saver:
    def __init__(self, byte_lines: list[str], code: list[str], comments: list[str], start_pos: str):
        self.code = code
        self.start_pos = int(start_pos, 16)
        self.comments = comments
        self.byte_lines = byte_lines
    
    def save(self, input_filename: str) -> None:
        try:
            output_filename = input_filename + ".xlsx" if not("." in input_filename) else ".".join(input_filename.split(".")[:-1]) + ".xlsx"

            wb = Workbook()
            ws = wb.active
            ws.title = "Табличка БЭВМ"
            ws.append(["Адрес", "Байты", "Мнемоника", "Комментарии"])

            for i in range(len(self.code)):
                ws.append([hex(self.start_pos + i)[2:].upper(), self.byte_lines[i], self.code[i], self.comments[i]])
            
            wb.save(output_filename)
            print(f"Файл {output_filename} успешно сохранен")
        except Exception as exp:
            print(f"Ошибка во время записи в excel: {exp}")
