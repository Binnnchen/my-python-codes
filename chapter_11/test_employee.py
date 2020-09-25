import unittest
from employee_salary import Employee

class EmployeeTestCase(unittest.TestCase):
    """测试employee类"""
    
    def setUp(self):
        """创建一个employee对象"""
        self.employee=Employee('bill','gates',9000)
    
    def test_give_default_raise(self):
        """测试加默认工资"""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary,14000)
    
    def test_give_custom_raise(self):
        """测试加给定工资"""
        self.employee.give_raise(11000)
        self.assertEqual(self.employee.salary,20000)

#测试代码时，应将子类里面的多个测试函数的运行看做是独立的
#即先后顺序互不影响
        
unittest.main()
    