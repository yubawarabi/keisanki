#! /usr/bin/python

# 1から100の和を求めるプログラムですが、バグがあります。

print("1から100までの和を求めます")
sum = 0
for i in range(1, 100):
  sum = sum + i
print("合計は", sum, "です")
