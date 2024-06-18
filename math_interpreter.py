def main():
    expression = input("Expression: ").split(" ")
    output = "Please enter a valid expression."

    if len(expression) == 3:
        try:
            a = int(expression[0])
            b = int(expression[2])
            sign = expression[1]
            if sign == "+":
                output = (a+b)
            elif sign == "-":
                output = (a-b)
            elif sign == "/":
                output = (a / b)
            elif sign == "*":
                output = (a * b)
        except:
            pass
    try:
        print(f"{output:.2f}")
    except:
        print("Please enter a valid expression.")

main()
