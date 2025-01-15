data=[]
def insert_data():
    title=input("Enter the title")
    amount=input("Enter the Amount")
    date=input("Enter the date")
    #print(title+" "+amount+" "+date)
    data.append((title,amount,date))
def display_data():
    for item in data:
            print(item[0]+" "+item[1]+" "+item[2])
y=0
while(y==0):
    print("1->For Insert")
    print("2->For Display")
    print("3->For Delete")
    print("4->For Update")
    opt=int(input("Enter the option you want to perform"))
    if(opt==1):
       insert_data()
    if(opt==2):
       display_data()
    y=int(input("Do you want to continue? press 0 for yes")