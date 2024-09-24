import numpy as np

# Русский алфавит (без "ё") плюс символ "_"
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя_'

# Функция для нахождения обратного по модулю
def mod_inv(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError(f'Нет обратного элемента для {a} по модулю {m}')

# Функция для получения обратной матрицы по модулю 33
def inverse_matrix_mod33(matrix):
    det = int(np.round(np.linalg.det(matrix)))  # Определитель матрицы
    det_inv = mod_inv(det % 34, 34)  # Обратный к определителю по модулю 33
    matrix_adj = np.round(np.linalg.inv(matrix) * det)  # Сопряжённая матрица
    matrix_modinv = (det_inv * matrix_adj) % 34  # Обратная матрица по модулю 33
    return matrix_modinv.astype(int)

# Функция шифрования
def hill_encrypt(message, key_matrix):
    message = message.lower().replace(" ", "")  # Убираем пробелы
    n = key_matrix.shape[0]  # Размер матрицы
    
    # Добавляем символ "ъ" для кратности размеру матрицы
    if len(message) % n != 0:
        message += 'ъ' * (n - len(message) % n)
    
    # Преобразуем символы в числа по индексу алфавита
    message_vector = [alphabet.index(char) for char in message]
    
    # Разбиваем сообщение на блоки и шифруем
    encrypted_message = []
    for i in range(0, len(message_vector), n):
        block = np.array(message_vector[i:i+n]).reshape(-1, 1)
        encrypted_block = np.dot(key_matrix, block) % 34
        encrypted_message.extend(encrypted_block.flatten())
    
    # Преобразуем числа обратно в символы
    encrypted_message = ''.join([alphabet[num] for num in encrypted_message])
    return encrypted_message

# Функция дешифрования
def hill_decrypt(encrypted_message, key_matrix):
    inverse_key_matrix = inverse_matrix_mod33(key_matrix)  # Обратная матрица ключа
    n = inverse_key_matrix.shape[0]
    
    # Преобразуем символы в числа
    encrypted_vector = [alphabet.index(char) for char in encrypted_message]
    
    # Разбиваем на блоки и дешифруем
    decrypted_message = []
    for i in range(0, len(encrypted_vector), n):
        block = np.array(encrypted_vector[i:i+n]).reshape(-1, 1)
        decrypted_block = np.dot(inverse_key_matrix, block) % 34
        decrypted_message.extend(decrypted_block.flatten())
    
    # Преобразуем числа обратно в символы
    decrypted_message = ''.join([alphabet[int(num)] for num in decrypted_message])
    return decrypted_message

# Пример использования
key_matrix = np.array([[7, 8], [11, 11]])  # Пример матрицы ключа
message = "КОТИК_КАТИТ_НИТКУ"

# Шифрование
encrypted = hill_encrypt(message, key_matrix)
print(f"Зашифрованное сообщение: {encrypted}")

# Дешифрование
decrypted = hill_decrypt(encrypted, key_matrix)
print(f"Расшифрованное сообщение: {decrypted}"[:-1])
