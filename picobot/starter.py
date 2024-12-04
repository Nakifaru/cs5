import random


# Dimensions of the world
HEIGHT = 25
WIDTH = 25

# Limit of states
NUMSTATES = 5

POSSIBLE_SURROUNDINGS = ['xxxx', 'Nxxx', 'NExx', 'NxWx', 'xxxS', 'xExS', 'xxWS', 'xExx', 'xxWx']

class Program:
    """Run of a single picobot
    """

    def __init__(self):
        """Creates a program with empty rules
        """
        # Dictionary of conditions as keys and outcomes as values
        self.rules = {}

    def __repr__(self):
        """Prints the rules of the program
        """
        unsorted_conditions = list(self.rules.keys())
        sorted_conditions = sorted(unsorted_conditions)
        formated_rules = ''
        
        current_state = 0
        for condition in sorted_conditions:
            formated_rule = f'{condition[0]} {condition[1]} -> {self.rules[condition][0]} {self.rules[condition][1]} \n'
            
            # Adds empty line transitioning before new state
            if current_state != condition[0]:
                current_state = condition[0]
                formated_rule = '\n' + formated_rule

            formated_rules += formated_rule

        return formated_rules

    def randomize(self):
        """Creates random set of legal rules
        """
        for state in range(NUMSTATES):
            for surroundings in POSSIBLE_SURROUNDINGS:
                possible_steps = []
                for step in 'NEWS':
                    if step not in surroundings:
                        possible_steps += [step]
                condition = (state, surroundings)
                outcome = (random.choice(possible_steps), random.randint(0, NUMSTATES - 1))
                self.rules[condition] = outcome

