#"""
#Please replace this comment with your solution:
#Feel free to use these strings:
    #"Enter loan term: "
    #"Enter interest rate: "
    #"Enter starting loan: "
    #Enter step value: "
#"Enter stop loan: "
#"""


loanterm = float(input("Enter loan term: "))
interest = float(input("Enter interest rate: "))
startingloan = float(input("Enter starting loan: "))
stepvalue = float(input("Enter step value: "))
stoploan = float(input("Enter stop loan: \n"))


def loan(loanterm, interest, startingloan, stepvalue, stoploan):
	print("\tLoan","Table\n")
	formated_loanterm = "{:.1f}".format(loanterm)
	wholeinterest = interest*100
	formated_interest = "{:.1f}".format(wholeinterest)
	print("\tTerm:  "+ formated_loanterm)
	print("\tInterest Rate:", formated_interest + "%\n")
	print("\tLoan\t\t\tPayment")
	print("\t----", "\t\t\t-------")
	while startingloan <= stoploan:
		payment = (startingloan*interest/12)/(1-(1+interest/12)**(-12*loanterm))
		formated_float = "{:,.2f}".format(payment)
		formated_loan = "{:,.2f}".format(startingloan)
		print("\t$"+formated_loan,"\t\t$"+formated_float)
		startingloan = startingloan + stepvalue
	return

                





loan(loanterm, interest, startingloan, stepvalue, stoploan)







