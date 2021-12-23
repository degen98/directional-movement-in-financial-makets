ARIMA based Code:
	import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.arima_model import ARIMA 
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.stattools import adfuller

x=pd.read_csv("AAPL.csv",index_col=[0])
x1=x.round(2)
x2=x1['close']
plt.plot(x2)
x3=x2.rolling(window=4).mean()
x3=x3.dropna()
n=int(len(x3)*0.8)
x_train=x3[:n]
plt.plot(x_train)
series=x3.dropna()

plot_acf(series)
plt.xlabel('Lags (Days)')
plt.show()

plot_pacf(spy_close_diff_1)
plt.xlabel('Lags (Days)')
plt.show()

spy_close_diff_1 = series.diff()
spy_close_diff_1.dropna(inplace=True)
plot_acf(spy_close_diff_1)
plt.xlabel('Lags (Days)')
plt.show()

plot_pacf(spy_close_diff_1)
plt.xlabel('Lags (Days)')
plt.show()

spy_arima = ARIMA(x_train,order=(1,1,1))
spy_arima_fit = spy_arima.fit(disp=0)
print(spy_arima_fit.summary())

x_test=x3[n:]
x_test=x_test.dropna()
y=model_fit.forecast(steps=251)
plt.figure(figsize=(16,8))
plt.plot(x_test,label="Actual",color='red')
result=adfuller(x2)
result[1]
from tkinter import * 
root = Tk()  
root.title("STOCK PRICE PREDICTION")
root.geometry("900x700+0+0") 
root['bg'] = '#49A'  
Label(root, text="WELCOME",fg = "light blue",bg = "green",font = "Helvetica 24 bold italic").pack(pady=20,fill=X) 
Label(root, text="STOCK PRICE PREDICTION PROJECT",fg = "light green",bg = "dark green",font = "Helvetica 24 bold italic").pack(pady=20,fill=X)
l1=Label(root, text="Enter number of days: ",bg = "pink",font = "Helvetica 18 bold italic",justify=LEFT)
l1.place(x=40,y=200)
endays=Entry(root,width=50)
endays.place(x= 350,y=200,height = 38)

B = Button(root, text ="Predict",font = "Helvetica 14 bold italic", command = lambda : helloCallBack(endays.get()))
B.config(width=15, height=1)
B.place(x=700,y=200)

frame1 = Frame(root) 
frame1.pack(pady = 20)
root.mainloop()
