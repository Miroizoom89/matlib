# %%
import pandas as pd
import matplotlib.pyplot as plt
# %%

header_names=['Time','Temp1','Temp2','Humi','Press']
df = pd.read_csv('Prokal/prokal.csv', header=None, skiprows=1, names=header_names)
df = df.iloc[ :-1, :]
# %%
def basic_plot_implenet_1():
    plt.figure(figsize=(16,10))

    val_temp = ['Temp1', 'Temp2']
    for x in df:
        if x in val_temp:
            plt.plot(df.Time, df[x], marker='.')


    plt.xticks(df.Time[::10])
    plt.xlabel('time interval 4 min')
    plt.ylabel('temperature')

    plt.legend(['temp1','temp2'])

    plt.show()

basic_plot_implenet_1()

# %%
def basic_plot_implenet_2():
    plt.figure(figsize=(16,10))

    val_temp = ['Humi']
    for x in df:
        if x in val_temp:
            plt.plot(df.Time, df[x], marker='.')


    plt.xticks(df.Time[::10])
    plt.xlabel('time interval 4 min')
    plt.ylabel('temperature')

    plt.legend(['Humi'])

    plt.show()

basic_plot_implenet_2()
# %%
def basic_plot_implenet_3():
    plt.figure(figsize=(16,10))

    val_temp = ['Press']
    for x in df:
        if x in val_temp:
            plt.plot(df.Time, df[x], marker='.')


    plt.xticks(df.Time[::10])
    plt.xlabel('time interval 4 min')
    plt.ylabel('temperature')

    plt.legend(['Press'])

    plt.show()

basic_plot_implenet_3()
# %%
