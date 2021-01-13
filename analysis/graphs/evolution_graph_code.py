import pandas as pd
import matplotlib.pyplot as plt

## initialising dataframe
protests_data = pd.read_csv("mass-mobilization-protest-data-QueryResult.csv")
# print(protests_data)
df = pd.DataFrame(protests_data)

## editing dataframe
# replacing names
df.replace(to_replace='Congo Brazzaville', value='Republic of the Congo', inplace=True)
df.replace(to_replace='Congo Kinshasa', value='Democratic Republic of the Congo', inplace=True)
df.replace(to_replace='Bosnia', value='Bosnia and Herzegovina', inplace=True)
df.replace(to_replace='Slovak Republic', value='Slovakia', inplace=True)
# deleting countries that do not exist anymore
df = df[df.country != 'Yugoslavia']
df = df[df.country != 'Serbia and Montenegro']
df.reset_index(inplace=True)
# uncomment below to save cleaned csv file
# df.to_csv("protests_data_filtered.csv")
#print(df)


# extract dataframes from df
#countries = df.loc[:, 'country']
years = df.loc[:, 'year']
has_protest = df.loc[:, 'protest']
countries_years = df.loc[:, ['country', 'year']]
# print(years)
# print(countries)

## initialising lists & dictionaries
#country_list = []  # list of countries
#number_of_years = [] # list of number of years data is provided
year_list = [] #list of years
protest_list = []  # list of number of protests
#average_protests = []  # list of average protests
#country_to_protest = {}  # dictionary of country:total protests
#country_to_avg_protest = {}  # dic of country:average protests
year_to_protest = {} # dic of year: total protests that year



## appending lists and dictionaries
# making year list
for year in years:
    if year not in year_list:
        year_list.append(year)
year_list = sorted(year_list)
#print(year_list)



# initialising year: total protests that year dic
for year in year_list:
    year_to_protest[year] = 0


# counting total protests and adding to dic
for i in range(len(years)):
    if has_protest[i] == 1:
        # print(i, countries[i])
        year_to_protest[years[i]] += 1


# making protest list
for i in range(len(year_list)):
    protest_list.append(year_to_protest[year_list[i]])

df_year_to_protest = pd.DataFrame(list(year_to_protest.items()), columns=['year', 'protests'])


plt.style.use('ggplot')
plt.plot(list(year_to_protest.keys()),list(year_to_protest.values()))

plt.title('Total number of protests around the world since 2000', fontsize=15)
plt.ylabel('Number of protests', fontsize=15)
plt.xlabel('Year', fontsize=15)
#plt.grid(b=True, which='major', color='#666666', linestyle='-')
