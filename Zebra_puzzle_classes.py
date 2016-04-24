# Author Conor O'Kelly
# This file will contain all of the classes required by the puzzle


class Problem:

    problem_solved = False
    varialbes_list = []

    def __init__(self,variables):
        self.nationalities = variables[0]
        self.colors = variables[1]
        self.pets = variables[2]
        self.board_games = variables[3]
        self.drinks = variables[4]

        # Call function to create varialbes from list
        self.__create_variables()

    def __repr__(self):
        return "Main problems class. The problem is currently sloved =>" + self.problem_solved

    def __create_variables(self):

        # Create a variables for each of the catagories
        for item in self.nationalities:
            nationality = Variable(item,"Nationality",5)
            self.varialbes_list.append(nationality)

        for item in self.colors:
            color = Variable(item,"Color",5)
            self.varialbes_list.append(color)

        for item in self.pets:
            pet = Variable(item,"Pet",5)
            self.varialbes_list.append(pet)

        for item in self.board_games:
            board_game = Variable(item,"Board Game",5)
            self.varialbes_list.append(board_game)

        for item in self.drinks:
            drink = Variable(item,"Drink",5)
            self.varialbes_list.append(drink)




    def test_if_problem_sloved(self):

        if 1 == 1:
            self.problem_solved = True

class Variable:

    def __init__(self,name,type,domain_choice = 5):
        self.name = name
        self.type = type
        self.domain = Domain(domain_choice)

    def __repr__(self):
        return "Variable " +self.name+" with type id of "+self.type+" with current domains of " + str(self.domain.domain_values)

    def __eq__(self, other):
        return self.domain == other



class Domain:

    def __init__(self,no_values=5):
        self.domain_values = []
        self.__create(no_values)

    def __repr__(self):
        string_version = str(self.domain_values)
        return string_version

    def __eq__(self, other):
       return self.domain_values == other

    def __create(self,no_values):
        values = list(range(1,no_values+1))
        self.domain_values = values

    def delete(self, target_value):
        self.domain_values.remove(target_value)

    # Function not finished
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


class Constraints:

    constaint_set = []

    def __init__(self):
        Constraints.constaint_set.append(self)

    def __repr__(self):
        return "Main constraint class with all constraints"

    # Abstract method - Check that constraint is staisfied
    def is_satisfied(self):
        return

    # Abstract method - Keep common domain values
    def reduction(self):
        return

class Constraint_equality_var_var(Constraints):

    def __init__(self,variable_1,varialbe_2):
        self.varialbe_1 = variable_1
        self.varaible_2 = varialbe_2
        return

    #Do they have at least 1 value in common.
    def is_satisfied(self):
        boolChecker = False

        print(self.varialbe_1.domain())
        print(self.varaible_2.domain())


    def apply_constraint(self):
        return


    def __repr__(self):
        return "Equality constraint for " + str(self.varialbe_1) + " equal to "+ str(self.varaible_2)

class Constraint_equality_var_cons(Constraints):

    def __init__(self,variable_1,constant_1):
        self.varialbe_1 = variable_1
        self.constant_1 = constant_1
        return

    def test(self):

        if self.varialbe_1 == self.varialbe_2:
            return True

    def __repr__(self):
        return "Equality constraint for varialbe and constant " + str(self.varialbe_1) + " equal to "+ str(self.constant_1)

class Constraint_equality_var_plus_cons(Constraints):

    def __init__(self,variable_1,varialbe_2,constant_1):
        self.varialbe_1 = variable_1
        self.varaible_2 = varialbe_2
        return

    def __repr__(self):
        return "Equality constraint for variable_1 equally to to varialbe_2 + constant" + str(self.varialbe_1) + " equal to "+ str(self.varaible_2)

class Constraint_difference_var_var(Constraints):

    def __init__(self,varailbe_1,varialbe_2):
        self.varialbe_1 = varailbe_1
        self.varialbe_2 = varialbe_2

    def __repr__(self):
        return "Constraint for varialbe_1 not being equal to varialbe_2"



if __name__ == '__main__':
    c = Domain()
    v = Domain()

    print(c,v)

    varr = [4, 5]
    var = [1, 2, 3, 4, 5]

    common = list(set(var).intersection(varr))

    variables = [["English", "Spaniard", "Ukrainian", "Norwegian", "Japanese"],
                 ["red","green","ivory","blue","yellow"],
                 ["dog","snails","fox","zebra","horse"],
                 ["Snakes and Ladders", "Cluedo", "Pictionary", "Travel the World", "Backgammon"],
                 ["Coffee","milk","orange Juice","tea","water"]]

    Zebra_problem = Problem(variables)

