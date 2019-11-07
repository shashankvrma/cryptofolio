import requests
import json
from tkinter import *



def my_portfolio():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=e2c48ed7-ace4-4849-82f4-7634f2a4747d")
    api = json.loads(api_request.content)
    coins = [
              { 
                "symbol":"BTC",      
                "no_of_coins": 2,
                "price_per_coin": 3000
              },  
              { 
                "symbol":"XRP",      
                "no_of_coins": 100,
                "price_per_coin": 0.40
              }      
            ]
    totalvalue = 0
    totalcurrentvalue = 0
    
    coin_row = 4
    for i in range(0,5): 
        for coin in coins:
            if(api["data"][i]["symbol"] == coin["symbol"]):
                     current_value = coin["no_of_coins"]*api["data"][i]["quote"]["USD"]["price"]
                     buying_value = coin["no_of_coins"] * coin["price_per_coin"]
                     if(current_value < buying_value):
                         status = 'LOSS'
                         amount = buying_value - current_value
                     elif(current_value > buying_value):
                         status = 'PROFIT'
                         amount = current_value - buying_value
                     else:
                         status = 'neutral'
                         amount = 0
                       
                     buying_value = str(buying_value)                 
                     L1 = Label(window,text = api["data"][i]["name"],fg = 'darkred' , bg = 'white' ,padx = 2, pady= 2, relief = 'sunken',font = 'Lato 11')
                     L1.grid(row = coin_row, column = 0,sticky = N+S+E+W)
                    
                     L2 = Label(window,text = coin["no_of_coins"],fg = 'black' , bg = 'white' ,padx = 2, pady= 2, relief = 'sunken',font = 'Lato 11')
                     L2.grid(row = coin_row, column = 1,sticky = N+S+E+W)
                    
                     L3 = Label(window,text = '$' + buying_value,fg = 'black' , bg = 'white' ,padx = 2, pady= 2, relief = 'sunken',font = 'Lato 11')
                     L3.grid(row = coin_row, column = 2,sticky = N+S+E+W)
                    
                     L4 = Label(window,text = "${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]),fg = 'black' , bg ='white' ,padx = 2, pady= 2, relief = 'sunken',font = 'Lato 11')
                     L4.grid(row = coin_row, column = 3,sticky = N+S+E+W)
                    
                     if(status == 'PROFIT'):
                         L5 = Label(window,text = status,fg = 'white' , bg = 'green' ,padx = 2, pady= 2, relief = 'sunken',font = 'Lato 11')
                         L5.grid(row = coin_row, column = 4,sticky = N+S+E+W)
                     elif(status == 'LOSS'):
                         L5 = Label(window,text = status,fg = 'white' , bg = 'red' ,padx = 2, pady= 2, relief = 'sunken',font = 'Lato 11')
                         L5.grid(row = coin_row, column = 4,sticky = N+S+E+W)
                     else:
                         L5 = Label(window,text = status,fg = 'black' , bg = 'white' ,padx = 2, pady= 2, relief = 'sunken',font = 'Lato 11')
                         L5.grid(row = coin_row, column = 4,sticky = N+S+E+W)
                    
                     L6 = Label(window,text = "${0:.2f}".format(amount),fg = 'black' , bg = 'white' ,padx = 2, pady= 2, relief = 'sunken',font = 'Lato 11')
                     L6.grid(row = coin_row, column = 5,sticky = N+S+E+W)
                     
                     totalvalue += coin["no_of_coins"] *  coin["price_per_coin"]
                     totalcurrentvalue += coin["no_of_coins"] * api["data"][i]["quote"]["USD"]["price"]
                     coin_row = coin_row+1

    api = ''              
    T1 = Label(window, text ="${0:.2f}".format(totalvalue) ,fg = 'black',bg = 'white' , padx = 5, pady = 5,  font = 'Lato 14 bold' )
    T1.grid(row = 1 , column = 2)         
    
    T2 = Label(window, text ="${0:.2f}".format(totalcurrentvalue),fg = 'black',bg = 'white' , padx = 5, pady = 5,  font = 'Lato 14 bold'    )
    T2.grid(row = 1 , column = 4)      
    
    B1 = Button(window, text = 'update',fg ='white',bg = 'darkblue',command = my_portfolio, font = 'Lato 14 bold', padx = 5, pady = 5, relief = 'groove')
    B1.grid(row = coin_row + 1  ,column = 5 )

window = Tk()

window.title('My Crypto Portfolio')
window.iconbitmap('icon.ico')

L9 = Label(window,text = 'Total investment',fg = 'white',bg = 'maroon' ,font = 'ariel 14 bold', padx = 5, pady = 5, relief = 'groove')
L9.grid(row = 1, column = 1,sticky = N+S+E+W)


L8 = Label(window,text = 'Mycoins',fg = 'white',bg = 'maroon' ,font = 'ariel 14 bold', padx = 5, pady = 5, relief = 'groove')
L8.grid(row = 1, column = 3,sticky = N+S+E+W)


L1 = Label(window,text = 'Mycoins',fg = 'darkblue',bg = 'lightgrey' ,font = 'Lato 12 bold', padx = 5, pady = 5, relief = 'groove')
L1.grid(row = 3, column = 0,sticky = N+S+E+W)

L2 = Label(window,text = 'Quantity',fg = 'darkblue',bg = 'lightgrey' ,font = 'Lato 12 bold', padx = 5, pady = 5, relief = 'groove')
L2.grid(row = 3, column = 1,sticky = N+S+E+W)

L3 = Label(window,text = 'amount invested',fg = 'darkblue',bg = 'lightgrey' ,font = 'Lato 12 bold', padx = 5, pady = 5, relief = 'groove')
L3.grid(row = 3, column = 2,sticky = N+S+E+W)

L4 = Label(window,text = 'current price',fg = 'darkblue',bg = 'lightgrey' ,font = 'Lato 12 bold', padx = 5, pady = 5, relief = 'groove')
L4.grid(row = 3, column = 3,sticky = N+S+E+W)

L5 = Label(window,text = 'status',fg = 'darkblue',bg = 'lightgrey' ,font = 'Lato 12 bold', padx = 5, pady = 5, relief = 'groove')
L5.grid(row = 3, column = 4,sticky = N+S+E+W)

L6 = Label(window,text = 'status value',fg = 'darkblue',bg = 'lightgrey' ,font = 'Lato 12 bold', padx = 5, pady = 5, relief = 'groove')
L6.grid(row = 3, column = 5,sticky = N+S+E+W)




my_portfolio()
window.mainloop()

