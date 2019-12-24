'''

API_KEY: ETFVDNKGJT88BXUA

'''

'''

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='ETFVDNKGJT88BXUA', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MELI',interval='1min', outputsize='1')
data['4. close'].plot()
plt.title('Intraday Times Series for the MELI stock (1 min)')
plt.show()

'''

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='ETFVDNKGJT88BXUA', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MELI',interval='1min', outputsize='full')
plt.plot(data['4. close'], marker='o', label="close")
data['1. open'].plot(label="open", marker="*")
data['2. high'].plot(label="high", marker="h")
data['3. low'].plot(label="low")
plt.title('Intraday Times Series for the MELI stock (1 min)')
plt.legend()
plt.show()