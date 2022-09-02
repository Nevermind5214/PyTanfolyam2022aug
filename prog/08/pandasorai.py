#%%
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
#%%
stock1 = yf.Ticker("NG=F")
#%%
ng = stock1.history(period='max')
print(ng.head())
print(ng.tail())

#%%
ng.axes
ng.index.tolist()

# %%
ng['Dividends'] = ng['Open'].tolist()
ng['Mean'] = (ng['High'] + ng['Low'])/2

# %%

#ng[['Mean','Open']][10:20]
ng.iloc[10:12,[0,1,6]]

ng.describe()
# %%
print(ng.mean())
plt.plot(ng['Mean'])
plt.show()
#%%

ls = [i.year for i in ng.index.tolist()]
ng['Year'] = ls
ng.head()
#%%
tmp = ng.groupby(['Year']).mean()
print(tmp.head())

plt.bar(tmp.index.tolist(), tmp['Mean'])
plt.show()
# %%
stock2 = yf.Ticker("BZ=F")
brent = stock2.history(period='max')

plt.plot(ng['Mean'],'r')
plt.plot(brent['Open'], 'b')
plt.legend(['NGas','Brent'])
plt.show()
# %%

stock3 = yf.Ticker('USDHUF=X')
rate = stock3.history(period='max')
plt.plot(rate['Open'])
plt.show()
# %%

tmp = {'Date':[], 'Open':[], 'High':[], 'Low':[], 'Close':[]}
for i in range(len(rate)):
    try:
        value = brent.index.get_value(brent, rate.index[i])
        tmp['Open'].append(value[0]*rate['Open'][i])
        tmp['High'].append(value[1]*rate['Open'][i])
        tmp['Low'].append(value[2]*rate['Open'][i])
        tmp['Close'].append(value[3]*rate['Open'][i])
        tmp['Date'].append(rate.index[i])
    except:
        continue
# %%
brent_converted = pd.DataFrame(tmp).set_index('Date')

# %%
merged_df = pd.merge(ng, rate, left_index=True, right_index=True)
merged_df['Conv_Open'] = merged_df['Open_x'] * merged_df['Open_y']

# %%
plt.plot(brent_converted['Open'])
plt.plot(merged_df['Conv_Open'])
plt.legend(['Brent', 'NG'])
plt.xlabel('Date')
plt.ylabel('HUF')
plt.show()
# %%
