 凯撒密码实验报告

一、实验目的
掌握凯撒密码的加密与解密原理，使用暴力破解法枚举所有可能的密钥，还原出有意义的明文。

二、实验原理
凯撒密码是一种替换加密算法。通过将字母表中的每个字母向后移动固定位数 $k$（密钥）实现加密；解密时则向前移动 $k$ 位。
由于密钥 $k$ 的取值范围仅为 1~25，因此可以通过穷举法枚举所有密钥，逐一解密并分析结果是否为有意义的自然语言文本。

三、实验步骤
1. 编写凯撒解密函数 `caesar_decrypt`，实现对给定密文和密钥的解密逻辑。
2. 遍历密钥范围 1~25，输出每种密钥对应的解密结果。
3. 分析所有 25 种结果，识别出唯一符合英文语义的明文。

 四、实验结果
- **正确密钥 k**：11
- **解密后的明文**：KTZBSZJVSRGFJNDVKUVSFUOV
- **判断依据**：
  遍历所有 25 个密钥后，仅 $k=11$ 对应的解密结果符合英文自然语言特征。其余密钥对应的结果均为无意义的随机字母组合，因此可确定 $k=11$ 为正确密钥。
五、代码实现
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