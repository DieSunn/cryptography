let key = [];
let gamma = [];

// Создание случайной перестановки
function getRandomPermutation(len) {
    let array = Array.from(Array(len).keys());
    for (let i = 0; i < len * 2; i++) {
        let i1 = Math.floor(Math.random() * len);
        let i2 = Math.floor(Math.random() * len);
        [array[i1], array[i2]] = [array[i2], array[i1]];
    }
    return array;
}

// Создание генератора с ключом
function initializeGenerator(key) {
    let gen = Array.from(Array(256).keys());
    let j = 0;
    for (let i = 0; i < 256; i++) {
        j = (j + gen[i] + key[i]) % 256;
        [gen[i], gen[j]] = [gen[j], gen[i]];
    }
    return gen;
}

// Создание гамма последовательности
function makeGamma(gen, messageLen) {
    let gamma = [];
    let i = 0, j = 0;
    for (let k = 0; k < messageLen; k++) {
        i = (i + 1) % 256;
        j = (j + gen[i]) % 256;
        [gen[i], gen[j]] = [gen[j], gen[i]];
        let t = (gen[i] + gen[j]) % 256;
        gamma.push(gen[t]);
    }
    return gamma;
}

// XOR с гаммой
function xorMessage(message, gamma) {
    return message.map((m, index) => m ^ gamma[index]);
}

// Конвертация строки в массив байтов
function stringToByteArray(str) {
    return str.split('').map(c => c.charCodeAt(0));
}

// Конвертация массива байтов в строку
function byteArrayToString(bytes) {
    return String.fromCharCode(...bytes);
}

// Шифрование
function encryptMessage() {
    const message = document.getElementById("inputMessage").value;
    key = getRandomPermutation(256);  // Создание ключа
    let gen = initializeGenerator(key);
    const messageBytes = stringToByteArray(message);
    gamma = makeGamma(gen, messageBytes.length);  // Создание гаммы
    const encryptedBytes = xorMessage(messageBytes, gamma);
    document.getElementById("encryptedMessage").value = byteArrayToString(encryptedBytes);
}

// Дешифровка
function decryptMessage() {
    const encryptedMessage = document.getElementById("encryptedMessage").value;
    const messageBytes = stringToByteArray(encryptedMessage);
    let gen = initializeGenerator(key);  // Вызов генератора с тем же ключом
    const gammaForDecryption = makeGamma(gen, messageBytes.length);  // Повторное создание гаммы
    const decryptedBytes = xorMessage(messageBytes, gammaForDecryption);
    document.getElementById("decryptedMessage").value = byteArrayToString(decryptedBytes);
}
