from AES import *

def test_trace():
    from lib import state

    # TODO! TEST 1:
    print('===Проверка 1 | Подстановка одного байта===')
    substituted_state = sub_bytes(state)
    print("Substituted State:")
    for row in substituted_state:
        print(" ".join(format(byte, '02X') for byte in row))

    #TODO! TEST 2
    print('\n===Проверка 2 | Проверка Shift rows===')
    # Пример использования:
    initial_state = [
        [0x32, 0x88, 0x31, 0xe0],
        [0x43, 0x5a, 0x31, 0x37],
        [0xf6, 0x30, 0x98, 0x07],
        [0xa8, 0x8d, 0xa2, 0x34]
    ]

    print("Initial State:")
    for row in initial_state:
        print(" ".join(format(byte, '02X') for byte in row))

    shifted_state = shift_rows(initial_state)

    print("\nShifted State:")
    for row in shifted_state:
        print(" ".join(format(byte, '02X') for byte in row))

    #TODO! Проверка 3:
    print('\n===Проверка 3 | Умножение в полях Галуа===')
    print("Изначальное состояние:")
    for row in state:
        print(" ".join(format(byte, '02X') for byte in row))

    mixed_state = mix_columns(state)
    print("\nMixed State:")
    for row in mixed_state:
        print(" ".join(format(byte, '02X') for byte in row))

    #TODO! TEST 4:
    round_key = [
        [0x2b, 0x7e, 0x15, 0x16],
        [0x28, 0xae, 0xd2, 0xa6],
        [0xab, 0xf7, 0x97, 0x75],
        [0x46, 0x20, 0x63, 0xed]
    ]

    print('\n===Проверка 4 | Добавление раундового ключа===')
    print("Изначальное состояние:")
    for row in state:
        print(" ".join(format(byte, '02X') for byte in row))

    state = add_round_key(state, round_key)

    print("\nState после добавления раундового ключа:")
    for row in state:
        print(" ".join(format(byte, '02X') for byte in row))

    #TODO! TEST 5:
    key = [
        [0x2b, 0x7e, 0x15, 0x16],
        [0x28, 0xae, 0xd2, 0xa6],
        [0xab, 0xf7, 0x97, 0x05],
        [0x97, 0x9d, 0x93, 0xc]
    ]

    print('\n===Проверка 5 | Расширенный ключ===')
    expanded_key = key_expansion(key)
    print("Expanded Key:")
    for row in expanded_key:
        print(" ".join(format(byte, '02X') for byte in row))

if __name__ == '__main__':
    test_trace()

