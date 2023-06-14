from django.shortcuts import render


def index_view(request):
    if request.method == 'POST':
        first_number = int(request.POST.get('first_number'))
        second_number = int(request.POST.get('second_number'))
        operation = request.POST.get('operation')
        result = ''
        if operation == 'add':
            operation_result = add(first_number, second_number)
            result = f'Result: {first_number} + {second_number} = {operation_result}'
        elif operation == 'subtract':
            operation_result = subtract(first_number, second_number)
            result = f'Result: {first_number} - {second_number} = {operation_result}'
        elif operation == 'multiply':
            operation_result = multiply(first_number, second_number)
            result = f'Result: {first_number} * {second_number} = {operation_result}'
        elif operation == 'divide':
            operation_result = divide(first_number, second_number)
            result = f'Result: {first_number} / {second_number} = {operation_result}'

        return render(request, 'index.html', {'result': result})

    elif request.method == 'GET':
        return render(request, 'index.html')


def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    if second_number != 0:
        if first_number % second_number == 0:
            return int(first_number / second_number)
        else:
            return round(first_number / second_number, 1)
    else:
        return 'Error: Division by zero'
