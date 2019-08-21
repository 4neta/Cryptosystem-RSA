# Cryptosystem RSA
*Cryptosystem RSA implemented in Python*
________
I give you a script that allows you to encrypt a message from a *.txt file in accordance with the most popular (and considered the most secure) RSA cryptosystem.
### How can I use it?
1. Prepare a text message and name it **message_for.txt**. For example, we'll use the file I posted:
```
There is some message. :)
```
2. Open script **gen_keys.py** and choose two big prime numbers. They can be numbers **5077** and **557** (you can find another [here](https://primes.utm.edu/lists/small/10000.txt "The First 10,000 Primes")). The program will calculate public and private keys:
```
-- RSA Algorithm \ GENERATING KEYS --
Choose two big prime numbers:
 10 < p = 5077
 12 < q = 557
Your public key: (1300859,2827889)
Your private key: (2794499,2827889)
```
Write down or copy these numbers.
*Note that you can get different key sets from the same prime numbers. The random factor decides what you receive.*
(...)
### How does it work?
(...)
