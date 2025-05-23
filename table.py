class Table:
    opcode_dict = {
    "0000": "NOP",
    "0100": "HLT",
    "0200": "CLA",
    "0280": "NOT",
    "0300": "CLC",
    "0380": "CMC",
    "0400": "ROL",
    "0480": "ROR",
    "0500": "ASL",
    "0580": "ASR",
    "0600": "SXTB",
    "0680": "SWAB",
    "0700": "INC",
    "0740": "DEC",
    "0780": "NEG",
    "0800": "POP",
    "0900": "POPF",
    "0A00": "RET",
    "0B00": "IRET",
    "0C00": "PUSH",
    "0D00": "PUSHF",
    "0E00": "SWAP",
    "10XX": "DI",
    "11XX": "EI",
    "12XX": "IN REG",
    "13XX": "OUT REG",
    "18XX": "INT NUM",
    "2XXX": "AND M",
    "3XXX": "OR M",
    "4XXX": "ADD M",
    "5XXX": "ADC M",
    "6XXX": "SUB M",
    "7XXX": "CMP M",
    "8XXX": "LOOP M",
    "AXXX": "LD M",
    "BXXX": "SWAP M",
    "CXXX": "JUMP M",
    "DXXX": "CALL M",
    "EXXX": "ST M",
    "F0XX": "(BEQ|BZS)",
    "F1XX": "(BNE|BNZ)",
    "F2XX": "(BMI|BNS)",
    "F3XX": "(BPL|BNC)",
    "F4XX": "(BHIS|BCS)",
    "F5XX": "(BLO|BCC)",
    "F6XX": "BVS",
    "F7XX": "BVC",
    "F8XX": "BLT",
    "F9XX": "BGE"
}
    cmd_description = {
    "0000": "Нет операции",
    "0100": "Остановка",
    "0200": "0 -> AC",
    "0280": "~AC -> AC",
    "0300": "0 -> C",
    "0380": "~C -> C",
    "0400": "Цикл сдвиг влево",
    "0480": "Цикл сдвиг вправо",
    "0500": "Арифм сдвиг влево (AC*2 -> AC)",
    "0580": "Арифм сдвиг вправо (AC//2 -> AC",
    "0600": "Расширение знака младшего байта",
    "0680": "Обмен байтами младший <-> старший",
    "0700": "AC + 1 -> AC",
    "0740": "AC - 1 -> AC",
    "0780": "~AC + 1 -> AC",
    "0800": "(SP)+ -> AC",
    "0900": "(SP)+ -> PS",
    "0A00": "(SP)+ -> IP",
    "0B00": "(SP)+ -> PS, (SP)+ -> IP",
    "0C00": "AC -> -(SP)",
    "0D00": "PS -> -(SP)",
    "0E00": "Обмен A и вершины стека",
    "10XX": "Запрет прерыаний",
    "11XX": "Разрешение прерываний",
    "12XX": "Чтение из ВУ",
    "13XX": "Запись в ВУ",
    "18XX": "Программное прерывание с вектором",
    "2XXX": "M & AC -> AC",
    "3XXX": "M | AC -> AC",
    "4XXX": "M + AC -> AC",
    "5XXX": "M + AC + C -> AC",
    "6XXX": "AC - M -> AC",
    "7XXX": "Устанавливает флаги по результату AC - M (не меняет AC)",
    "8XXX": "M - 1 -> M, если  M <= 0, то IP + 1 -> IP",
    "9XXX": "Резерв",
    "AXXX": "M -> AC",
    "BXXX": "M <-> AC",
    "CXXX": "M -> IP",
    "DXXX": "SP - 1 -> SP; IP -> (SP), M -> IP",
    "EXXX": "AC -> M",
    "F0XX": "Переход если равенство (Z == 1)",
    "F1XX": "Переход если неравенство (Z == 0)",
    "F2XX": "Переход если минус (N == 1)",
    "F3XX": "Переход если плюч (N == 0)",
    "F4XX": "Переход если выше или равно/перенос (C == 1)",
    "F5XX": "Переход если ниже/нет переноса (C == 0)",
    "F6XX": "Переход если переполнение (V == 1)",
    "F7XX": "Переход если нет переполнение (V == 0)",
    "F8XX": "Переход если меньше (N xor V == 1 ИЛИ ЖЕ N != V)",
    "F9XX": "Переход если больше или равно (N xor V == 0 ИЛИ ЖЕ N == V)",
    "FAXX": "Резерв"
}
