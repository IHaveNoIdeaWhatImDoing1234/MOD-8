class ItemToPurchase: #ItemToPurchase Class
    
    item_name = "none" #Set intial item name to "none"
    item_price = 0#Set intial item price to 0
    item_quantity = 0 #Set intial item quantity to 0
    item_description = "none" #Set intial item description to "none"

    def __init__(self, item_name, item_quantity, item_price, item_description): #ItemToPurchase Constructor
        self.item_name = item_name #change item name to inputted string
        self.item_price = item_price #change item price to inputted value
        self.item_quantity = item_quantity #change item quantity to inputted value
        self.item_description = item_description #change item name to inputted string
    
    def print_item_cost(self): 
        print("{} {} @ ${} = ${} ".format(self.item_name, self.item_quantity, self.item_price, self.item_quantity * self.item_price )) # formatted print out item cost
        
    def total_cost(self):
        return self.item_quantity * self.item_price #print out total item cost, quantity * price

class ShoppingCart(ItemToPurchase): #Shopping Cart Class
    
    def __init__(self, customer_name, current_date): #Shoppingcart Constructor
        self.customer_name = customer_name #set customer name to inputted value
        self.current_date = current_date #set current date to inputted value
        self.cart_items = [] #create empty list for the shopping cart
    
    def add_item(self, ItemToPurchase): #Method to add item to cart
        self.cart_items.append( [ ItemToPurchase.item_name, ItemToPurchase.item_quantity, ItemToPurchase.item_price, ItemToPurchase.item_description ] ) #Adds item to end of list, utilizes inputed
    

    def remove_item(self, shoppingcart, item_name): #Method to remove item to cart
        print('\nREMOVE ITEM FROM CART', end='\n')
        string = str(input('Enter name of item to remove:\n'))
        for item in self.cart_items:
            if (item.item_name == string):
                self.cart_items.remove(item)
                flag = True
                break
            else:
                flag = False
        if (flag == False):
            print('Item not found in cart. Nothing removed.')
    def modify_item(self, ItemToPurchase, item_name ): #Method to modify item quantity of an item in cart
        modified_item_quantity = int(input("Enter {} item quantity: ".format(item_name) )) #user inputs new value for quantity
        for row, col in enumerate(self.cart_items): #iterate through list
           if (self.item_name == item_name): #if item name of teh object in teh list matches, remove item from list
                self.item_quantity[i] = modified_item_quantity #modify the specified item's quantity, with the new value being inputted by the user
                    
    def get_num_items_in_cart(self): #Method to count the total number of items in the cart
        item_in_carts = 0 #set counter varible to 0
        for row, col in enumerate(self.cart_items): #Iterate through list of objects
            item_in_carts = self.cart_items[row][-3] + item_in_carts #add each object to the total number of items
        return item_in_carts #return value
    
    def get_cost_of_cart(self): #Method to count the total cost of all items in the cart
        total_item_cost = 0 #set counter varible to 0
        for row, col in enumerate(self.cart_items): #Iterate through list of objects
            total_item_cost += ( self.cart_items[row][-2] * self.cart_items[row][-3]) #add each object quantity * price to the total number of items
        return total_item_cost #return value
    
    def print_total(self): #Method to output all items in the cart
        if (self.get_num_items_in_cart() is 0): #check if cart is empty
            print("SHOPPING CART IS EMPTY") #If empty, state it, and exit method
            return
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date) )#primt formated header with customer name and date
        print("Number of Items: {}".format(self.get_num_items_in_cart())) #print formated number items in cart
        for row, col in enumerate(self.cart_items): #Iterate through list of objects
            print("{} {} @ ${:0.2f} = ${:0.2f} ".format(self.cart_items[row][0], self.cart_items[row][1], self.cart_items[row][2], self.cart_items[row][1] * self.cart_items[row][2] )) # print formatted item in the cart, 
        print("Total: ${:0.2f}".format(self.get_cost_of_cart())) # print total cost of all items in cart
     
    def print_descriptions(self): #Method to output all item descriptions in the cart
        if (self.get_num_items_in_cart() is 0): #check if cart is empty
            print("SHOPPING CART IS EMPTY") #If empty, state it, and exit method
            return
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date) ) #print out header
        print("Item Descriptions") #print out header
        for row, col in enumerate(self.cart_items): #Iterate through list of objects
            print("{}: {}".format(self.cart_items[row][0], self.cart_items[row][-1])) #print each items name and description 
               
def print_menu(ShoppingCart): #Print menu Method
    user_input = ''
    while (user_input != "q"): #while loop to keep menu running until user quits
        print("MENU") #header
        print("a - Add item to cart") #add item
        print("r - Remove item from cart") # remove item
        print("c - Change item quantity") # change quantity
        print("i - Output items' descriptions") # output all item descriptions and names in cart
        print("o - Output shopping cart") #output all items in cart, name, description, cost, quantity
        print("q - Quit") #quit
        user_input = str(input("Choose an option: ")) #get user input on menu selection
        if (user_input == "a"): #if/else section for what to do when user selects certain actions from menu
            add_item_cart(ShoppingCart) # add item
        elif (user_input == "r"):
            remove_item_cart(ShoppingCart) # remove item
        elif (user_input == "c"):# change item quanity
            if (ShoppingCart.get_num_items_in_cart() != 0):
                for row, col in enumerate(ShoppingCart.cart_items):
                    print("{} {} @ ${:0.2f} = ${:0.2f} ".format(ShoppingCart.cart_items[row][0], ShoppingCart.cart_items[row][1], ShoppingCart.cart_items[row][2], ShoppingCart.cart_items[row][1] * ShoppingCart.cart_items[row][2] ))
                item_name = str(input("What item do you like to change? "))
                change_item_cart(ShoppingCart, item_name) 
            else: print("Your shopping cart is empty")
        elif (user_input == "i"):
            output_items_description(ShoppingCart) #list decriptions
        elif (user_input == "o"):
            output_shopping_cart(ShoppingCart) #output eniter cart
        elif (user_input == "q"): #quit
            print("Thank you for Shopping with us!  Goodbye")
        else:
            print("Invalid input, please try again")

def output_items_description(ShoppingCart): #if user selects "i" from menu, executes print description method and lists all descriptions of items in cart
    ShoppingCart.print_descriptions()

def change_item_cart(ShoppingCart, item_name): #if user selects "c", changes quantity of item in cart
    ShoppingCart.modify_item(ShoppingCart, item_name)
    
def output_shopping_cart(ShoppingCart): #if user selects "o", outputs all infomration about items in cart
    print("OUTPUT SHOPPING CART")
    ShoppingCart.print_total()

def add_item_cart(ShoppingCart): #if user selects "a", allows user to add new item to their cart
    print("ADD ITEM TO CART")
    item_name = str(input("Enter the item name: "))
    item_description = str(input("Enter an item descriptions: "))
    item_price = float(input("Enter the item price: "))
    item_quantity = int(input("Enter the item quantity: "))
    
    item = ItemToPurchase(item_name, item_quantity, item_price, item_description)
    ShoppingCart.add_item(item)
    print("ITEM ADDED")

def remove_item_cart(ShoppingCart): #if user selects "r", allows user to remove item form cart
        item_name = input('\nREMOVE ITEM FROM CART :', end='\n')
        ShoppingCart.remove_item(item_name)
        print("REMOVED ITEM FROM CART")

if __name__== "__main__": #main
    print("Enter customer's name:")
    customer_name = str(input())
    print("Enter today's date: ")
    todays_date = str(input())
    print("Customer's name: {}".format(customer_name) )
    print("Today's date: {}".format(todays_date) )
    shoppingcart = ShoppingCart(customer_name, todays_date)
    print_menu(shoppingcart)
    

