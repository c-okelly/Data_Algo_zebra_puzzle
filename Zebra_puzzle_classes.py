# Author Conor O'Kelly
# This file will contain all of the classes required for the puzzle


class Problem:

    __problem_solved = False
    __varialbes_list = []
    __constraint_set = []

    def __init__(self,variables):
        # Generate type and domain no from data input
        self.varialbe_types = variables[-1]
        self.no_domains = len(variables[0])

        # Call function to create varialbes from list
        self.__create_variables()

    def __repr__(self):
        return "Main problems class. The problem is currently sloved => " + str(self.problem_solved)

    def print_current_resutls(self):

        for item in self.__varialbes_list:
            print(item)

    def __create_variables(self):
        # Create a variables for each of the catagories
        for no_1 in range(0,len(self.varialbe_types)):
            for no_2 in range(0,len(variables[no_1])):
                variable = Variable(variables[no_1][no_2],self.varialbe_types[no_1],self.no_domains)
                self.__varialbes_list.append(variable)

    def get_varialbe_by_name(self,search_name):

        for variable in self.__varialbes_list:
            if variable.name == search_name:
                return variable

    def create_constraint(self,constriant):
        self.__constraint_set.append(constriant)

    def apply_reduction(self):

        # Cycle through all constraints
        for constraint in self.__constraint_set:
            print(type(constraint))
            # var equal to var constraint
            if type(constraint) == Constraint_equality_var_var:
                print(True)

            # var equal to constant constraint
            elif type(constraint) == Constraint_equality_var_cons:
                print(True)

            # var plus constant constraint
            elif type(constraint) == 


            # var not equal to other of same type

                # First constraint
        #     con = self.__constraint_set[0]
        #     print(con.ob_variable_1,con.ob_variable_2)
        #     x =self.get_varialbe_by_name(con.ob_variable_1)
        #     x.domain.delete(5)
        #     y = self.get_varialbe_by_name(con.ob_variable_2)
        #     y.domain.delete(1)

                # Second type of constraint testing
            # con = self.__constraint_set[1]
            # # print(con)
            # x =self.get_varialbe_by_name(con.ob_variable_1)
            # y = con.ob_constant_1
            # x.domain.delete(5)
            # x.domain.delete(4)
            # x.domain.delete(3)
            # x.domain.delete(2)
            # # print(x,y)
        # con.is_satisfied(self.get_varialbe_by_name(con.ob_variable_1), con.ob_constant_1)

        # Third type of constraint
        # con = self.__constraint_set[2]
        # print(con)
        # ivory = self.get_varialbe_by_name(con.ob_variable_2)
        # ivory.domain.delete(1)
        # ivory.domain.delete(2)
        # ivory.domain.delete(5)
        # ivory.domain.delete(4)
        # con.is_satisfied(self.get_varialbe_by_name(con.ob_variable_1),self.get_varialbe_by_name(con.ob_variable_2),con.ob_constant_1)

        # Forth type constraint

        # con = self.__constraint_set[4]
        # print(con, "\n")
        # x = self.get_varialbe_by_name("Japanese")
        # x.domain.domain_values = [5]
        # # print(x)
        # list_varialbe_of_same_type = self.return_varialbes_by_type(con.variable_type)
        # # print(var_type)
        #
        # # Apply constriant by calling object variable referance and putting in object
        # con.is_satisfied(list_varialbe_of_same_type)

        return

    def return_varialbes_by_type(self,search_type):

        variable_list = []
        for var in self.__varialbes_list:
            if var.type == search_type:
                variable_list.append(var)
        return variable_list

    def test_if_problem_sloved(self):

        problem_solved = True

        for var in self.__varialbes_list:
            problem_solved = var.domain.is_reduced_to_one_value()
            print(problem_solved)
        return problem_solved

class Variable:

    def __init__(self,name,type,domain_choice = 5):
        self.name = name
        self.type = type
        self.domain = Domain(domain_choice)

    def __repr__(self):
        return "Variable " +self.name+" with type "+self.type+" with current domains of " + str(self.domain.domain_values)

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

    def __init__(self):
        return

    # def __repr__(self):
    #     return "Main constraint class with all constraints"

    # Abstract method - Check that constraint is staisfied
    def is_satisfied(self):
        return

    # Abstract method - Keep common domain values
    def reduction(self):
        return

class Constraint_equality_var_var(Constraints):

    def __init__(self,variable_1,variable_2):
        self.ob_variable_1 = variable_1
        self.ob_variable_2 = variable_2
        return

    #Do they have at least 1 value in common.
    def is_satisfied(self,variable_1,variable_2):

        print(variable_1.domain, variable_2.domain)

        if variable_1 == variable_2:
            satisfied = True

        else:
            inseresction = list(set(variable_1.domain.domain_values).intersection(variable_2.domain.domain_values))
            print("Intersection",inseresction)
            # Remove options from domain if not common in both
            for i in variable_1.domain.domain_values:
                if i not in inseresction:
                    variable_1.domain.delete(int(i))

            for i in variable_2.domain.domain_values:
                if i not in inseresction:
                    variable_2.domain.delete(int(i))

            satisfied = True

        print(variable_1.domain, variable_2.domain)
        print(satisfied)


    def __repr__(self):
        return "Equality constraint for " + str(self.varialbe_1) + " equal to "+ str(self.varaible_2)

class Constraint_equality_var_cons(Constraints):

    def __init__(self,variable_1,constant_1):
        self.ob_variable_1 = variable_1
        self.ob_constant_1 = constant_1


    def is_satisfied(self,variable_1,constant_1):

        # If constant is in the list replace domain list with single value
        if constant_1 in variable_1.domain.domain_values:
            variable_1.domain.domain_values = [constant_1]
        # Not sure if this error will ever arise?
        else:
            print(constant_1, "is not in the list")


    def __repr__(self):
        return "Equality constraint for varialbe and constant " + str(self.ob_variable_1) + " equal to "+ str(self.ob_constant_1)

class Constraint_equality_var_plus_cons(Constraints):

    # Extra variable either side. If 0 only look for plus constant. If one can but plus or minus constant
    def __init__(self,variable_1,varialbe_2,constant_1,either_side):
        self.ob_variable_1 = variable_1
        self.ob_variable_2 = varialbe_2
        self.ob_constant_1 = constant_1
        self.either_side = either_side

    def is_satisfied(self,variable_1,variable_2,constant_1):

        print(variable_1,variable_2,constant_1)

        possilbe_locations = []

        if self.either_side == 0:
            for value in variable_2.domain.domain_values:
                possilbe_domain = value + 1
                possilbe_locations.append(possilbe_domain)
            print(possilbe_locations)
            # Set variable 1 to new possilbe domains
            variable_1.domain.domain_values = possilbe_locations
        elif self.either_side:
            right_of_house = []
            left_of_house = []
            for value in variable_2.domain.domain_values:
                # Add domain value for house to right
                possible_domain = value + 1
                right_of_house.append(possible_domain)
                # Add domain value for house to left
                possible_domain = value - 1
                left_of_house.append(possible_domain)
            # Get list of unique elements from set
            possilbe_locations = list(set(left_of_house+right_of_house))
            # Set variable 1 to new possilbe domains
            variable_1.domain.domain_values = possilbe_locations
            print(possilbe_locations)



        print(variable_1,variable_2,constant_1)




    def __repr__(self):
        return "Equality constraint for variable_1 equally to to varialbe_2 + constant => " + self.ob_variable_1 + " equal to " + self.ob_variable_2 +" plus " + str(self.ob_constant_1)

class Constraint_difference_var_var(Constraints):

    def __init__(self,variable_type):
        self.variable_type = variable_type

    def is_satisfied(self,list_1_variable_type):

        for variable in list_1_variable_type:
            # Check if reduced to 1 value
            if variable.domain.is_reduced_to_one_value():
                # Cycle through type_list_of_variables, skip where the variable from first loop is same as varialbe form second
                # Other wise remove the domain that variable 1 has from other variables in list
               for variable_2 in list_1_variable_type:
                   if variable.name != variable_2.name:
                       variable_2.domain.delete(variable.domain.domain_values[0])

    def __repr__(self):
        return "Constraint for varialbe_1 not being equal to varialbe_2 in same type"



if __name__ == '__main__':
    # Slightly altered from standard format so late item in list is the variable types.
    # Format would allow program to be more flexible in future
    variables = [["English", "Spaniard", "Ukrainian", "Norwegian", "Japanese"],
                 ["Red","Green","Ivory","Yellow","Blue"],
                 ["Dog","Snails","Fox","Zebra","Horse"],
                 ["Snakes and Ladders", "Cluedo", "Pictionary", "Travel The World", "Backgammon"],
                 ["Coffee","Milk","Orange Juice","Tea","Water"],
                 ["Nationality", "Color", "Pet","Board Game","Drink"]]

    # Create the problem
    zebra_problem = Problem(variables)

    # Create constraints
    zebra_problem.create_constraint(Constraint_equality_var_var("Red","English"))
    zebra_problem.create_constraint(Constraint_equality_var_cons("Red",1))
    zebra_problem.create_constraint(Constraint_equality_var_plus_cons("Green","Ivory",1,0))
    zebra_problem.create_constraint(Constraint_equality_var_plus_cons("Norwegian","Norwegian",1,1))
    zebra_problem.create_constraint(Constraint_difference_var_var("Nationality"))

    # Run reduction tillgs all ture
    zebra_problem.apply_reduction()
    # zebra_problem.print_current_resutls()


