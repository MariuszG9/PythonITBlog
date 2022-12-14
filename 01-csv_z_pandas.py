import pandas

data_frame = pandas.read_csv("weather_data.csv")
print(data_frame["temperature"])
