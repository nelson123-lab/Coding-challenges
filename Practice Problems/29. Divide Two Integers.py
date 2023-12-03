def divide(dividend, divisor):
    # Handle edge case: divisor is 0
    if divisor == 0:
        raise ValueError("Cannot divide by zero")

    # Handle overflow cases
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1

    # Determine the sign of the result
    negative = (dividend < 0) ^ (divisor < 0)

    # Convert both dividend and divisor to positive numbers
    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            quotient += i
            i <<= 1
            temp <<= 1

    # Restore the sign of the result
    return -quotient if negative else quotient
