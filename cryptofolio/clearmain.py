# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:01:30 2019

@author: shashank verma
"""

import requests
import json
from tkinter import *
import sqlite3

#creating connection to database
conn = sqlite3.connect('coins.db')
cur = conn.cursor()

#making coins table
cur.execute("""CREATE TABLE IF NOT EXISTS coins
                 (id INTEGER PRIMARY KEY, symbol TEXT, coins_no INTEGER, amount INTEGER)""")
conn.commit()

cur.execute("SELECT * FROM coins")
coins = cur.fetchall()
#initial row no
rowno = 0

#api request data from coin market API
api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=e2c48ed7-ace4-4849-82f4-7634f2a4747d")
api = json.loads(api_request.content)

mainwindow = Tk()
mainwindow.title('MY CRYPTO PORTFOLIO')
mainwindow.iconbitmap('icon.ico')
    
def header():
    L1 = Label(mainwindow,text = 'ID',fg = 'darkblue',bg = 'lightgrey' ,font = 'Lato 12 bold', padx = 5, pady = 5, relief = 'groove')
    L1.grid(row = rowno, column = 0,sticky = N+S+E+W)
    
    L2 = Label(mainwindow,text = 'COIN',fg = 'darkblue',bg = 'lightgrey' ,font = 'Lato 12 bold', padx = 5, pady = 5, relief = 'groove')
    L2.grid(row = rowno, column = 1,sticky = N+S+E+W)
    
    L3 = Label(mainwindow,text = 'QUANTITY',fg = 'darkblue',bg = 'lightgrey' ,font = 'Lato 12 bold', padx = 5, pady = 5, relief = 'groove')
    L3.grid(row = rowno, column = 2,sticky = N+S+E+W)
    
    L4 = Label(mainwindow,text = 'INVESTMENT',fg = 'darkblue',bg = 'lightgrey' ,font = 'Lato 12 bold', padx = 5, pady = 5, relief = 'groove')
    L4.grid(row = rowno, column = 3,sticky = N+S+E+W)
    
    L5 = Label(mainwindow,text = 'CURRENT VALUE',fg = 'darkblue',bg = 'lightgrey' ,font = 'Lato 12 bold', padx = 5, pady = 5, relief = 'groove')
    L5.grid(row = rowno, column = 4,sticky = N+S+E+W)
    
    L6 = Label(mainwindow,text = 'TOTAL P/L VALUE',fg = 'darkblue',bg = 'lightgrey' ,font = 'Lato 12 bold', padx = 5, pady = 5, relief = 'groove')
    L6.grid(row = rowno, column = 5,sticky = N+S+E+W)
 
#calculate current value     
def calculatecurrent(symbol):
    for i in range(0,50,1):
        if(api["data"][i]["symbol"] == symbol):
               return api["data"][i]["quote"]["USD"]["price"]

#check status           
def checkstatus(invest,current):
    if invest<current:
        return 'PROFIT'
    elif invest>current:
        return 'LOSS'
    else:
        return 'NEUTRAL'

#reset function destroy every frame and reconstruct it   
def reset():
    for frame in mainwindow.winfo_children():
        frame.destroy()
        
    header()
    portfolio()
    
def close_window():
    editwindow.destroy()
    
#edit coins function for adding,deleting and updating coins
def edit_coins():
    #adding coin to the database
    def addcoin():
        cur.execute("INSERT INTO coins(symbol, coins_no, amount) VALUES(?,?,?)",(symbol_add.get(), quantity_add.get(), amount_add.get()))
        conn.commit()
        #reset()
     
    #for updating coing    
    def update_coin():
        cur.execute("UPDATE coins SET symbol = ?, coins_no = ?,amount = ? WHERE id = ?",(symbol_update.get(),quantity_update.get(),amount_update.get()))
        conn.commit()
        #reset()
    
    #for deleting coins    
    def delete_coin():
        cur.execute("DELETE FROM coins WHERE id=?",(id_delete.get(),))
        conn.commit()
        #reset()
    
    
    editwindow = Tk()
    editwindow.title('EDIT COINS')
    editwindow.iconbitmap('icon.ico')
    
    symbol_add = Entry(editwindow,borderwidth = 2,relief = 'groove')
    symbol_add.grid(row = 0,column = 1)    
    
    quantity_add = Entry(editwindow,borderwidth = 2,relief = 'groove')
    quantity_add.grid(row = 0,column = 2)
    
    amount_add = Entry(editwindow,borderwidth = 2,relief = 'groove')
    amount_add.grid(row = 0,column = 3)
    
    add = Button(editwindow, text = 'ADD',fg ='white',bg = 'darkblue',command = addcoin, font = 'Lato 12 bold', padx = 3, pady = 3, relief = 'groove')
    add.grid(row = 0  ,column = 4 )
    
    #updating coins
    id_update = Entry(editwindow,borderwidth = 2,relief = 'groove')
    id_update.grid(row = 1,column = 0) 
    
    symbol_update = Entry(editwindow,borderwidth = 2,relief = 'groove')
    symbol_update.grid(row = 1,column = 1)    
    
    quantity_update = Entry(editwindow,borderwidth = 2,relief = 'groove')
    quantity_update.grid(row = 1,column = 2)
    
    amount_update = Entry(editwindow,borderwidth = 2,relief = 'groove')
    amount_update.grid(row = 1,column = 3)
    
    update = Button(editwindow, text = 'UPDATE',fg ='white',bg = 'darkblue',command = update_coin, font = 'Lato 12 bold', padx = 3, pady = 3, relief = 'groove')
    update.grid(row = 1  ,column = 4 )
    
    #deleting entry
    id_delete = Entry(editwindow,borderwidth = 2,relief = 'groove')
    id_delete.grid(row = 2,column = 0)
    
    delete = Button(editwindow, text = 'DELETE',fg ='white',bg = 'darkblue',command = delete_coin, font = 'Lato 12 bold', padx = 3, pady = 3, relief = 'groove')
    delete.grid(row = 3  ,column = 4 )
    
    exitt = Button(editwindow,text="EXIT",fg ='white',bg = 'darkblue',command = close_window, font = 'Lato 12 bold', padx = 3, pady = 3, relief = 'groove')
    exitt.grid(row = 5, column = 0, columnspan = 5)

    editwindow.mainloop()
def portfolio():
    header()
    coin_row = rowno + 1
    
    for coin in coins:
        id_no = Label(mainwindow,text = coin[0],fg = 'black' , bg = 'white' ,padx = 2, pady= 2, relief = 'sunken',font = 'Lato 11')
        id_no.grid(row = coin_row, column = 0,sticky = N+S+E+W)
        
        symbol = Label(mainwindow,text = coin[1],fg = 'black' , bg = 'white' ,padx = 2, pady= 2, relief = 'sunken',font = 'Lato 11')
        symbol.grid(row = coin_row, column = 1,sticky = N+S+E+W)
        
        quantity = Label(mainwindow,text = coin[2],fg = 'black' , bg = 'white' ,padx = 2, pady= 2, relief = 'sunken',font = 'Lato 11')
        quantity.grid(row = coin_row, column = 2,sticky = N+S+E+W)
        
        amount = Label(mainwindow,text = '$' + str(coin[3]),fg = 'black' , bg = 'white' ,padx = 2, pady= 2, relief = 'sunken',font = 'Lato 11')
        amount.grid(row = coin_row, column = 3,sticky = N+S+E+W)
        
        current = calculatecurrent(coin[1])
        current =current * coin[2]
        
        curr = Label(mainwindow,text = "${0:.2f}".format(current),fg = 'black' , bg ='white' ,padx = 2, pady= 2, relief = 'sunken',font = 'Lato 11')
        curr.grid(row = coin_row, column = 4,sticky = N+S+E+W)
        
        status = checkstatus(coin[3],current)
        value = current - coin[3]
        
        
        if status == 'PROFIT':
            pl = Label(mainwindow,text = "${0:.2f}".format(value),fg = 'green' , bg ='white' ,padx = 2, pady= 2, relief = 'sunken',font = 'Lato 11 bold')
            pl.grid(row = coin_row, column = 5,sticky = N+S+E+W)
        elif status == 'LOSS':
            pl = Label(mainwindow,text = "${0:.2f}".format(value),fg = 'red' , bg ='white' ,padx = 2, pady= 2, relief = 'sunken',font = 'Lato 11 bold')
            pl.grid(row = coin_row, column = 5,sticky = N+S+E+W)
        else:
            pl = Label(mainwindow,text = "${0:.2f}".format(value),fg = 'black' , bg ='white' ,padx = 2, pady= 2, relief = 'sunken',font = 'Lato 11 bold')
            pl.grid(row = coin_row, column = 5,sticky = N+S+E+W)
        
        coin_row += 1
        
    refresh = Button(mainwindow, text = 'REFRESH',fg ='white',bg = 'darkblue',command = reset, font = 'Lato 12 bold', padx = 3, pady = 3, relief = 'groove')
    refresh.grid(row = coin_row  ,column = 5 )
    
    edit = Button(mainwindow, text = 'EDIT COINS',fg ='white',bg = 'lightblue',command = edit_coins, font = 'Lato 12 bold', padx = 3, pady = 3, relief = 'groove')
    edit.grid(row = coin_row + 1  ,column = 0,columnspan = 4 )
        
portfolio()        
mainwindow.mainloop() 
conn.close()
