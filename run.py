from model import *
import matplotlib.pyplot as plt
import numpy as np

# initialize the model
model = MoneyModel(50, 10, 10)

# run the model with 20 steps
for i in range(20):
    model.step()

agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell in model.grid.coord_iter():
    # get the cell contents
    cell_content, x, y = cell
    # count the number of agents in the cell
    agent_count = 0
    if cell_content:
        agent_count = len(cell_content)
    # store the number of agents in the cell
    agent_counts[x][y] = agent_count

# plt.imshow(agent_counts, interpolation="nearest")
# plt.colorbar()
# plt.show()

# print the agent_counts for each cell
# print(agent_counts)

gini = model.datacollector.get_model_vars_dataframe()
# print(gini)
gini.plot()
# call x axis "Step"
plt.xlabel("Step")
# call y axis "Gini"
plt.ylabel("Gini")
plt.show()

# gini = model.datacollector.get_model_vars_dataframe()
# print(gini.head())