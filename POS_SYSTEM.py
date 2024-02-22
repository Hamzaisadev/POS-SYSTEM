import datetime
import tkinter 
from tkinter import *
from tkinter import ttk

import customtkinter
import pandas as pd
import xlrd
from CTkListbox import *
from CTkMessagebox import CTkMessagebox
from customtkinter import *
from PIL import Image

bill_amount = 0
#images
img = customtkinter.CTkImage(Image.open('images/logo1.png'),size=(170,170))





# Set the appearance of the custom Tkinter to dark
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")  
# Themes: "blue" (standard), "green", "dark-blue"

# now i will Create the main window (root)
root = customtkinter.CTk()

#here i am taking the size of the screenof the user with .winfo_screenwidth() and .winfo_screenheight()

#width= root.winfo_screenwidth() 
#height=root.winfo_screenheight()



# now I will use .geometry to set a size of the window and
#I will give the width and height variable as arguments

root.geometry("1920x1080")

root.state("zoomed")


#now I will set the title of the window

root.title('POS System')


# Add an icon to the window (uncomment and provide the correct path to your icon file)
#root.iconbitmap("images/logo1.ico")

#creating the first function

# Define the function for the add to cart button

def add_to_cart():

#first we will we will take product and quantity from the entry boxes with .get
  df = pd.read_excel('data/products.xlsx')
  product = enter_product.get()
  quantity = enter_quantity.get()
  #now I will read the data from our Excel file using Panda module I imported
  available_products=pd.read_excel('data/products.xlsx')

  #now I will locate the name data frame from my excel file by using .df lock

  row = df.loc[df['name'] == product]

  #as you can see I took the name of the product from the entry box and I used .loc to locate the row of that product in my excel file

  #now I will use the if not condition to check if product is found or not

  if not row.empty:

    #now I will get the product price in the quantity from the XL file

    price = row["price"].item
    stock = row["stock"].item

    #now I will check if the stock is greater than the quantity
    if stock >= quantity:

      #now I will add the detailed of the product and the quantity and price into the list box I have created later in this code

      cart_listbox.insert(customtkinter.END,f"{product} - Quantity: {quantity} - Price: {price}Rs")

   #now I will update the bill amount by adding price multipied by the quantity
      global bill_amount
      bill_amount += price * quantity
      bill_label.cofigure(text=f"Bill Amount: {bill_amount}Rs")

  #now I will update the stock by subtracting the quantity from the stock

      df.loc[df["name"]==product, "stock"] -quantity
      df.to_excel("data/products.xlsx",
        index = False)

      #now I will show the error if quantity is not available

    else:
      CTkMessagebox(title="error",message="Quantity not available", icon="warning")

  #creating and another error if the product is not found

  else:
    CTkMessagebox(title="error",message="Product not found", icon="warning")

#function to exit program connected to exit button

def exit_program():
    # Show some retry/cancel warnings
    msg = CTkMessagebox(master=root,
      title="Are You Sure!",
    message="Do you want exit?",
    icon="warning",
    option_1="Yes",
    option_2= "No")
    yes_or_no = msg.get()
    if yes_or_no == "Yes":
        root.destroy()
    else:
        print("press yes to exit")


def calculate_total():

   return 



def login():
  username = enter_username.get()
  password = enter_password.get()
  if username == "admin" and password == "admin":
    admin = customtkinter.CTkToplevel(root)
    admin.geometry("1920x1080")
    admin.title("Admin Page")
    admin.wm_transient(root)





  #first i will configure the main frames in admin window
  
  
    admin_heading_frame = customtkinter.CTkFrame(admin, width=100, height=100)
    product_add_frame = customtkinter.CTkFrame(admin, width=100, height=100)
    exel_file_frame = customtkinter.CTkFrame(admin, width=100, height=100)


    save_product = customtkinter.CTkButton(product_add_frame, text ="Save Product",
      width =120,
      height =60,
      font=("helvetica",19),
      text_color="black",
      fg_color="yellow",
      hover_color="#c2b84e",
      corner_radius=200,
      command=exit_program)

    delete_product = customtkinter.CTkButton(product_add_frame, text ="Delete Product",
      width =120,
      height =60,
      font=("helvetica",19),
      text_color="black",
      fg_color="yellow",
      hover_color="#c2b84e",
      corner_radius=200,)





    enter_product_name = customtkinter.CTkEntry(product_add_frame,
      placeholder_text= "Enter product name",
      width=500,
      height=60,
      font=("helvetica",24),
      text_color="#F5DD90",
      placeholder_text_color="yellow",
      corner_radius=200)


    enter_product_quantity = customtkinter.CTkEntry(product_add_frame,
      placeholder_text= "Enter product quantity",
      width=500,
      height=60,
      font=("helvetica",24),
      text_color="#F5DD90",
      placeholder_text_color="yellow",
      corner_radius=200)

    admin_heading_Label= customtkinter.CTkLabel(admin_heading_frame ,text='HELLO ADMIN',
      font=('times new roman',50,'bold'),
      text_color='yellow',
      image=img, # i imported this img at the start of the code
      compound=LEFT)
    
    
    enter_product_price = customtkinter.CTkEntry(product_add_frame,
      placeholder_text= "Enter Product Price",
      width=500,
      height=60,
      font=("helvetica",24),
      text_color="#F5DD90",
      placeholder_text_color="yellow",
      corner_radius=200)

    admin.columnconfigure(0,weight =1,uniform="a")
    admin.columnconfigure(1,weight =3,uniform="a")
    admin.rowconfigure(0,weight =1,uniform="a")
    admin.rowconfigure(1,weight =5,uniform="a")
    # Adding widgets to the frames
    admin_heading_frame.grid(row=0, column=0, columnspan=2,padx=5, sticky=tkinter.EW)
    product_add_frame.grid(row=1, column=0,padx=5, sticky=tkinter.NSEW)
    exel_file_frame.grid(row=1, column=1,padx=5, sticky=tkinter.NSEW)
    
    admin_heading_frame.columnconfigure(1,weight =5,uniform="a")
    admin_heading_Label.grid(row=0, column=0, columnspan=2,padx=5, sticky=tkinter.EW)
    
    
    product_add_frame
    exel_file_frame
    

    
    
    


  elif username == "" and password == "":
      CTkMessagebox(title="Error", message="Please enter username and password", icon="warning")


  elif username == "":
    CTkMessagebox(title="Error", message="Please enter username", icon="warning")

  elif password == "":
    CTkMessagebox(title="Error", message="Please enter password", icon="warning")

  else:
    CTkMessagebox(title="Error", message="Invalid username or password", icon="warning")




def print_bill():
  print()






def show_history():
  return



#lets make heading menu i will include a logo ,name and login function
#first i will make a frame in which i will put widgets

heading_frame = customtkinter.CTkFrame(master=root, width=1100, height=500)
#now i will make a Username and Password entryboxes

enter_username= customtkinter.CTkEntry(heading_frame,
    placeholder_text= "Enter Username",
    width=460,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200,)

enter_password = customtkinter.CTkEntry(heading_frame,
    placeholder_text= "Enter Password",
    width=460,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200)
    
#i have entered the name of frame i created as the first argument  it is neccessary

#here i maked a login button ans at last set the command to login function i created earlier

login_button = customtkinter.CTkButton(heading_frame, text ="Login",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200,
    command=login)

#now i have created the main text label 

headingLabel= customtkinter.CTkLabel(heading_frame ,text='KAMAL PAINT PORTAL',
  font=('times new roman',50,'bold'),
  text_color='yellow',
  image=img, # i imported this img at the start of the code
  compound=LEFT)
  
  ##so there are two function that are used to place widgets .pack and .grid  so I will use . grid to place the widgets in frame and window and i will do it ate the end of the code

  
  
  
  
  #-----------------heading frame done----------------------
  #-----------------now i will work on details frame----------------------
  
  #here is little complicated so i will make a details_frame and inside that details_frame i will place  two more frames
  #                   Main frame   
  
details_frame = customtkinter.CTkFrame(master=root,
width=10, 
height=10)
  
  #as you can see master of details_frame is root which is main main window
  
#                     order detail frame

order_detail_frame = ttk.LabelFrame(master=details_frame,
   text= "Order Details",
   width=200,
   height=200)

##here I used the LabelFrame from ttk ( you will have to import this aswell) 

    
    #       here i will create entry boxes 
    
enter_product = customtkinter.CTkEntry(order_detail_frame,
    placeholder_text= "Enter product name",
    width=500,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200)

#Quantity box
enter_quantity = customtkinter.CTkEntry(order_detail_frame,
    placeholder_text= "Enter Quantity",
    width=500,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200)

    #as you can see i have these entry boxes in order detail frame
    
    #now i will create buttons
    
    
add_to_cart_button = customtkinter.CTkButton(details_frame,
    text ="add to cart",
    width =120,   # change width of button
    height =60,  # change height of button
    font=("helvetica",19),  # Change font of button
    text_color="black",  #  Change color of button
    fg_color="yellow",  # Change color of button foreground
    hover_color="#c2b84e",  #   Change color of when mouse hovers
    corner_radius=200,#    change corner raduis of button
    command=add_to_cart ) #and now we will add function to our button by calling def function created before
    
    
    
total_button = customtkinter.CTkButton(details_frame,
    text ="Total",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200)
    
    #as  you can see i have these buttons in details_frame outside of order_detail_frame
    
    
    
    
    #           customer  detail frame
customer_detail_frame = ttk.LabelFrame(master=details_frame,
   text= "Customer Details",
   width=200,
   height=200)


#same as i did with order_detail_frame

#and the master of these 2 frames is my details frame
customer_name = customtkinter.CTkEntry(customer_detail_frame,
    placeholder_text= "Customer Name",
    width=500,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200) 
    
    
    
customer_number = customtkinter.CTkEntry(customer_detail_frame,
    placeholder_text= "Customer Number",
    width=500,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200)

print_bill_button = customtkinter.CTkButton(details_frame, text ="Print Bill",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200 )

#now i will create a cart frame in which i will have a label cart and a listbox that i imported in starting

cart_frame = customtkinter.CTkFrame(master=root,
  width=5,
  height=5,
)


cart_label = customtkinter.CTkLabel(cart_frame,
    text ="Cart",
    font=('times new roman',30,'bold'),
  text_color='yellow',)
    
    
cart_listbox = CTkListbox(cart_frame,
  width=500,
  height=500,
  font=("helvetica",24))


#now i will create a bill frame in which i will have bill label and a text box which will print all bill

    
    

bill_frame = customtkinter.CTkFrame(master=root, width=200, height=50)

    
bill_label = customtkinter.CTkLabel(bill_frame,
    text ="Bill",
    font=('times new roman',30,'bold'),
  text_color='yellow',)
    



#here i created an  another frame for 3 button clear cart,save and 'exit'

cse_button_frame = customtkinter.CTkFrame(master=root, 
width=100,
height=200)



clear_button = customtkinter.CTkButton(cse_button_frame, text ="Clear Cart",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="#1B1B1E",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200)

save_button = customtkinter.CTkButton(cse_button_frame, text ="Exit",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200,
    command=exit_program)
    
    
    
exit_button = customtkinter.CTkButton(cse_button_frame, text ="Exit",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200,
    command=exit_program)





# Creating a grid for the widgets and frames

#firt i will make columns and rows with .configure
root.columnconfigure(0,weight =1,uniform="a")
root.columnconfigure(1,weight =1,uniform="a")
root.columnconfigure(2,weight =1,uniform="a")
root.rowconfigure(0,weight =1,uniform="a")
root.rowconfigure(1,weight =2,uniform="a")
root.rowconfigure(2,weight =1,uniform="a")

#giving weight is neccessary,weight means the size of the particular column

#now that i have configured the rows and column i will use.grid to place widegets in that row .grid takes few arguments like row,column,columnspan,sticky etc

#first i will grid the frames then widgets in them
#columnspan means how much columns our widgets will take
#sticky means direction
heading_frame.grid(column=0 ,row=0,columnspan=3, sticky=tkinter.NSEW, padx=5,pady=5)
details_frame.grid(column=0 ,row=1,rowspan=2, sticky=tkinter.NSEW, padx=5,pady=5)
cart_frame.grid(column=1 ,row=1, sticky=tkinter.NSEW,padx=75,pady=20)
bill_frame.grid(column=2 ,row=1, sticky=tkinter.NSEW, padx=75,pady=20)
cse_button_frame.grid(column=1 ,row=2,columnspan=2, sticky=tkinter.NSEW,padx=5,pady=5)

#now i will place widgets in frames with same grid method

#this time I will use the frame name instead of root

heading_frame.columnconfigure(0,weight =3,)
heading_frame.columnconfigure(1,weight =1,)
heading_frame.columnconfigure(2,weight =1,)
heading_frame.columnconfigure(3,weight =1,)
heading_frame.rowconfigure(0,weight =1)

headingLabel.grid(row=0, column=0,padx=5, sticky=tkinter.EW)

enter_username.grid(row=0, column=2,padx=5)

enter_password.grid(row=0, column=3,padx=5)

login_button.grid(row=0, column=4,padx=5)

#-------------heading frame done------------------



#-----------------now i will work on details frame----------------------

#here first I will make four rows and two column in my details frame

details_frame.rowconfigure(0,weight =1,uniform="a")
details_frame.rowconfigure(1,weight =1,uniform="a")
details_frame.rowconfigure(2,weight =1,uniform="a")
details_frame.rowconfigure(3,weight =1,uniform="a")
details_frame.columnconfigure(0,weight =1,uniform="a")
details_frame.columnconfigure(1,weight =1,uniform="a")

#now i will place widgets in details frame
#putting widgets in order detail frame

order_detail_frame.grid(row=0, column=0, columnspan=2,pady=10)
customer_detail_frame.grid(row=2, column=0,columnspan=2)

#configiring  order detail frame
order_detail_frame.columnconfigure(0,weight =1)
order_detail_frame.rowconfigure(0,weight =1)
order_detail_frame.rowconfigure(1,weight =1)

#configuring customer detail frame
customer_detail_frame.columnconfigure(0, weight=1,)
customer_detail_frame.rowconfigure(0, weight=1,)
customer_detail_frame.rowconfigure(1, weight=1,)

#griding widgets in order details frame

enter_product.grid(row=1, column=0,pady=10,padx=6)
enter_quantity.grid(row=2, column=0,pady=10,padx=6)

#griding button in  details frame

add_to_cart_button.grid(row=1, column=0,sticky=E,pady=10,padx=6)
total_button.grid(row=1, column=1,sticky=W,pady=10,padx=6)

#griding widgets in customer details frame
customer_name.grid(row=0, column=0,pady=10,padx=6)
customer_number.grid(row=1, column=0,pady=10,padx=6)
#griding button in customer details frame
print_bill_button.grid(row=3, column=0, columnspan=2)
#-----------------details frame done------------------

#-----------------now i will work on cart frame----------------------

#first i will make two rows and one columns in my cart frame
cart_frame.rowconfigure(0,weight =1)
cart_frame.rowconfigure(1,weight =5)
cart_frame.columnconfigure(0,weight =1)
#now i will place widgets in cart frame
cart_label.grid(row=0, column=0,)
cart_listbox.grid(row=1, column=0,)



#-----------------cart frame done------------------


#-----------------now i will work on bill box ------------------


#bill box done

bill_frame.rowconfigure(0,weight =1,uniform="a")
bill_frame.rowconfigure(1,weight =5,uniform="a")
bill_frame.columnconfigure(0,weight =1,uniform="a")
#now i will place widgets in cart frame
bill_label.grid(row=0, column=0,)


#now i will do in last cse buttons

cse_button_frame.columnconfigure(0,weight=1,uniform="a")
cse_button_frame.columnconfigure(1,weight=1,uniform="a")
cse_button_frame.columnconfigure(2,weight=1,uniform="a")
cse_button_frame.rowconfigure(0,weight=1)

clear_button.grid(row=0, column=0,padx=7, sticky=tkinter.EW)
save_button.grid(row=0, column=1,padx=7, sticky=tkinter.EW)

exit_button.grid(row=0, column=2,padx=7, sticky=tkinter.EW)

# Start the main loop

root.mainloop()
#lets make a function that will show output from entry box when i click button