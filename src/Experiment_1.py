"""
开局每个人100个硬币
1. 每轮随机选一个人给随机另一个人一个硬币
2. 如果没钱则不用给
"""

from random import random
import matplotlib.pyplot as plt

people_count = 100
init_balance = 100

rounds = 50000000


class Person:
    def __init__(self, balance):
        self.balance = balance


if __name__ == '__main__':
    people = []
    for i in range(people_count):
        people.append(Person(init_balance))

    for round in range(rounds):
        person_give = int(random() * people_count)
        person_receive = int(random() * people_count)

        if people[person_give].balance > 0:
            people[person_give].balance -= 1
            people[person_receive].balance += 1

    result = []
    for i in range(people_count):
        result.append(people[i].balance)

    result.sort()
    print(result)
    plt.bar(range(len(result)), result)
    plt.show()
