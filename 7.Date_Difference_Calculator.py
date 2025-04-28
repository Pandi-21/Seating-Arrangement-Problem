# Problem:
# Calculate the difference in days between two dates given by the user (format: dd-mm-yyyy).
# Example: Find how many days a person has lived.

# solution:
# - Use datetime module to parse the input strings into date objects.
# - Subtract the two dates to find the difference in days.

from datetime import datetime

def dates(start_date_str, end_date_str):
    # Convert string to datetime object
    start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
    end_date = datetime.strptime(end_date_str, "%d-%m-%Y")
    
    #diffe=>difference
    
    diffe = end_date - start_date
    print(f"Difference in start to till now day: {diffe.days}")
 
birth_date = input("Enter your birthdate (dd-mm-yyyy): ")
present_date = input("Enter present_date's date (dd-mm-yyyy): ")

dates(birth_date, present_date)

#enter output format like this
#Enter your birthdate (dd-mm-yyyy): 31-10-2001
#Enter present_date's date (dd-mm-yyyy): 28-04-2025
 
