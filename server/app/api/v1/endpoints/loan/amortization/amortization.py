def calculate_monthly_payment(principal, interest_rate, term):
    """
    Calculates the monthly payment for a loan.

    Args:
      principal: The loan amount (present value).
      interest_rate: The annual interest rate (as a decimal).
      term: The loan term in years.

    Returns:
      The monthly payment amount.
    """
    # Convert annual interest rate to monthly rate
    monthly_interest_rate = interest_rate / 12

    # Calculate the number of payments
    num_payments = term * 12

    # Use the loan payment formula
    payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / (
      (1 + monthly_interest_rate) ** num_payments - 1
    )

    return payment


def calculate_amortization_schedule(principal, interest_rate, term):
    """
    Calculates the amortization schedule for a loan.

    Args:
      principal: The loan amount (present value).
      interest_rate: The annual interest rate (as a decimal).
      term: The loan term in years.

    Returns:
      A list of dictionaries, each representing a payment in the schedule.
    """
    # Calculate monthly payment
    monthly_payment = calculate_monthly_payment(principal, interest_rate, term)

    # Convert annual interest rate to monthly rate
    monthly_interest_rate = interest_rate / 12

    # Calculate the number of payments
    num_payments = term * 12

    # Initialize schedule list
    schedule = []
    remaining_balance = principal

    # Iterate through each payment period
    for month in range(1, num_payments + 1):
        # Calculate interest paid
        interest_paid = remaining_balance * monthly_interest_rate

        # Calculate principal paid
        principal_paid = monthly_payment - interest_paid

        # Update remaining balance
        remaining_balance -= principal_paid

        # Add payment details to schedule
        schedule.append({
            "Month": month,
            "Payment": monthly_payment,
            "Principal Paid": principal_paid,
            "Interest Paid": interest_paid,
            "Remaining Balance": remaining_balance
        })

    return schedule


def print_amortization_schedule(schedule):
    """
    Prints the amortization schedule in a tabular format.

    Args:
      schedule: A list of dictionaries representing the amortization schedule.
    """
    print("Month\tPayment\tPrincipal\tInterest\tBalance")
    print("-" * 60)
    for row in schedule:
        print(f"{row['Month']}\t{row['Payment']:.2f}\t{row['Principal Paid']:.2f}\t{row['Interest Paid']:.2f}\t{row['Remaining Balance']:.2f}")

    # Example usage
    principal = 10000
    interest_rate = 0.05  # Annual rate
    term = 5  # Years

    amortization_schedule = calculate_amortization_schedule(principal, interest_rate, term)
    print_amortization_schedule(amortization_schedule)