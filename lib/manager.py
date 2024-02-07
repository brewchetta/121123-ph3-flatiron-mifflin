# Manager --< Employee


class Manager:

    all_managers = []

    # @classmethod
    # def all_managers(cls):
    #     return cls.all_managers
    
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
        Manager.all_managers.append(self)

    def __repr__(self):
        return f"Manager(name={self.name}, age={self.age}, department={self.department})"
    
    # age must be over 30 and an int
    @property
    def age(self):
        return self._age

    # BONUS PROPERTY! #
    @age.setter
    def age(self, new_age):
        # check whether the new_age is over 30 and if it's an int
        if type(new_age) == int and 30 <= new_age <= 300:
            self._age = new_age
        else:
            raise Exception("Age must be of type int between 30 and 300")
        
    # OBJECT RELATIONSHIP #

    def get_employees(self):
        # return all employees for this manager (self)
        return [ employee for employee in Employee.all_employees if employee.manager == self ]
    
    # AGGREGATE / ADDITIONAL METHODS #

    def hire_employee(self, new_name, new_salary):
        # creates and returns a new employee for this manager (self)
        return Employee(name=new_name, salary=new_salary, manager=self)
                                
    # m1.hire_employee("John", 10)

    @classmethod
    def all_departments(cls):
        # returns a list of all the department names that every manager oversees
        return [ manager.department for manager in Manager.all_managers ]

    @classmethod
    def average_age(cls):
        # return the average age of all managers
        # average is the sum / length of ages
        manager_ages_list = [ manager.age for manager in Manager.all_managers ]

        return sum( manager_ages_list ) / len( manager_ages_list )


class Employee:

    all_employees = []
    
    def __init__(self, name, salary, manager):
        self.name = name
        self.salary = salary
        self.manager = manager
        Employee.all_employees.append(self)

    def __repr__(self):
        return f"Employee(name={self.name}, salary={self.salary})"
    
    @property
    def manager(self):
        return self._manager
    
    @manager.setter
    def manager(self, new_manager):
        # check to make sure new_manager is an instance of Manager
        if isinstance(new_manager, Manager):
            self._manager = new_manager
        else:
            raise Exception("You're not a manager, get out!")

    # AGGREGATE METHODS #

    # takes a Number argument and returns an List of all the employee instances whose salaries are over that amount
    @classmethod
    def paid_over(cls, salary):
        # salary is the salary of employees who we want to target
        return [ employee for employee in Employee.all_employees if employee.salary > salary ]