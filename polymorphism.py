# Create two classes Car and Bike.
# Both should have a method move() but print different messages.

class Car:
    def move(self):
        print('Car is Moving')
class Bike:
    def move(self):
        print('Bike is Moving')
c= Car()
b= Bike()
c.move()
b.move()

# Create a parent class Employee with method salary().
#
# Create child classes:
#1-Manager
#2-Developer
#
# Each child should show a different salary.


class Employee:
    def salary(self):
        print("345500403034")
class Manager(Employee):
    def salary(self):
        print("4353534534")
class Developer(Employee):
    def salary(self):
        print("43654735")
e = Employee()
m = Manager()
d  = Developer()
a = [e,m,d]
for i in a:
    i.salary()

# Create classes:
#
# Email
# SMS
# WhatsApp
#
# Each must have method send()
# Use a loop to call send()


class Email:
    def send(self):
        print('Sending Email')
class Sms:
    def send(self):
        print('Sending SMS')
class Whatsapp:
    def send(self):
        print('Sending Whatsapp Message')
e = Email()
s = Sms()
w = Whatsapp()
a = [Email(), Sms(), Whatsapp()]
for i in a:
    i.send()





