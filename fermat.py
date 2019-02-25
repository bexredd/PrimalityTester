import random


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


# takes in 2 n-bit numbers x,N and an exponent y
# returns x^y mod N
def mod_exp(x, y, N):
    # if the exponent is 0 always return 1
    if y == 0:
        return 1

    # recursively call mod_exp, each time dividing y by 2 (doing a right bit shift)
    # this right shift means that this function will be called recursively n times.
    z = mod_exp(x, y//2, N)

    # if checks if y is odd or even and then calculates the answer using z, x and N
    if y % 2 == 0:
        # z*z is n^2 complexity
        return (z**2) % N
    else:
        # z*z = n^2, multiply this by n and it is 2n^2, drop the constant and we have n^2 complexity
        return (x*(z**2)) % N


def fprobability(k):
    # this complexity is just k
    return 1/2**k


def mprobability(k):
    # this complexity is just k
    return 1-(1/4**k)


def fermat(N, k):
    # run this test k times
    for x in range(k):
        # the complexity of this would be N-1 which simplifies to N
        a = random.randint(1, N-1)

        # complexity of this call is O(n^3)
        if mod_exp(a, N-1, N) != 1:
            return 'composite'
    return 'prime'


def miller_rabin(N, k):
    # run this test k times
    for x in range(k):
        # the complexity of this would be N-1 which simplifies to N
        a = random.randint(1, N-1)

        exp = N-1
        temp = 1

        # this can be called at most n times (each time we do a right bit shift of N)
        while temp == 1:
            # complexity of this call is O(n^3)
            temp = mod_exp(a, exp, N)

            if exp % 2 != 0:
                temp = N-1
            exp = exp/2

        if temp == N-1:
            continue
        else:
            return 'composite'

    return 'prime'
