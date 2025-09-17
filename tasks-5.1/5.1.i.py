class Queue:
    elems = []

    def push(self, p):
        # т.к. elems - атрибут класса, его надо брать через self
        self.elems.append(p)
        return self.elems

    def pop(self):
        return self.elems.pop(0)

    def is_empty(self):
        return len(self.elems) == 0