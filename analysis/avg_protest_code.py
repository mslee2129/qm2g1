## run this code to create a graph of average number of protests by country since 2000

import pandas as pd
import matplotlib.pyplot as plt

## initialising dataframe
protests_data = pd.read_csv("protests_data_filtered.csv")
# print(protests_data)
df = pd.DataFrame(protests_data)
# print(df)

# extract dataframes from df
countries = df.loc[:, 'country']
years = df.loc[:, 'year']
has_protest = df.loc[:, 'protest']
countries_years = df.loc[:, ['country', 'year']]
# print(years)
# print(countries)

## initialising lists & dictionaries
country_list = []  # list of countries
number_of_years = [] # list of number of years data is provided
protest_list = []  # list of number of protests
average_protests = []  # list of average protests
country_to_protest = {}  # dictionary of country:total protests
country_to_avg_protest = {}  # dic of country:average protests

## appending lists and dictionaries
# making country list
for country in countries:
    if country not in country_list:
        country_list.append(country)
country_list = sorted(country_list)
# print(country_list)
print(len(country_list))
# initialising country:total protest dic
for country in country_list:
    country_to_protest[country] = 0

# counting total protests and adding to dic
for i in range(len(countries)):
    if has_protest[i] == 1:
        # print(i, countries[i])
        country_to_protest[countries[i]] += 1

# making protest list
for i in range(len(country_list)):
    protest_list.append(country_to_protest[country_list[i]])

# calculating total number of years (as some countries did not exist for 20 years)
for country in country_list:
    min_year = (countries_years.loc[countries_years['country'] == country, 'year']).min()
    max_year = 2020
    diff = max_year - min_year
    number_of_years.append(diff)

# making list of average protests
for i in range(len(country_list)):
    average_protests.append(protest_list[i]/number_of_years[i])

# making country:avg protest dic
for i in range(len(average_protests)):
    country_to_avg_protest[country_list[i]] = average_protests[i]

# uncomment below to test
# print(country_to_protest)
# print(country_list)
# print(protest_list)
# print(year_list)
# print(len(country_list))
# print(number_of_years)
# print(average_protests)
# print(country_to_avg_protest)

## country:average protest bar chart
# convert country:avg protest dic to dataframe
df_avg_protest = pd.DataFrame(list(country_to_avg_protest.items()), columns=['country', 'avg_protests'])
# print(df_avg_protest)
# uncomment below to save avg_protest to csv
# df_avg_protest.to_csv('avg_protests.csv')

# plot horizontal bar chart
df_avg_protest.reset_index().plot(x='country', y='avg_protests', kind='barh', title='Avg Protests per Year by Country', figsize=(60, 45))
plt.title('Avg Protests per Year by Country', fontsize=35)
plt.ylabel('Country', fontsize=25)
plt.xlabel('Average Protests from 2000', fontsize=25)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
# uncomment below to show graph
# plt.show()
# uncomment below to save graph as .png
# plt.savefig('avg_protests_by_country.png')
