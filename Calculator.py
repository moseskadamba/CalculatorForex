from tkinter import *

root = Tk()
root.title("Position Sizing Calculator")

#Entry fields
entryAccountSize = Entry(root, borderwidth=5)
entryRiskPercentage = Entry(root, borderwidth=5)
entryPips = Entry(root, borderwidth=5)

entryAccountSize.grid(row=1, column=1)
entryRiskPercentage.grid(row=2, column=1)
entryPips.grid(row=3, column=1)

labelResultLotSize = ""
labelResultRiskAmount = ""

def formularSizing():

   account_amount = float(entryAccountSize.get())
   risk_percent = float(entryRiskPercentage.get())
   pips_no = float(entryPips.get())

   risk_amount = account_amount*risk_percent/100
   result = risk_amount/(pips_no*10)
   
   labelResultLotSize = Label(root, text=str(round(result,2)))
   labelResultRiskAmount = Label(root, text=str(risk_amount))
   
   labelResultLotSize.grid(row=7, column=1)
   labelResultRiskAmount.grid(row=8, column=1)
   

#function to clear pip entry
def clearFun():
   entryPips.delete(0, END)

# Creating a Label widget
labelTitle = Label(root, text="")

labelAcountSize = Label(root, text="Account Size")
labelRiskPercentage = Label(root, text="Risk Ratio in %")
labelPips = Label(root, text="Pips to Risk")

labelLotSize = Label(root, text="Lot Size")
labelRiskAmount = Label(root, text="Amount $")


buttonCalculate = Button(root, text="Calculate", padx=30, command=formularSizing)
buttonClear = Button(root, text="Clear", padx=30, command=clearFun)

# shoving it into the screen
labelTitle.grid(row=0, column=1)

labelAcountSize.grid(row=1, column=0)
labelRiskPercentage.grid(row=2, column=0)
labelPips.grid(row=3, column=0)


labelLotSize.grid(row=7, column=0)
labelRiskAmount.grid(row=8, column=0)

buttonCalculate.grid(row=9,column=0)
buttonClear.grid(row=9, column=1)

root.mainloop()
