#interest calculator

#list to contain results
results_list = []

#simple annual interest
def smp_interest(principal, interest_rate, years):
    smpinterest = principal * interest_rate/100 * years
    return smpinterest

#simple non-annual interest
def smp_nonan_interest(principal, interest_rate, years, computation_frequency):
    smpnonan_interest = principal * (interest_rate/100 * 1/computation_frequency) * years * computation_frequency
    return smpnonan_interest 

# compound interest compounded annually
def cmp_an_interest(principal, interest_rate, years):
    cmpan_interest = principal * (1 + interest_rate / 100) ** years
    return cmpan_interest - principal

# function for compound interest other than annually
def cmp_interest(principal , interest_rate, years, cmp_frequency):
    cmpinterest = principal * (1 + (interest_rate / 100) * 1 / cmp_frequency) ** (years * cmp_frequency)
    return cmpinterest - principal

#total amount payable
def amount_payable(principal, interest):
    amtpayble = principal + interest
    return amtpayble 

#add results to list
def add_to_results(result_message):
    results_list.append(result_message)
    print(result_message)

#view results
def view_results():
    if results_list:
        print("Calculated Results:")
        for idx, result in enumerate(results_list, 1):
            print(f"{idx}. {result}")
    else:
        print("No results to display.")

def main():
    print("Interest Calculator")

    principal = 0
    result = 0
    years = 0

    while True:
        interest_type = input("Press \"s\" for simple interest and \"c\" for compound interest, \"v\" to view results or press \"e\" to exit the program: ")

        if interest_type == "e":
            print("Exiting the program, Have a good day!")
            break

        elif interest_type == "v":
            view_results()

        #simple annual interest
        elif interest_type == "s":
            principal = eval(input("Enter the principal: "))
            interest_rate = float(input("Enter the rate of interest per year: ")) 
            years = eval(input("Enter the number of years: "))
            type_of_smpinterest = input("Press \"a\" for annual and \"o\" for non-annual interest: ")
        
            if type_of_smpinterest == "a":
                result = smp_interest(principal, interest_rate, years)
                total_amount = amount_payable(principal, result)
                result_message = f'The interest after {years} years is: ${result}, ' \
                             f'and the total amount due is: ${total_amount}'
                
            elif type_of_smpinterest == "o":
                computing_frequency = input("Press \"q\" for quarterly computing and \"m\" for monthly computing:")
                
                if computing_frequency == "q":
                    comp_frequency = 4
                    result = smp_nonan_interest(principal, interest_rate, years, comp_frequency)
                    total_amount = amount_payable(principal, result)
                    result_message = f'The interest after {years} years is: ${result}, ' \
                             f'and the total amount due is: ${total_amount}'
                    
                elif computing_frequency == "m":
                    comp_frequency = 12
                    result = smp_nonan_interest(principal, interest_rate, years, comp_frequency)
                    total_amount = amount_payable(principal, result)
                    result_message = f'The interest after {years} years is: ${result}, ' \
                             f'and the total amount due is: ${total_amount}'

                else:
                    print("Invalid choice. Try again.")
                    continue
            
            else:
                print("Invalid choice. Try again.")
                continue

        #compound interest
        elif interest_type == "c":
            principal = eval(input("Enter the principal: "))
            interest_rate = float(input("Enter the rate of interest per year: ")) 
            years = eval(input("Enter the number of years: "))
            type_of_cmp = input("Press \"a\" for annual compounding and \"o\" for other: ")

            #annual compound interest
            if type_of_cmp == "a":
                result = cmp_an_interest(principal, interest_rate, years)
                total_amount = amount_payable(principal, result)
                result_message = f'The interest after {years} years is: ${result}, ' \
                             f'and the total amount due is: ${total_amount}'

            #non-annual compound interest
            elif type_of_cmp == "o":
                comp_frequency = input("Press \"q\" for quarterly compounding, \"m\" for monthly compounding and \"d\" for daily compounding: ")
            
                if comp_frequency == "q":
                    cmp_frequency = 4
                    result = cmp_interest(principal, interest_rate, years, cmp_frequency)
                    total_amount = amount_payable(principal, result)
                    result_message = f'The interest after {years} years is: ${result}, ' \
                             f'and the total amount due is: ${total_amount}'

                elif comp_frequency == "m":
                    cmp_frequency = 12
                    result = cmp_interest(principal, interest_rate, years, cmp_frequency)
                    total_amount = amount_payable(principal, result)
                    result_message = f'The interest after {years} years is: ${result}, ' \
                             f'and the total amount due is: ${total_amount}'

                elif comp_frequency == "d":
                    cmp_frequency = 365
                    result = cmp_interest(principal, interest_rate, years, cmp_frequency)
                    total_amount = amount_payable(principal, result)
                    result_message = f'The interest after {years} years is: ${result}, ' \
                             f'and the total amount due is: ${total_amount}'
                    

                else:
                    print("Invalid choice. Try again.")
                    continue
            
            else:
                print("Invalid choice. Try again.")
                continue
                
        else:
            print("Invalid choice. Try again.")
            continue
        
        
        
        add_to_results(result_message)

main()