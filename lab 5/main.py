import random

# Подпрограмма 1: Перевод символа в 16-битную последовательность
def char_to_bits(c):
    return f'{ord(c):016b}'

# Подпрограмма 2: Перевод строки из двух символов в 32-битную последовательность
def str_to_bits(s):
    return char_to_bits(s[0]) + char_to_bits(s[1])

# Подпрограмма 3: Генерация случайной перестановки списка
def random_permutation(lst):
    lst_copy = lst.copy()
    for _ in range(64):
        i, j = random.sample(range(len(lst_copy)), 2)
        lst_copy[i], lst_copy[j] = lst_copy[j], lst_copy[i]
    return lst_copy

# Подпрограмма 4: Генерация n перестановок
def generate_permutations(lst, n):
    permutations = []
    while len(permutations) < n:
        perm = random_permutation(lst)
        if perm != lst and perm not in permutations:
            permutations.append(perm)
    return permutations

# Подпрограмма 5: Шифрующий P-блок
def p_block(bits, perm):
    return ''.join(bits[i] for i in perm)

# Подпрограмма 6: Расшифровывающий P-блок
def inverse_p_block(bits, perm):
    inverse_perm = [0] * len(perm)
    for i, p in enumerate(perm):
        inverse_perm[p] = i
    return ''.join(bits[i] for i in inverse_perm)

# Подпрограмма 7: Перевод двоичной строки в десятичное число
def bin_to_dec(b):
    return int(b, 2)

# Подпрограмма 8: Перевод десятичного числа в двоичную строку фиксированной длины
def dec_to_bin(n, bits_len=4):
    return f'{n:0{bits_len}b}'

# Подпрограмма 9: Шифрующий S-блок
def s_block(bits, perm):
    decimal = bin_to_dec(bits)
    new_decimal = perm[decimal]
    return dec_to_bin(new_decimal)

# Подпрограмма 10: Расшифровывающий S-блок
def inverse_s_block(bits, perm):
    decimal = bin_to_dec(bits)
    inverse_perm = [0] * len(perm)
    for i, p in enumerate(perm):
        inverse_perm[p] = i
    new_decimal = inverse_perm[decimal]
    return dec_to_bin(new_decimal)

# Подпрограмма 11: Шифрование с помощью батареи S-блоков
def s_blocks_encrypt(bits, perm):
    return ''.join(s_block(bits[i:i+4], perm) for i in range(0, len(bits), 4))

# Подпрограмма 12: Расшифрование с помощью батареи S-блоков
def s_blocks_decrypt(bits, perm):
    return ''.join(inverse_s_block(bits[i:i+4], perm) for i in range(0, len(bits), 4))

# Подпрограмма 13: Перевод битовой строки в строку из символов
def bits_to_str(bits):
    return chr(bin_to_dec(bits[:16])) + chr(bin_to_dec(bits[16:]))

# Генерация перестановок для P-блоков и S-блоков
p_permutations = generate_permutations(list(range(32)), 10)
s_permutations = generate_permutations(list(range(16)), 10)

# Основная программа: шифрование
def encrypt(message, p_perm_idx=3, s_perm_idx=2):
    bits = str_to_bits(message)
    p1_bits = p_block(bits, p_permutations[p_perm_idx])
    s_bits = s_blocks_encrypt(p1_bits, s_permutations[s_perm_idx])
    p2_bits = p_block(s_bits, p_permutations[p_perm_idx])
    return bits_to_str(p2_bits)

# Основная программа: расшифрование
def decrypt(ciphertext, p_perm_idx=3, s_perm_idx=2):
    bits = str_to_bits(ciphertext)
    p1_bits = inverse_p_block(bits, p_permutations[p_perm_idx])
    s_bits = s_blocks_decrypt(p1_bits, s_permutations[s_perm_idx])
    p2_bits = inverse_p_block(s_bits, p_permutations[p_perm_idx])
    return bits_to_str(p2_bits)

# Пример использования
if __name__ == "__main__":
    message = "ЖП"
    print("Исходное сообщение:", message)

    print(f"{str_to_bits(message)}")
    
    encrypted_message = encrypt(message)
    print("Зашифрованное сообщение:", encrypted_message)
    
    decrypted_message = decrypt(encrypted_message)
    print("Расшифрованное сообщение:", decrypted_message)
