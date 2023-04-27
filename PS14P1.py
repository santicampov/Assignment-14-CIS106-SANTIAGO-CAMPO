class Employee:

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay

  def bonus(self, rate):
    b = float(rate) * float(self.pay)
    return b


emp_1 = Employee('Santiago', 'Campo', 85000)

print(emp_1.first)
print(emp_1.last)
print(emp_1.pay)
print(emp_1.bonus(.10))
print(emp_1.bonus(.20))