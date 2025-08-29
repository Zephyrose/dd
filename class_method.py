class Student:
    student_num = 0
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        Student.student_num += 1
    
    @classmethod
    def from_str(cls,info):
       name , gender = info.split(' ')
       return cls(name,gender)
    @staticmethod
    def num_len(name):
        return len(name)


s1 = Student('xx',20)
s2 = Student.from_str('qq 18')

print(f's1.name:{s1.name}')
print(f's2.name:{s2.name}')
print(f's2.name_len:{Student.num_len(s2.name)}')

