
#Description: Returns the lowest provincial tax bracket and the Basic Personal Amount
#Parameters: location - The province input selected by the user
#Return: A tupple representing with the first element being the lowest marginal tax rate and the second element being the Basic Personal Amount
def minProvincialTaxBracketAndBPA(location):
	if location=="Alberta":
		return 0.10,19369
	elif location=="British Columbia":
		return 0.0506,10949
	elif location=="Manitoba":
		return 0.108,9838
	elif location=="New Brunswick":
		return 0.0968,10459
	elif location=="Newfoundland and Labrador":
		return 0.087,9498	
	elif location=="Northwest Territories":
		return 0.059,15093
	elif location=="Nova Scotia":
		return 0.0879,8481
	elif location=="Nunavut":
		return 0.04,16304
	elif location=="Ontario":
		return 0.0505,10783
	elif location=="Prince Edward Island":
		return 0.098,10000	
	elif location=="Quebec":
		return 0.15,15532
	elif location=="Saskatchewan":
		return 0.105,16065
	elif location=="Yukon":
		return 0.064,13229
	else:
		raise Exception("Location Not Found")
		return -1





#Description: Returns amount needed to be paid in provincial income taxes if location is Alberta
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#Return: A float representing the amount of provincial income taxes to be paid if location is Alberta
#Source:https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html#provincial
def calculateProvincialIncomeTaxAlberta(beforeTaxIncome):
	# 10% on the first $131,220 of taxable income, plus
	# 12% on the next $26,244 of taxable income (on the portion of taxable income over $131,220 up to $157,464), plus
	# 13% on the next $52,488 of taxable income (on the portion of taxable income over $157,464 up to $209,952), plus
	# 14% on the next $104,976 of taxable income (on the portion of taxable income over $209,952 up to $314,928), plus
	# 15% of taxable income over $314,928
	remainingTaxableIncome = beforeTaxIncome
	taxesPayable = 0
	#10% marginal tax
	if remainingTaxableIncome>0:
		taxableIncomeAtPercentBracket = min(remainingTaxableIncome,131220)
		taxesPayable+=taxableIncomeAtPercentBracket*0.10
		remainingTaxableIncome-= taxableIncomeAtPercentBracket
		#12% marginal tax
		if remainingTaxableIncome>0:
			taxableIncomeAtPercentBracket = min(remainingTaxableIncome,26244)
			taxesPayable+=taxableIncomeAtPercentBracket*0.12
			remainingTaxableIncome-= taxableIncomeAtPercentBracket
			#13% marginal tax
			if remainingTaxableIncome>0:
				taxableIncomeAtPercentBracket = min(remainingTaxableIncome,52488)
				taxesPayable+=taxableIncomeAtPercentBracket*0.13
				remainingTaxableIncome-= taxableIncomeAtPercentBracket
				#14% marginal tax
				if remainingTaxableIncome>0:
					taxableIncomeAtPercentBracket = min(remainingTaxableIncome,104976)
					taxesPayable+=taxableIncomeAtPercentBracket*0.14
					remainingTaxableIncome-= taxableIncomeAtPercentBracket
					#15% marginal tax
					if remainingTaxableIncome>0:
						taxableIncomeAtPercentBracket = remainingTaxableIncome
						taxesPayable+=taxableIncomeAtPercentBracket*0.15
	return taxesPayable



#Description: Returns amount needed to be paid in provincial income taxes if location is British Columbia
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#Return: A float representing the amount of provincial income taxes to be paid if location is British Columbia
#Source:https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html#provincial
def calculateProvincialIncomeTaxBritishColumbia(beforeTaxIncome):
	# 5.06% on the first $41,725 of taxable income, plus
	# 7.7% on the next $41,725.99 of taxable income (on the portion of taxable income over $41,725 up to $83,451), plus
	# 10.5% on the next $12,360.99 of taxable income (on the portion of taxable income over $83,451 up to $95,812), plus
	# 12.29% on the next $20,531.99 of taxable income (on the portion of taxable income over $95,812 up to $116,344), plus
	# 14.70% on the next $41,403.99 of taxable income (on the portion of taxable income over $116,344 up to $157,748), plus
	# 16.80% on the next $62,251.99 of taxable income (on the portion of taxable income over $157,748 up to $220,000), plus
	# 20.05% of taxable income over $220,000
	remainingTaxableIncome = beforeTaxIncome
	taxesPayable = 0
	#5.06% marginal tax
	if remainingTaxableIncome>0:
		taxableIncomeAtPercentBracket = min(remainingTaxableIncome,41725)
		taxesPayable+=taxableIncomeAtPercentBracket*0.0506
		remainingTaxableIncome-= taxableIncomeAtPercentBracket
		#7.7% marginal tax
		if remainingTaxableIncome>0:
			taxableIncomeAtPercentBracket = min(remainingTaxableIncome,41725.99)
			taxesPayable+=taxableIncomeAtPercentBracket*0.077
			remainingTaxableIncome-= taxableIncomeAtPercentBracket
			#10.5% marginal tax
			if remainingTaxableIncome>0:
				taxableIncomeAtPercentBracket = min(remainingTaxableIncome,12360.99)
				taxesPayable+=taxableIncomeAtPercentBracket*0.105
				remainingTaxableIncome-= taxableIncomeAtPercentBracket
				#12.29% marginal tax
				if remainingTaxableIncome>0:
					taxableIncomeAtPercentBracket = min(remainingTaxableIncome,20531.99)
					taxesPayable+=taxableIncomeAtPercentBracket*0.1229
					remainingTaxableIncome-= taxableIncomeAtPercentBracket
					#14.70% marginal tax
					if remainingTaxableIncome>0:
						taxableIncomeAtPercentBracket = min(remainingTaxableIncome,41403.99)
						taxesPayable+=taxableIncomeAtPercentBracket*0.147
						remainingTaxableIncome-= taxableIncomeAtPercentBracket	
						#16.80% marginal tax
						if remainingTaxableIncome>0:
							taxableIncomeAtPercentBracket = min(remainingTaxableIncome,62251.99)
							taxesPayable+=taxableIncomeAtPercentBracket*0.168
							remainingTaxableIncome-= taxableIncomeAtPercentBracket	
							#20.5% marginal tax
							if remainingTaxableIncome>0:
								taxableIncomeAtPercentBracket = remainingTaxableIncome
								taxesPayable+=taxableIncomeAtPercentBracket*0.205
	return taxesPayable


#Description: Returns amount needed to be paid in provincial income taxes if location is Manitoba
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#Return: A float representing the amount of provincial income taxes to be paid if location is Manitoba
#Source: https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html#provincial
def calculateProvincialIncomeTaxManitoba(beforeTaxIncome):
	# 10.8% on the first $33,389 of taxable income, plus
	# 12.75% on the next $38,775 of taxable income (on the portion of taxable income over $33,389 up to $72,164), plus
	# 17.4% of taxable income over $72,164
	remainingTaxableIncome = beforeTaxIncome
	taxesPayable = 0
	#10.8% marginal tax
	if remainingTaxableIncome>0:
		taxableIncomeAtPercentBracket = min(remainingTaxableIncome,33389)
		taxesPayable+=taxableIncomeAtPercentBracket*0.108
		remainingTaxableIncome-= taxableIncomeAtPercentBracket
		#12.75% marginal tax
		if remainingTaxableIncome>0:
			taxableIncomeAtPercentBracket = min(remainingTaxableIncome,38775)
			taxesPayable+=taxableIncomeAtPercentBracket*0.1275
			remainingTaxableIncome-= taxableIncomeAtPercentBracket
			#17.4% marginal tax
			if remainingTaxableIncome>0:
				taxableIncomeAtPercentBracket = remainingTaxableIncome
				taxesPayable+=taxableIncomeAtPercentBracket*0.174
	return taxesPayable


#Description: Returns amount needed to be paid in provincial income taxes if location is New Brunswick
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#Return: A float representing the amount of provincial income taxes to be paid if location is New Brunswick
#Source: https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html#provincial
def calculateProvincialIncomeTaxNewBrunswick(beforeTaxIncome):
	# 9.68% on the first $43,401 of taxable income, plus
	# 14.82% on the next $43,402 of taxable income (on the portion of taxable income over $43,401 up to $86,803), plus
	# 16.52% on the next $54,319 of taxable income (on the portion of taxable income over $86,803 up to $141,122), plus
	# 17.84% on the next $19,654 of taxable income (on the portion of taxable income over $141,122 up to $160,776), plus
	# 20.3% of taxable income over $160,776
	remainingTaxableIncome = beforeTaxIncome
	taxesPayable = 0
	#9.68% marginal tax
	if remainingTaxableIncome>0:
		taxableIncomeAtPercentBracket = min(remainingTaxableIncome,43401)
		taxesPayable+=taxableIncomeAtPercentBracket*0.0968
		remainingTaxableIncome-= taxableIncomeAtPercentBracket
		#14.82% marginal tax
		if remainingTaxableIncome>0:
			taxableIncomeAtPercentBracket = min(remainingTaxableIncome,43402)
			taxesPayable+=taxableIncomeAtPercentBracket*0.1482
			remainingTaxableIncome-= taxableIncomeAtPercentBracket
			#16.52% marginal tax
			if remainingTaxableIncome>0:
				taxableIncomeAtPercentBracket = min(remainingTaxableIncome,54319)
				taxesPayable+=taxableIncomeAtPercentBracket*0.1652
				remainingTaxableIncome-= taxableIncomeAtPercentBracket
				#17.84% marginal tax
				if remainingTaxableIncome>0:
					taxableIncomeAtPercentBracket = min(remainingTaxableIncome,19654)
					taxesPayable+=taxableIncomeAtPercentBracket*0.1784
					remainingTaxableIncome-= taxableIncomeAtPercentBracket
					#20.3% marginal tax
					if remainingTaxableIncome>0:
						taxableIncomeAtPercentBracket = remainingTaxableIncome
						taxesPayable+=taxableIncomeAtPercentBracket*0.203
	return taxesPayable


#Description: Returns amount needed to be paid in provincial income taxes if location is Newfoundland and Labrador
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#Return: A float representing the amount of provincial income taxes to be paid if location is Newfoundland and Labrador
def calculateProvincialIncomeTaxNewfoundlandAndLabrador(beforeTaxIncome):
	# 8.7% on the first $37,929 of taxable income, plus
	# 14.5% on the next $37,929 of taxable income (on the portion of taxable income over $37,929 up to $75,858), plus
	# 15.8% on the next $59,574 of taxable income (on the portion of taxable income over $75,858 up to $135,432), plus
	# 17.3% on the next $54,172 of taxable income (on the portion of taxable income over $135,432 up to $189,604), plus
	# 18.3% of taxable income over $189,604
	#Source: https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html#provincial
	remainingTaxableIncome = beforeTaxIncome
	taxesPayable = 0
	# 8.7% marginal tax
	if remainingTaxableIncome>0:
		taxableIncomeAtPercentBracket = min(remainingTaxableIncome,37929)
		taxesPayable+=taxableIncomeAtPercentBracket*0.087
		remainingTaxableIncome-= taxableIncomeAtPercentBracket
		#14.5% marginal tax
		if remainingTaxableIncome>0:
			taxableIncomeAtPercentBracket = min(remainingTaxableIncome,37929)
			taxesPayable+=taxableIncomeAtPercentBracket*0.145
			remainingTaxableIncome-= taxableIncomeAtPercentBracket
			#15.8% marginal tax
			if remainingTaxableIncome>0:
				taxableIncomeAtPercentBracket = min(remainingTaxableIncome,59574)
				taxesPayable+=taxableIncomeAtPercentBracket*0.158
				remainingTaxableIncome-= taxableIncomeAtPercentBracket
				#17.3% marginal tax
				if remainingTaxableIncome>0:
					taxableIncomeAtPercentBracket = min(remainingTaxableIncome,54172)
					taxesPayable+=taxableIncomeAtPercentBracket*0.173
					remainingTaxableIncome-= taxableIncomeAtPercentBracket
					#18.3% marginal tax
					if remainingTaxableIncome>0:
						taxableIncomeAtPercentBracket = remainingTaxableIncome
						taxesPayable+=taxableIncomeAtPercentBracket*0.183
	return taxesPayable


#Description: Returns amount needed to be paid in provincial income taxes if location is Northwest Territorie
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#Return: A float representing the amount of provincial income taxes to be paid if location is Northwest Territorie
#Source: https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html#provincial
def calculateProvincialIncomeTaxNorthwestTerritories(beforeTaxIncome):
	# 5.9% on the first $43,957 of taxable income, plus
	# 8.6% on the next $43,959 of taxable income (on the portion of taxable income over $43,957 up to $87,916), plus
	# 12.2% on the next $55,016 of taxable income (on the portion of taxable income over $87,916 up to $142,932), plus
	# 14.05% of taxable income over $142,932
	remainingTaxableIncome = beforeTaxIncome
	taxesPayable = 0
	#5.9% marginal tax
	if remainingTaxableIncome>0:
		taxableIncomeAtPercentBracket = min(remainingTaxableIncome,43957)
		taxesPayable+=taxableIncomeAtPercentBracket*0.059
		remainingTaxableIncome-= taxableIncomeAtPercentBracket
		#8.6% marginal tax
		if remainingTaxableIncome>0:
			taxableIncomeAtPercentBracket = min(remainingTaxableIncome,43959)
			taxesPayable+=taxableIncomeAtPercentBracket*0.086
			remainingTaxableIncome-= taxableIncomeAtPercentBracket
			#12.2% marginal tax
			if remainingTaxableIncome>0:
				taxableIncomeAtPercentBracket = min(remainingTaxableIncome,55016)
				taxesPayable+=taxableIncomeAtPercentBracket*0.122
				remainingTaxableIncome-= taxableIncomeAtPercentBracket
				#14.05% marginal tax
				if remainingTaxableIncome>0:
					taxableIncomeAtPercentBracket = remainingTaxableIncome
					taxesPayable+=taxableIncomeAtPercentBracket*0.1405
	return taxesPayable


#Description: Returns amount needed to be paid in provincial income taxes if location is Nova Scotia
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#Return: A float representing the amount of provincial income taxes to be paid if location is Nova Scotia
#Source: https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html#provincial
def calculateProvincialIncomeTaxNovaScotia(beforeTaxIncome):
	# 8.79% on the first $29,590  of taxable income, plus
	# 14.95% on the next $29,590 of taxable income (on the portion of taxable income over $29,590 up to $59,180), plus
	# 16.67% on the next $33,820 of taxable income (on the portion of taxable income over $59,180 up to $93,000), plus
	# 17.5% on the next $57,000 of taxable income (on the portion of taxable income over $93,000 up to $150,000), plus
	# 21% of taxable income over $150,000
	remainingTaxableIncome = beforeTaxIncome
	taxesPayable = 0
	#8.79% marginal tax
	if remainingTaxableIncome>0:
		taxableIncomeAtPercentBracket = min(remainingTaxableIncome,29590)
		taxesPayable+=taxableIncomeAtPercentBracket*0.0879
		remainingTaxableIncome-= taxableIncomeAtPercentBracket
		#14.95% marginal tax
		if remainingTaxableIncome>0:
			taxableIncomeAtPercentBracket = min(remainingTaxableIncome,29590)
			taxesPayable+=taxableIncomeAtPercentBracket*0.1495
			remainingTaxableIncome-= taxableIncomeAtPercentBracket
			#16.67% marginal tax
			if remainingTaxableIncome>0:
				taxableIncomeAtPercentBracket = min(remainingTaxableIncome,33820)
				taxesPayable+=taxableIncomeAtPercentBracket*0.1667
				remainingTaxableIncome-= taxableIncomeAtPercentBracket
				#17.5% marginal tax
				if remainingTaxableIncome>0:
					taxableIncomeAtPercentBracket = min(remainingTaxableIncome,57000)
					taxesPayable+=taxableIncomeAtPercentBracket*0.175
					remainingTaxableIncome-= taxableIncomeAtPercentBracket
					#21% marginal tax
					if remainingTaxableIncome>0:
						taxableIncomeAtPercentBracket = remainingTaxableIncome
						taxesPayable+=taxableIncomeAtPercentBracket*0.21
	return taxesPayable


#Description: Returns amount needed to be paid in provincial income taxes if location is Nunavut
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#Return: A float representing the amount of provincial income taxes to be paid if location is Nunavut
#Source: https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html#provincial
def calculateProvincialIncomeTaxNunavut(beforeTaxIncome):
	# 4% on the first $46,277 of taxable income, plus
	# 7% on the next $46,278 of taxable income (on the portion of taxable income over $46,277 up to $92,555), plus
	# 9% on the next $57,918 of taxable income (on the portion of taxable income over $92,555 up to $150,473), plus
	# 11.5% of taxable income over $150,473	
	remainingTaxableIncome = beforeTaxIncome
	taxesPayable = 0
	#4% marginal tax
	if remainingTaxableIncome>0:
		taxableIncomeAtPercentBracket = min(remainingTaxableIncome,46277)
		taxesPayable+=taxableIncomeAtPercentBracket*0.04
		remainingTaxableIncome-= taxableIncomeAtPercentBracket
		#7% marginal tax
		if remainingTaxableIncome>0:
			taxableIncomeAtPercentBracket = min(remainingTaxableIncome,46278)
			taxesPayable+=taxableIncomeAtPercentBracket*0.07
			remainingTaxableIncome-= taxableIncomeAtPercentBracket
			#9% marginal tax
			if remainingTaxableIncome>0:
				taxableIncomeAtPercentBracket = min(remainingTaxableIncome,57918)
				taxesPayable+=taxableIncomeAtPercentBracket*0.09
				remainingTaxableIncome-= taxableIncomeAtPercentBracket
				#11.5% marginal tax
				if remainingTaxableIncome>0:
					taxableIncomeAtPercentBracket = remainingTaxableIncome
					taxesPayable+=taxableIncomeAtPercentBracket*0.115
	return taxesPayable


#Description: Returns amount needed to be paid in provincial income taxes if location is Ontario
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#Return: A float representing the amount of provincial income taxes to be paid if location is Ontario
#Source: https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html#provincial
def calculateProvincialIncomeTaxOntario(beforeTaxIncome):
	# 5.05% on the first $44,740 of taxable income, plus
	# 9.15% on the next $44,742 of taxable income (on the portion of taxable income over $44,740 up to $89,482), plus
	# 11.16% on the next $60,518 of taxable income (on the portion of taxable income over $89,482 up to $150,000), plus
	# 12.16% on the next $70,000 of taxable income (on the portion of taxable income over $150,000 up to $220,000), plus
	# 13.16% of taxable income over $220,000
	remainingTaxableIncome = beforeTaxIncome
	taxesPayable = 0
	#5.05% marginal tax
	if remainingTaxableIncome>0:
		taxableIncomeAtPercentBracket = min(remainingTaxableIncome,44740)
		taxesPayable+=taxableIncomeAtPercentBracket*0.0505
		remainingTaxableIncome-= taxableIncomeAtPercentBracket
		#9.15% marginal tax
		if remainingTaxableIncome>0:
			taxableIncomeAtPercentBracket = min(remainingTaxableIncome,44742)
			taxesPayable+=taxableIncomeAtPercentBracket*0.0915
			remainingTaxableIncome-= taxableIncomeAtPercentBracket
			#11.16% marginal tax
			if remainingTaxableIncome>0:
				taxableIncomeAtPercentBracket = min(remainingTaxableIncome,60518)
				taxesPayable+=taxableIncomeAtPercentBracket*0.1116
				remainingTaxableIncome-= taxableIncomeAtPercentBracket
				#12.16% marginal tax
				if remainingTaxableIncome>0:
					taxableIncomeAtPercentBracket = min(remainingTaxableIncome,70000)
					taxesPayable+=taxableIncomeAtPercentBracket*0.1216
					remainingTaxableIncome-= taxableIncomeAtPercentBracket
					#13.16% marginal tax
					if remainingTaxableIncome>0:
						taxableIncomeAtPercentBracket = remainingTaxableIncome
						taxesPayable+=taxableIncomeAtPercentBracket*0.1316
	#Ontario has a surtax
	# where the provincial tax payable is less than or equal to $4,830, the surtax is $0
	# where the provincial tax payable is greater than $4,830 and less than or equal to $6,182, the surtax is 20% of the basic provincial tax payable over $4,830
	# where the provincial tax payable is greater than $6,182, the surtax is 20% of the basic provincial tax payable over $4,830, plus 36% of the basic provincial tax payable over $6,182
	surtax=0
	if(taxesPayable>4830 and taxesPayable<6182):
		surtax=1352*0.2
	elif(taxesPayable>=6182):
		surtax= (1352*0.2 + (taxesPayable-6182)*0.56)

	taxesPayable+=surtax
	return taxesPayable


#Description: Returns amount needed to be paid in provincial income taxes if location is Prince Edward Island
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#Return: A float representing the amount of provincial income taxes to be paid if location is Prince Edward Island
#Source: https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html#provincial
def calculateProvincialIncomeTaxPrinceEdwardIsland(beforeTaxIncome):
	# 9.8% on the first $31,984 of taxable income, plus
	# 13.8% on the next $31,985 of taxable income (on the portion of taxable income over $31,984 up to $63,969), plus
	# 16.7% of taxable income over $63,969
	remainingTaxableIncome = beforeTaxIncome
	taxesPayable = 0
	#10.8% marginal tax
	if remainingTaxableIncome>0:
		taxableIncomeAtPercentBracket = min(remainingTaxableIncome,31984)
		taxesPayable+=taxableIncomeAtPercentBracket*0.098
		remainingTaxableIncome-= taxableIncomeAtPercentBracket
		#12.75% marginal tax
		if remainingTaxableIncome>0:
			taxableIncomeAtPercentBracket = min(remainingTaxableIncome,31985)
			taxesPayable+=taxableIncomeAtPercentBracket*0.138
			remainingTaxableIncome-= taxableIncomeAtPercentBracket
			#17.4% marginal tax
			if remainingTaxableIncome>0:
				taxableIncomeAtPercentBracket = remainingTaxableIncome
				taxesPayable+=taxableIncomeAtPercentBracket*0.167
	#Prince Edward Island has a surtax
	# where the provincial tax payable is less than or equal to $12500, the surtax is $0
	# where the provincial tax payable is greater than $12500 the surtax is 10% of the provincial tax payable
	surtax=0
	if taxesPayable>12500:
		surtax= (taxesPayable-12500)*0.10
	taxesPayable+=surtax
	return taxesPayable



#Description: Returns amount needed to be paid in provincial income taxes if location is Saskatchewan
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#Return: A float representing the amount of provincial income taxes to be paid if location is Saskatchewan
#Source: https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html#provincial
def calculateProvincialIncomeTaxSaskatchewan(beforeTaxIncome):
	# 10.5% on the first $45,225 of taxable income, plus
	# 12.5% on the next $83,989 of taxable income (on the portion of taxable income over $45,225 up to $129,214), plus
	# 14.5% of taxable income over $129,214
	remainingTaxableIncome = beforeTaxIncome
	taxesPayable = 0
	#10.5% marginal tax
	if remainingTaxableIncome>0:
		taxableIncomeAtPercentBracket = min(remainingTaxableIncome,45225)
		taxesPayable+=taxableIncomeAtPercentBracket*0.105
		remainingTaxableIncome-= taxableIncomeAtPercentBracket
		#12.5% marginal tax
		if remainingTaxableIncome>0:
			taxableIncomeAtPercentBracket = min(remainingTaxableIncome,83989)
			taxesPayable+=taxableIncomeAtPercentBracket*0.125
			remainingTaxableIncome-= taxableIncomeAtPercentBracket
			#14.5% marginal tax
			if remainingTaxableIncome>0:
				taxableIncomeAtPercentBracket = remainingTaxableIncome
				taxesPayable+=taxableIncomeAtPercentBracket*0.145
	return taxesPayable



#Description: Returns amount needed to be paid in provincial income taxes if location is Yukon
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#Return: A float representing the amount of provincial income taxes to be paid if location is Yukon
#Source: https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html#provincial
def calculateProvincialIncomeTaxYukon(beforeTaxIncome):
	# 6.4% on the first $48,535 of taxable income, plus
	# 9% on the next $48,534 of taxable income (on the portion of taxable income over $48,535 up to $97,069), plus
	# 10.9% on the next $53,404 of taxable income (on the portion of taxable income over $97,069 up to $150,473), plus
	# 12.8% on the next $349,527 of taxable income (on the portion of taxable income over over $150,473 up to $500,000), plus
	# 15% of taxable income over $500,000
	remainingTaxableIncome = beforeTaxIncome
	taxesPayable = 0
	#6.4% marginal tax
	if remainingTaxableIncome>0:
		taxableIncomeAtPercentBracket = min(remainingTaxableIncome,48535)
		taxesPayable+=taxableIncomeAtPercentBracket*0.064
		remainingTaxableIncome-= taxableIncomeAtPercentBracket
		#9% marginal tax
		if remainingTaxableIncome>0:
			taxableIncomeAtPercentBracket = min(remainingTaxableIncome,48534)
			taxesPayable+=taxableIncomeAtPercentBracket*0.09
			remainingTaxableIncome-= taxableIncomeAtPercentBracket
			#10.9% marginal tax
			if remainingTaxableIncome>0:
				taxableIncomeAtPercentBracket = min(remainingTaxableIncome,53404)
				taxesPayable+=taxableIncomeAtPercentBracket*0.109
				remainingTaxableIncome-= taxableIncomeAtPercentBracket
				#12.8% marginal tax
				if remainingTaxableIncome>0:
					taxableIncomeAtPercentBracket = min(remainingTaxableIncome,349527)
					taxesPayable+=taxableIncomeAtPercentBracket*0.128
					remainingTaxableIncome-= taxableIncomeAtPercentBracket
					#15% marginal tax
					if remainingTaxableIncome>0:
						taxableIncomeAtPercentBracket = remainingTaxableIncome
						taxesPayable+=taxableIncomeAtPercentBracket*0.15
	return taxesPayable



#Description: Returns amount needed to be paid in provincial income taxes if location is Quebec
#			  QUEBEC INCOME TAXES ARE CALCULATED VERY DIFFERENTLY FROM OTHER PROVINCES
#Parameters: beforeTaxIncome - Income before any taxes or payroll deductions
#Return: A float representing the amount of TOTAL income taxes to be paid if location is Quebec
def calculateProvincialIncomeTaxQuebec(beforeTaxIncome):
	# 15% on the first $44,545 of taxable income, plus
	# 20% on the next $44,535 of taxable income (on the portion of taxable income over $44,545 up to $89,080), plus
	# 24% on the next $19,310 of taxable income (on the portion of taxable income over $89,080 up to $108,390), plus
	# 25.75% of taxable income over $108,390
	remainingTaxableIncome = beforeTaxIncome
	taxesPayable = 0
	#15% marginal tax
	if remainingTaxableIncome>0:
		taxableIncomeAtPercentBracket = min(remainingTaxableIncome,44545 )
		taxesPayable+=taxableIncomeAtPercentBracket*0.15
		remainingTaxableIncome-= taxableIncomeAtPercentBracket
		#20% marginal tax
		if remainingTaxableIncome>0:
			taxableIncomeAtPercentBracket = min(remainingTaxableIncome,44535)
			taxesPayable+=taxableIncomeAtPercentBracket*0.20
			remainingTaxableIncome-= taxableIncomeAtPercentBracket
			#24% marginal tax
			if remainingTaxableIncome>0:
				taxableIncomeAtPercentBracket = min(remainingTaxableIncome,19310)
				taxesPayable+=taxableIncomeAtPercentBracket*0.24
				remainingTaxableIncome-= taxableIncomeAtPercentBracket
				#25.75% marginal tax
				if remainingTaxableIncome>0:
					taxableIncomeAtPercentBracket = remainingTaxableIncome
					taxesPayable+=taxableIncomeAtPercentBracket*0.2575
	return taxesPayable



















