# task 7

while True:
    text = input("Your operation: ")
    operationList = text.split(' ')
    operand1 = int(operationList[0])
    operator = operationList[1]
    operand2 = int(operationList[2])

    '''
    For Step 2 we could use an additional variable
    '''
    result = None  # We don't set a type because of divosion through zero

    '''
    Decide which operation is wanted
    '''
    if operator == '+':
        print(operand1 + operand2)
        result = operand1 + operand2

    elif operator == '-':
        print(operand1 - operand2)
        result = operand1 - operand2

    elif operator == '/':
        '''
        This exception handler is needet if someone wants to divide through zero
        '''
        try:
            print(operand1 / operand2)
            result = operand1 / operand2
        except ZeroDivisionError as error:
            print('Division through zero is not allowed')
            result = 'Division through zero is not allowed'
    else:
        print(operand1 * operand2)
        result = operand1 * operand2

    '''
    This is Step 2 only!
    '''
    with open('calculations.log', 'a') as log:
        logText = '{calculation} = {result}\n'.format(calculation=text,
                                                      result=result)
        log.write(logText)
