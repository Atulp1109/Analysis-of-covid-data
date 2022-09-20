from cProfile import label
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
corona_confirmed_data = pd.read_csv(
    "covid19_Confirmed_dataset.csv")
corona_confirmed_data.drop(["Lat", "Long"], axis=1, inplace=True)
actual_corona_confirmed_data = corona_confirmed_data.groupby(
    "Country/Region").sum()
countries = list(actual_corona_confirmed_data.index)
max_infection_rates = []
for country in countries:
    max_infection_rates.append(
        actual_corona_confirmed_data.loc[country].diff().max())
actual_corona_confirmed_data['max infection rate'] = max_infection_rates
print(actual_corona_confirmed_data.head())
x = actual_corona_confirmed_data.loc[actual_corona_confirmed_data["max infection rate"]
                                     > 5000]
y = np.log(actual_corona_confirmed_data["max infection rate"].head(10))
plt.plot(y)
i=pd.DataFrame(actual_corona_confirmed_data.loc['India'])
ind=i.loc["max infection rate"]
c=pd.DataFrame(actual_corona_confirmed_data.loc['China'])
chi=c.loc["max infection rate"]
# plt.plot(actual_corona_confirmed_data.loc['China'],label='India')
# plt.boxplot(ind,label="India")
# plt.boxplot(chi)
# plt.plot(actual_corona_confirmed_data.loc['China'],label="China")
plt.plot(actual_corona_confirmed_data.loc['Italy'],label="Italy")
plt.legend()
plt.show()
