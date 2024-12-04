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

    def get_move(self, state, surroundings):
        """Returns a move that can be made if possible
        """

        outcome = self.rules[(state, surroundings)]
        return outcome
                

class World:
    """Environment of picobot
    """

    def __init__(self, initial_row, initial_column, program):
        """Creates an environment for picobot and places picobot in it
        """
        self.row = initial_row
        self.column = initial_column
        self.state = 0
        self.program = program
        self.room = [[' ']*WIDTH for row in range(HEIGHT)]

    def __repr__(self):
        """Prints the environment of picobot
        """
        w = ''
        for col in range(WIDTH):
            self.room[0][col] = '+'
            self.room[WIDTH - 1][col] = '+'

        for row in range(HEIGHT):
            self.room[row][0] = '+'
            self.room[row][HEIGHT - 1] = '+'

        self.room[self.row][self.column] = 'P'

        for row in range(HEIGHT):
            for col in range(WIDTH):
                w += self.room[row][col]
            w += '\n'

        return w
        

    def get_current_surroundings(self):
        """Returns the surroundings of picobot at the instance
        """  
        if self.room[self.row - 1][self.column] != '+':
            north = 'x'
        else:
            north = 'N'

        if self.room[self.row + 1][self.column] != '+':
            south = 'x'
        else:
            south = 'S'

        if self.room[self.row][self.column - 1] != '+':
            west = 'x'
        else:
            west = 'W'

        if self.room[self.row][self.column + 1] != '+':
            east = 'x'
        else:
            east = 'E'

        current_surroundings = f'{north}{east}{west}{south}'
        return current_surroundings

    def step(self):
        """Makes one movement of picobot in the world
        """
        surroundings = self.get_current_surroundings()
        outcomes = self.program.get_move(self.state, surroundings)
        #update previous position to o
        self.room[self.row][self.column] = 'o'
        self.state = outcomes[1]

        # make new position P
        if outcomes[0] == "N":
            self.row = self.row - 1
            self.room[self.row][self.column] = 'P'
        if outcomes[0] == "S":
            self.row = self.row + 1
            self.room[self.row][self.column] = 'P'
        if outcomes[0] == "W":
            self.column = self.column - 1
            self.room[self.row][self.column] = 'P'
        if outcomes[0] == "E":
            self.column = self.column + 1
            self.room[self.row][self.column] = 'P'



    def run(self, steps):
        """Executes specified number of steps for picobot
        """
        for i in range(steps):
            self.step()
