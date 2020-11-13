from . import provincialTaxMethods


#Description: Returns After Tax Income
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#Return: A float representing the after tax income
def calculateAfterTaxIncome(beforeTaxIncome,location):
	#If tax deductions and tax credits outweigh tax payable then there is $0 income tax paid
	if location == "Quebec":
		#Quebec has a completely different method of calculating taxes so we cannot use the general methods used for other provinces
		federalTaxesPayable= max(calculateFederalIncomeTax(beforeTaxIncome)-minimalFederalTaxCredits(),0)
		#Federal income tax payable for Quebec is reduced by 16.5% due to the "Quebec Abatement"
		federalTaxesPayable=federalTaxesPayable*(1-0.165)
		provincialTaxesPayable = max(calculateProvincialIncomeTax(beforeTaxIncome,location)-minimumProvincialTaxCredits(location),0)
		QPPandQPIPandEIContributions = calcualateQuebecTaxContributions(beforeTaxIncome)
		return(beforeTaxIncome - federalTaxesPayable - provincialTaxesPayable - QPPandQPIPandEIContributions)
	else:
		federalTaxesPayable= max(calculateFederalIncomeTax(beforeTaxIncome)-minimalFederalTaxCredits(),0)
		provincialTaxesPayable = max(calculateProvincialIncomeTax(beforeTaxIncome,location)-minimumProvincialTaxCredits(location),0)
		cppAndEIDeductions=cppEIDeductions(beforeTaxIncome)
		return (beforeTaxIncome - federalTaxesPayable - provincialTaxesPayable - cppAndEIDeductions)


#Description: Returns amount needed to be paid in federal income taxes
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#Return: A float representing the amount of federal income taxes to be paid
#Source: https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html
def calculateFederalIncomeTax(beforeTaxIncome):
# 15% on the first $48,535 of taxable income, plus
# 20.5% on the next $48,534 of taxable income (on the portion of taxable income over 48,535 up to $97,069), plus
# 26% on the next $53,404 of taxable income (on the portion of taxable income over $97,069 up to $150,473), plus
# 29% on the next $63,895 of taxable income (on the portion of taxable income over 150,473 up to $214,368), plus
# 33% of taxable income over $214,368
	remainingTaxableIncome = beforeTaxIncome
	taxesPayable = 0
	#15% marginal tax
	if remainingTaxableIncome>0:
		taxableIncomeAtPercentBracket = min(remainingTaxableIncome,48535)
		taxesPayable+=taxableIncomeAtPercentBracket*0.15
		remainingTaxableIncome-= taxableIncomeAtPercentBracket
		#20.5% marginal tax
		if remainingTaxableIncome>0:
			taxableIncomeAtPercentBracket = min(remainingTaxableIncome,48534)
			taxesPayable+=taxableIncomeAtPercentBracket*0.205
			remainingTaxableIncome-= taxableIncomeAtPercentBracket
			#26% marginal tax
			if remainingTaxableIncome>0:
				taxableIncomeAtPercentBracket = min(remainingTaxableIncome,53404)
				taxesPayable+=taxableIncomeAtPercentBracket*0.26
				remainingTaxableIncome-= taxableIncomeAtPercentBracket
				#29% marginal tax
				if remainingTaxableIncome>0:
					taxableIncomeAtPercentBracket = min(remainingTaxableIncome,63895)
					taxesPayable+=taxableIncomeAtPercentBracket*0.29
					remainingTaxableIncome-= taxableIncomeAtPercentBracket
					#33% marginal tax
					if remainingTaxableIncome>0:
						taxableIncomeAtPercentBracket = remainingTaxableIncome
						taxesPayable+=taxableIncomeAtPercentBracket*0.33
	return taxesPayable



#Description: Returns amount needed to be paid in provincial income taxes
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#			 location - The province input selected by the user
#Return: A float representing the amount of provincial income taxes to be paid
def calculateProvincialIncomeTax(beforeTaxIncome, location):

	if location=="Alberta":
		return provincialTaxMethods.calculateProvincialIncomeTaxAlberta(beforeTaxIncome)
	elif location=="British Columbia":
		return provincialTaxMethods.calculateProvincialIncomeTaxBritishColumbia(beforeTaxIncome)
	elif location=="Manitoba":
		return provincialTaxMethods.calculateProvincialIncomeTaxManitoba(beforeTaxIncome)
	elif location=="New Brunswick":
		return provincialTaxMethods.calculateProvincialIncomeTaxNewBrunswick(beforeTaxIncome)
	elif location=="Newfoundland and Labrador":
		return provincialTaxMethods.calculateProvincialIncomeTaxNewfoundlandAndLabrador(beforeTaxIncome)
	elif location=="Northwest Territories":
		return provincialTaxMethods.calculateProvincialIncomeTaxNorthwestTerritories(beforeTaxIncome)
	elif location=="Nova Scotia":
		return provincialTaxMethods.calculateProvincialIncomeTaxNovaScotia(beforeTaxIncome)
	elif location=="Nunavut":
		return provincialTaxMethods.calculateProvincialIncomeTaxNunavut(beforeTaxIncome)
	elif location=="Ontario":
		return provincialTaxMethods.calculateProvincialIncomeTaxOntario(beforeTaxIncome)
	elif location=="Prince Edward Island":
		return provincialTaxMethods.calculateProvincialIncomeTaxPrinceEdwardIsland(beforeTaxIncome)
	elif location=="Quebec":
		return provincialTaxMethods.calculateProvincialIncomeTaxQuebec(beforeTaxIncome)
	elif location=="Saskatchewan":
		return provincialTaxMethods.calculateProvincialIncomeTaxSaskatchewan(beforeTaxIncome)
	elif location=="Yukon":
		return provincialTaxMethods.calculateProvincialIncomeTaxYukon(beforeTaxIncome)
	else:
		raise Exception("Location Not Found")
		return -1



#Description: Calculates the minimum amount the income taxes would be reduced by federal tax credits
#Parameters: n/a
#Return: A float representing the amount that federal tax credits will reduce taxes paid
#BPA: https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/federal-government-budgets/basic-personal-amount.html
#Canadian Employment Amount: https://www.taxtips.ca/filing/canadaemployment.htm#:~:text=The%20Canada%20employment%20base%20amount,line%2031260%20of%20Schedule%201
def minimalFederalTaxCredits():
	#Lowest Federal Tax Bracket in 2020 is 15%
	lowestFederalTaxBracket = 0.15
	#In 2020 the Basic Personal Amount is $13,229
	basicPersonalAmountTaxCredit = 13229 * lowestFederalTaxBracket
	#Canadian Employment Amount is $1245
	canadaEmploymentAmountTaxCredit = 1245 * lowestFederalTaxBracket
	minimalFederalTaxCredits = basicPersonalAmountTaxCredit + canadaEmploymentAmountTaxCredit
	return minimalFederalTaxCredits

		

#Description: Calculates the minimum amount the provincial(or overall???) taxes would be reduced by federal tax credits
#Parameters: n/a
#Return: A float representing the amount that provincial(or overall???) tax credits will reduce taxes paid
def minimumProvincialTaxCredits(location):
	#Obtain the minimum provincial tax bracket and the Basic Personal Amount
	result = provincialTaxMethods.minProvincialTaxBracketAndBPA(location)
	minProvincialTaxBracket=result[0]
	basicPersonalAmount=result[1]
	return minProvincialTaxBracket*basicPersonalAmount



#Description: Calculates the amount CPP and EI deductions reduce overall?? taxes paid
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#Return: A float representing the amount that overall?? tax credits will reduce taxes paid
#Source: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html
def cppEIDeductions(beforeTaxIncome):
	#Contribution rate for CPP is 5.25% of before tax income subtracted by the basic exemption amount of $3500
	#The maximum contribution is $2898 per year
	cppDeduction = min((beforeTaxIncome - 3500)*0.0525,2898.00)
	if cppDeduction<0:
		cppDeduction=0
	#Contribution rate for EI is 1.58% of before tax income
	#The maximum contribution is $856.36 per year
	eiDeduction = min(beforeTaxIncome*0.0158,856.36)
	total=cppDeduction+eiDeduction
	return total

#Description: Returns amount needed to be paid in QPP, QPIP and EI to be paid in QUEBEC
#			  QUEBEC INCOME TAXES ARE CALCULATED VERY DIFFERENTLY FROM OTHER PROVINCES
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#Return: A float representing the amount of QPP, QPIP and EI  taxes to be paid in Quebec
def calcualateQuebecTaxContributions(beforeTaxIncome):
	QPPContribution = max((beforeTaxIncome-3500)*0.057,0)
	#Maximum QPP contribution is $3146.40
	QPPContribution = min(QPPContribution,3146.40)
	#Maxium QPIP contribution is $387.79
	QPIPContribution = min(beforeTaxIncome*0.00494,387.79)
	eiContribution = min(beforeTaxIncome*0.0158,856.36)
	return QPPContribution+QPIPContribution+eiContribution



#Description: Detetmines whether or not the savings are sufficient to retire on. Assume 3% dividend
#Parameters: savings - a number
#Return: A boolean value representing if the person has enough savings to retire on
def isEnoughSavingsToRetire(annualIncome,cummulativeCapitalGains,totalSavings,yearlyLivingExpensesRetirement,yearlyLivingExpenses,location):
	#When retiring, assume that person will sell entire savings portfolio and switch to dividend portfolio
	#Capital Gains tax is 50%. This means before tax income is increased by 50% of the capital gains
	#Calculate the total taxes paid for the year
	taxesPaid=(annualIncome+cummulativeCapitalGains*0.50)-calculateAfterTaxIncome((annualIncome+cummulativeCapitalGains*0.50),location)
	#The increase in savings could be negative depending on how much taxes were paid
	increaseInSavings=annualIncome-taxesPaid-yearlyLivingExpenses
	temporaryTotalSavings=totalSavings+increaseInSavings
	#Assume that you will receive 3% in dividends after tax from dividend portfolio
	#3% is a very conservative estimate
	if temporaryTotalSavings*0.03>yearlyLivingExpensesRetirement:
		return True
	else:
		return False



