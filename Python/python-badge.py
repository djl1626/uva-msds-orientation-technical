import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
"""Project Euler Problem 1"""


def solveProblem1():
    sum = 0
    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print("Problem 1: " + str(sum))


"""Project Euler Problem 2"""


def solveProblem2():
    prev = 1
    next = 2
    sum = 2
    while prev < 4000000 and next < 4000000:
        temp = prev + next
        prev = next
        next = temp
        if next % 2 == 0 and next < 4000000:
            sum += next
    print("Problem 2: " + str(sum))


"""Project Euler Problem 3"""


def isPrime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    factor = 3
    while factor <= int(np.sqrt(n) + 1):
        if n % factor == 0:
            return False
        factor += 2
    return True


def solveProblem3():
    max = 3
    j = 3
    num = 600851475143
    while num > 1:
        if num % j == 0 and isPrime(j):
            max = j
        while num % j == 0:
            num /= j
        j += 1
    print("Problem 3: " + str(max))


def plotHistograms():
    plt.hist(np.random.uniform(size=1000))
    plt.title("Random Uniform Distribution")
    plt.show()
    plt.hist(np.random.normal(size=1000))
    plt.title("Random Normal Distribution")
    plt.show()
    plt.hist(np.random.poisson(size=1000))
    plt.title("Random Poisson Distribution")
    plt.show()


def normalDistribution():
    binomial = np.random.binomial(100, .1, 1000)
    x = np.linspace(0, 20, 100)
    y = norm.pdf(x, 10, np.sqrt(9))
    plt.hist(binomial, alpha=.75, density=True)
    plt.plot(x, y, color='black')
    plt.savefig(
        "/Users/djl47/Documents/Graduate School/uva-msds-orientation-technical/Python/normal-binomial-approx.png")


if __name__ == "__main__":
    normalDistribution()
