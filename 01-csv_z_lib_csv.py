import csv

OPEN_FILE = "weather_data.csv"

with open(OPEN_FILE) as data_file:
    weather_data = csv.reader(data_file)
    day_list = []
    temp_list = []
    condit_list = []
    rainmm_list = []
    all_lists = [day_list, temp_list, condit_list, rainmm_list]

    for row in weather_data:
        if row[0] != "day" or row[1] != "temperature" or row[2] != "condition" or row[3] != "rain_mm":
            day_list.append(row[0])
            temp_list.append(int(row[1]))
            condit_list.append(row[2])
            rainmm_list.append(int(row[3]))


def print_test():
    print(day_list)
    print(temp_list)
    print(condit_list)
    print(rainmm_list)
    print('\n')
    for i in range(0, 4):
        print(all_lists[i])






