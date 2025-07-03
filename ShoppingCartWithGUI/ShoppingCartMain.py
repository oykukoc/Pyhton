import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Shopping Cart")

def centerIt (window,width,height):
    screenWidth = window.winfo_screenwidth()
    screenHeigth = window.winfo_screenheight()

    x = (screenWidth - width) // 2
    y = (screenHeigth - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

centerIt(root,300,250)


foods = []
prices = []

def shopping():
    food = foodEntry.get().strip()
    priceText = priceEntry.get().strip()

    if not food:
        messagebox.showwarning("Warning!","Please enter a food name!")
        return
    if not priceText.isdigit():
        messagebox.showwarning("Warning!","Please enter a valid price (numbers only!)")
        return

    price = int(priceText)
    foods.append(food)
    prices.append(price)

    # delete the written input after clicked the button
    foodEntry.delete(0,tk.END)
    priceEntry.delete(0,tk.END)


def showCart():
    if not foods:
        messagebox.showinfo("Your shopping cart is empty!")
        return
    cartText = ""
    for food,price in zip(foods,prices):
        cartText += f"{food} is {price}$\n"

    messagebox.showinfo("Shopping Cart", cartText)

def totalCount():
    total = 0
    cartPrice = ""
    for p in prices:
        p = int(p)
        total += p
    cartPrice += f"Total Count is : {total}"
    messagebox.showinfo("Total Count",cartPrice)


#GUI ELEMENTS
tk.Label(root,text="Enter the food name").pack()
foodEntry = tk.Entry(root)
foodEntry.pack(pady=10)

tk.Label(root,text="Enter the price of the food").pack()
priceEntry = tk.Entry(root)
priceEntry.pack(pady=10)

tk.Button(root,text="Add to Cart",command=shopping).pack(pady=10)
tk.Button(root,text="Show Cart",command=showCart).pack(pady=10)
tk.Button(root,text="Show the total count",command = totalCount).pack(pady=10)

root.mainloop()
