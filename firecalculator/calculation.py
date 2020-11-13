import re
from . import taxCalculation
def calculationMethod(request):
	#Obtain user input and set this data in local variables
	calculationData = dict();
	originalData=dict()
	annualIncome = request.POST["annualIncome"]
	yearlyLivingExpenses = request.POST["yearlyLivingExpenses"]
	yearlyLivingExpensesRetirement = request.POST["yearlyLivingExpensesRetirement"]
	initialSavings= request.POST["savings"]
	incomeGrowth = request.POST["incomeGrowth"]
	returnOnInvestment = request.POST["returnOnInvestment"]
	location = request.POST["location"]
	ageToRetire = request.POST["age"]

	originalData["annualIncome"] = annualIncome
	originalData["yearlyLivingExpenses"]=yearlyLivingExpenses
	originalData["yearlyLivingExpensesRetirement"]=yearlyLivingExpensesRetirement
	originalData["initialSavings"]=initialSavings
	originalData["incomeGrowth"]=incomeGrowth
	originalData["returnOnInvestment"]=returnOnInvestment
	originalData["location"]=location
	originalData["age"]=ageToRetire


	#Convert input variables to ints and doubles
	annualIncome=annualIncome.replace(",",'')
	yearlyLivingExpenses=yearlyLivingExpenses.replace(",","")
	yearlyLivingExpensesRetirement=yearlyLivingExpensesRetirement.replace(",","")
	initialSavings=initialSavings.replace(",","")
	


	
	annualIncome = float(re.search(r"\d+",annualIncome).group(0))
	yearlyLivingExpenses = float(re.search(r"\d+",yearlyLivingExpenses).group(0))
	yearlyLivingExpensesRetirement = float(re.search(r"\d+",yearlyLivingExpensesRetirement).group(0))
	initialSavings = float(re.search(r"\d+",initialSavings).group(0))
	incomeGrowth=float(incomeGrowth)
	returnOnInvestment=float(returnOnInvestment)
	ageToRetire = int(ageToRetire)


	#While Loop that determines age at which person will retire
	#Terminates when Age To Retire >=99 or when the person has sufficient savings to retire on
	calculationData[ageToRetire]=int(initialSavings)
	cummulativeCapitalGains=0

	totalSavings=initialSavings
	while ageToRetire<99:
		ageToRetire+=1
		#Add investment returns to cummulative capital gains
		cummulativeCapitalGains+=(totalSavings*returnOnInvestment/100)
		totalSavings*=(1+returnOnInvestment/100)
		if taxCalculation.isEnoughSavingsToRetire(annualIncome,cummulativeCapitalGains,totalSavings,yearlyLivingExpensesRetirement,yearlyLivingExpenses,location)==True:
			break;
		else:
	 		afterTaxIncome=taxCalculation.calculateAfterTaxIncome(annualIncome,location)
 			totalSavings=totalSavings+afterTaxIncome-yearlyLivingExpenses
 			annualIncome*=(1+incomeGrowth/100)
 			calculationData[ageToRetire]=int(totalSavings)
 			calculationData["ageToRetireBy"]=ageToRetire

	calculationData["originalData"] = originalData

	return calculationData
