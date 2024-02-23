class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name


def main():
    p1 = Student("naum", 20)

    #print(p1.name)
    print(p1.age)
    print(p1.get_name())


main()
