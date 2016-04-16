# Author Conor O'Kelly
# This file will contain all of the classes required by the puzzle


class Problem:

    def __repr__(self):
        return "The problem class"


class Domain:

    def __init__(self):
        self.domain_values = []

    def __repr__(self):
        string_version = str(self.domain_values)
        return string_version

    def __eq__(self, other):
       return self.domain_values == other

    def create(self):
        self.domain_values = [1,2,3,4,5]

    def deleate(self, target_value):
        self.domain_values.remove(target_value)

    def split_in_half(self):
        return

    def is_empty(self):
        if len(self.domain_values) == 0:
            return True
        else:
            return False

    def is_reduced_to_one_value(self):
        if len(self.domain_values) == 1:
            return True
        else:
            return False


class Constrain:

    def __repr__(self):
        return "Constraints for the current puzzle"



if __name__ == '__main__':
    domain = Domain()
    d = Domain()

    print(domain)
    domain.create()
    domain.deleate(1)
    domain.deleate(2)
    domain.deleate(3)
    domain.deleate(4)
    print(domain == d)

