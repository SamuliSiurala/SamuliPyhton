import random

def montecarlo_pi(N):
    n = 0
    for _ in range(N):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        if x**2 + y**2 < 1:
            n += 1

    return 4 * n / N

def main():
    try:
        N = int(input("Anna arvottavien pisteiden määrä: "))
        if N <= 0:
            print("Täytyy olla pos. kokonaisluku")
            return
        pi_approx = montecarlo_pi(N)
        print(f"Piin likiarvo {N} pisteellä on: {pi_approx}")
    except ValueError:
        print("Virheellinen arvo, anna kokonaisluku")

if __name__ == "__main__":
    main()
