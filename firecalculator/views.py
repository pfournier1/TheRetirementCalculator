from django.shortcuts import render
from . import calculation

def home(request):
	return render(request, 'firecalculator/home.html')

def about(request):
	return render(request, 'firecalculator/about.html')
 
def methodology(request):
	return render(request, 'firecalculator/methodology.html')

def result(request):
	calculationData=calculation.calculationMethod(request)
	if calculationData["ageToRetireBy"]==99:
		return render(request,'firecalculator/noresult.html',{'calculationData':calculationData})
	else:
		return render(request, 'firecalculator/result.html',{'calculationData': calculationData})

def recalculate(request):
	originalData=dict()
	originalData["annualIncome"]=request.POST["annualIncome"]
	originalData["yearlyLivingExpenses"]=request.POST["yearlyLivingExpenses"]
	originalData["yearlyLivingExpensesRetirement"]=request.POST["yearlyLivingExpensesRetirement"]
	originalData["initialSavings"]=request.POST["initialSavings"] 
	originalData["incomeGrowth"]=request.POST["incomeGrowth"] 
	originalData["returnOnInvestment"]=request.POST["returnOnInvestment"] 
	originalData["location"]=request.POST["location"] 
	originalData["age"]=request.POST["age"] 
	return render(request, 'firecalculator/recalculate.html',{'originalData':originalData})