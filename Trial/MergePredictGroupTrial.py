import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
print(df)
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AC'))
merged_df = pd.merge(df,df2,how='outer',on=['A'])
df = df.set_index('A').combine_first(df.set_index('A')).reset_index()
print(merged_df)

data = pd.read_csv('/Users/srikaavya/PycharmProjects/Diva/Project/static/data/GroupedCount.csv')
data_predict = pd.read_csv('/Users/srikaavya/PycharmProjects/Diva/Project/static/data/Prediction.csv')

data = pd.DataFrame(data=data)
data_predict = pd.DataFrame(data=data_predict)
print(data.dtypes)
print(data_predict.dtypes)
#data.merge(data_predict, outer_on='Date', right_index=True)
merged_df = pd.merge(data,data_predict,how='outer',on=['Date','District'])
print(merged_df.info())
merged_df.to_csv(r'/Users/srikaavya/PycharmProjects/Diva/Project/static/data/Merged_Prediction.csv', index = False, header=True)