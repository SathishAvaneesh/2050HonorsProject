import random

#This class is the " contestant Object" that will store each contestants name and their LOVE CALCULATOR proven match 
#The reason that this class was created was to better organize data and be able to quickly access the proven match
class contestant:
    def __init__(self, name, matchedNumber): 
        self._name = name 
        self._matchedNumber = matchedNumber
    def __str__(self):
        return ("Contestent Name: {}, Proven Paired Matching = {}".format(self._name, self._matchedNumber))

    #truthBooth is for algorithms that pass two contestant objects into the truth booth
    def truthBooth(self, other): 
        return self._matchedNumber == other._name
    
    #truthBoothName is the same concept as truthBooth however this is for if an algorithm wants to pass in one contestant object and then a integer representing the 
    #contestants proposed match (Will compare based on an int)
    def truthBoothName(self, name): 
        return self._matchedNumber == name
    
         

#This class handles the grunt work behind putting all the pairs together for testing 
class parings: 
    #During initialization this class will put together the contestants and populate them with their "LOVE ALGORITHM" proven matches
    def __init__(self): 
        numPairings = 16
        self._randomPairedList = random.sample(range(numPairings), numPairings)
        self._setPairings = []
        #This for loop will pair contestents with a random other contestent for half the list
        for i in range(0, len(self._randomPairedList), 2): 
            self._setPairings.append(contestant(self._randomPairedList[i], self._randomPairedList[i+1]))
        inverse = []
        #This for loop just inverses the previous made list so that the same contestents are matched with the same people
        #For example say the previous loop made the matches (1, 3) (2, 7) this means that 1 is matched with 3 and 2 is matched with 7 
        #The inverse for loop will take this previous matchings and append(3, 1) (7,2) because by definition these contestents are also perfect matches
        for i in self._setPairings: 
            inverse.append(contestant(i._matchedNumber, i._name))
        self._setPairings += inverse[:]
    

    #This function randomly creates pairs of two contestents. 
    #This is mainly for the algorithms to have a way to generate a list of pairs that are randomized so that every week there is a new set
    #This definition is different from the "Love calulated pairings" as these are the random pairs the contestents get into each week 
    def randomPairing(self, numberPairs = 8): 
        OneList = [i for i in range(numberPairs // 2)]
        random.shuffle(OneList)
        TwoList = [i for i in range((numberPairs // 2) , numberPairs)]
        random.shuffle(TwoList)
        proposedPairings = []
        for i in OneList: 
            proposedPairings.append((OneList[i], TwoList[i]))
        
        return proposedPairings
    
    #This definition is for the algoritms when they need to randomize a shortlisted set of contestants 
    #Say the algorithm starts with the sets (1,2) (7,4) and (3, 6)
    #The algorithm determines that (1,2) is a perfect pair through the truth booth so that pair exits the simulation 
    #To randomize the rest of the list we pass it into randomizeExisting
    def randomizeExisting(self, givenPairs): 
        temporaryList = []
        for pair in givenPairs: 
            temporaryList.append(pair[0])
            temporaryList.append(pair[1])
        listOfPairs = []
        random.shuffle(temporaryList)
        for i in range(0, len(temporaryList), 2): 
            listOfPairs.append((temporaryList[i], temporaryList[i+1]))
        return listOfPairs
    
    #This definition will count the correct pairings in the list and return that number
    #It does this by unpacking every pair in the thoughtPairings list that is passed into it and then comparing to see if that set is representative 
    # of the predifined Love algorithm based pairings defined in the initialization 
    def countCorrectPairings(self, thoughtPairings):
        numberCorrect = 0
        for items in thoughtPairings: 
            person1 = items[0]
            person2 = items[1]
            if self._setPairings[person1]._name == person2: 
                numberCorrect += 1
        return numberCorrect
    
    #This definition simply goes through the list of pairings with the name of the contestant to find their perspective contestant object to pass back
    def findCharecter(self, name): 
        for people in self._setPairings: 
            if people._name == name: 
                return people 



#This class implements the different algorithms to find the perfect matches
class theGame:
    #The init will just initialize a pairings object from the previous class. All the algorithms manipulate this object
    def __init__(self): 
        self._p1 = parings()
    
    #This class will run the most basic pairing algorithm, leaving it completley up to chance to see how many of these people pair up
    # The algorithms comes up with 8 pairs randomly, and if all 8 pairs do not perfectly match with the matches proven by the love algorithm, then all 8 pairs will re randomize and try again 
    # This algorithm is the slowest and takes an insanley long time to run because the chances of perfect matchmaking are very slim. We are not gods here only computerScientists :)
    def algorithm1(self): 
        proposed = self._p1.randomPairing()
        numberOfWeeks = 0
        correctPairings = 0
        while correctPairings < 8: 
            numberOfWeeks += 1
            correctPairings = self._p1.countCorrectPairings(proposed)
            proposed = proposed = self._p1.randomPairing()
        return "Game Over, Rounds Taken: {}".format(numberOfWeeks)

    #The following algorithm has an insanley long run time and will not produce results in a timley fashion, however if let run results may appear 
    # This algorithm takes algorithm1 to the next level 
    #essentially the algorithm checks each time if the first pair in the list is a perfect pair or not 
    # if it is not it reshuffles all the contestents in the list into new pairs 
    # if it is a perfect pair then it pops off the first pair and reshuffles the rest of the list 
    def algorithm2(self): 
        firstWeekPairings = self._p1.randomPairing()
        numberOfWeeks = 0
        wannaContinue = True
        numberOfPlayers = 16
        while wannaContinue: 
            wannaContinue = False
            person1Name, person1Match = firstWeekPairings[0]
            person1 = self._p1.findCharecter(person1Name)
            person2 = self._p1.findCharecter(person1Match)
            if person1 == person2:
                firstWeekPairings.pop(0)
                numberOfPlayers -= 1
            firstWeekPairings = self._p1.randomPairing(numberOfPlayers)
            numberOfWeeks += 1

            if len(firstWeekPairings) > 0: 
                wannaContinue = True
        
        return "Game complete. This algorithm took {} rounds".formt(numberOfWeeks)

    # The below algorithm is not optimized however and  will not output any results 
        # def algorithm3(self): 
        #     firstWeekPairings = self._p1.randomPairing()
        #     numberOfWeeks = 0
        #     wannaContinue = True
        #     startingCount = 16
        #     while wannaContinue: 
        #         wannaContinue = False
        #         numberOfWeeks += 1
        #         if firstWeekPairings is None: 
        #             break
        #         person1Name, person1Match = firstWeekPairings[0]
        #         person1 = self._p1.findCharecter(person1Name)
        #         person2 = self._p1.findCharecter(person1Match)
        #         if person1.truthBooth(person2): 
        #             firstWeekPairings.pop(0)
        #         numberOfCorrectPairs = self._p1.countCorrectPairings(firstWeekPairings)
        #         if numberOfCorrectPairs < 1: 
        #             firstWeekPairings = self._p1.randomPairing()
        #             wannaContinue = True
        #         else: 
        #             random.shuffle(firstWeekPairings[:numberOfCorrectPairs])
        #             wannaContinue = True
            
        #     return numberOfWeeks
    

    # This is the second fastest algorithm in the algorithms created
        # Algorithm 3 is desinged to do the following: 
        # First a randomized list of pairs is created. If the first pair in the list is a perfect match it will then leave the list and the remaining pairs will reshuffle 
        # The remaining pairs reshuffle based on the following criterion, if there are 3 perfect matches then the first 5 matches will reshuffle and the meathod starts over 
        # for example: 
            # in (1, 3) (2, 4) and (5, 7), (1,3) is a perfect match so it will leave the simulation
            # we are then told through the countCorrectMatches definition in the pairings class that there is another perfect match in the remaining matches
            # we reshuffle (2,4) with another match to see if we have better luck this time
    def algorithm5(self, weeks = 0, randomPairing = 'a'): 
        if randomPairing == 'a': 
            randomPairing = self._p1.randomPairing(16)
        numWeeks = weeks
        if len(randomPairing) < 1: 
            return numWeeks
        person1Name, person1Match = randomPairing[0]
        person1 = self._p1.findCharecter(person1Name)
        if (person1.truthBoothName(person1Match)): 
            randomPairing.pop(0)
            numWeeks += 1
            return self.algorithm5(numWeeks, randomPairing)
        else:
            randomPairing = self._p1.randomizeExisting(randomPairing)
            numWeeks += 1
            return self.algorithm5(numWeeks, randomPairing)
        
    
    # Algorithm 4 is the fastest of the algorithms 
    # This algorithm works by exploiting the truthBooth functionality of the program. 
    # The algorithm starts with a randomly generated list of people, their neighbors are the pairings that take place but to reduce unpacking time they
    # are stored as an int next to each other (eq: [1,2,3,4] means that (1,2) and (3,4) are pairs)
    # The algorithm starts by checking if the first two are a perfect match or not
    # If they are then the algorithm will pop off the first two numbers and restart
    # If they are not then the algorithm goes through the rest of the list to find the perfect pair of the contestent
    # Once found the algorithm pops off the initial contestant and the pair of that contestent and then continues
    def algorithm4(self): 
        people = [i for i in range(16)]
        random.shuffle(people)
        counter = 1
        numberOfWeeks = 0
        while len(people) > 0: 
            person1 = self._p1.findCharecter(people[0])
            while not (person1.truthBoothName(people[counter])): 
                counter += 1
                numberOfWeeks += 1
            people.pop(0)
            people.remove(people[counter - 1])
            counter = 1
        return numberOfWeeks
            












