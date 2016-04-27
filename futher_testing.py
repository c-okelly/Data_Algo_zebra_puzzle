from Zebra_puzzle_classes import *




if __name__ == '__main__':

    # Take way too long. Function would need to be more efficient to handle this level of size.
    variables_1 = [["English", "Spaniard", "Ukrainian", "Norwegian", "Japanese"],
             ["Red","Green","Ivory","Yellow","Blue"],
             ["Dog","Snails","Fox","Zebra","Horse"],
             ["Snakes and Ladders", "Cluedo", "Pictionary", "Travel The World", "Backgammon"],
             ["Coffee","Milk","Orange Juice","Tea","Water"],

             ["English_2", "Spaniard_2", "Ukrainian_2", "Norwegian_2", "Japanese_2"],
             ["Red_2","Green_2","Ivory_2","Yellow_2","Blue_2"],
             ["Dog_2","Snails_2","Fox_2","Zebra_2","Horse_2"],
             ["Snakes and Ladder_2s", "Cluedo_2", "Pictionary_2", "Travel The World_2", "Backgammon_2"],
             ["Coffee_2","Milk_2","Orange Juice_2","Tea_2","Water_2"],
             ["Nationality", "Color", "Pet","Board Game","Drink","Nationality_2", "Color_2", "Pet_2","Board Game_2","Drink_2"]]


    var_list_2 = variables = [["English", "Spaniard", "Ukrainian", "Norwegian", "Japanese","Irish"],
                 ["Red","Green","Ivory","Yellow","Blue","Super Green"],
                 ["Dog","Snails","Fox","Zebra","Horse","Irish Dog"],
                 ["Snakes and Ladders", "Cluedo", "Pictionary", "Travel The World", "Backgammon","Irish game"],
                 ["Coffee","Milk","Orange Juice","Tea","Water","Beer"],
                 ["Nationality", "Color", "Pet","Board Game","Drink"]]

    var_list_3 = variables = [["English", "Spaniard", "Ukrainian", "Norwegian", "Japanese","Irish"],
                 ["Red","Green","Ivory","Yellow","Blue","Super Green"],
                 ["Dog","Snails","Fox","Zebra","Horse","Irish Dog"],
                 ["Snakes and Ladders", "Cluedo", "Pictionary", "Travel The World", "Backgammon","Irish game"],
                 ["Coffee","Milk","Orange Juice","Tea","Water","Beer"],
                ["Kill bill","Cars 2","Iron Man","Avengers","Ferris Bullers Day off","Zootopia"],
                 ["Nationality", "Color", "Pet","Board Game","Drink","Movie"]]

    # Create the problem
    further_testing_zebra = Problem(var_list_3)


    # Create constraints
    further_testing_zebra.create_constraint(Constraint_equality_var_var("Red","English"))
    further_testing_zebra.create_constraint(Constraint_equality_var_var("Spaniard","Dog"))
    further_testing_zebra.create_constraint(Constraint_equality_var_var("Coffee","Green"))
    further_testing_zebra.create_constraint(Constraint_equality_var_var("Ukrainian","Tea"))

    further_testing_zebra.create_constraint(Constraint_equality_var_plus_cons("Green","Ivory",1,0))
    further_testing_zebra.create_constraint(Constraint_equality_var_var("Snakes and Ladders","Snails"))
    further_testing_zebra.create_constraint(Constraint_equality_var_var("Cluedo","Yellow"))

    further_testing_zebra.create_constraint(Constraint_equality_var_cons("Milk",3))
    further_testing_zebra.create_constraint(Constraint_equality_var_cons("Norwegian",1))

    further_testing_zebra.create_constraint(Constraint_equality_var_plus_cons("Pictionary","Fox",1,1))
    further_testing_zebra.create_constraint(Constraint_equality_var_plus_cons("Cluedo","Horse",1,1))

    further_testing_zebra.create_constraint(Constraint_equality_var_var("Travel The World","Orange Juice"))
    further_testing_zebra.create_constraint(Constraint_equality_var_var("Japanese","Backgammon"))

    further_testing_zebra.create_constraint(Constraint_equality_var_plus_cons("Norwegian","Blue",1,1))


    # Constraints for var list 3
    further_testing_zebra.create_constraint(Constraint_equality_var_cons("Kill bill",1))
    further_testing_zebra.create_constraint(Constraint_equality_var_cons("Iron Man",4))
    further_testing_zebra.create_constraint(Constraint_equality_var_cons("Avengers",2))

    # General constraint for domains being unable to have the same value
    further_testing_zebra.create_constraint(Constraint_difference_var_var())

    # Run reduction till no more domains can be reduced
    further_testing_zebra.apply_reduction()


    # Run domain splitting. If multiple results wanted set varialbe to 1
    further_testing_zebra.domain_splitting(results_single=0)

    # Print current results - Single results
    # further_testing_zebra.print_final_resutls_single()

    # Print results - Multiple results
    further_testing_zebra.print_mulit_results()