__author__ = 'Ivan'

class Quiz6B:
    def __init__(self):
        self.name = "Quiz6B"

    def Question7(self):
        n = 1000
        numbers = range(2,n)
        copy = list(numbers)
        results = []
        while len(numbers) > 0:
            results.append(numbers[0])
            for nr in copy:
                if nr % results[-1] == 0:
                    if nr in numbers: numbers.remove(nr)

        return len(results)

    def Question8(self):
        print ("YEAR" + "\t" + "SLOW" + "\t" + "AFST")
        slow_wumpuses = 1000
        fast_wumpuses = 1
        year = 0
        while slow_wumpuses >= fast_wumpuses:
            year += 1
            slow_wumpuses += slow_wumpuses
            slow_wumpuses -= 0.4 * slow_wumpuses
            fast_wumpuses += fast_wumpuses
            fast_wumpuses -= 0.3 * fast_wumpuses
            print (str(year) + "\t" + str(slow_wumpuses) + "\t" + str(fast_wumpuses))

q6b = Quiz6B()
print(str(q6b.Question7()))

q6b.Question8()

