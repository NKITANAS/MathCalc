import math
import fractions
import sys
import main

# Command Loop, everything here is self-explanatory
while True:
    print("Welcome to the noui version of MathCalc! \nType help for a list of commands.")
    cmd = input()
    if cmd == "help":
        print("mathcalc - outputs info about the mathcalc build you are using")
        print("quadraticfactorer - factors a quadratic equation.")
        print("quadraticinfo - gives you info abouat a quadratic equation(descriminant, roots).")
        print("fractioncalc - A fractions calculator")
        print("fractionsimp - Simplifies fractions")
        print("decfraction - Converts decimals to fractions")
        print("fractiondec - Converts fractions to decimals")
        print("funcangle - Conversts the result of a trigonometric function(ex: sin) and returns it as an angle(ex: input 0.5, returns 30)")
        print("sidecalc - Calculates a side of a right triangle using an angle and a side")
        print("trianglearea - Calculates the area of a triangle")
        print("rectarea - Calculates the area of a rectangle")
        print("trapezoidarea - Calculates the area of a trapezoid")
        print("ellipsearea - Calculates the area of a Ellipse(π = 3.14)")
        print("circlearea - Calculates the area of a circle(π = 3.14)")
        print("exit - exits the program")

    elif cmd == "mathcalc":
        print("Version: main 0.0.0")
        print("Build: 0")
        print("Noui: true")
        print("cmd: 0.0.0")

    elif cmd == "quadraticfactorer":
        a = input("A: ")
        b = input("B: ")
        c = input("C: ")
        print(main.QuadraticFactorer(a, b, c))

    elif cmd == "quadraticinfo":
        a = input("A: ")
        b = input("B: ")
        c = input("C: ")
        print(main.QuadraticInfo(a, b, c))

    elif cmd == "fractioncalc":
        a = input("A numerator: ")
        b = input("A denominator: ")
        c = input("B numerator: ")
        d = input("B denominator: ")
        e = input("Action: ")
        print(main.FractionCalculator(a, b, c, d, e))

    elif cmd == "fractionsimp":
        a = input("Numerator: ")
        b = input("Denominator: ")
        print(main.FractionsSimplifier(a, b))

    elif cmd == "decfraction":
        a = input("Decimal: ")
        print(main.DecimaltoFraction(a))

    elif cmd == "fractiondec":
        a = input("Numerator: ")
        b = input("Denominator: ")
        print(main.FractiontoDecimal(a, b))

    elif cmd == "funcangle":
        a = input("Function(sin, cos, or tg): ")
        b = input("Value: ")
        print(main.FunctoAngle(a, b))

    elif cmd == "sidecalc":
        a = input("Angle(a or b): ")
        b = input("Angle Value: ")
        c = input("Side(a, b, c): ")
        d = input("Side Value: ")
        e = input("Side you want to find: ")
        print(main.SideCalculator(a, b, c, d, e))

    elif cmd == "trianglearea":
        a = input("Base: ")
        b = input("Height: ")
        print(main.TriangleAreaCalc(a, b))

    elif cmd == "rectarea":
        a = input("Base: ")
        b = input("Width/Height: ")
        print(main.RectAreaCalc(a, b))

    elif cmd == "trapezoidarea":
        a = input("Base1: ")
        b = input("Base2: ")
        c = input("Height: ")
        print(main.TrapezoidAreaCalc(a, b, c))

    elif cmd == "ellipsearea":
        a = input("a: ")
        b = input("b: ")
        print(main.EllipseArecalc(a, b))

    elif cmd == "circlearea":
        a = input("Radius: ")
        print(main.CircleAreaCalc(a))
    
    elif cmd == "exit":
        sys.exit()

    else:
        print("Unknown command,", cmd, ". Type help for a list of commands.")