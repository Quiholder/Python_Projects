#parenr class user

class user:
    name='Skyler'
    email='sky@gmail.com'
    password='12345'

    def getLoginInfo(self):
        entry_name= input('enter your name:')
        entry_email= input('enter your email:')
        entry_password=input('enter your password:')
        if (entry_email==self.email and entry_password==self.password):
            print('welcome back, {}!'.format(entry_name))
            
        else:
            print('the passowrd or email is not correct.')

#child class Employee
class Employee(user):
    base_pay= 100.00
    department='general'
    emp_id='1234'

#this is the same method in the parent class "user"
# the difference is that instead od using entry_password we're using emp_id

    def getLoginInfo(self):
        entry_name= input('enter your name:')
        entry_email= input('enter your email:')
        entry_password=input('enter your password:')
        if (entry_email==self.email and emp_id==self.emp_id):
            print('welcome back, {}!'.format(entry_name))
            
        else:
            print('the passowrd or email is not correct.')

#another child Student
class Student(user):
    Grade_level=10
    GPA=3.6
    hobby='basketball'

    def getLoginInfo(self):
        entry_name= input('enter your name:')
        entry_email= input('enter your email:')
        entry_password=input('enter your password:')
        if (entry_email==self.email and GPA==self.GPA):
            print('welcome back, {}!'.format(entry_name))
            
        else:
            print('the passowrd or email is not correct.')


            

        
#the following code invokes the method inside each class user and employee
if __name__=="__main__":
    
    customer=user()
    customer.getLoginInfo()

    manager= Employee()
    manager.getLoginInfo()

    person= Student()
    person.getLoginInfo()
