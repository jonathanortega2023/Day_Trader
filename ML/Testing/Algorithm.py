import numpy as np
import sklearn
import pandas as pd
from fbprophet import Prophet
import git
from fbprophet.plot import plot_plotly, plot_components_plotly

df = pd.read_csv('/home/jon/Desktop/ML/Testing/example_wp_log_peyton_manning.csv')
df.head()

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods = 365)
future.tail()

forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

fig1 = m.plot(forecast)

fig2 = m.plot_components(forecast)

plot_plotly(m, forecast)

plot_components_plotly(m, forecast)