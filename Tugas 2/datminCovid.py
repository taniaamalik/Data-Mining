import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics

data_read = pd.read_csv('D:/Tania/UB/Semester 6/DATMIN/Tugas/Tugas 2/covid_19_data.csv', header = 0, usecols = ["Confirmed", "Deaths", "Recovered"])

confirmed_mean = data_read["Confirmed"].mean()
confirmed_median = data_read["Confirmed"].median()
confirmed_mode = data_read["Confirmed"].mode()
confirmed_min = data_read["Confirmed"].min()
confirmed_max = data_read["Confirmed"].max()
confirmed_midrange = (confirmed_min+confirmed_max)/2
confirmed_q1 = data_read["Confirmed"].quantile(0.25)
confirmed_q2 = data_read["Confirmed"].quantile(0.5)
confirmed_q3 = data_read["Confirmed"].quantile(0.75)
confirmed_iqr = confirmed_q3 - confirmed_q1
low_outlier = confirmed_q1 - (1.5 * confirmed_iqr)
up_outlier = confirmed_q3 + (1.5 * confirmed_iqr)

deaths_mean = data_read["Deaths"].mean()
deaths_median = data_read["Deaths"].median()
deaths_mode = data_read["Deaths"].mode()
deaths_min = data_read["Deaths"].min()
deaths_max = data_read["Deaths"].max()
deaths_midrange = (deaths_min+deaths_max)/2
deaths_q1 = data_read["Deaths"].quantile(0.25)
deaths_q2 = data_read["Deaths"].quantile(0.5)
deaths_q3 = data_read["Deaths"].quantile(0.75)
deaths_iqr = deaths_q3 - deaths_q1
low_outlier = deaths_q1 - (1.5 * deaths_iqr)
up_outlier = deaths_q3 + (1.5 * deaths_iqr)

recovered_mean = data_read["Recovered"].mean()
recovered_median = data_read["Recovered"].median()
recovered_mode = data_read["Recovered"].mode()
recovered_min = data_read["Recovered"].min()
recovered_max = data_read["Recovered"].max()
recovered_midrange = (recovered_min+recovered_max)/2
recovered_q1 = data_read["Recovered"].quantile(0.25)
recovered_q2 = data_read["Recovered"].quantile(0.5)
recovered_q3 = data_read["Recovered"].quantile(0.75)
recovered_iqr = recovered_q3 - recovered_q1
low_outlier = recovered_q1 - (1.5 * recovered_iqr)
up_outlier = recovered_q3 + (1.5 * recovered_iqr)

print("Confirmed mean : " + str(confirmed_mean))
print("Confirmed median : " + str(confirmed_median))
print("Confirmed mode : " + str(confirmed_mode))
print("Confirmed min : " + str(confirmed_min))
print("Confirmed max : " + str(confirmed_max))
print("Confirmed midrange : " + str(confirmed_midrange))
print("Confirmed Q1 : " + str(confirmed_q1))
print("Confirmed Q2 : " + str(confirmed_q2))
print("Confirmed Q3 : " + str(confirmed_q3))
print("=================================================")

print("Deaths mean : " + str(deaths_mean))
print("Deaths median : " + str(deaths_median))
print("Deaths mode : " + str(deaths_mode))
print("Deaths min : " + str(deaths_min))
print("Deaths max : " + str(deaths_max))
print("Deaths midrange : " + str(deaths_midrange))
print("Deaths Q1 : " + str(deaths_q1))
print("Deaths Q2 : " + str(deaths_q2))
print("Deaths Q3 : " + str(deaths_q3))
print("=================================================")

print("Recovered mean : " + str(recovered_mean))
print("Recovered median : " + str(recovered_median))
print("Recovered mode : " + str(recovered_mode))
print("Recovered min : " + str(recovered_min))
print("Recovered max : " + str(recovered_max))
print("Recovered midrange : " + str(recovered_midrange))
print("Recovered Q1 : " + str(recovered_q1))
print("Recovered Q2 : " + str(recovered_q2))
print("Recovered Q3 : " + str(recovered_q3))