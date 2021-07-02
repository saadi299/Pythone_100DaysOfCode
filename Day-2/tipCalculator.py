#Ask for total bill
totalBill=int(input("Your total bill = \n"))

tip=int(input("tip: 10, 12 or 15 percent = \n"))

totalPerson=int(input("total person"));

if tip==10:
    eachPersonBill=round((totalBill+(totalBill*10/100)) / totalPerson)
    print("Each Peron Bill = ",eachPersonBill)

elif tip == 12:
    eachPersonBill = round((totalBill + (totalBill * 12 / 100)) / totalPerson)
    print("Each Peron Bill = ", eachPersonBill)

elif tip == 15:
    eachPersonBill = round((totalBill + (totalBill * 15 / 100)) / totalPerson)
    print("Each Peron Bill = ", eachPersonBill)


