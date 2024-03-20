# Prime Number Generator

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-brightgreen)](http://www.apache.org/licenses/)

This is Optimized version of Sieve of Eratosthenes to find first N prime number.

## Overview

The `GeneratePrime` class provides a method for generating prime numbers efficiently. It utilizes a primality check to determine if a number is prime and return the next prime number in the sequence.

## Algorithm

 - **Initialization**: When you initialize the object, it creates an empty array of primes and initializes the prime number as 2.
 - **Request prime**: Whenever you request the next prime number, it starts its while loop from the last prime number found and checks whether it is prime or not. It checks if a number is prime by using divisibility checks from all the prime numbers less than its square root, which it retrieves from the primes list. If it finds a prime number, it appends it to the list of primes and returns it. If the number is not prime, it increments it and repeats the steps until it finds a prime number.
 - **Exit**: When the object is closed, it automatically deletes all the stored prime numbers, as there may be a large number stored in it.

## Advantage

1. **Efficiency for Large Ranges**: The GeneratePrime() algorithm is more efficient for generating a large number of prime numbers when the upper limit is not known in advance. The Sieve of Eratosthenes requires a predefined upper limit for the range of numbers to be sieved, which can be impractical or inefficient for very large ranges. In contrast, GeneratePrime() dynamically generates prime numbers as needed, without needing to specify an upper limit.
2. **Space Complexity**: The space complexity of GeneratePrime() is potentially lower than the Sieve of Eratosthenes, especially for large ranges. In the Sieve of Eratosthenes, you need to store a boolean array of size N to mark numbers as prime or composite. This can be memory-intensive for very large ranges. On the other hand, GeneratePrime() only needs to store the list of prime numbers found so far, which grows much slower than the size of the range being generated.
3. **Adaptability**: GeneratePrime() is more adaptable to situations where memory constraints are a concern or where the range of prime numbers needed is not known in advance. It can generate prime numbers indefinitely, making it suitable for applications where prime numbers are needed on-the-fly.
4. **Lazy Evaluation**: GeneratePrime() uses lazy evaluation, generating prime numbers one at a time as needed. This can be advantageous in situations where only a small subset of prime numbers is required, as it avoids unnecessary computation.
5. **Ease of Implementation**: The GeneratePrime() algorithm is relatively simple to implement compared to the Sieve of Eratosthenes, especially for those who may not be familiar with more complex algorithms. It uses a straightforward iterative approach to generate prime numbers, making it accessible and easy to understand.
6. **Automatic Resource Management**: GeneratePrime() implements a context manager, allowing for automatic resource management. When used within a `with` statement, the context manager ensures that resources are properly cleaned up after use. In the `__exit__` method, the storage used for storing prime numbers is automatically cleared, ensuring efficient memory usage and preventing potential memory leaks.

## Usage

To use the `GeneratePrime` class, simply import it into your Python code and create an instance. You can then use the `next()` function to generate prime numbers one at a time.

Example:

```python
from prime_generator import GeneratePrime

# Create an instance of GeneratePrime
with GeneratePrime() as prime_generator:
    n = 10  # Number of prime numbers to generate
    for _ in range(n):
        prime = next(prime_generator)
        print(prime, end=", ")
    print("\n")
# Output: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
```
