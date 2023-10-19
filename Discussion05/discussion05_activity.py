
import logging

def main():
    logging.basicConfig(filename='calculator.log', level=logging.INFO)

    while True:
        try:
            num1 = int(input('Enter numerator >> '))
            num2 = int(input('Enter denominator >> '))
        except ValueError:
            logging.error("Invalid input: Please enter integers only.")
            print("Invalid input. Please enter integers only.")
            continue

        if num2 == 0:
            logging.error("Division by zero: Denominator cannot be zero.")
            print("Denominator cannot be zero. Please enter a non-zero value.")
            continue

        result = num1 / num2
        logging.info(f"Input: {num1}/{num2}, Output: {result}")
        print(num1, '/', num2, '=', result)

        rerun = input('Keep going? [Y/n] >> ')
        if rerun not in ['Y', 'y']:
            break

if __name__ == '__main__':
    main()
