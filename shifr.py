class MorzeShifr:
    def __init__(self):
        self.shifr = {"А":".-", "Б":"-...", "В":".--", "Г":"--.", "Д":"-..", "Е":".", "Ё":".", "Ж":"...-"
       , "З":"--..", "И":"..", "Й":".---", "К":"-.-", "Л":".-..", "М":"--", "Н":"-.", "О":".---"
       , "П":".--.", "Р":".-.", "С":"...", "Т":"-", "У":"..-", "Ф":"..-.", "Х":"....", "Ц":"-.-."
       , "Ч":"---.", "Ш":"----", "Щ":"--.-", "Ь":".--.-.", "Ы":"-.--", "Ъ":"-..-", "Э":"..-..", "Ю":"..--", "Я":".-.-"
       , " ":"|", "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9", "0":"0", ",":","
       , ".":".", "!":"!", "?":"?"}

    def encrypt(self, text='Здесь ничего НЕТ', check = 0):
        self.check = check
        self.text = text.upper()
        self.cipher_dictionary = []
        self.temporary_dictionary = []

        for self.text_brute in self.text:
            self.temporary_dictionary.append(self.text_brute)

        for self.temporary_data in self.temporary_dictionary:
            for self.shifr_key, self.shifr_values in self.shifr.items():
                if self.temporary_data == self.shifr_key:
                    if self.check == 0:
                        self.cipher_dictionary.append(self.shifr_values)
                    elif self.check == 1:
                        self.cipher_dictionary.append(f"{self.shifr_values} >> {self.shifr_key}")
                    else:
                        return "Введен неверный параметр проверки! 0 -проверка отключена, 1 - проверка включена."
        return ' '.join(self.cipher_dictionary)

    def decrypt(self, morze = "-. . -"):
        self.morze = morze
        print(self.morze)

crypto = MorzeShifr()
print(crypto.decrypt(crypto.encrypt("жопка")))