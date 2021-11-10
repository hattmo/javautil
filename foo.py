class foo:
    bar = 5

class baz:
    def print_baz(self):
        print(self.bar)

myfoo = foo()
myfoo.blah = baz.print_baz
myfoo.blah()