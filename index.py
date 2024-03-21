
class GeneratePrime:
    """
    A class that generates prime numbers.

    Attributes:
        primes (list): A list to store the generated prime numbers.
        i (int): An integer representing the current number being checked for primality.

    Methods:
        __next__(): Generates the next prime number.
        __enter__(): Enters the context manager.
        __exit__(): Exits the context manager.
    """

    def __init__(self):
        self.primes = []
        self.i = 1

    def __next__(self)->int:
        """
        Generates the next prime number.

        Returns:
            int: The next prime number.
        """
        while True:
            self.i += 1
            isPrime = True
            for x in self.primes:
                if x * x > self.i:
                    break
                if self.i % x == 0:
                    isPrime = False
                    break
            if isPrime:
                self.primes.append(self.i)
                return self.i

    def __enter__(self):
        """
        Enters the context manager.

        Returns:
            GeneratePrime: The instance of the GeneratePrime class.
        """
        return self

    def __exit__(self, *ignore):
        """
        Exits the context manager.
        """
        self.i = 1
        self.primes.clear()

# Create an instance of GeneratePrime
with GeneratePrime() as prime_generator:
    n = 10  # Number of prime numbers to generate
    for _ in range(n):
        prime = next(prime_generator)
        print(prime, end=", ")
    print()
# Output: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
