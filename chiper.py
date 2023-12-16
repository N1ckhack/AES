from AES import aes_encrypt as encrypt

plaintext = [
    [0x32, 0x88, 0x31, 0xe0],
    [0x43, 0x5a, 0x31, 0x37],
    [0xf6, 0x30, 0x98, 0x07],
    [0xa8, 0x8d, 0xa2, 0x34]
]

key = [
    [0x2b, 0x7e, 0x15, 0x16],
    [0x28, 0xae, 0xd2, 0xa6],
    [0xab, 0xf7, 0x97, 0x05],
    [0x97, 0x9d, 0x93, 0xc]
]

print("\n1. Plaintext:")
for row in plaintext:
    print(' '.join(format(byte, '02X') for byte in row))


print("\n2. Key:")
for row in key:
    print(' '.join(format(byte, '02X') for byte in row))


encrypted_text = encrypt(plaintext, key)
print("\n3. Encrypted Text:")
for row in encrypted_text:
    print(' '.join(format(byte, '02X') for byte in row))