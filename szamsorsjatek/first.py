#import libraries
import seaborn as sns
import pandas
import matplotlib.pyplot as plt

#implementations
sns.set_style("darkgrid")
sns.set_theme(style='white', font_scale=1.25)
csv = pandas.read_csv('arbevetel.csv')
fig, axes = plt.subplots(1, 3)

#lineplots

#1
sns.lineplot(x = "naptari_ev_het", y = "arbevetel", data = csv, marker='*',
              color='limegreen', linewidth=2, markerfacecolor='b', markersize=8, ax = axes[0]) 

#2
sns.lineplot(x = 'jatekar', y = 'arbevetel', data = csv, marker='*',
              color='limegreen', linewidth=3, markerfacecolor='r', markersize=8, ax = axes[1]) 
 
#3
sns.lineplot(x = 'naptari_ev_het', y = 'fonyeremeny', data = csv, marker='*',
              color='limegreen', linewidth=4, markerfacecolor='y', markersize=8, ax = axes[2]) 

#lineplots settings 

axes[0].set(title='1', xlabel='--Dátum (Év-Hét)--', ylabel='--Árbevétel (Ft)--')
axes[1].set(title='2', xlabel='--Játék ára (Ft)--', ylabel='--Árbevétel (Ft)--')
axes[2].set(title='3', xlabel='--Dátum (Év-Hét)--', ylabel='--Főnyeremény (MFt)--')
plt.suptitle("Számsorsjáték - Heti - kimutatások, 2019-01-2021-52:")

#open
plt.show() 
