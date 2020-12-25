from tkinter import Tk

class ClipboardCopier:

    def __init__(self):
        self.root = Tk()
        self.root.withdraw()

    def copy_text_to_clipboard(self, text):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update()

    def destroy(self):
        self.root.destroy()

class ELanguageTranslator:

    def __init__(self, to_convert = "aeiou"):
        self.to_convert = to_convert.lower()

    def text_contains_character(self, text, character):
        return text.find(character) != -1

    def get_translated_character(self, character):
        original_character = character
        character = character.lower()
        if self.text_contains_character(self.to_convert, character):
            return 'E'
        return original_character

    def translate(self, text = "e language"):
        translated_text = []
        for character in text:
            translated_character = self.get_translated_character(character)
            translated_text.append(translated_character)
        return "".join(translated_text)

class ELanguageTranslatorProgram:

    def __init__(self):
        self.clipboard_copier = ClipboardCopier()
        self.language_translator = ELanguageTranslator()
        self.user_text = ""
        self.translated_text = ""
        self.user_response = ""

    def validate_user_response(self):
        while self.user_response.lower() != 'y' and self.user_response.lower() != 'n':
            self.user_response = input("Unrecognized input. Continue translating? (y/n): ")

    def run(self):
        while True:
            self.user_text = input("Enter text to convert to E language:\n\n")
            print()
            self.translated_text = self.language_translator.translate(self.user_text)
            print("Translated text:\n")
            print(self.translated_text)
            self.clipboard_copier.copy_text_to_clipboard(self.translated_text)
            print()
            self.user_response = input("Translated text has been copied to clipboard. Continue translating? (y/n): ")
            self.validate_user_response()
            if self.user_response.lower() == 'n':
                self.clipboard_copier.destroy()
                break
            elif self.user_response.lower() == 'y':
                print()
                continue


if __name__ == "__main__":
    program = ELanguageTranslatorProgram()
    program.run()