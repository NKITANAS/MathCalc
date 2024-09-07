import sys
import main

print("Welcome to the noui version of MathCalc! \nType help for a list of commands.")
# Command Loop, everything here is self-explanatory
while True:
    cmd = input()
    if cmd == "help":
        print("mathcalc - Outputs info about the mathcalc build you are using")
        print("quadraticfactorer - Factors a quadratic equation.")
        print("quadraticinfo - Gives you info about a quadratic equation(discriminant, roots).")
        print("compoundmasscalc - Calculates the molar mass of a compound")
        print("compoundmolecalc - Calculates the amount of moles of a compound")
        print("fractioncalc - A fractions calculator")
        print("fractionsimp - Simplifies fractions")
        print("decfraction - Converts decimals to fractions")
        print("fractiondec - Converts fractions to decimals")
        print("funcangle - Converts the result of a trigonometric function(ex: sin) and returns it as an angle(ex: input 0.5, returns 30)")
        print("sidecalc - Calculates a side of a right triangle using an angle and a side")
        print("trianglearea - Calculates the area of a triangle")
        print("rectarea - Calculates the area of a rectangle")
        print("trapezoidarea - Calculates the area of a trapezoid")
        print("ellipsearea - Calculates the area of a Ellipse(π = 3.14)")
        print("circlearea - Calculates the area of a circle(π = 3.14)")
        print("exit - Exits the program")

    elif cmd == "mathcalc":
        print(main.version())
        print("BUILD: 0")
        print("CMD: 1.1.0")

    elif cmd == "quadraticfactorer":
        a = float(input("A: "))
        b = float(input("B: "))
        c = float(input("C: "))
        print(main.QuadraticFactorer(a, b, c))

    elif cmd == "quadraticinfo":
        a = float(input("A: "))
        b = float(input("B: "))
        c = float(input("C: "))
        print(main.QuadraticInfo(a, b, c))
    
    elif cmd == "compoundmasscalc":
        a = input("Compound:")
        print(main.CompoundMassCalculator(a))
    
    elif cmd == "compoundmolecalc":
        a = input("Compound: ")
        b = float(input("Mass: "))
        print(main.CompoundMoleCalculator(a, b))

    elif cmd == "fractioncalc":
        a = float(input("A numerator: "))
        b = float(input("A denominator: "))
        c = float(input("B numerator: "))
        d = float(input("B denominator: "))
        e = int(input("Action: "))
        print(main.FractionCalculator(a, b, c, d, e))

    elif cmd == "fractionsimp":
        a = float(input("Numerator: "))
        b = float(input("Denominator: "))
        print(main.FractionsSimplifier(a, b))

    elif cmd == "decfraction":
        a = float(input("Decimal: "))
        print(main.DecimaltoFraction(a))

    elif cmd == "fractiondec":
        a = float(input("Numerator: "))
        b = float(input("Denominator: "))
        print(main.FractiontoDecimal(a, b))

    elif cmd == "funcangle":
        a = input("Function(sin, cos, or tg): ")
        b = float(input("Value: "))
        print(main.FunctoAngle(a, b))

    elif cmd == "sidecalc":
        a = input("Angle(a or b): ")
        b = float(input("Angle Value: "))
        c = input("Side(a, b, c): ")
        d = float(input("Side Value: "))
        e = input("Side you want to find: ")
        print(main.SideCalculator(a, b, c, d, e))

    elif cmd == "trianglearea":
        a = float(input("Base: "))
        b = float(input("Height: "))
        print(main.TriangleAreaCalc(a, b))

    elif cmd == "rectarea":
        a = float(input("Base: "))
        b = float(input("Width/Height: "))
        print(main.RectAreaCalc(a, b))

    elif cmd == "trapezoidarea":
        a = float(input("Base1: "))
        b = float(input("Base2: "))
        c = float(input("Height: "))
        print(main.TrapezoidAreaCalc(a, b, c))

    elif cmd == "ellipsearea":
        a = float(input("a: "))
        b = float(input("b: "))
        print(main.EllipseAreaCalc(a, b))

    elif cmd == "circlearea":
        a = float(input("Radius: "))
        print(main.CircleAreaCalc(a))
    
    elif cmd == "exit":
        sys.exit()

    else:
        print("Unknown command, " + '"' + cmd + '"' + ". Type help for a list of commands.")