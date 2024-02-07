from lib.manager import Manager, Employee
from random import choice as random_choice
from faker import Faker

faker = Faker()

# Test your code here

m1 = Manager(name=faker.name(), age=32, department="Civilian Consulting")
m2 = Manager(name=faker.name(), age=232, department="Restaurant Division")

e1 = Employee(name="Chett", salary=6000000, manager=random_choice(Manager.all_managers))
e2 = Employee(name="Mohammad", salary=3, manager=random_choice(Manager.all_managers))
e3 = Employee(name="Kash", salary=6, manager=random_choice(Manager.all_managers))
e4 = Employee(name="Sakib", salary=9, manager=random_choice(Manager.all_managers))

# your code above!
import ipdb; ipdb.set_trace()
