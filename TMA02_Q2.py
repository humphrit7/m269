"""The Marathon ADT.

For TMA02 Question 2 of M269 17J.
"""


class Marathon:

    # Creator: Thomas Humphries
    # -------
    
    def __init__(self):
        """Set up this marathon without any runners."""
        self.entrants = set()
        self.completers = dict()

        
    # Inspectors
    # ----------

    # These are called anytime.
    
    def registered(self, runner):
        """Return True if runner has registered, otherwise False."""
        if runner in self.entrants:
            return True
        return False

    def finishers(self):
        """Return the number of entrants who finished the race so far."""
        return len(self.completers)

    
    def finished(self, runner):
        """Return True if runner has finished the race, otherwise False."""
        if runner in self.completers:
            return True
        return False
         
    # These inspectors are called after the race ends.
    
    def finishers_up_to(self, time):
        """Return how many runners finished in the given time or less.

        
        Assume the unit of time is seconds.
        """
        runners = 0
        for key in self.completers:
            if self.completers[key][0] <= time:
                runners += 1
        return runners

        
    def place(self, runner):
        """Return in which place the runner finished."""
        if self.finished(runner):
            return self.completers[runner][1]
        else:
            return "{0} has not finished the race".format(runner)

        
    def name(self, place):
        """Return the name of the runner finishing in the given place."""
        if place > len(self.completers):
            return "So far only {0} runners have finished".format(len(self.completers))
        for key in self.completers:
            if self.completers[key][1]==place:
                return key

        
    def time(self, place):
        """Return the time of the runner finishing in the given place."""
        return self.completers[self.name(place)][0]

    # Modifiers
    # ---------
    
    # This modifier is called before the race starts.
    def register(self, runner):
        """Register the runner. Return nothing."""
        if not self.registered(runner):
            self.entrants.add(runner)
        else:
            print("{0} is already registered".format(runner))
    
    # This modifier is called after the race starts and before it ends.
    def finish(self, runner, time):
        """Record that the runner just finished the race in the given time.
    
        Return nothing. Assume the unit of time is seconds.
        """
        if self.registered(runner):
            self.completers[runner]=[time, len(self.completers)+1]
        else:
            print("{0} has not registered for this marathon".format(runner))


# Tests
# -----
# The following tests are minimal and don't cover several possibilities. 
# You should add more tests to reassure yourself your code is correct.

def check(name, actual, expected):
    """Print a message if the actual and expected values differ."""
    if actual != expected:
        print(name, ': expected', expected, 'but got', actual)

T1 = 60 * 60        # 1h
T3 = 3 * T1         # 3h
T3_30 = T3 + 30*60  # 3h 30min
T4 = 4 * T1         # 4h

# The Milton Keynes marathon
mk = Marathon()
mk.register('jane')
mk.register('john')
mk.register('anne')
mk.register('anne') # Testing that a runner can't be registered twice.

mk.finish('anne', T3)
mk.finish('jane', T3_30)
mk.finish('peter', T4) # Testing that a runner who is not registered cannot finish the marathon

check('finishers', mk.finishers(), 2)
check('up to 4h', mk.finishers_up_to(T4), 2)
check('up to 3h', mk.finishers_up_to(T3), 1)
check('up to 1h', mk.finishers_up_to(T1), 0)
check('gold', mk.name(1), 'anne')
check('silver', mk.name(2), 'jane')
check('name() test for failure', mk.name(10000), "So far only {0} runners have finished".format(len(mk.completers)))
check('winning time', mk.time(1), T3)
check('place of anne', mk.place('anne'), 1)
check('place of john', mk.place('john'), "john has not finished the race")
check('is jane registered', mk.registered('jane'), True)
check('is abraham registered', mk.registered('abraham'), False)
check('is anne finished', mk.finished('anne'), True)
check('is disco stu finished', mk.finished('disco stu'), False)
check('is john finished', mk.finished('john'), False)


print('All tests have run.')