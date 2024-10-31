#
# hw8pr4.py
#


def menu():
    """Prints the menu of options that the user can choose."""
    print()
    print("(0) Input a new list")
    print("(1) Print the current list")
    print("(2) Find the average price")
    print("(3) Find the standard deviation")
    print("(4) Find the minimum and its day")
    print("(5) Find the maximum and its day")
    print("(6) Your TT investment plan")
    print("(9) Break! (quit)")
    print()


def find_min(L):
    """find min uses a loop to return the minimum of L.
       Argument L: a nonempty list of numbers.
       Return value: the smallest value in L.
    """
    result = L[0]
    for x in L:
        if x < result:     # A smaller one was found!
            result = x
    return result

def find_max(L):
    """find max uses a loop to return the maximum of L.
       Argument L: a nonempty list of numbers.
       Return value: the largest value in L.
    """
    result = L[0]
    for x in L:
        if x > result:     # A bigger one was found!
            result = x
    return result    


def strategy(L):
    """Takes in a list of values of stock L with their indexes representing the days.
       Returns a comprehensive strategy to maximize profit.
    """
    max_profit = 0
    buy_day = 0
    buy_value = 0
    sell_day = 0
    sell_value = 0
    for b in range(len(L)):
        for s in range(b, len(L)):
            print("b:", b, "s:", s)
            if L[s] - L[b] > max_profit:
                max_profit = L[s] - L[b]
                buy_day = b
                sell_day = s
                buy_value = L[b]
                sell_value = L[s]
    
    return max_profit, buy_day, sell_day, buy_value, sell_value
            
def average(L):
    """Returns the average of an integer list L
    """
    return sum(L)/len(L)

def st_dev(L):
    """Returns the standard deviation of the list L
    """
    avg = average(L)
    squares = [(L[i] - avg)**2 for i in range(len(L))]
    sumation = sum(squares)
    dividend = sumation/len(L)
    sq_root = dividend ** 0.5
    return sq_root

def main():
    """The main user-interaction loop."""

    L = [30, 10, 20]  # an initial list

    while True:       # The user-interaction loop
        print("\n\nThe list is", L)
        menu()
        choice = input("Choose an option: ")

        try:
            choice = int(choice)   # Make into an int!
        except:
            print("I didn't understand your input! Continuing...")
            continue

        if choice == 9:    # We want to quit
            break          # Leaves the while loop altogether

        elif choice == 1:  # We want to continue (and print) ...
            print("Continuing...")
            continue   

        elif choice == 0:  # We want to enter a new list
            newL = input("Enter a new list: ")    # Enter _something_

            try: 
                newL = eval(newL) # eval runs Python's interpreter! Note: Danger!
                if type(newL) != type([]): 
                    print("That didn't seem like a list. Not changing L.")
                else: 
                    L = newL 
            except:
                print("I didn't understand your input. Not changing L.")

        elif choice == 2:
            avg = average(L)

            print(f"The average of the current list is {avg}")

        elif choice == 3: 
            dev = st_dev(L)
            print(f"The st. dev of the list is {dev}")

        elif choice == 4:
            m = find_min(L)
            print("The minimum value in L is", m, 'at day (index)', L.index(m))

        elif choice == 5:
            m = find_max(L)
            print("The maximum value in L is", m, "at day (index)", L.index(m))

        # TTS = max_profit, buy_day, sell_day, buy_value, sell_value
        elif choice == 6:
            TTS = strategy(L)
            print("Your TTS investment strategy is to")
            print()
            print("Buy on day",TTS[1] ,"at price", TTS[3])
            print("Sell on day", TTS[2], "at price", TTS[4])
            print()
            print("For a total profit of", TTS[0])


        else:
            print(choice, " ?      That's not on the menu!")

    print()
    print("See you yesterday!")