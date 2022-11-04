import mesa

w = 1
p = 1

class MoneyAgent(mesa.Agent):
    """An agent with fixed initial wealth"""

    # initialize the agent
    def __init__(self, unique_id, model):
        # call the parent class constructor to get the agent id
        super().__init__(unique_id, model)
        # set the initial wealth
        self.wealth = w

    # define the step function
    def step(self):
        if self.wealth == 0:
            # remove the agent from the schedule
            # self.model.schedule.remove(self)
            return 
            # remove the agent from the model

        # select any other agent in the model
        self.model.schedule.remove(self)
        other_agent = self.random.choice(self.model.schedule.agents)
        self.model.schedule.add(self)
        other_agent.wealth += p
        self.wealth -= p
        # self.move()
        # if self.wealth > 0:
        #     self.give_money()

    # # define the move function
    # def move(self):
    #     # get possible steps
    #     possible_steps = self.model.grid.get_neighborhood(
    #         self.pos,
    #         moore=True,
    #         include_center=False
    #     )
    #     # choose a random step
    #     new_position = self.random.choice(possible_steps)
    #     # move the agent
    #     self.model.grid.move_agent(self, new_position)

    # # define the give money function
    # def give_money(self):
    #     cellmates = self.model.grid.get_cell_list_contents([self.pos])
    #     if len(cellmates) > 1:
    #         other = self.random.choice(cellmates)
    #         other.wealth += p
    #         self.wealth -= p


# class MoneyModel(mesa.Model):
#     """A model with some number of agents"""
    
#     # initialize the model
#     def __init__(self, N):
#         # set the number of agents
#         self.num_agents = N
#         # create a schedule for the agents
#         self.schedule = mesa.time.RandomActivation(self)
#         # Create agents
#         for i in range(self.num_agents):
#             # create an agent with a unique id
#             a = MoneyAgent(i, self)
#             # add the agent to the schedule
#             self.schedule.add(a)

#     # define the step function
#     def step(self):
#         """Advance the model by one step"""
#         self.schedule.step()


class MoneyModel(mesa.Model):
    """A model with some number of agents"""

    # intialize the model
    def __init__(self, N, width, height):
        # set the number of agents
        self.num_agents = N
        # # create a grid for the agents
        # self.grid = mesa.space.MultiGrid(width, height, torus=True)
        # create a schedule for the agents
        self.schedule = mesa.time.RandomActivation(self)

        # Create agents
        for i in range(self.num_agents):
            # create an agent with a unique id
            a = MoneyAgent(i, self)
            # add the agent to the schedule
            self.schedule.add(a)
            # add variable for batch runner
            self.running = True

            # # add the agent to a random grid cell
            # x = self.random.randrange(self.grid.width)
            # y = self.random.randrange(self.grid.height)
            # # self.grid.place_agent(a, (x, y))

        # create data collectors
        self.datacollector = mesa.DataCollector(
            model_reporters={"Gini": compute_gini,
                            "AWealth": get_agent_wealth},
            agent_reporters={"Wealth": "wealth"}
        )


    def step(self):
        """Advance the model by one step"""
        print([("id:"+str(agent.unique_id) + " wealth:"+ str(agent.wealth)) for agent in self.schedule.agents])
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)


def compute_gini(model):
    # get the agent wealths
    agents_wealth = [agent.wealth for agent in model.schedule.agents]
    # compute the Gini coefficient
    x = sorted(agents_wealth)
    N = model.num_agents
    B = sum(xi * (N-i) for i, xi in enumerate(x)) / (N*sum(x))
    return (1 + (1/N) - 2*B)

# get agent wealth for the agent whose unique_id is 1
def get_agent_wealth(model):
    for agent in model.schedule.agents:
        if agent.unique_id == 1:
            return agent.wealth

    else:
        return 0
