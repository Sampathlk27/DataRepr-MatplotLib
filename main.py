import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
da=pd.read_csv("Video_Games.csv")
data=pd.DataFrame(da)
dfh=data.head(20)
dfh.plot(x="Name",y="Global_Sales",kind="barh",title="SALES PER YEAR",color='c')
plt.show()
