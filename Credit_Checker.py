def is_valid_credit_card(number):
    # Convert the credit card number to a list of integers
    digits = [int(d) for d in str(number)]

    # Double every second digit, starting from the right
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2

        # If doubling the digit results in a two-digit number, add the digits together
        if digits[i] > 9:
            digits[i] = sum(divmod(digits[i], 10))

    # Sum all the digits
    total = sum(digits)

    # If the total is divisible by 10, the credit card number is valid
    return total % 10 == 0

card_number=input("Enter your credit card number")

if is_valid_credit_card(card_number):
    print("Credit card number is valid")
else:
    print("Credit card number is invalid")
