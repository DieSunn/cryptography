from ciphers import *


def main():
    russian_alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    english_alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    alphabet = ["О", 'И', 'У', 'Ы', 'Н', 'Т', 'К', '_'] 
    text = 'МЕТОД ПРЯМОГО ПЕРЕБОРА'

    text = CaesarCipher.encrypt(text, 4, russian_alphabet)
    print(text)

    text = CaesarCipher.decrypt(text, 4, russian_alphabet)
    print(text)

    text = VigenereCipher.encrypt(text, 'выбрать', russian_alphabet)
    print(text)
    
    text = VigenereCipher.decrypt(text, 'выбрать', russian_alphabet)
    print(text)

if __name__ == '__main__':
    main()