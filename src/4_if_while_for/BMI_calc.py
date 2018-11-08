def BMI_calc(h, w):
    """Check BMI."""
    h = float(h)
    w = float(w)
    bmi = w / h ** 2
    print("your BMI is", bmi)

    if bmi < 18.5:
        print("過輕")
    elif bmi < 24:
        print("適中")
    else:
        print("過重")


height = input("your height in meter?")
weight = input("your weight in kg?")
BMI_calc(height, weight)
