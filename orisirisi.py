sex = "male"
marital_status = "married"

def kids():
    query=input ("do you have kids? ")
    if query == "yes":
        print("come and buy diapers")
    else:
        print("lets plan some vacation")

def clipper(repeat: int):    
    print(f"barb your hair {repeat} times")

def marital_stat():
    con_mar_sta=input("enter your marital status ")
    if con_mar_sta == marital_status:
       kids()


print("welcome to gbogbolowo enterprises")
sex_type = str(input("enter your sex "))
if sex_type==sex:
    print("you are welcome to our barbering services ")
    clipper(3)
else: 
    marital_stat()


             








