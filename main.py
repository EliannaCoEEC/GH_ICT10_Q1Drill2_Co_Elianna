# working with numbers
from pyscript import display, document

# adds num 1 and num 2
def adding_numbers(e):
    document.getElementById('result').innerHTML = " " # clear the previous output
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    sum = first_number + second_number

    display(f'The sum of {first_number} and {second_number} is {sum}', target='result')

# subtracts num 2 from num 1
def subtracting_numbers(e):
    document.getElementById('result').innerHTML = " " # clear the previous output
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    difference = first_number - second_number

    display(f'The difference of {first_number} and {second_number} is {difference}', target='result')

# multiplies num 1 by num 2
def multiplying_numbers(e):
    document.getElementById('result').innerHTML = " " # clear the previous output
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    product = first_number * second_number

    display(f'The product of {first_number} and {second_number} is {product}', target='result')

# divides num 1 by num 2
def dividing_numbers(e):
    document.getElementById('result').innerHTML = " " # clear the previous output
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    quotient = first_number / second_number

    display(f'The quotient of {first_number} and {second_number} is {quotient}', target='result')

# exponentiates num 1 by num 2
def exponentiating_numbers(e):
    document.getElementById('result').innerHTML = " " # clear the previous output
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    power = first_number ** second_number

    display(f'The power of {first_number} and {second_number} is {power}', target='result')