import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm

unemployment_data = pd.read_csv('unemployment_data_filtered.csv')
protests_data = pd.read_csv('protests_data_filtered.csv')
corruption_data = pd.read_csv('corruption_data_filtered.csv')

df_protests = pd.DataFrame(protests_data)
df_unemployment = pd.DataFrame(unemployment_data)
df_corruption = pd.DataFrame(corruption_data)

country_name = 'Afghanistan'

# change country below
protests_country = protests_data.loc[protests_data['country'] == country_name]
# print(protests_country)


protests_country = protests_country[['year', 'protest']]
# print(protests_country)

years = protests_country.loc[:, 'year']
years = years.reset_index(drop=True)
year_list = []
has_protest = protests_country.loc[:, 'protest']
has_protest = has_protest.reset_index(drop=True)
print(has_protest[0])
for year in years:
    if year not in year_list:
        year_list.append(year)
year_list.sort()
# print(year_list)

# initialise dictionary to 0
year_to_protests = {}
for year in year_list:
    year_to_protests[year] = 0
# print(year_to_protests)

# counting total protests and adding to dic
for i in range(len(has_protest)):
    if has_protest[i] == 1:
        # print(i, countries[i])
        year_to_protests[years[i]] += 1
print(year_to_protests)
df_years_protests = pd.DataFrame(list(year_to_protests.items()), columns=['year', 'protests'])
# print(df_years_protests)

## unemployment data
# print(unemployment_data)
# change country below
unemployment_country = unemployment_data[unemployment_data['country'] == country_name].T
unemployment_country.reset_index(inplace=True)
unemployment_country.drop([0, 1], inplace=True)
unemployment_country.reset_index(inplace=True)
unemployment_country.drop('level_0', axis=1, inplace=True)
unemployment_country.columns = ['year', 'unemployment_rate']
# print(unemployment_country)

df = df_years_protests
df['unemployment_rate'] = unemployment_country['unemployment_rate']
# print(protests_and_unemployment)

## corruption data
corruption_country = corruption_data[corruption_data['country'] == country_name].T
corruption_country.reset_index(inplace=True)
corruption_country.drop([0, 1, 2, 3], inplace=True)
corruption_country.reset_index(inplace=True)
corruption_country.drop('level_0', axis=1, inplace=True)
corruption_country.columns = ['year', 'CPI_Score']
corruption_country.sort_values(by=['year'], ascending=True, inplace=True)
corruption_country.reset_index(inplace=True)
# print(corruption_country)
df['CPI_Score'] = corruption_country['CPI_Score']


print(df)

plt.scatter(df['unemployment_rate'], df['protests'], color='green')
plt.title('Protests Vs Unemployment Rate', fontsize=14)
plt.xlabel('Unemployment Rate', fontsize=14)
plt.ylabel('Number of Protests', fontsize=14)
plt.grid(True)
# uncomment below to show graph
# plt.show()
# uncomment below to save graph as .png
# plt.savefig('unemployment_vs_protests_' + country_name + '.png')

plt.scatter(df['CPI_Score'], df['protests'], color='green')
plt.title('Protests Vs CPI Score', fontsize=14)
plt.xlabel('CPI Score', fontsize=14)
plt.ylabel('Number of Protests', fontsize=14)
plt.grid(True)
# uncomment below to show graph
# plt.show()
# uncomment below to save graph as .png
# plt.savefig('corruption_vs_protests_' + country_name + '.png')

# X = df[['unemployment_rate']]
# Y = df['protests']
#
# # with sklearn
# reg = linear_model.LinearRegression()
# reg.fit(X, Y)
#
# print('Intercept: \n', reg.intercept_)
# print('Coefficients: \n', reg.coef_)
# print('Coefficient of determination: \n', r2_score())
# # prediction with sklearn
# # New_Interest_Rate = 2.75
# # New_Unemployment_Rate = 5.3
# # print('Predicted Stock Index Price: \n', regr.predict([[New_Interest_Rate, New_Unemployment_Rate]]))
#
# # with statsmodels
# X = sm.add_constant(X)  # adding a constant
#
# model = sm.OLS(Y, X).fit()
# predictions = model.predict(X)
#
# print_model = model.summary()
# print(print_model)
