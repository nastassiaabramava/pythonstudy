class Empty:
    def __str__(self):
        raise Exception

    def __repr__(self):
        raise Exception


func(Empty())

