#imported random module to assist in generating random numbers for x and y locations.
import random

#created class agent, setting x and y variables to the random function.
#appended the environment values within this class to share from my main model.
#appended the agents list values within this class to link with the agents.
#store saves the eaten environment for each agent.
class Agent:
    def __init__(self, environment, agents):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment
        self.agents = agents
        self.store = 0 
                
#  returns the outcome of the x and y variables.   
    def get_xy(self):
        return self.x, self.y
                 
# moves the agents twice.
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

# eats 10  values within an envronment if the random number generated is above 10.
# 10 is taken away and stored within store.
#            
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
  
# identifies if each agents are within 20 unit from each other.If so, thier current variables
#will changes to share space with one another at an average distance.(object-object communiation)
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                print("sharing " + str(dist) + " " + str(ave))

#created a function to calculate the distance between coordinates (agents).                
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 