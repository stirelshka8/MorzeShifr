class MorzeShifr:
    def __init__(self):
        self.shifr = {"А":".-", "Б":"-...", "В":".--", "Г":"--.", "Д":"-..", "Е":"*", "Ё":".", "Ж":"...-"
       , "З":"--..", "И":"..", "Й":".---", "К":"-.-", "Л":".-..", "М":"--", "Н":"-.", "О":".---"
       , "П":".--.", "Р":".-.", "С":"...", "Т":"-", "У":"..-", "Ф":"..-.", "Х":"....", "Ц":"-.-."
       , "Ч":"---.", "Ш":"----", "Щ":"--.-", "Ь":".--.-.", "Ы":"-.--", "Ъ":"-..-", "Э":"..-..", "Ю":"..--", "Я":".-.-"
       , " ":"|", "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9", "0":"0", ",":","
       , ".":".", "!":"!", "?":"?"}

    def encrypt(self, text='ВВЕДЕНО ПУСТОе ЗНАЧЕНИЕ', check = 0):
        self.check = check
        self.text = text.upper()
        self.cipher_dictionary = []
        self.temporary_dictionary = []
        self.messanger_ecrypt = None

        for self.text_brute in self.text:
            self.temporary_dictionary.append(self.text_brute)

        for self.temporary_data in self.temporary_dictionary:
            for self.shifr_key, self.shifr_values in self.shifr.items():
                if self.temporary_data == self.shifr_key:
                    if self.check == 0:
                        self.cipher_dictionary.append(self.shifr_values)
                        self.messanger_ecrypt = "[INFO] Зашифрование завершено"
                    elif self.check == 1:
                        self.cipher_dictionary.append(f"{self.shifr_values} >> {self.shifr_key}")
                        self.messanger_ecrypt = "[INFO] Зашифрование завершено ЗАШИФРОВАННЫЙ ТЕКСТ >> КЛЮЧ"
                    else:
                        self.messanger_ecrypt = "[ERROR] Ошибка зашифрования!"
                        return

        return ' '.join(self.cipher_dictionary)

    def decrypt(self, morze = ".-- .-- * -.. * -. .--- | .--. ..- ... - .--- * | --.. -. .- ---. * -. .. *"):
        self.morze = morze.split(' ')
        self.invert_shifr = {}
        self.decrypt_dictionary = []
        self.messanger_ecrypt = None

        for self.invert_shifr_key, self.invert_shifr_values in self.shifr.items():
            self.invert_shifr[self.invert_shifr_values] = self.invert_shifr_key

        for self.data_morze in self.morze:
            for self.decrypt_shifr_key, self.decrypt_shifr_values in self.invert_shifr.items():
                if self.data_morze == self.decrypt_shifr_key:
                    self.decrypt_dictionary.append(self.decrypt_shifr_values)
                    self.messanger_ecrypt = "[INFO] Расшифрование завершено"
        return ''.join(self.decrypt_dictionary)
    
    def create_key_dictionary(self, shhifr_file = 'key.fsb', check_create = 0):
        self.check_create = check_create
        self.shifr_file = shhifr_file
        self.messanger_create = None
        with open(self.shifr_file, "w+") as self.open_shifr_file:
            for self.upd_shifr_key, self.upd_shifr_val  in self.shifr.items():
                if self.check_create == 0:
                    self.open_shifr_file.write(f'{str(self.upd_shifr_key)} \n')
                    self.messanger_create = "[INFO] Создан словарь"
                elif self.check_create == 777:
                    self.open_shifr_file.write(f'{str(self.upd_shifr_key)} >> {str(self.upd_shifr_val)} \n')
                    self.messanger_create = "[INFO] Создан словарь КЛЮЧ >> ЗНАЧЕНИЕ"
                else:
                    self.messanger_create = "[ERROR] Словарь не создан! Неверный аргумент"
        
        return self.messanger_create

if __name__ == '__main__':
    crypto = MorzeShifr()
    print(crypto.decrypt())

