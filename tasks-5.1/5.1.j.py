class Stack:
    elems = []

    def push(self, p):
        self.elems.append(p)
        return self.elems

    def pop(self):
        return self.elems.pop(-1)

    def is_empty(self):
        return len(self.elems) == 0