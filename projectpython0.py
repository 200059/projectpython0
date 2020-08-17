from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime


def main():
    root = Tk()
    app = salesLogin(root)


class salesLogin:
    def __init__(self, master):
        self.master = master
        self.master.title("Restaurant Billing Managment system")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="#C0C0C0")
        self.Frame = Frame(self.master, bg='#C0C0C0')
        self.Frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lbltitle = Label(self.Frame, text="  Resturant Billing Managment system   ", font=('arial', 60, 'bold'),
                              bg='#C0C0C0')
        self.lbltitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.F1 = LabelFrame(self.Frame, width=1350, height=400, font=('arial', 20, 'bold'), relief='ridge',
                             bg='#C0C0C0', bd=30)
        self.F1.grid(row=1, column=0)
        self.F2 = LabelFrame(self.Frame, width=1000, height=200, font=('arial', 20, 'bold'), relief='ridge',
                             bg='#C0C0C0', bd=30)
        self.F2.grid(row=2, column=0)

        self.lblUsername = Label(self.F1, text='Username', font=('arial', 30, 'bold'), bd=22, bg='#C0C0C0')
        self.lblUsername.grid(row=0, column=0)
        self.FramextUsername = Entry(self.F1, textvariable=self.Username, font=('arial', 30, 'bold'), bd=7, width=33)
        self.FramextUsername.grid(row=0, column=1, padx=88)

        self.lblPassword = Label(self.F1, text='Password', font=('arial', 30, 'bold'), bd=22, bg='#C0C0C0')
        self.lblPassword.grid(row=1, column=0)
        self.FramextPassword = Entry(self.F1, textvariable=self.Password, show="*", font=('arial', 30, 'bold'), bd=7,
                                     width=33)
        self.FramextPassword.grid(row=1, column=1, columnspan=2, pady=30)

        self.btnL = Button(self.F2, text="Login", width=15, command=self.Login_system, font=('arial', 30, 'bold'),
                           bg="#C0C0C0")
        self.btnL.grid(row=3, column=0, pady=20, padx=8)

        self.btnR = Button(self.F2, text="reset", command=self.iReset, width=15, font=('arial', 30, 'bold'),
                           bg="#C0C0C0")
        self.btnR.grid(row=3, column=1, pady=20, padx=8)

        self.btnE = Button(self.F2, text="Exit", command=self.iExit, width=15, font=('arial', 30, 'bold'), bg="#C0C0C0")
        self.btnE.grid(row=3, column=2, pady=20, padx=8)

    def Login_system(self):
        user = (self.Username.get())
        password = (self.Password.get())
        if (user == str("Sakriyajungthapa") and password == str(12345)):
            self.Login_window()
        else:
            tkinter.messagebox.askyesno("Restaurant Billing Managment system ", "Invalid Login details")
            self.Username.set("")
            self.Password.set("")

    def iReset(self):
        self.Username.set("")
        self.Password.set("")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Restaurant Billing Managment system", "Confirm if you want")
        if self.iExit > 0:
            self.master.destroy()
            return

    def Login_window(self):
        self.App1 = Toplevel(self.master)
        self.app = App1(self.App1)


class App1:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Billing Managment system")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="#C0C0C0")
        self.Frame = Frame(self.root, bg='#C0C0C0')
        self.Frame.pack()
        # ======================================================================================
        FF = Frame(self.Frame, bg="Black", bd=20, relief="raise")
        FF.grid()
        T1 = Frame(self.Frame, bd=20, width=1350, height=150, bg="#C0C0C0", relief="raise")
        T1.grid(row=1, column=0)
        self.A = Label(T1, text="      Restaurant Billing Managment system      ", bg="#C0C0C0", padx=10,
                       font=("arial", 50, "bold"), justify=CENTER).grid(row=0, column=0)
        localtime = time.asctime(time.localtime(time.time()))
        self.B = Label(T1, font=("arial", 30, "bold"), bg="#C0C0C0", text=localtime, anchor=W).grid(row=2, column=0)
        B = Frame(self.Frame, bd=10, width=1350, height=600, bg="#C0C0C0", relief="raise")
        B.grid(row=2, column=0)
        F1 = Frame(B, width=665, height=550, bd=10, bg="#C0C0C0", relief="raise")
        F1.grid(row=1, column=0)
        F2 = Frame(B, width=665, height=550, bd=10, bg="#C0C0C0", relief="raise")
        F2.grid(row=1, column=1)
        F3 = Frame(F2, width=660, height=315, bd=0, bg="#737CA1", relief="raise")
        F3.grid(row=4, column=0)
        # ================================================initialing variables==============================================================================================================

        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()
        var13 = IntVar()
        var14 = StringVar()

        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set("")

        varVchowmein = StringVar()
        varEchowmein = StringVar()
        varFry = StringVar()
        varCFry = StringVar()
        varEggFry = StringVar()
        varSamosa = StringVar()
        varPasta = StringVar()
        varOmlet = StringVar()
        varSalad = StringVar()
        varPizza = StringVar()
        varChange = StringVar()
        varServiceCharge = StringVar()
        varSubTotal = StringVar()
        varTotal = StringVar()
        varPayment = IntVar()

        varVchowmein.set('0')
        varEchowmein.set('0')
        varFry.set('0')
        varCFry.set('0')
        varEggFry.set('0')
        varSamosa.set('0')
        varPasta.set('0')
        varOmlet.set('0')
        varSalad.set('0')
        varPizza.set('0')
        varChange.set('0')
        varServiceCharge.set('0')
        varSubTotal.set('0')
        varTotal.set('0')
        varPayment.set('0')

        # ===========================================Reset Button============================================================================================================================
        def Reset():

            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set(0)
            var12.set(0)
            var13.set(0)

            varVchowmein.set('0')
            varEchowmein.set('0')
            varFry.set('0')
            varCFry.set('0')
            varEggFry.set('0')
            varSamosa.set('0')
            varPasta.set('0')
            varOmlet.set('0')
            varSalad.set('0')
            varPizza.set('0')
            varChange.set('0')
            varServiceCharge.set('0')
            varSubTotal.set('0')
            varTotal.set('0')
            varPayment.set('0')

            self.FramextVchowmein.configure(state=DISABLED)
            self.FramextEchowmein.configure(state=DISABLED)
            self.FramextFry.configure(state=DISABLED)
            self.FramextCFry.configure(state=DISABLED)
            self.FramextEggFry.configure(state=DISABLED)
            self.FramextSamosa.configure(state=DISABLED)
            self.FramextPasta.configure(state=DISABLED)
            self.FramextOmlet.configure(state=DISABLED)
            self.FramextSalad.configure(state=DISABLED)
            self.FramextPizza.configure(state=DISABLED)

        # ===========================================Checkbutton============================================================================================================================

        def chkVchowmein():
            if (var4.get() == 1):
                self.FramextVchowmein.configure(state=NORMAL)
                varVchowmein.set("")
            elif (var4.get() == 0):
                self.FramextVchowmein.configure(state=DISABLED)
                varVchowmein.set("0")

        def chkEchowmein():
            if (var5.get() == 1):
                self.FramextEchowmein.configure(state=NORMAL)
                varEchowmein.set("")
            elif (var5.get() == 0):
                self.FramextEchowmein.configure(state=DISABLED)
                varEchowmein.set("0")

        def chkFry():
            if (var6.get() == 1):
                self.FramextFry.configure(state=NORMAL)
                varFry.set("")
            elif (var6.get() == 0):
                self.FramextFry.configure(state=DISABLED)
                varFry.set("0")

        def chkCFry():
            if (var7.get() == 1):
                self.FramextCFry.configure(state=NORMAL)
                varCFry.set("")
            elif (var7.get() == 0):
                self.FramextCFry.configure(state=DISABLED)
                varCFry.set("0")

        def chkEggFry():
            if (var8.get() == 1):
                self.FramextEggFry.configure(state=NORMAL)
                varEggFry.set("")
            elif (var8.get() == 0):
                self.FramextEggFry.configure(state=DISABLED)
                varEggFry.set("0")

        def chkSamosa():
            if (var9.get() == 1):
                self.FramextSamosa.configure(state=NORMAL)
                varSamosa.set("")
            elif (var9.get() == 0):
                self.FramextSamosa.configure(state=DISABLED)
                varSamosa.set("0")

        def chkPasta():
            if (var10.get() == 1):
                self.FramextPasta.configure(state=NORMAL)
                varPasta.set("")
            elif (var10.get() == 0):
                self.FramextPasta.configure(state=DISABLED)
                varPasta.set("0")

        def chkOmlet():
            if (var11.get() == 1):
                self.FramextOmlet.configure(state=NORMAL)
                varOmlet.set("")
            elif (var11.get() == 0):
                self.FramextOmlet.configure(state=DISABLED)
                varOmlet.set("0")

        def chkSalad():
            if (var12.get() == 1):
                self.FramextSalad.configure(state=NORMAL)
                varSalad.set("")
            elif (var12.get() == 0):
                self.FramextSalad.configure(state=DISABLED)
                varSalad.set("0")

        def chkPizza():
            if (var13.get() == 1):
                self.FramextPizza.configure(state=NORMAL)
                varPizza.set("")
            elif (var13.get() == 0):
                self.FramextPizza.configure(state=DISABLED)
                varPizza.set("0")

        # =================================================Cost of items and total=========================================================================================
        def money():

            meal4 = float(varVchowmein.get())
            meal5 = float(varEchowmein.get())
            meal6 = float(varFry.get())
            meal7 = float(varCFry.get())
            meal8 = float(varEggFry.get())
            meal9 = float(varSamosa.get())
            meal10 = float(varPasta.get())
            meal11 = float(varOmlet.get())
            meal12 = float(varSalad.get())
            meal13 = float(varPizza.get())
            iTotal = ((meal4 * 70) + (meal5 * 80) + (meal6 * 75) + (meal7 * 100) + (meal8 * 90) + (meal9 * 60) + (
                        meal10 * 75) + (meal11 * 50) + (meal12 * 50) + (meal13 * 100))
            if (var14.get() == "Cash"):
                iChange = int(varPayment.get())
                iCost = iTotal
                iServiceCharge = 10
                iServiceChargeq = str('%.2f' % (iServiceCharge))
                varServiceCharge.set(iServiceChargeq)
                iCostq = str('%.2f' % (iCost))
                varSubTotal.set(iCostq)
                iTotalq = str('%.2f' % (iCost + iServiceCharge))
                varTotal.set(iTotalq)
                cChange = (iChange - (iCost + iServiceCharge))
                cChangeq = str('%.2f' % (cChange))
                varChange.set(cChangeq)
            elif (var14.get() == 'Master Card' or 'Visa Card' or 'Debit Card'):
                varPayment.set("")
                iCost = iTotal
                iServiceCharge = 10
                iServiceChargeq = str('%.2f' % (iServiceCharge))
                varServiceCharge.set(iServiceChargeq)
                iCostq = str('%.2f' % (iCost))
                varSubTotal.set(iCostq)
                iTotalq = str('%.2f' % (iCost + iServiceCharge))
                varTotal.set(iTotalq)
                varChange.set("0")

        # ==================================================Exit Button===================================================================

        def eExit():
            eExit = tkinter.messagebox.askyesno("Restaurant Billing Managment system", "Do you want to quit?")
            if eExit > 0:
                root.destroy()
                return

        # ==================================================Labeling Frame(F1)================================================================================================

        self.Vchowmein = Checkbutton(F1, text="Veg.chowmein\tRs.70", command=chkVchowmein, font=("arial", 25, "bold"),
                                     bg="#C0C0C0", variable=var4, onvalue=1, offvalue=0).grid(row=1, column=0, sticky=W)
        self.FramextVchowmein = Entry(F1, font=("arial", 18, "bold"), textvariable=varVchowmein, width=6,
                                      justify="right", state=DISABLED)
        self.FramextVchowmein.grid(row=1, column=1)
        self.Echowmein = Checkbutton(F1, text="Egg chowmein\tRs.80", command=chkEchowmein, font=("arial", 25, "bold"),
                                     variable=var5, onvalue=1, offvalue=0, bg="#C0C0C0").grid(row=2, column=0, sticky=W)
        self.FramextEchowmein = Entry(F1, font=("arial", 18, "bold"), textvariable=varEchowmein, width=6,
                                      justify="right", state=DISABLED)
        self.FramextEchowmein.grid(row=2, column=1)
        self.Fry = Checkbutton(F1, text="Fry rice\t\tRs.75", command=chkFry, font=("arial", 25, "bold"), variable=var6,
                               onvalue=1, offvalue=0, bg="#C0C0C0").grid(row=3, column=0, sticky=W)
        self.FramextFry = Entry(F1, font=("arial", 18, "bold"), textvariable=varFry, width=6, justify="right",
                                state=DISABLED)
        self.FramextFry.grid(row=3, column=1)
        self.CFry = Checkbutton(F1, text="Chicken Fry rice\tRs.100", command=chkCFry, font=("arial", 25, "bold"),
                                variable=var7, onvalue=1, offvalue=0, bg="#C0C0C0").grid(row=4, column=0, sticky=W)
        self.FramextCFry = Entry(F1, font=("arial", 18, "bold"), textvariable=varCFry, width=6, justify="right",
                                 state=DISABLED)
        self.FramextCFry.grid(row=4, column=1)
        self.EggFry = Checkbutton(F1, text="Egg Fry rice\tRs.90", command=chkEggFry, font=("arial", 25, "bold"),
                                  variable=var8, onvalue=1, offvalue=0, bg="#C0C0C0").grid(row=5, column=0, sticky=W)
        self.FramextEggFry = Entry(F1, font=("arial", 18, "bold"), textvariable=varEggFry, width=6, justify="right",
                                   state=DISABLED)
        self.FramextEggFry.grid(row=5, column=1)
        self.Samosa = Checkbutton(F1, text="Samosa\t\tRs.60", command=chkSamosa, font=("arial", 25, "bold"),
                                  variable=var9, onvalue=1, offvalue=0, bg="#C0C0C0").grid(row=6, column=0, sticky=W)
        self.FramextSamosa = Entry(F1, font=("arial", 18, "bold"), textvariable=varSamosa, width=6, justify="right",
                                   state=DISABLED)
        self.FramextSamosa.grid(row=6, column=1)
        # ====================================================Labeling Frame(F3)================================================================================================

        self.Pasta = Checkbutton(F1, text="Pasta\t\tRs.75", command=chkPasta, font=("arial", 25, "bold"),
                                 variable=var10, onvalue=1, offvalue=0, bg="#C0C0C0").grid(row=7, column=0, sticky=W)
        self.FramextPasta = Entry(F1, font=("arial", 18, "bold"), textvariable=varPasta, width=6, justify="right",
                                  state=DISABLED)
        self.FramextPasta.grid(row=7, column=1)
        self.Omlet = Checkbutton(F1, text="Omlet\t\tRs.50", command=chkOmlet, font=("arial", 25, "bold"),
                                 variable=var11, onvalue=1, offvalue=0, bg="#C0C0C0").grid(row=8, column=0, sticky=W)
        self.FramextOmlet = Entry(F1, font=("arial", 18, "bold"), textvariable=varOmlet, width=6, justify="right",
                                  state=DISABLED)
        self.FramextOmlet.grid(row=8, column=1)
        self.Salad = Checkbutton(F1, text="Salad\t\tRs.50", command=chkSalad, font=("arial", 25, "bold"),
                                 variable=var12, onvalue=1, offvalue=0, bg="#C0C0C0").grid(row=9, column=0, sticky=W)
        self.FramextSalad = Entry(F1, font=("arial", 18, "bold"), textvariable=varSalad, width=6, justify="right",
                                  state=DISABLED)
        self.FramextSalad.grid(row=9, column=1)
        self.Pizza = Checkbutton(F1, text="Pizza\t\tRs.100", command=chkPizza, font=("arial", 25, "bold"),
                                 variable=var13, onvalue=1, offvalue=0, bg="#C0C0C0").grid(row=10, column=0, sticky=W)
        self.FramextPizza = Entry(F1, font=("arial", 18, "bold"), textvariable=varPizza, width=6, justify="right",
                                  state=DISABLED)
        self.FramextPizza.grid(row=10, column=1)
        # =========================================================Labeling Frame(F4)================================================================================================
        self.lblPaymentMethod = Label(F3, font=('arial', 20, 'bold'), text="Payment Method", bg="#737CA1", bd=10,
                                      width=20, anchor='w').grid(row=0, column=0)
        self.cmbPaymentMethod = ttk.Combobox(F3, textvariable=var14, state='readonly', font=('arial', 15, 'bold'),
                                             width=15)
        self.cmbPaymentMethod['value'] = ('Cash', 'Master Card', 'Visa Card', 'Debit Card')
        self.cmbPaymentMethod.current(0)
        self.cmbPaymentMethod.grid(row=1, column=0)
        self.FramextPayment = Entry(F3, font=('arial', 20, 'bold'), textvariable=varPayment, width=6,
                                    justify='right').grid(row=2, column=0)
        self.lblChange = Label(F3, font=('arial', 20, 'bold'), text="Change", bg="#737CA1", anchor="w").grid(row=0,
                                                                                                             column=1)
        self.FramextChange = Entry(F3, font=('arial', 20, 'bold'), textvariable=varChange, justify='right', width=6,
                                   state=DISABLED).grid(row=0, column=2)
        self.lblServiceCharge = Label(F3, font=('arial', 20, 'bold'), text="service charge", bg="#737CA1",
                                      anchor="w").grid(row=1, column=1)
        self.FramextServiceCharge = Entry(F3, font=('arial', 20, 'bold'), textvariable=varServiceCharge, width=6,
                                          justify='right', state=DISABLED).grid(row=1, column=2)
        self.lblSubTotal = Label(F3, font=('arial', 20, 'bold'), bg="#737CA1", text="Sub Total", anchor="w").grid(row=2,
                                                                                                                  column=1)
        self.FramextSubTotal = Entry(F3, font=('arial', 20, 'bold'), textvariable=varSubTotal, width=6, justify='right',
                                     state=DISABLED).grid(row=2, column=2)
        self.lblTotal = Label(F3, font=('arial', 20, 'bold'), bg="#737CA1", text="Total", anchor="w").grid(row=3,
                                                                                                           column=1)
        self.FramextTotal = Entry(F3, font=('arial', 20, 'bold'), textvariable=varTotal, width=6, justify='right',
                                  state=DISABLED).grid(row=3, column=2)
        # ===========================================================Button========================================================================================================
        self.btnTotal = Button(F3, text="Total", width=4, command=money, bg="#737CA1", padx=14, pady=1,
                               font=("arial", 20, "bold")).grid(row=5, column=0)
        self.btnReset = Button(F3, text="Reset", width=4, padx=14, pady=1, bg="#737CA1", font=("arial", 20, "bold"),
                               command=Reset).grid(row=5, column=1)
        self.btnExit = Button(F3, text="Exit", font=("arial", 20, "bold"), width=4, padx=14, pady=1, bg="#737CA1",
                              command=eExit).grid(row=5, column=2)
        self.space = Label(F3, text="\n", bg="#737CA1").grid(row=4, column=0)


if __name__ == "__main__":
    main()
