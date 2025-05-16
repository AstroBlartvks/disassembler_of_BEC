from reader import Reader
from translator import Translator
from commenter import Commenter
from saver import Saver
            

if __name__ == "__main__":
    reader: Reader = Reader("code.asm")
    reader.read()

    translator: Translator = Translator(reader.get_hex_lines())
    translator.translate_all()

    commenter: Commenter = Commenter(reader.get_hex_lines())
    commenter.comment_all()

    start_pos = input("Введите начало программы (в формате 0xFF): ").strip().removeprefix("0x")
    saver: Saver = Saver(reader.get_hex_lines(), translator.get_translated(), commenter.get_comments(), start_pos)
    saver.save()
