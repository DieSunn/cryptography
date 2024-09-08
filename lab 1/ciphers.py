class CaesarCipher:
    # Шифратор шифра Цезаря
    @classmethod 
    def encrypt(plaintext: str, key: int, alphabet: list) -> str:
        N = len(alphabet)
        ciphertext = []

        for word in plaintext.split(' '):
            new_word = ''
            for letter in word:
                if letter.upper() in alphabet:
                    index = alphabet.index(letter.upper())
                    new_letter = alphabet[(index + key) % N]
                    new_word += new_letter if letter.isupper() else new_letter.lower()
                else:
                    new_word += letter
            ciphertext.append(new_word)

        return ' '.join(ciphertext)
    
    # Дешифратор шифра Цезаря
    @classmethod
    def decrypt(ciphertext: str, key: int, alphabet: list) -> str:
        N = len(alphabet)
        plaintext = []

        for word in ciphertext.split(' '):
            new_word = ''
            for letter in word:
                if letter.upper() in alphabet:
                    index = alphabet.index(letter.upper())
                    new_letter = alphabet[(index - key) % N]
                    new_word += new_letter if letter.isupper() else new_letter.lower()
                else:
                    new_word += letter
            plaintext.append(new_word)

        return ' '.join(plaintext)

    
class VigenereCipher:
    @classmethod
    def encrypt(cls, plaintext: str, key: str, alphabet: list) -> str:
        ciphertext = ''
        N = len(alphabet)

        key = cls.__fill_key(plaintext, key)

        for index, letter in enumerate(plaintext):
            if letter.upper() in alphabet:
                cipherletter = alphabet[(alphabet.index(letter.upper()) + alphabet.index(key[index].upper())) % N]
                ciphertext += cipherletter if letter.isupper() else cipherletter.lower()
            else:
                ciphertext += letter  # если символ не в алфавите, он остается неизменным

        return ciphertext
    
    @classmethod
    def decrypt(cls, ciphertext: str, key: str, alphabet: list) -> str:
        plaintext = ''
        N = len(alphabet)

        key = cls.__fill_key(ciphertext, key)

        for index, letter in enumerate(ciphertext):
            if letter.upper() in alphabet:
                plainletter = alphabet[(alphabet.index(letter.upper()) - alphabet.index(key[index].upper())) % N]
                plaintext += plainletter if letter.isupper() else plainletter.lower()
            else:
                plaintext += letter  # если символ не в алфавите, он остается неизменным

        return plaintext    

    @staticmethod
    def __fill_key(text: str, key: str) -> str:
        new_key = ''
        index = 0
        
        for letter in text:
            if letter != ' ':
                new_key += key[index % len(key)]
                index += 1
            else:
                new_key += ' '

        return new_key