import pandas as pd
data = pd.read_csv("diamonds.csv", index_col=0)

#змінюємо типи
pd.to_numeric(data['carat'], downcast='float')
pd.to_numeric(data['depth'], downcast='float')
pd.to_numeric(data['table'], downcast='float')
pd.to_numeric(data['price'], downcast='float')
pd.to_numeric(data['x'], downcast='float')
pd.to_numeric(data['y'], downcast='float')
pd.to_numeric(data['z'], downcast='float')
data['cut'].astype(str)
data['color'].astype(str)
data['clarity'].astype(str)
#Удаляем дубликаты
data.drop_duplicates(subset=['carat','cut','color','clarity','depth','table'], keep=False)
#Считаем количество пустых ячеек в таблице
count=0
for i in data:
    if (data[i].isnull().sum()!=0):
        count=count+1
#Видем, что пустых ячеек нет
# print(count)

#Видалення зайвих параметрів
data = data.drop(columns='x')
data = data.drop(columns='y')
data = data.drop(columns='z')
data = data.drop(columns='depth')
data = data.drop(columns='table')

#plt.show()

colors_=pd.get_dummies(data['color'])
clarity_=pd.get_dummies(data['clarity'])
cut_=pd.get_dummies(data['cut'])

data=data.join(cut_)
data=data.join(clarity_)
data=data.join(colors_)

data = data.drop(columns='color')
data = data.drop(columns='cut')
data = data.drop(columns='clarity')
