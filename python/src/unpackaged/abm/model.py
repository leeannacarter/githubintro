#imported modules from pythons library.
import matplotlib.pyplot
import time
import agentframework
import csv
import random

#times how long the code takes to run
start = time.process_time()

#created 10 agents through assinging the value to a variable.
#created 100 interations through assinging the value to a varibale.
#created an empty list to add the x and y values to (agents).
#created an empty environment lists to add the in.txt data into.
#created a neighbourhood variable to allow agents to communicate with each other.    
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []
environment = []

#open and read through a csv formated file saved within my directory.
#loops through the rows and collumns of my file, adding the rows to the empty rowlist.
#Values within rowlist is then added to the empty environment list.
file = open("in.txt")
dataset = csv.reader(file, delimiter=",")
for row in dataset:
    rowlist = []
    for values in row:
        #print(values) to a 2d list to read with the enviornment grid.
        rowlist.append(int(values))
    environment.append(rowlist)
print(environment)
file.close()

# Make the agents through adding the random functions to lists.
#appened the environment values for each agent to share.
#agents 
for i in range(num_of_agents):
     agents.append(agentframework.Agent(environment, agents))

# Move the agents.
#Eats the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        #randomly shuffles the order of agents more.
        random.shuffle([i])
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)  
        # tests to see if the agents list is accessible
#        print(agents[i].environment, agents[i].store)

#plots the y/x coordinates (agents) on a grid.
#created a for loop to read through the agents and produce a number of 10 agents \n
# from the num_of_agenst variable, to plot them.
#imshow plots the imagine (environment)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show() 

#loops through the agents which has been appended to an empty agents list.
#Calculates the distance between y and x values within the for loop.
#for agents_row_a in agents:
#    for agents_row_b in agents:
#        distance = distance_between(agents_row_a, agents_row_b) 
#        print(distance)


# Test to see if y and x generates a random number from my Agent class.
# a = agentframework.Agent()
# print(a.y, a.x) 
#times how long the code takes to end
end = time.process_time()
print("time = " + str(end - start))
