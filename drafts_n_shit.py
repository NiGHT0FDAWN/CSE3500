import time as t
import random as r
import math as m
import pandas as pd
import numpy as np
import itertools as it
import functools as ft


def divisible_by_5_or_7(a: int, b: int) -> str:
    results = []
    for _ in range(a, b + 1):
        if _ % 5 == 0 or _ % 7 == 0:
            results.append(str(_))
    return ", ".join(results)


def divisible_by_5_or_7_single_line(a: int, b: int) -> str:
    ", ".join([str(_) for _ in range(1000, 2000 + 1) if _ % 5 == 0 or _ % 7 == 0])


def count_letters_in_string(s: str) -> dict:
    letters = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
               "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    for l in s.lower():
        letters[l] += 1
    return letters


class Student:
    def __init__(self, grade: float):
        self.grade = grade
        self.passing = 60.0

    def pass_fail(self):
        if self.grade < self.passing:
            return "Fail"
        return "Pass"


class CSEStudent(Student):
    def __init__(self, grade: float, CSE_classes: int):
        super().__init__(grade)
        self.CSE_classes = CSE_classes
        self.passing = 70.0


def add1(a: int, b: int) -> int:
    return a + b


def test_add1():
    assert add1(1, 2) == 3
    return "seems all good"


def csv_editor1():
    csv = pd.read_csv("a.csv")
    csv["year"] += 1
    csv.to_csv("new_a.csv", index=False)


def vanilla_csv_editor1():
    with open("b.csv", "r") as csv:
        file = csv.readlines()
        data = file[1:]
        new_data = []
        for line in data:
            n, b, y = line.strip().split(",")
            y = str(int(y) + 1)
            new_data.append(f"{n},{b},{y}\n")
    with open("b.csv", "w") as csv:
        csv.write(file[0])
        csv.writelines(new_data)


class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        self.ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",
                      "King"]
        self.reset()

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, i: int):
        return self.cards[i]

    def __iter__(self):
        return iter(self.cards)

    def reset(self, shuffle=True):
        self.cards = [Card(s, r) for s in self.suits for r in self.ranks]
        if shuffle:
            self.shuffle()

    def shuffle(self):
        r.shuffle(self.cards)

    def print_deck(self):
        for card in self.cards:
            return card

    def deal_card(self):
        self.cards.pop(0)


def simple_cache(func):
    cache = {}

    @ft.wraps(func)  # not necessary for credit
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper
