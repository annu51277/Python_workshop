import pandas as pd



#
#
# data = pd.read_csv("weather_data.csv")
#
# # print(type(data)) DataFrame
# # series= data["temp"].to_list()
# # # print(type(data["temp"])) Series
# # print(data["temp"].mean())
# # print(data["temp"].max())
# # print(f'The average temperature is: {sum(series)/len(series)}')
# # print(data[data.day == 'Monday'])
# # print(f'{data[data.temp == data.temp.max()]}')
#
# monday = data[data.day == 'Monday']
# print(monday)
# # °F = °C × (9/5) + 32 Formula to convert celsius to Fahrenheit .
# print(f'{monday.temp[0]*(9/5)+32}°F')
#
#
# data_dict = {
#     'students': [
#         'Amy', 'James', 'Sarah' ],
#     'Scores': [
#         77, 88, 92  ]
# }
#
# print(data_dict['students'][0])
# print(data_dict['students'].index('Amy'))
#
#
# data = pd.DataFrame(data_dict)
# data.to_csv('data_dict.csv')

squirrel_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241127.csv')

colors = {'Squirrel_Colors' : ['Gray','Cinnamon','Black'] , 'Count' : []
         }
count_color = []

for i in range(0,len(colors['Squirrel_Colors'])):
    Squirrel_Color = squirrel_data[squirrel_data['Primary Fur Color'] == colors['Squirrel_Colors'][i]]
    count_color.append(Squirrel_Color['Unique Squirrel ID'].nunique())
colors['Count'] = count_color

data = pd.DataFrame(colors)
data.to_csv('Squirrel_count_color.csv',index=False)
print(data)


