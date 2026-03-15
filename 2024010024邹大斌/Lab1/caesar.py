
ciphertext = "NUFECMWBYUJMBIQGYNBYWIXY"

def caesar_decrypt(cipher, k):
    plaintext = ""
    for c in cipher:
        if c.isalpha():
            # 处理大写字母
            if c.isupper():
                plaintext += chr((ord(c) - ord('A') - k) % 26 + ord('A'))
            # 处理小写字母（本实验中无小写，可保留兼容）
            else:
                plaintext += chr((ord(c) - ord('a') - k) % 26 + ord('a'))
        else:
            plaintext += c
    return plaintext

# 枚举所有可能的密钥（1~25）
for k in range(1, 26):
    plain = caesar_decrypt(ciphertext, k)
    print(f"k={k} : {plain}")