class Student:

  def __init__(self, first, last, district, credits):
    self.first = first
    self.last = last
    self.district = district
    self.code = credits

  def tuition(self, rate):
    if self.district == 'I':
      tuition = 250.00 * self.code
    else:
      tuition = 500.00 * self.code
    return tuition

stu_1 = Student('Santiago', 'Campo', 'I', 14)

print(stu_1.first)
print(stu_1.last)
print(stu_1.code)
print(stu_1.tuition(0.05))