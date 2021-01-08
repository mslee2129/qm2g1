import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import seaborn as sn
import plotly.graph_objects as go

unemployment_data = pd.read_csv('unemployment_data_filtered.csv')
protests_data = pd.read_csv('protests_data_filtered.csv')
corruption_data = pd.read_csv('corruption_data_filtered.csv')

df_protests = pd.DataFrame(protests_data)
df_unemployment = pd.DataFrame(unemployment_data)
df_corruption = pd.DataFrame(corruption_data)

country_list = ['Algeria', 'Bahrain', 'Egypt', 'Iraq', 'Iran', 'Kuwait', 'Lebanon', 'Libya', 'Morocco', 'Oman',
                'Saudi Arabia', 'Sudan', 'Syria', 'Tunisia', 'Yemen']
country_to_r2 = {}
p_list = []
r2_list = []
intercept_list = []
coeff_list = []

for country in country_list:
    country_name = country

    # change country below
    protests_country = df_protests.loc[df_protests['country'] == country_name]
    # print(protests_country)

    protests_country = protests_country[['year', 'protest']]
    protests_country = protests_country[protests_country.year >= 2000]
    # print(protests_country)

    years = protests_country.loc[:, 'year']
    years = years.reset_index(drop=True)
    year_list = []
    has_protest = protests_country.loc[:, 'protest']
    has_protest = has_protest.reset_index(drop=True)
    # print(has_protest[0])
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
    # print(year_to_protests)
    df_years_protests = pd.DataFrame(list(year_to_protests.items()), columns=['year', 'protests'])
    # print(df_years_protests)

    df = df_years_protests

    ## unemployment data
    unemployment_country = unemployment_data[unemployment_data['country'] == country_name].T
    unemployment_country.reset_index(inplace=True)
    unemployment_country.drop([0, 1, 2, 3], inplace=True)
    unemployment_country.reset_index(inplace=True)
    unemployment_country.drop('level_0', axis=1, inplace=True)
    # print(unemployment_country)
    unemployment_country.columns = ['year', 'unemployment_rate']
    unemployment_country.sort_values(by=['year'], ascending=True, inplace=True)
    unemployment_country.reset_index(inplace=True)
    unemployment_country.drop('index', axis=1, inplace=True)
    print(unemployment_country)
    df['unemployment_rate'] = unemployment_country['unemployment_rate']
    df.dropna(inplace=True)

    # print(df)

    df = df.astype(float)

    sn.regplot(x="protests", y="unemployment_rate", data=df, scatter=True, fit_reg=True)
    plt.title(country + ' Protests vs Unemployment rate since 2000')
    plt.grid(True)
    # plt.savefig(country + '_unemployment_regression_2000.png')
    # plt.show()

    Y = df['unemployment_rate']
    X = np.array(df['protests']).reshape((-1, 1))

    X = sm.add_constant(X)
    mod = sm.OLS(Y, X)
    res = mod.fit()
    p_values = res.pvalues[1]
    r2_values = res.rsquared
    intercept = res.params[0]
    coeff = res.params[1]
    param = res.params
    # print(country)
    # print('Intercept: ', param[0])
    # print('Coefficient: ', param[1])
    # print('R2: ', r2_values)
    # print('P-value: ', p_values)
    # print(res.summary())
    p_list.append(round(p_values, 5))
    r2_list.append(round(r2_values, 5))
    intercept_list.append(round(intercept, 5))
    coeff_list.append(round(coeff, 5))

    # prediction with sklearn
    # New_Interest_Rate = 2.75
    # New_Unemployment_Rate = 5.3
    # print('Predicted Stock Index Price: \n', regr.predict([[New_Interest_Rate, New_Unemployment_Rate]]))

    # with statsmodels
    # X = sm.add_constant(X)  # adding a constant
    #
    # model = sm.OLS(Y, X).fit()
    # predictions = model.predict(X)
    #
    # print_model = model.summary()
    # print(print_model)
print(r2_list)
print(p_list)
fig = go.Figure(data=[go.Table(header=dict(values=['Country', 'Coefficient 2000', 'Intercept 2000', 'p-values 2000', 'r2 values 2000',]),
                 cells=dict(values=[country_list, coeff_list, intercept_list, p_list, r2_list]))
                     ])
fig.show()