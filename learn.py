#!/user/bin/env python
# coding=utf-8
# exercise
# P142 9-1 9-2
'''
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        #餐馆名字+类型
        print ("The restaurant name is "+self.name+".")
        print ("The restaurant type is "+self.type+'.')
    def open_restaurant(self):
        #正在营业
        print ("the restaurant is opening")
    def set_number_served(self,num):
        # 正在用餐人数
        self.number_served =num
    def increment_number_served(self,number):
        #递增的就餐人数
        self.number_served+=number
    def eating(self):
        print("There are %d people have a dinner" % (self.number_served))

restaurant1=Restaurant('yijiacangaun','zizhu')
restaurant1.name
restaurant1.type
# restaurant1.number_served=5
restaurant1.set_number_served(10)
restaurant1.increment_number_served(20)
restaurant1.eating()

restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2=Restaurant('diehf','huoguo')
restaurant2.name
restaurant2.type
restaurant2.describe_restaurant()


'''

# 9-3

class User():
    def __init__(self,first_name,last_name,sexual,age):
        #初始化函数
        self.first_name=first_name
        self.last_name=last_name
        self.sexual=sexual
        self.age=age
        self.login_attempts =0
    def describe_user(self):
        #用户描述
        print('%s %s is a %s,the age is %d' % (self.first_name,self.last_name,self.sexual,self.age))
    def greet_user(self):
        #问候
        print ("Hello,%s" % (self.first_name))
    def increment_login_attempts(self):
        ''' 登录次数属性值+1'''
        self.login_attempts+=1
    def reset_login_attempts(self):
        #重置登录次数
        self.login_attempts= 0


user =User('Sunny','Wang','girl',28)
# user.describe_user()
# user.greet_user()
user.increment_login_attempts()   #调用1次
print ("%s attempt %d frequnecy" % (user.first_name,user.login_attempts))

user.increment_login_attempts()    #调用2次
print ("%s attempt %d frequnecy" % (user.first_name,user.login_attempts))

user.increment_login_attempts()     #调用3次
print ("%s attempt %d frequnecy" % (user.first_name,user.login_attempts))

user.increment_login_attempts()      #调用4次
print ("%s attempt %d frequnecy" % (user.first_name,user.login_attempts))

user.reset_login_attempts()          #重置登录次数
print ("%s attempt %d frequnecy" % (user.first_name,user.login_attempts))