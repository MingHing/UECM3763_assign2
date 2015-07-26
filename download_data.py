from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pandas as pd
import pylab as p

start = dt(2011, 1, 1)  #start date
end = dt(2015, 1, 1)    #end date
data = DR("3182.KL", 'yahoo', start, end)  #download Genting stock price
genting = DR("3182.KL",'yahoo',start,end)['Close']  #taking the genting closing value

#calculate moving average
avg_days = 5
mov_avg = pd.rolling_mean(genting,avg_days)
p.plot(mov_avg)  #plot moving average
p.title('5-day moving average plot for Genting')
p.xlabel('Days')
p.ylabel('Stock price,$RM$')
p.show()

#Download FTSEKLCI daily data for the same duration
KLCI = DR("^KLSE", 'yahoo', start, end)

#Correlation between Genting and FTSEKLCI
combine = ["3182.KL","^KLSE"]
new_data = DR(combine,'yahoo', start, end)['Close']

#Calculate correlation
Correlation = new_data.corr()
print('Correlation between Genting and FTSEKLCI is \n', Correlation)
