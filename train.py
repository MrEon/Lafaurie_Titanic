import pandas as pd
import math
import matplotlib as mp
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sb

def colonToList(colname,dtframe):
    return dtframe[colname].tolist()

if __name__ == '__main__':
    fig = mp.pyplot.figure()
    ax = fig.add_subplot(111, projection= '3d')
    data = pd.read_csv('train.csv',header=0)
    print(list(data.columns.values))
    survived = colonToList("Survived",data)
    pclass = colonToList("Pclass",data)
    age = colonToList("Age",data)
    print(len(survived),len(pclass),len(age))

    print(age)
    ax.scatter(survived,pclass,age,zdir='z',s=20,c=None)
    ax.set_xlabel('Survival')
    ax.set_ylabel('Passenger Class')
    ax.set_zlabel('Age')
    mp.pyplot.show()