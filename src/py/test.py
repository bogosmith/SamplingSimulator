
class Employee:
  pass

emp_1 = Employee()
emp_2 = Employee()
print(emp_1)
print(emp_2)

emp_1.first = 'aa'
emp_1.last = 'bb'

print('{}{}'.format(emp_1.first, emp_1.last))

