import pandas as pd

corruption_data = pd.read_csv("CPI2019.csv")
df_corruption = pd.DataFrame(corruption_data)
countries_corruption = df_corruption.loc[:, 'country']

file_name = ["CPI-2011-new_200601_104308.csv", "CPI-2010-new_200601_105629.csv", "CPI-2009-new_200601_120052.csv", "CPI-Archive-2008-2.csv", "CPI-2007-new_200602_092501.csv", "CPI-2006-new_200602_095933.csv", "CPI-2005_200602_104136.csv", "CPI-2004_200602_110140.csv", "CPI-2003_200602_113929.csv", "CPI-2002_200602_115328.csv", "CPI-2001_200603_082938.csv", "CPI-2000_200603_083012.csv"]
column_name = ['CPI Score 2011', 'CPI Score 2010', 'CPI Score 2009', 'CPI Score 2008', 'CPI Score 2007', 'CPI Score 2006', 'CPI Score 2005', 'CPI Score 2004', 'CPI Score 2003', 'CPI Score 2002', 'CPI Score 2001', 'CPI Score 2000']
for i in range(len(file_name)):
    corruption_num = pd.read_csv(file_name[i])
    df_corruption_num = pd.DataFrame(corruption_num)
    countries_num = df_corruption_num.loc[:, 'country']
    cpi_score_num = pd.Series([])
    values = pd.Series([])
    for x in range(len(countries_num)):
        values[x] = corruption_num.loc[x, 'score'] * 10
    corruption_num['value'] = values
    for j in range(len(countries_corruption)):
        for k in range(len(countries_num)):
            if countries_num[k] == countries_corruption[j]:
                cpi_score_num[j] = df_corruption_num.loc[k, 'value']
    # print(cpi_score_num)
    df_corruption.insert(i+11, column_name[i], cpi_score_num)
# print(df_corruption)
# uncomment below to save as .csv
df_corruption.to_csv('corruption_data_final.csv')