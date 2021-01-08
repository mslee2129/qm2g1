import pandas as pd
import matplotlib.pyplot as plt

protests_data = pd.read_csv('protests_data_filtered.csv')
corruption_data = pd.read_csv('corruption_data_filtered.csv')
unemployment_data = pd.read_csv('unemployment_data_filtered.csv')

df_protests = pd.DataFrame(protests_data)
df_corruption = pd.DataFrame(corruption_data)
df_unemployment = pd.DataFrame(unemployment_data)

country_list = ['Algeria', 'Bahrain', 'Egypt', 'Iraq', 'Iran', 'Kuwait', 'Lebanon', 'Libya', 'Morocco', 'Oman',
                'Saudi Arabia', 'Sudan', 'Syria', 'Tunisia', 'Yemen']

for country in country_list:
    protests_country = df_protests.loc[df_protests['country'] == country]
    # print(protests_country)

    protests_country = protests_country[['year', 'protest']]
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

    unemployment_country = unemployment_data[unemployment_data['country'] == country].T
    unemployment_country.reset_index(inplace=True)
    unemployment_country.drop([0, 1, 2, 3], inplace=True)
    unemployment_country.reset_index(inplace=True)
    unemployment_country.drop('level_0', axis=1, inplace=True)
    # print(unemployment_country)
    unemployment_country.columns = ['year', 'unemployment_rate']
    unemployment_country.sort_values(by=['year'], ascending=True, inplace=True)
    unemployment_country.reset_index(inplace=True)
    unemployment_country.drop('index', axis=1, inplace=True)
    unemployment_country.dropna(inplace=True)
    # print(unemployment_country)

    corruption_country = corruption_data[corruption_data['country'] == country].T
    corruption_country.reset_index(inplace=True)
    corruption_country.drop([0, 1, 2, 3], inplace=True)
    corruption_country.reset_index(inplace=True)
    corruption_country.drop('level_0', axis=1, inplace=True)
    corruption_country.columns = ['year', 'CPI_Score']
    corruption_country.sort_values(by=['year'], ascending=True, inplace=True)
    corruption_country.reset_index(inplace=True)
    print(corruption_country)

    # plt.plot(year_list, df_years_protests['protests'])
    # plt.title(country + ' Protests')
    # plt.xlabel('Year')
    # plt.ylabel('No. of Protests')
    # plt.savefig(country + '_protests.png')
    # plt.show()

    plt.plot(year_list, corruption_country['CPI_Score'])
    plt.title(country + ' CPI Scores')
    plt.xlabel('Year')
    plt.ylabel('CPI Score')
    plt.savefig(country + '_CPI_score.png')
    plt.show()

    # year_list.remove(2000)
    # year_list.remove(2001)
    # plt.plot(year_list, unemployment_country['unemployment_rate'])
    # plt.title(country + ' Unemployment Rate')
    # plt.ylabel('Unemployment Rate')
    # plt.xlabel('Year')
    # plt.savefig(country + '_unemployment.png')
    # plt.show()