# Discarded code from project that might be usefull later

        # self.__nationalities = variables[0]
#         self.__colors = variables[1]
#         self.__pets = variables[2]
#         self.__board_games = variables[3]
#         self.__drinks = variables[4]

# for item in self.__nationalities:
        #     nationality = Variable(item,"Nationality",5)
        #     self.varialbes_list.append(nationality)
        #
        # for item in self.__colors:
        #     color = Variable(item,"Color",5)
        #     self.varialbes_list.append(color)
        #
        # for item in self.__pets:
        #     pet = Variable(item,"Pet",5)
        #     self.varialbes_list.append(pet)
        #
        # for item in self.__board_games:
        #     board_game = Variable(item,"Board Game",5)
        #     self.varialbes_list.append(board_game)
        #
        # for item in self.__drinks:
        #     drink = Variable(item,"Drink",5)
        #     self.varialbes_list.append(drink)


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


            right_of_house_2 = []
            left_of_house_2 = []
            for value in variable_1.domain.domain_values:
                # Add domain value for house to right
                possible_domain = value + 1
                right_of_house_2.append(possible_domain)
                # Add domain value for house to left
                possible_domain = value - 1
                left_of_house_2.append(possible_domain)
            # Get list of unique elements from set
            possilbe_locations = list(set(left_of_house_2+right_of_house_2))

            # Set variable 1 to new possilbe domains
            # Only allow legal domains
            legal_domains = list(set(domain_range).intersection(possilbe_locations))
            # Only take domains already in variable domain list
            select_domains = list(set(legal_domains).intersection(variable_2.domain.domain_values))
            variable_2.domain.domain_values = select_domains
