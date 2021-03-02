from Person import Person
from random import random

p_count = 20
init_balance = 100


if __name__ == '__main__':
    p = []
    for i in range(p_count):
        p.append(Person(init_balance))

    for g in range(1000000):
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