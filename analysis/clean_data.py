## cleaning all related datasets
import pandas as pd

# download from datasets file
unemployment_data = pd.read_csv("API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_1622103.csv")
protests_data = pd.read_csv("mass-mobilization-protest-data-QueryResult.csv")
corruption_data = pd.read_csv("corruption_data_final.csv")

df_unemployment = pd.DataFrame(unemployment_data)
df_protests = pd.DataFrame(protests_data)
df_corruption = pd.DataFrame(corruption_data)

## replacing & deleting values
# replacing values in unemployment_data
df_unemployment = df_unemployment[['Country Name', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', r'2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']]
df_unemployment.rename(columns={'Country Name': 'country'}, inplace=True)
df_unemployment.replace(to_replace='Cabo Verde', value='Cape Verde', inplace=True)
df_unemployment.replace(to_replace="Cote d'Ivoire", value='Ivory Coast', inplace=True)
df_unemployment.replace(to_replace='Egypt, Arab Rep.', value='Egypt', inplace=True)
df_unemployment.replace(to_replace='Gambia, The', value='Gambia', inplace=True)
df_unemployment.replace(to_replace='Iran, Islamic Rep.', value='Iran', inplace=True)
df_unemployment.replace(to_replace='Kyrgyz Republic', value='Kyrgyzstan', inplace=True)
df_unemployment.replace(to_replace='Korea, Rep.', value='South Korea', inplace=True)
df_unemployment.replace(to_replace="Korea, Dem. People’s Rep.", value='North Korea', inplace=True)
df_unemployment.replace(to_replace='Russian Federation', value='Russia', inplace=True)
df_unemployment.replace(to_replace='Slovak Republic', value='Slovakia', inplace=True)
df_unemployment.replace(to_replace='Eswatini', value='Swaziland', inplace=True)
df_unemployment.replace(to_replace='Timor-Leste', value='Timor Leste', inplace=True)
df_unemployment.replace(to_replace='Yemen, Rep.', value='Yemen', inplace=True)
df_unemployment.replace(to_replace='Lao PDR', value='Laos', inplace=True)
df_unemployment.replace(to_replace='Syrian Arab Republic', value='Syria', inplace=True)
df_unemployment.replace(to_replace='Venezuela, RB', value='Venezuela', inplace=True)
df_unemployment.dropna(inplace=True)

# replacing values in protests_data
df_protests.replace(to_replace='Congo Brazzaville', value='Congo, Rep.', inplace=True)
df_protests.replace(to_replace='Congo Kinshasa', value='Congo, Dem. Rep.', inplace=True)
df_protests.replace(to_replace='Bosnia', value='Bosnia and Herzegovina', inplace=True)
df_protests.replace(to_replace='Macedonia', value='North Macedonia', inplace=True)
df_protests.replace(to_replace='Slovak Republic', value='Slovakia', inplace=True)
df_protests.replace(to_replace='United Arab Emirate', value='United Arab Emirates', inplace=True)
# deleting countries that do not exist anymore
df_protests = df_protests[df_protests.country != 'Yugoslavia']
df_protests = df_protests[df_protests.country != 'Serbia and Montenegro']

# replacing values in corruption_data
df_corruption.replace(to_replace='Cabo Verde', value='Cape Verde', inplace=True)
df_corruption.replace(to_replace='Congo', value='Congo, Rep.', inplace=True)
df_corruption.replace(to_replace="Cote d'Ivoire", value='Ivory Coast', inplace=True)
df_corruption.replace(to_replace="Democratic Republic of the Congo", value='Congo, Dem. Rep.', inplace=True)
df_corruption.replace(to_replace='Eswatini', value='Swaziland', inplace=True)
df_corruption.replace(to_replace='Guinea Bissau', value='Guinea-Bissau', inplace=True)
df_corruption.replace(to_replace='Guinea Bissau', value='Guinea-Bissau', inplace=True)
df_corruption.replace(to_replace='Korea, South', value='South Korea', inplace=True)
df_corruption.replace(to_replace='Korea, North', value='North Korea', inplace=True)
df_corruption.replace(to_replace='Korea, North', value='North Korea', inplace=True)
df_corruption.replace(to_replace='Timor-Leste', value='Timor Leste', inplace=True)


# initialise lists to use in loop
countries_protests = df_protests.loc[:, 'country']
countries_unemployment = df_unemployment.loc[:, 'country']
countries_corruption = df_corruption.loc[:, 'country']
countries_protests_list = countries_protests.values.tolist()
countries_unemployment_list = countries_unemployment.values.tolist()
countries_corruption_list = countries_corruption.values.tolist()

# delete countries in unemployment data that aren't in protests data
for country in countries_unemployment_list:
    if country not in countries_protests_list:
        df_unemployment = df_unemployment[df_unemployment.country != country]
df_unemployment.sort_values('country', inplace=True)
df_unemployment.reset_index(inplace=True)
df_unemployment.drop('index', axis=1, inplace=True)
# uncomment below to save to .csv
# df_unemployment.to_csv('unemployment_data_filtered.csv')

# delete countries in protests data that aren't in unemployment data
df_protests.reset_index(inplace=True)
for country in countries_protests_list:
    if country not in countries_unemployment_list:
        df_protests = df_protests[df_protests.country != country]
df_protests.reset_index(inplace=True)
df_protests.sort_values('country', inplace=True)
df_protests.drop('index', axis=1, inplace=True)
df_protests.drop('level_0', axis=1, inplace=True)
# uncomment below to save cleaned csv file
# df_protests.to_csv("protests_data_filtered.csv")

# delete countries in corruption data that are not in the other two
for country in countries_corruption_list:
    if country not in countries_protests_list or country not in countries_unemployment_list:
        df_corruption = df_corruption[df_corruption.country != country]
df_corruption.sort_values('country', inplace=True)
df_corruption.reset_index(inplace=True)
df_corruption.drop('index', axis=1, inplace=True)
df_corruption.drop('Unnamed: 0', axis=1, inplace=True)
# uncomment below to save as csv file
# df_corruption.to_csv("corruption_data_filtered.csv")
