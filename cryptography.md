### An Introduction of Cryptography

--

What is cryptogrphy?

![Lorenz-SZ42](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Lorenz-SZ42-2.jpg/640px-Lorenz-SZ42-2.jpg)

Note:
> Cryptography or cryptology is the practice and study of techniques for secure communication in the presence of third parties called adversaries.

### 密码学 (Cryptography/Cryptology)
--

### 密码学 (Cryptology)

> (from the Greek kryptós, "hidden," and lógos, "word") is the science of secure (or, generally speaking, secret) communication. 

* 密码编码学 (Cryptography)
* 密码分析学 (Cryptanalysis)

Note:
> was concerned initially with providing secrecy for written messages...


--

### 术语 Terminology

* cipher
* 明文 plaintext
* 密文 ciphertext
* 加密 encrypt(encipher)
* 解密 decrypt(decipher)

Note:
* 密码分析 cryptanalysis
    * algorithm for transforming plaintext to ciphertext
    * message to be sent, in readable form
    * message in coded form
    * turn plaintext into ciphertext
    * turn ciphertext back into plaintext
    * the art and science of breaking the cipher text

--

### 必备知识(Prerequisites)

* [离散数学 Discrete mathematics](https://en.wikipedia.org/wiki/Discrete_mathematics)
* [模算数 Modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic)
* [数论 Number Theory](https://en.wikipedia.org/wiki/Number_theory)
* [概率论 Probability theory](https://en.wikipedia.org/wiki/Probability_theory)
* [数学证明 Mathematical proof](https://en.wikipedia.org/wiki/Mathematical_proof)
* ...

--

### reference

* [Wikipedia: Cryptography](https://en.wikipedia.org/wiki/Cryptography)

---

### Why use Cryptography?

* 信息的机密性 Confidentiality
* 信息的完整性 Integrity
* 信息的认证性 Authentication
* 信息的不可抵赖性（数字签名） Non-Repudiation

--

### 对称密码 Symmetric Key Cryptography

* 传统密码 Conventional cryptogrphy
* 私钥密码 Secret-key cryptography
* 公共密钥密码 Common-key cryptography
* 块密码 Block Cipher/流密码 Stream Cipher

--

### 非对称密码 Asymmetric Key Cryptography

* Public Key Cryptography
* Public Key for encrypt data
* Private Key is for decrypt the data
* RSA(Rivest-Shamir-Adleman)
* DSA(Digital Signature Algorithm), Diffie-Helman

---

### 对称密码 Symmetric-key cryptography

* Stream ciphers
    * OTP
    * RC4/RC5(Rivest Cipher)
    * CSS
* Block ciphers
    * DES(Data Enryption Standard)
    * 3DES
    * AES(Advanced Encryption Standard)
    * Blowfish
    * Twofish

--

### Skytale
 
![Skytale](https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Skytale.png/800px-Skytale.png)

--

### Skytale

```
          | I | a | m | h | u |    |
     _____| r | t | v | e | r |____| 
    |     | y | b | a | d | l |
    |     | y | H | E | L | P |
```
> "I am hurt very badly HELP" 

> "IryyatbHmvaEhedLurlP"

[Cryptool online: Scytale](https://www.cryptool.org/en/cto-ciphers/scytale)

--

### ROT

> HELLO -> URYYB -> HELLO

--
### ROT13

![ROT13](https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/ROT13_table_with_example.svg/1000px-ROT13_table_with_example.svg.png)

Note: ROT13 replaces each letter by its partner 13 characters further along the alphabet. 

--
### XOR encryption

plaintext | "a" | "b" | "c"
----|-----|-----|----
Dec | 97 | 98 | 99
Hex | 01100001 | 01100010 | 01100011
x-Key | 01100100 | 01100100 | 01100100
cipherHex | 00000101 | 00000110 | 00000111
cipherDec | 5 | 6 | 7

--
### XOR decryption

cipherDec | 5 | 6 | 7
----|-----|-----|----
binary | 00000101 | 00000110 | 00000111
x-Key | 01100100 | 01100100 | 01100100
result | 01100001 | 01100010 | 01100011
Dec | 97 | 98 | 99
 | "a" | "b" | "c"

--
### XOR decryption

cipherDec | 5 | 6 | 7
----|-----|-----|----
binary | 00000101 | 00000110 | 00000111
wrong-Key | 01101011 | 01101011 | 01101011
result | 01101110 | 01101101 | 01101100
Dec | 110 | 109 | 108
 | "n" | "m" | "l"


--

Vigenère cipher

![Vigenère cipher](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Vigen%C3%A8re_square_shading.svg/600px-Vigen%C3%A8re_square_shading.svg.png)

--
![](https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/FIG-VIG-Table-EX-M.jpg)

--
![](https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/FIG-VIG-Table-EX-N.jpg)
--

* | string
--------|-----------
Plaintext: | ATTACKATDAWN
Key | LEMONLEMONLE
Ciphertext | LXFOPVEFRNHR

--

![Enigma machine](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Enigma_%28crittografia%29_-_Museo_scienza_e_tecnologia_Milano.jpg/704px-Enigma_%28crittografia%29_-_Museo_scienza_e_tecnologia_Milano.jpg)

Note: 
* Enigma was invented by the German engineer Arthur Scherbius at the end of World War I.
* Alan Turing (1912-1954) was a remarkable British cryptologist and mathematician of that time.

--

### Sigaba

![Sigaba](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/SIGABA-patent.png/800px-SIGABA-patent.png)

Note:
ECM Mark II was a cipher machine used by the United States for message encryption from World War II until the 1950s. The machine was also known as the SIGABA or Converter M-134 by the Army, or CSP-888/889 by the Navy, and a modified Navy version was termed the CSP-2900. 

--

### Enigma machine

![](http://www.crypto-it.net/Images/simple_ciphers/rotor_machines/enigma_eng.png)

[Cryptool online: Enigma](https://www.cryptool.org/en/cto-ciphers/enigma)


--

![](https://dzone.com/storage/temp/7395837-symmetricencryption.png)

---

### 公钥密码 Public-key cryptography

--

![Public key](https://dzone.com/storage/temp/7395826-publickeyencryption.png)


Note:

![Symmetric-key cryptography](https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Symmetric_key_encryption.svg/500px-Symmetric_key_encryption.png)

1. Bob and Alice are shared a key
2. Bob encrypted a message with the key and send the encrypted message to Alice
3. Alice decrpyted Bob's message with the same key

![Public-key cryptography](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Public_key_encryption.svg/500px-Public_key_encryption.png)

1. Bob encrypted a message with Alice's public key
2. Alice decrpyted Bob's message with her private key


![Public-key cryptography](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Private_key_signing.png/500px-Private_key_signing.png)
1. Alice signs a message(not encrypted) with her private key. 
2. Bob can verify that Alice sent the message and that the message has not been modified.


[Extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)

--
![digital signature](https://dzone.com/storage/temp/7395825-digitalsignature.png)

--
> RSA was designed by Ron Rivest, Adi Shamir and Leonard Adleman in 1977. 

![RSA scheme](http://www.crypto-it.net/Images/rsa/rsa_scheme.png)

[Cryptool online: RSA](https://www.cryptool.org/en/cto-highlights/rsa-step-by-step)

--

---
### 消息摘要和数字签名(Digital Signature)

![](https://www.docusign.com/sites/default/files/ds_subpage_diagram2.svg)

Note:
### Simple diagram of the process of digital Signing and verification

![](images/digital_signature_and_verification.png)

--

![](https://www.camcert.gov.kh/wp-content/uploads/2017/12/digital-signatures-methodology.jpg)

---

### 散列函数 Hash functions

* 高速的完整性鉴别
* 防止发送信息的一方否认曾经发送信息
* MD5, SHA

--

### MD5 

* 128bit

--

### SHA1/SHA2

* SHA-1(160bit), SHA-2(256/384/512bit)

--

### MAC

* Message Authentication Code

--

### HMAC

* Hash-Based Message Authentication Code

Note:
### Base64
[](https://en.wikipedia.org/wiki/Base64)
[](https://www.pixelstech.net/article/1457585550-How-does-Base64-work)

---

### TO BE CONTINUE...

* SSL/TLS/OpenSSL
* HTTPS/SSH/SFTP
* PGP/OpenPGP/GnuPG(GPG)
* IKEv1/IKEv2
* IPSec
* X.509
* ECC(Elliptic Curve Cryptography)
* PKI(Public Key Infrastructure)

--

* Demo of OpenSSL
* Demo of GPG

---

# Q&A

---


### Reference 

* [Portal: Cryptography](https://en.wikipedia.org/wiki/Portal:Cryptography)
* [Outline of Cryptography](https://en.wikipedia.org/wiki/Outline_of_cryptography)
* [Wikipedia: Encryption](https://en.wikipedia.org/wiki/Encryption)
* [Cryptool](https://www.cryptool.org/images/ct1/presentations/CrypTool1-Presentation-en.pdf)
* [Cryptography Visualization Software Downloads ](http://pages.mtu.edu/~shene/NSF-4/)
* [Art of the Problem](https://www.youtube.com/user/ArtOfTheProblem)
* [Crypto-IT](http://www.crypto-it.net/eng/index.html)
* [What is a Digital Signature](https://dzone.com/articles/what-is-a-digital-signature)
* [Alan Turing Cryptography Competition](http://www.maths.manchester.ac.uk/cryptography_competition/archive.php)
* [A slide of Cryptography](https://slides.com/kenilt/crytography/)
* [redhat: Introduction to Public-Key Cryptography](https://access.redhat.com/documentation/en-US/Red_Hat_Certificate_System/8.1/html/Deploy_and_Install_Guide/Introduction_to_Public_Key_Cryptography.html)

* [Cryptography Visualization Software](http://pages.mtu.edu/~shene/NSF-4/)
* [Cryptography Tutorial](https://www.tutorialspoint.com/cryptography/index.htm)
* [Introduction to Cryptography](https://gpgtools.tenderapp.com/kb/how-to/introduction-to-cryptography)

---

# THE END

--
### [Cryptography I (on coursera)](https://www.coursera.org/learn/crypto)
> by Stanford University

#### Slides:

 [1](http://spark-university.s3.amazonaws.com/stanford-crypto/slides/01-intro-v2-annotated.pdf)
 [2](http://spark-university.s3.amazonaws.com/stanford-crypto/slides/02-stream-v2-annotated.pdf)
 [3](http://spark-university.s3.amazonaws.com/stanford-crypto/slides/03-block-v2-annotated.pdf)
 [4](http://spark-university.s3.amazonaws.com/stanford-crypto/slides/04-using-block-v2-annotated.pdf)
 [5](http://spark-university.s3.amazonaws.com/stanford-crypto/slides/05-integrity-v2-annotated.pdf)
 [6](http://spark-university.s3.amazonaws.com/stanford-crypto/slides/06-collision-resistance-v2-annotated.pdf)
 [7](http://spark-university.s3.amazonaws.com/stanford-crypto/slides/07-authenc-v2-annotated.pdf)
 [8](http://spark-university.s3.amazonaws.com/stanford-crypto/slides/08-odds-and-ends-v2-annotated.pdf)
 [9](http://spark-university.s3.amazonaws.com/stanford-crypto/slides/09-basic-key-exchange-annotated.pdf)
 [10](http://spark-university.s3.amazonaws.com/stanford-crypto/slides/10-numth-annotated.pdf)
 [11](http://spark-university.s3.amazonaws.com/stanford-crypto/slides/11-pubkey-trapdoor-annotated.pdf)
 [12](http://spark-university.s3.amazonaws.com/stanford-crypto/slides/12-pubkey-dh-annotated.pdf)


--
Free Electronic References


[The Handbook of Applied Cryptography - Chapter 2](http://cacr.uwaterloo.ca/hac/)
[A Computational Introduction to Number Theory and Algebra](https://shoup.net/ntb/)
[Stick-figure introduction to AES](http://www.moserware.com/2009/09/stick-figure-guide-to-advanced.html)
[The Udacity Applied Crypto course](https://www.udacity.com/course/applied-cryptography--cs387)
[Coursera cryptography course](https://www.coursera.org/learn/crypto)
[Algorithms by DPV - Chapter 1.2-1.4](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf)
[CMSC 456 --- Introduction to Cryptography](http://www.cs.umd.edu/~jkatz/crypto/s18/lectures.html)
[Introduction to Modern Cryptography (2nd edition)](http://www.cs.umd.edu/~jkatz/imc.html)