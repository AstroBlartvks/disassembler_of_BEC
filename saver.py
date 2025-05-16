from openpyxl import Workbook

class Saver:
    def __init__(self, byte_lines: list[str], code: list[str], comments: list[str], start_pos: str):
        self.code = code
        self.start_pos = int(start_pos, 16)
        self.comments = comments
        self.byte_lines = byte_lines
    
    def save(self) -> None:
        try:
            wb = Workbook()
            ws = wb.active
            ws.title = "Табличка БЭВМ"
            ws.append(["Адрес", "Байты", "Мнемоника", "Комментарии"])

            for i in range(len(self.code)):
                ws.append([hex(self.start_pos + i)[2:].upper(), self.byte_lines[i], self.code[i], self.comments[i]])
            
            wb.save("asm_code.xlsx")
            print("Файл 'asm_code.xlsx' успешно сохранен")
        except Exception as exp:
            print(f"Ошибка во время записи в excel: {exp}")
