import pandas as pd

# Function to format currency
def currency(x):
    return "${:.2f}".format(x)

# Function to validate yes/no responses
def validate_yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "no", "y", "n"]:
            return response
        else:
            print("Please answer yes or no.")

# Function to validate non-empty responses
def validate_not_blank(question):
    while True:
        response = input(question)
        if response.strip():
            return response.strip()
        else:
            print("Sorry, this can't be blank. Please try again.")

# Function to validate integer input
def validate_integer(question):
    while True:
        response = input(question)
        try:
            return int(response)
        except ValueError:
            print("Please enter a valid integer.")

# Function to calculate ticket price based on age
def calc_ticket_price(age):
    if age < 16:
        return 7.50
    elif age < 65:
        return 10.50
    else:
        return 6.50

# Function to choose payment method
def choose_payment_method(question):
    while True:
        response = input(question).lower()
        if response in ["cash", "credit", "ca", "cr"]:
            return response
        else:
            print("Please choose a valid payment method (cash or credit).")

# Function to validate responses based on a list of options
def validate_response(question, valid_responses):
    while True:
        response = input(question).lower()
        if response in valid_responses:
            return response
        else:
            print("Please choose from the provided options.")

# Constants
MAX_TICKETS = 3
tickets_sold = 0

# Ask user if they want to see the instructions
want_instructions = validate_yes_no('Do you want to read the instructions? ')
if want_instructions == "yes":
    print("Instructions go here")

# Loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = validate_not_blank("Enter your name (or 'xxx' to quit): ")
    if name.lower() == "xxx":
        break

    age = validate_integer("Age: ")
    if age < 12:
        print("Sorry, you are too young for this movie.")
        continue

    ticket_cost = calc_ticket_price(age)
    payment_method = choose_payment_method("Choose a payment method (cash or credit): ")
    print("You chose", payment_method)

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print('Congratulations, you have sold all the tickets.')
else:
    print("You have sold {} ticket/s. There is {} ticket/s remaining.".format(tickets_sold, MAX_TICKETS - tickets_sold))

# DataFrame creation
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

ticket_data = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}

ticket_df = pd.DataFrame(ticket_data)
ticket_df.set_index('Name', inplace=True)

# Calculate total ticket cost (ticket + surcharge)
ticket_df['Total'] = ticket_df['Ticket Price'] + ticket_df['Surcharge']

# Calculate profit for each ticket
ticket_df['Profit'] = ticket_df['Ticket Price'] - 5

# Currency formatting
currency_columns = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for col in currency_columns:
    ticket_df[col] = ticket_df[col].apply(currency)

# Output ticket data
print("---- Ticket Data ----\n")
print(ticket_df)

# Output total ticket sales and profit
total_sales = ticket_df['Total'].sum()
total_profit = ticket_df['Profit'].sum()
print("\nTotal Ticket Sales: {}".format(total_sales))
print("Total Profit: {}".format(total_profit))
