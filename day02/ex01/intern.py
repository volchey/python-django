class Intern:
    def __init__(self, name = "My name? I’m nobody, an intern, I have no name."):
        self.Name = name
        self.coffee = self.Coffee()

    def __str__(self):
        return self.Name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I’m just an intern, I can’t do that ...")

    def make_coffee(self):
        return self.coffee

if __name__ == '__main__':
    unkown_intern = Intern()
    mark = Intern("Mark")

    print(unkown_intern)
    print(mark)

    print(mark.make_coffee())
    try:
        print(unkown_intern.work())
    except Exception as e:
        print(e)