import mesa
from model import MoneyModel
from mesa.visualization.ModularVisualization import VisualizationElement, CHART_JS_FILE
import numpy as np

class HistogramModule(VisualizationElement):
    package_includes = CHART_JS_FILE
    local_includes = ["HistogramModule.js"]
    
    def __init__(self, bins, canvas_height, canvas_width):
        self.canvas_height = canvas_height
        self.canvas_width = canvas_width
        self.bins = bins
        new_element = "new HistogramModule({}, {}, {})"
        new_element = new_element.format(bins, canvas_width, canvas_height)

        self.js_code = "elements.push(" + new_element + ");"

    def render(self, model):
        wealth_vals = [agent.wealth for agent in model.schedule.agents]
        hist = np.histogram(wealth_vals, bins=self.bins)[0]
        return [int(x) for x in hist]


# generate a portrayal dictionary
def agent_portrayal(agent):
    portrayal = {
        "Shape": "circle",
        "Filled": "true",
        "r": 0.5
    }
    if agent.wealth > 0:
        # set the color of the agent
        portrayal["Color"] = "red"
        # set the scale of the agent
        portrayal["Layer"] = 0
    else:
        # set the color of the agent
        portrayal["Color"] = "grey"
        # set the scale of the agent
        portrayal["Layer"] = 1
        # set the stroke color of the agent
        portrayal["r"] = 0.2
    return portrayal

# instantiate canvas grid
# grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 10, 500, 500)

# instantiate chart
chart = mesa.visualization.ChartModule([
    {"Label": "Gini", "Color": "Black"}],
    data_collector_name='datacollector'
)

# instantiate chart to display first agent wealth
chart2 = mesa.visualization.ChartModule([
    {"Label": "AWealth", "Color": "Black"}],
    data_collector_name='datacollector'
)

# create a function taht takes initial value, final value, and float step size and returns a list of values
def frange(start, stop, step):
    lst = []
    i = start
    while i < stop:
        lst.append(i)
        i += step
    return lst

    



# instantiate histogram
histogram = HistogramModule(frange(0,10,1), 200, 500)

# instantiate server
server = mesa.visualization.ModularServer(
    MoneyModel,
    [chart, chart2, histogram],
    "Money Model",
    {"N": 100, "width": 10, "height": 10}
)



# set the port number
server.port = 8521
# launch server
server.launch()
