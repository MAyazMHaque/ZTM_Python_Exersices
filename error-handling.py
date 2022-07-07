while True:
    try:
        height = int(input('Please the your height in cm: '))
        weight = int(input('Please you weight in kg: '))
        print(f'your BMI is {weight / (height/100) ^ 2}')
    except:
        print('Please enter a valid number')
    else:
        print('thankyou!')
        break