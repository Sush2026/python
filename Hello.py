class Hi:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f"{self.a}"
    def display(self):
        print(self.a)

x = (int(input("enter the value")))

obj = Hi(x)
obj.display()
print(obj)








