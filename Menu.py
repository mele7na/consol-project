def anamenu():
    food =["Burger","Drink","Fries","Apple pie"]
    prices = [5,1,3,2]

    myorderFood=[]
    myorderCost=[]
    counter=0
    total=0
    print("Welcome to Mcdonalds")
    print("==  MCDONALDS     ==")
    print("==== Menu       ====")
    print("= 0.Burger         =")
    print("= 1.Drink          =")
    print("= 2.Fries          =")
    print("= 3.Apple Pie      =")
    print("====================")
    print("Can I take your order?")
    secim = input()
    FoodOrder = input("Please enter item")
    if secim == "0":
        Burger
    if secim =="1":
        Drink
    if secim =="2":
        Fries
    if secim =="3":
        ApplePie
    else:print("Not on menu")
    finished = input("Have you finished ordering Y/N")
    if finished =="N":
       nextOder =True
    else:
         nextOrder = False
         print(myorderFood)
         print(myorderCost)
         print(counter)

    
    else:
        print("Thank you")
    nextOrder = True
    while nextOrder ==True:

    print("Here is your order")
    print("")
    print("********************")
    print(myorderFood[y])

    while y <counter:
        print("Item":+(myorderFood[y]))
        print("Cost":$+str(myorderCost{y}))
        y=y+1
        
