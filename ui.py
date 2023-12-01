import main
import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("MathCalc")
        #setting window size
        width=779
        height=584
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Quadratics Button
        Button_Quadratics=tk.Button(root)
        Button_Quadratics["bg"] = "#e9e9ed"
        Button_Quadratics["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        Button_Quadratics["font"] = ft
        Button_Quadratics["fg"] = "#000000"
        Button_Quadratics["justify"] = "center"
        Button_Quadratics["text"] = "Quadratics"
        Button_Quadratics.place(x=10,y=10,width=98,height=46)
        Button_Quadratics["command"] = self.Button_Quadratics_command

        # Rational Nums Button
        Button_Rational=tk.Button(root)
        Button_Rational["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        Button_Rational["font"] = ft
        Button_Rational["fg"] = "#000000"
        Button_Rational["justify"] = "center"
        Button_Rational["text"] = "Rational Numbers"
        Button_Rational.place(x=230,y=10,width=97,height=46)
        Button_Rational["command"] = self.Button_Rational_command

        # Geometry Button
        Button_Geometry=tk.Button(root)
        Button_Geometry["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        Button_Geometry["font"] = ft
        Button_Geometry["fg"] = "#000000"
        Button_Geometry["justify"] = "center"
        Button_Geometry["text"] = "Geometry &\n Trigonometry"
        Button_Geometry.place(x=450,y=10,width=98,height=47)
        Button_Geometry["command"] = self.Button_Geometry_command

        # Area Button
        Button_Area=tk.Button(root)
        Button_Area["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        Button_Area["font"] = ft
        Button_Area["fg"] = "#000000"
        Button_Area["justify"] = "center"
        Button_Area["text"] = "Area Calculators"
        Button_Area.place(x=670,y=10,width=98,height=49)
        Button_Area["command"] = self.Button_Area_command

        # Quadratics Widgets #

        GLabel_783=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_783["font"] = ft
        GLabel_783["fg"] = "#333333"
        GLabel_783["justify"] = "center"
        GLabel_783["text"] = "Quadratic Info"
        GLabel_783.place(x=70,y=90,width=172,height=82)

        GLabel_872=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_872["font"] = ft
        GLabel_872["fg"] = "#333333"
        GLabel_872["justify"] = "center"
        GLabel_872["text"] = "Equation Factorer"
        GLabel_872.place(x=520,y=100,width=178,height=67)

        GLabel_984=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_984["font"] = ft
        GLabel_984["fg"] = "#333333"
        GLabel_984["justify"] = "center"
        GLabel_984["text"] = "A:"
        GLabel_984.place(x=530,y=160,width=30,height=30)

        GLabel_909=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_909["font"] = ft
        GLabel_909["fg"] = "#333333"
        GLabel_909["justify"] = "center"
        GLabel_909["text"] = "B:"
        GLabel_909.place(x=530,y=190,width=30,height=30)

        GLabel_557=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_557["font"] = ft
        GLabel_557["fg"] = "#333333"
        GLabel_557["justify"] = "center"
        GLabel_557["text"] = "C:"
        GLabel_557.place(x=530,y=220,width=30,height=30)

        GLabel_263=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_263["font"] = ft
        GLabel_263["fg"] = "#333333"
        GLabel_263["justify"] = "center"
        GLabel_263["text"] = "ax²+bx+c"
        GLabel_263.place(x=320,y=120,width=101,height=36)

        Button_EquationFactorer=tk.Button(root)
        Button_EquationFactorer["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        Button_EquationFactorer["font"] = ft
        Button_EquationFactorer["fg"] = "#000000"
        Button_EquationFactorer["justify"] = "center"
        Button_EquationFactorer["text"] = "GO"
        Button_EquationFactorer.place(x=690,y=190,width=67,height=30)
        Button_EquationFactorer["command"] = self.Button_EquationFactorer_command

        GListBox_953=tk.Listbox(root)
        GListBox_953["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_953["font"] = ft
        GListBox_953["fg"] = "#333333"
        GListBox_953["justify"] = "center"
        GListBox_953.place(x=570,y=160,width=80,height=25)

        GListBox_520=tk.Listbox(root)
        GListBox_520["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_520["font"] = ft
        GListBox_520["fg"] = "#333333"
        GListBox_520["justify"] = "center"
        GListBox_520.place(x=570,y=190,width=80,height=25)

        GListBox_939=tk.Listbox(root)
        GListBox_939["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_939["font"] = ft
        GListBox_939["fg"] = "#333333"
        GListBox_939["justify"] = "center"
        GListBox_939.place(x=570,y=220,width=80,height=25)

        GLabel_141=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_141["font"] = ft
        GLabel_141["fg"] = "#333333"
        GLabel_141["justify"] = "center"
        GLabel_141["text"] = "A:"
        GLabel_141.place(x=60,y=160,width=70,height=25)

        GLabel_993=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_993["font"] = ft
        GLabel_993["fg"] = "#333333"
        GLabel_993["justify"] = "center"
        GLabel_993["text"] = "B:"
        GLabel_993.place(x=60,y=190,width=70,height=25)

        GLabel_42=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_42["font"] = ft
        GLabel_42["fg"] = "#333333"
        GLabel_42["justify"] = "center"
        GLabel_42["text"] = "C:"
        GLabel_42.place(x=60,y=220,width=70,height=25)

        GListBox_55=tk.Listbox(root)
        GListBox_55["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_55["font"] = ft
        GListBox_55["fg"] = "#333333"
        GListBox_55["justify"] = "center"
        GListBox_55.place(x=110,y=160,width=80,height=25)

        GListBox_792=tk.Listbox(root)
        GListBox_792["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_792["font"] = ft
        GListBox_792["fg"] = "#333333"
        GListBox_792["justify"] = "center"
        GListBox_792.place(x=110,y=190,width=80,height=25)

        GListBox_220=tk.Listbox(root)
        GListBox_220["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_220["font"] = ft
        GListBox_220["fg"] = "#333333"
        GListBox_220["justify"] = "center"
        GListBox_220.place(x=110,y=220,width=80,height=25)

        Button_QuadraticInfo=tk.Button(root)
        Button_QuadraticInfo["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        Button_QuadraticInfo["font"] = ft
        Button_QuadraticInfo["fg"] = "#000000"
        Button_QuadraticInfo["justify"] = "center"
        Button_QuadraticInfo["text"] = "GO"
        Button_QuadraticInfo.place(x=230,y=190,width=67,height=30)
        Button_QuadraticInfo["command"] = self.Button_QuadraticInfo_command

        global quadratics_pressed
        global rational_pressed
        global geometry_pressed
        global  area_pressed

        # What gets executed when the respective button is clicked
        def quadratics_pressed():
            # Show
            GLabel_42.place(x=60,y=220,width=70,height=25)
            GListBox_55.place(x=110,y=160,width=80,height=25)
            GLabel_783.place(x=70,y=90,width=172,height=82)
            Button_QuadraticInfo.place(x=230,y=190,width=67,height=30)
            GLabel_872.place(x=520,y=100,width=178,height=67)
            GListBox_220.place(x=110,y=220,width=80,height=25)
            GListBox_792.place(x=110,y=190,width=80,height=25)
            GLabel_993.place(x=60,y=190,width=70,height=25)
            GLabel_141.place(x=60,y=160,width=70,height=25)
            GListBox_939.place(x=570,y=220,width=80,height=25)
            GLabel_984.place(x=530,y=160,width=30,height=30)
            GLabel_909.place(x=530,y=190,width=30,height=30)
            GLabel_557.place(x=530,y=220,width=30,height=30)
            GLabel_263.place(x=320,y=120,width=101,height=36)
            Button_EquationFactorer.place(x=690,y=190,width=67,height=30)
            GListBox_953.place(x=570,y=160,width=80,height=25)
            GListBox_520.place(x=570,y=190,width=80,height=25)

        def rational_pressed():
            # Show

            # Hide Quadratics
            GLabel_42.place_forget()
            GListBox_55.place_forget()
            GLabel_783.place_forget()
            Button_QuadraticInfo.place_forget()
            GLabel_872.place_forget()
            GListBox_220.place_forget()
            GListBox_792.place_forget()
            GLabel_993.place_forget()
            GLabel_141.place_forget()
            GListBox_939.place_forget()
            GLabel_984.place_forget()
            GLabel_909.place_forget()
            GLabel_557.place_forget()
            GLabel_263.place_forget()
            Button_EquationFactorer.place_forget()
            GListBox_953.place_forget()
            GListBox_520.place_forget()

        def geometry_pressed():
            # Show

            # Hide Quadratics
            GLabel_42.place_forget()
            GListBox_55.place_forget()
            GLabel_783.place_forget()
            Button_QuadraticInfo.place_forget()
            GLabel_872.place_forget()
            GListBox_220.place_forget()
            GListBox_792.place_forget()
            GLabel_993.place_forget()
            GLabel_141.place_forget()
            GListBox_939.place_forget()
            GLabel_984.place_forget()
            GLabel_909.place_forget()
            GLabel_557.place_forget()
            GLabel_263.place_forget()
            Button_EquationFactorer.place_forget()
            GListBox_953.place_forget()
            GListBox_520.place_forget()

        def area_pressed():
            # Show

            # Hide Quadratics
            GLabel_42.place_forget()
            GListBox_55.place_forget()
            GLabel_783.place_forget()
            Button_QuadraticInfo.place_forget()
            GLabel_872.place_forget()
            GListBox_220.place_forget()
            GListBox_792.place_forget()
            GLabel_993.place_forget()
            GLabel_141.place_forget()
            GListBox_939.place_forget()
            GLabel_984.place_forget()
            GLabel_909.place_forget()
            GLabel_557.place_forget()
            GLabel_263.place_forget()
            Button_EquationFactorer.place_forget()
            GListBox_953.place_forget()
            GListBox_520.place_forget()




    # Button Functions
    def Button_Quadratics_command(self):
        quadratics_pressed()

    def Button_Rational_command(self):
        rational_pressed()

    def Button_Geometry_command(self):
        geometry_pressed()

    def Button_Area_command(self):
        area_pressed()

    def Button_EquationFactorer_command(self):
        print("EqFactorer")


    def Button_QuadraticInfo_command(self):
        print("QuadInfo")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
