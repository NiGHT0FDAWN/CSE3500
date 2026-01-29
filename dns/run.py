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

