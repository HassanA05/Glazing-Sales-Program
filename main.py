from Glazing_Sales_Functions import*

def readEmployeeData():
    Employees = open("EmployeePay.txt","r")
    Salespeople= []
    Salaries = []
    Window_Sales = []
    Door_Sales = []
    Solar_Sales = []
    Tax_Percents = []
    num_employees = 0

    for line in Employees:
        row = line.split(',')
        Salespeople.append(row[0])
        Salaries.append(float(row[1]))
        Window_Sales.append(float(row[2]))
        Door_Sales.append(float(row[3]))
        Solar_Sales.append(float(row[4]))
        Tax_Percents.append(int(row[5]))
        num_employees += 1
        
    Employees.close()

    return Salespeople,Salaries,Window_Sales,Door_Sales,Solar_Sales,Tax_Percents,num_employees


def calculatePayandTax(Salaries,Window_Sales,Door_Sales,Solar_Sales,Tax_Percents,num_employees):                     
    Gross_Pays = []
    Taxes = []
    Net_Pays = []

    for x in range(num_employees):
        Gross_Pays.append(Salaries[x] + bonusCalculation(Window_Sales[x])+ bonusCalculation(Door_Sales[x])+ bonusCalculation(Solar_Sales[x]))
        Taxes.append(Gross_Pays[x] * percentDecimal(Tax_Percents[x]))
        Net_Pays.append(Gross_Pays[x] - Taxes[x])
        
    return Gross_Pays,Taxes,Net_Pays, Window_Sales, Solar_Sales, num_employees

def counting_occuriencies(Salespeople, Salaries, num_employees):

  
 names = []
 count = 0

 for x in range(num_employees):
   if Salaries[x] <= 20000:
     names.append(Salespeople[x])
     count = count + 1

 print("There are", count,"Employees with Salary less than £20,000, Their names are:")

 for x in range(len(names)):
   print(names[x] + ", " , end="")

 print()
 print("------------") 
 return Salespeople, Salaries, num_employees

def displayWritePayInfo(Salespeople,Gross_Pays,Taxes,Net_Pays,num_employees):
    Pay = open("Payroll.txt","w")

    print ("Payroll Info")
    print ("------------")
    print ("Name \t\t\t\t Gross Pay \t\t Tax \t\t\t Net Pay")
    for y in range(num_employees):
        print ((Salespeople[y]),"\t\t\t","£{:.2f}".format(Gross_Pays[y]),"\t\t","£{:.2f}".format(Taxes[y]),"\t\t","£{:.2f}".format(Net_Pays[y]))
        Pay.write(Salespeople[y] + " " + "£{:.2f}".format(Gross_Pays[y]) + " " + "£{:.2f}".format(Taxes[y])+ " " + "£{:.2f}".format(Net_Pays[y]) + "\n")  

    Pay.close()
    print()
    print("--------------------")
    print("Lowest Sales Figures ")
    print("--------------------")
    return Salespeople
    
def find_min(Window_Sales, Salespeople):
 min = Window_Sales[0]
 name = ""
 for x in range(len(Window_Sales)):
   if Window_Sales[x] < min:
     min = Window_Sales[x]
     name = Salespeople[x]
 print("The lowest Window Sales amount is","£{:.2f}".format(min), " And was by",name)

 return Salespeople

def find_max(Solar_Sales, Salespeople, num_employees):
  max = Solar_Sales[0]
  namenew = Salespeople[0]

  for x in range(1, num_employees):
    if Solar_Sales[x] > max:
      max = Solar_Sales[x]
      namenew = Salespeople[x]
  
  print()
  print("--------------------------------")
  print("Solar Sales Figures and Employee")    
  print("--------------------------------")
  
  print("The Highest Solar sales were: £", max, "By", namenew)  
  
  
  return

Salespeople,Salaries,Window_Sales,Door_Sales,Solar_Sales,Tax_Percents,num_employees = readEmployeeData()

Gross_Pays,Taxes,Net_Pays, Window_Sales, Solar_Sales, num_employees = calculatePayandTax(Salaries,Window_Sales,Door_Sales,Solar_Sales,Tax_Percents,num_employees)

Salespeople, Salaries, num_employees = counting_occuriencies(Salespeople, Salaries, num_employees)

Salespeople = displayWritePayInfo(Salespeople,Gross_Pays,Taxes,Net_Pays,num_employees)

find_min(Window_Sales, Salespeople)

find_max(Solar_Sales, Salespeople, num_employees)