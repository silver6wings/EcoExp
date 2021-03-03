from random import random
import matplotlib.pyplot as plt

p_count = 100
init_balance = 100

class Person:
    def __init__(self, balance):
        self.balance = balance

if __name__ == '__main__':
    p = []
    for i in range(p_count):
        p.append(Person(init_balance))

    for g in range(50000000):
        p_from = int(random() * p_count)
        p_to = int(random() * p_count)

        if p[p_from].balance > 0:
            p[p_from].balance -= 1
            p[p_to].balance += 1

    a = []
    for i in range(p_count):
         a.append(p[i].balance)

    a.sort()
    print(a)
    plt.bar(range(len(a)), a)
    plt.show()
