from drafts_n_shit import *
import random as r

print(divisible_by_5_or_7(1000, 2000))
print(divisible_by_5_or_7_single_line(1000, 2000))
print(count_letters_in_string("Writeafunctionhatreturnsthetalcountofachcharacterinastringndictionary"))
sad_student = CSEStudent(grade=65.0, CSE_classes=5)
print(sad_student.pass_fail())
print(test_add1())
csv_editor1()
vanilla_csv_editor1()
d = Deck()
d.reset(False)
print(d[0])
for i in range(1, 41):
    d.deal_card()
print(len(d))
for _ in d:
    print(_)
print(binary_search([1, 2, 3, 4, 6, 7, 8, 11, 32, 36, 44, 45, 45, 48, 54, 56, 152, 235, 437, 958, 2312, 2346, 3265, 5876, 7264, 35243, 45568], 35243))
a = [-100, -11, -5, 0, 9, 16, 31]
b = [-76, -28, -3, 1, 12, 35, 42]
r.shuffle(a)
r.shuffle(b)
print(pair_of_least_difference_naive(a, b))
print(pair_of_least_difference(a, b))

node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node0.next = node1
node1.next = node2
head = node0

current = head
while current is not None:
    print(current)
    current = current.next