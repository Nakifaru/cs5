#
# hw10pr1.py 
#
# Name: Michael Mumo
#

# First, the class definition
#
# ++ ALSO ++  below, we define several useful objects of type Date
#  +++ keep those and/or add your own! +++


class Date:
    """A user-defined data structure that
       stores and manipulates dates.
    """

    # The constructor is always named __init__ !
    def __init__(self, month, day, year):
        """Construct a Date with the given month, day, and year."""
        self.month = month
        self.day = day
        self.year = year


    # The "printing" function is always named __repr__ !
    def __repr__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

           ** Note that this function _can_ be called explicitly, but
              it more often is used implicitly via the print statement
              or simply by expressing self's value.
        """
        d = self.day
        m = self.month
        y = self.year
        string = f"{m:02d}/{d:02d}/{y:04d}"
        # The "d" after the integer stands for "_d_ecimal integer..."
        return string

        #
        # Note that we could have also written:
        #
        # return f"{self.month:02d}/{self.day:02d}/{self.year:04d}"


    # Here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """Returns True if the calling object is
           in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """Returns a new object with the same month, day, year
           as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        """Decides whether self and d2 represent the same calendar date,
           regardless of whether they are in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month \
                    and self.day == d2.day:    # The backslash allows this on a new line!
            return True
        else:
            return False
        
    def __eq__(self, d2):
        """Overrides the == operator so that it declares two of the same dates
           in history as ==.  This way , we don't need to use the awkward
           d.equals(d2) syntax...
        """
        return self.equals(d2)
    
    def isBefore(self, d2):
        """Checks if self comes before date d2 in the calendar
        """
        if self.year < d2.year:
            return True
        elif self.month < d2.month and self.year == d2.year:  
            return True
        elif self.day < d2.day and self.month == d2.month and self.year == d2.year:
            return True
        return False

    def __lt__(self, d2):
        """Overrides the < operator to compare dates.
        """
        return self.isBefore(d2)
    
    def isAfter(self, d2):
        """Checks if self comes after d2 on the date
        """
        if self == d2 or self < d2:
            return False
        return True  
    
    def __gt__(self, d2):
        """Overrides the > operator to compare dates.
        """
        return self.isAfter(d2)
    

    def tomorrow(self):
        """Changes the date it is called to, to the date of the next day."""

        # Luke Trick! Brilliant to use the Boolean as an integer!
        fdays = 28 + self.isLeapYear()

        # here, you will want to set fdays to the number of days in Feb.!
        DIM = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        self.day += 1
        if self.day > DIM[self.month]:    # We've gone past the end of this month: switch!
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1

    def yesterday(self):
        """Changes the date it is called to, the date of the day before."""

        fdays = 28 + self.isLeapYear()

        # be sure to define fdays here (perhaps use an if - or the "Luke" trick!)
        DIM = [31, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        self.day -= 1
        if self.day <= 0:    # We've wrapped to the previous month!
            self.month -= 1
            if self.month == 0:
                self.year -=  1
                self.month = 12
            self.day = DIM[self.month]

    def addNDays(self, N):
        """Increments the date it is called on by N days
        """
        print(self)
        for x in range(N):
            self.tomorrow()
            print(self)

    def __iadd__(self, N):
        """Overrides python internal += to increase a date
        """
        self.addNDays(N)
        return self

    def subNDays(self, N):
        """Increments the date it is called on by N days
        """
        print(self)
        for x in range(N):
            self.yesterday()
            print(self)

    def __isub__(self, N):
        """Overrides python internal -= to reduce a date
        """
        self.subNDays(N)
        return self

    def diff(self, d2):
        """Checks how many days self is from d2
        """
        selfcopy = self.copy()
        d2copy = d2.copy()

        d = 0

        while selfcopy < d2copy:
            selfcopy.tomorrow()
            d -= 1
        
        while selfcopy > d2copy:
            selfcopy.yesterday()
            d += 1

        return d

    def dow(self):
        """Returns the day of the week of self
        """
        wd10 = Date(10, 10, 2010)
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        n = self.diff(wd10) % 7
        return days[n]
    
    def dow2(self, refDate):
        """Returns the day of the week of self
        """
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        n = self.diff(refDate) % 7
        return days[n]

"""
Question 1:
nycounter checks the day of the week of each new year's date from 2024 to 2124.
"""


def nycounter():
    """Looking ahead to 100 years of NY celebrations..."""

    dow_dict = {}              # dow_dict == 'day of week dictionary'
    dow_dict["Sunday"] = 0     # A 0 entry for Sunday
    dow_dict["Monday"] = 0     # ...and so on...
    dow_dict["Tuesday"] = 0
    dow_dict["Wednesday"] = 0
    dow_dict["Thursday"] = 0
    dow_dict["Friday"] = 0
    dow_dict["Saturday"] = 0

    # Live for another 100 years...
    for year in range(2024, 2124):
        d = Date(1, 1, year)   # Get new year
        print('Current date is', d)
        s = d.dow()        # Get day of week
        dow_dict[s] += 1       # Count it

    print('Totals are', dow_dict)

    # We could return dow_dict here
    # ..but we don't need to right now
    # return dow_dict

def birthdaycounter():
    """Looking ahead to 100 years of my birthday celebrations..."""

    dow_dict = {}              # dow_dict == 'day of week dictionary'
    dow_dict["Sunday"] = 0     # A 0 entry for Sunday
    dow_dict["Monday"] = 0     # ...and so on...
    dow_dict["Tuesday"] = 0
    dow_dict["Wednesday"] = 0
    dow_dict["Thursday"] = 0
    dow_dict["Friday"] = 0
    dow_dict["Saturday"] = 0

    # Live for another 100 years...
    for year in range(2024, 2124):
        d = Date(3, 22, year)   # Get new year
        print('Current date is', d)
        s = d.dow()        # Get day of week
        dow_dict[s] += 1       # Count it

    print('Totals are', dow_dict)

"""
Question 2:
Totals are {'Sunday': 15, 'Monday': 15, 'Tuesday': 14, 'Wednesday': 13,
 'Thursday': 14, 'Friday': 14, 'Saturday': 15}
"""



def thirteenthcounter():
    """Looking ahead to 400 years of 13th celebrations..."""

    refDate = Date(11, 10, 2024)

    dow_dict = {}              # dow_dict == 'day of week dictionary'
    dow_dict["Sunday"] = 0     # A 0 entry for Sunday
    dow_dict["Monday"] = 0     # ...and so on...
    dow_dict["Tuesday"] = 0
    dow_dict["Wednesday"] = 0
    dow_dict["Thursday"] = 0
    dow_dict["Friday"] = 0
    dow_dict["Saturday"] = 0

    # Live for another 100 years...
    for year in range(2024, 2324):
        for month in range(1,13):
            d = Date(month, 13, year)   # Get new year
            s = d.dow2(refDate)        # Get day of week
            dow_dict[s] += 1       # Count it
            if s == "Sunday":
                refDate = d
        print('Current date is', d)
    print('Totals are', dow_dict)

"""Question 3:
Totals are {'Sunday': 514, 'Monday': 513, 'Tuesday': 515, 'Wednesday': 514, 'Thursday': 514, 'Friday': 516, 'Saturday': 514}
"""

#
# Be sure to add code for the Date class ABOVE--indented inside the class
# definition
#

#
# Lots of dates to work with...
#
# The nice thing about putting them here is that they get redefined with
#   each run of the software (needed for testing!)
#

today = Date(11, 7, 2024)     # Today? Yesterday?
d = Date(11, 7, 2024)     # Today? Yesterday?
d2 = Date(5, 17, 2025)    # Start of summer break
ny = Date(1, 1, 2025)     # New year
nd = Date(1, 1, 2030)     # New decade
nc = Date(1, 1, 2100)     # New century
graduation = Date(5, 14, 2028)    # Alter to suit!
nextsemester = Date(1, 21, 2025)  # Start of classes next semester
wd = Date(11, 12, 2013)   # A popular wedding day
wd2 = Date(11, 12, 2013)  # A copy of wd, to check == and .equals()
wd10 = Date(10, 10, 2010)  # 10/10/10
sm1 = Date(10, 28, 1929)  # One stock market crash
sm2 = Date(10, 19, 1987)  # Another crash: October Mondays are risky!