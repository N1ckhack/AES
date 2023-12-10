from lib import *
import test

def sub_bytes(state):
    # Заменяем каждый байт в стейте на соответствующий байт из S-блока
    substituted_state = [
        [S_BOX[b] for b in row]
        for row in state
    ]
    return substituted_state


def shift_rows(state):
    # Shifting rows
    state[1:4] = [
        state[1][1:] + [state[1][0]],
        state[2][2:] + state[2][:2],
        state[3][3:] + state[3][:3]
    ]
    return state


def mix_columns(state):
    # Проходим по каждому столбцу
    for i in range(4):
        # Получаем текущий столбец
        column = state[i]

        # Выполняем умножение в поле Галуа для текущего столбца
        new_column = [
            (0x02 * column[0] + 0x03 * column[1] + column[2] + column[3]) % 256,
            (column[0] + 0x02 * column[1] + 0x03 * column[2] + column[3]) % 256,
            (column[0] + column[1] + 0x02 * column[2] + 0x03 * column[3]) % 256,
            (0x03 * column[0] + column[1] + column[2] + 0x02 * column[3]) % 256,
        ]

        # Обновляем значения в стейте
        state[i] = new_column

    return state


def add_round_key(state, round_key):
    # Проходим по каждому байту стейта и добавляем соответствующий байт из раундового ключа
    for i in range(len(state)):  # количество столбцов в state
        for j in range(len(state[0])):  # количество байтов в каждом столбце
            state[j][i] ^= round_key[j][i]

    return state


def key_expansion_core(word, round_constant):
    # Циклический сдвиг слова
    rotated_word = word[1:] + [word[0]]

    # Замена байтов
    substituted_word = [S_BOX[b] for b in rotated_word]

    # Применение раундового константного значения
    substituted_word[0] ^= round_constant

    return substituted_word

def key_expansion(key):
    expanded_key = [byte for row in key for byte in row]  # Преобразуем в одномерный массив

    for i in range(1, 11):  # 11 раундовых констант для AES-128
        last_word = expanded_key[-4:]  # Последние 4 байта
        new_word = key_expansion_core(last_word, R_CON[0][i - 1])

        for j in range(4):
            expanded_key[j * 4:(j + 1) * 4] = [expanded_key[k] ^ new_word[k - j * 4] for k in range(j * 4, (j + 1) * 4)]

        expanded_key.extend(new_word)

    # Преобразуем расширенный ключ обратно в двумерный массив
    expanded_key_2d = [expanded_key[i:i + 4] for i in range(0, len(expanded_key), 4)]

    return expanded_key_2d

def aes_encrypt(plaintext, key):

    # Инициализация стейта
    state = plaintext

    # Начальный раундовый ключ
    round_key = key

    # Начальный раунд
    state = add_round_key(state, round_key)

    # 9 основных раундов
    for i in range(9):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        round_key = key_expansion(round_key)
        state = add_round_key(state, round_key)

    # Последний раунд без mix_columns
    state = sub_bytes(state)
    state = shift_rows(state)
    round_key = key_expansion(round_key)
    state = add_round_key(state, round_key)

    return state

# TODO: Тесты
if __name__ == '__main__':
    test.test_trace()