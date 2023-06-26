#Tk class is used to create a root window
root.configure(background='ivory')
root.title('Disease Prediction System')
#root.resizable(0,0)

#taking first input as symptom
Symptom1 = StringVar()
Symptom1.set("Select Here")

#taking second input as symptom
Symptom2 = StringVar()
Symptom2.set("Select Here")

#taking third input as symptom
Symptom3 = StringVar()
Symptom3.set("Select Here")

#taking fourth input as symptom
Symptom4 = StringVar()
Symptom4.set("Select Here")

#taking fifth input as symptom
Symptom5 = StringVar()
Symptom5.set("Select Here")
Name = StringVar()

Address = StringVar()

Email = StringVar()

Mobile = StringVar()

# function to Reset the given inputs to initial position
prev_win = None


def Reset():
    global prev_win

    Symptom1.set("Select Here")
    Symptom2.set("Select Here")
    Symptom3.set("Select Here")
    Symptom4.set("Select Here")
    Symptom5.set("Select Here")

    NameEn.delete(first=0, last=100)

    AddressEn.delete(first=0, last=100)

    EmailEn.delete(first=0, last=100)

    MobileEn.delete(first=0, last=100)

    pred1.set(" ")
    pred2.set(" ")
    pred3.set(" ")
    pred4.set(" ")
    try:
        prev_win.destroy()
        prev_win = None
    except AttributeError:
        pass

#Exit button to come out of system
from tkinter import messagebox
def Exit():
    qExit=messagebox.askyesno("System","Do you want to exit the system")
    if qExit:
        root.destroy()
        exit()

#Headings for the GUI written at the top of GUI
w2 = Label(root, justify=LEFT, text="Disease Prediction using Machine Learning", fg="Red", bg="ivory")
w2.config(font=("Times New Roman",18,"bold"))
w2.grid(row=1, column=0, columnspan=2, padx=60)
w2 = Label(root, justify=LEFT, text="A Project by Nadeem Akhtar", fg="Dark blue", bg="Ivory")
w2.config(font=("Times New Roman",18,"bold"))
w2.grid(row=2, column=0, columnspan=2, padx=60)

# labels for the name

NameLb = Label(root, text="Name of the Patient", fg="dark blue", bg="ivory")
NameLb.config(font=("Times New Roman",11,"bold"))
NameLb.grid(row=6, column=0, pady=8, sticky=W)

AddressLb = Label(root, text="Address of the Patient", fg="dark blue", bg="ivory")
AddressLb.config(font=("Times New Roman",11,"bold"))
AddressLb.grid(row=7, column=0, pady=8, sticky=W)

EmailLb = Label(root, text="Email of the Patient", fg="dark blue", bg="ivory")
EmailLb.config(font=("Times New Roman",11,"bold"))
EmailLb.grid(row=8, column=0, pady=8, sticky=W)

MobileLb = Label(root, text="Contact No. of the Patient", fg="dark blue", bg="ivory")
MobileLb.config(font=("Times New Roman",11,"bold"))
MobileLb.grid(row=9, column=0, pady=8, sticky=W)

# Creating Labels for the symptoms

S1Lb = Label(root, text="Symptom 1", fg="Black", bg="Ivory")
S1Lb.config(font=("Times",11,"bold"))
S1Lb.grid(row=10, column=0, pady=8, sticky=W)

S2Lb = Label(root, text="Symptom 2", fg="Black", bg="Ivory")
S2Lb.config(font=("Times New Roman",11,"bold"))
S2Lb.grid(row=11, column=0, pady=8, sticky=W)

S3Lb = Label(root, text="Symptom 3", fg="Black",bg="Ivory")
S3Lb.config(font=("Times New Roman",11,"bold"))
S3Lb.grid(row=12, column=0, pady=8, sticky=W)

S4Lb = Label(root, text="Symptom 4", fg="Black", bg="Ivory")
S4Lb.config(font=("Times New Roman",11,"bold"))
S4Lb.grid(row=13, column=0, pady=8, sticky=W)

S5Lb = Label(root, text="Symptom 5", fg="Black", bg="Ivory")
S5Lb.config(font=("Times New Roman",11,"bold"))
S5Lb.grid(row=14, column=0, pady=8, sticky=W)


# Creating Labels for the ML Algorithms

lrLb = Label(root, text="DecisionTree", fg="white", bg="red", width = 20)
lrLb.config(font=("Times New Roman",12,"bold"))
lrLb.grid(row=17, column=0, pady=9,sticky=W)

destreeLb = Label(root, text="RandomForest", fg="WHITE", bg="DARK BLUE", width = 20)
destreeLb.config(font=("Times New Roman",12,"bold"))
destreeLb.grid(row=19, column=0, pady=9, sticky=W)

ranfLb = Label(root, text="NaiveBayes", fg="White", bg="dark green", width = 20)
ranfLb.config(font=("Times New Roman",12,"bold"))
ranfLb.grid(row=21, column=0, pady=9, sticky=W)

knnLb = Label(root, text="kNearestNeighbour", fg="WHITE", bg="olive", width = 20)
knnLb.config(font=("Times New Roman",12,"bold"))
knnLb.grid(row=23, column=0, pady=9, sticky=W)
OPTIONS = sorted(l1)

# Taking name as input from user
NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1)

AddressEn = Entry(root, textvariable=Address)
AddressEn.grid(row=7, column=1)

EmailEn = Entry(root, textvariable=Email)
EmailEn.grid(row=8, column=1)

MobileEn = Entry(root, textvariable=Mobile)
MobileEn.grid(row=9, column=1)


#Taking Symptoms as input from the dropdown from the user
S1 = OptionMenu(root, Symptom1,*OPTIONS)
S1.grid(row=10, column=1)

S2 = OptionMenu(root, Symptom2,*OPTIONS)
S2.grid(row=11, column=1)

S3 = OptionMenu(root, Symptom3,*OPTIONS)
S3.grid(row=12, column=1)

S4 = OptionMenu(root, Symptom4,*OPTIONS)
S4.grid(row=13, column=1)

S5 = OptionMenu(root, Symptom5,*OPTIONS)
S5.grid(row=14, column=1)

# Buttons for predicting the disease using different Algorithms

dst = Button(root, text="Decision Tree", command=DecisionTree,bg="Red",fg="yellow")
dst.config(font=("Times New Roman",12,"bold"))
dst.grid(row=9, column=3,padx=8)

rnf = Button(root, text="Random Forest", command=randomforest,bg="dark blue",fg="light cyan")
rnf.config(font=("Times New Roman",12,"bold"))
rnf.grid(row=10, column=3,padx=8)

lr = Button(root, text="Naive Bayes", command=NaiveBayes,bg="dark green",fg="white")
lr.config(font=("Times New Roman",12,"bold"))
lr.grid(row=11, column=3,padx=8)

kn = Button(root, text="KNN", command=KNN,bg="olive",fg="silver")
kn.config(font=("Times New Roman",12,"bold"))
kn.grid(row=12, column=3,padx=8)

rs = Button(root,text="Reset Inputs", command=Reset,bg="chocolate",fg="ivory",width=15)
rs.config(font=("Times New Roman",12,"bold"))
rs.grid(row=13,column=3,padx=8)

ex = Button(root,text="Exit System", command=Exit,bg="dark red",fg="wheat",width=15)
ex.config(font=("Times New Roman",12,"bold"))
ex.grid(row=14,column=3,padx=8)

# showing the output of different Algorithms

t1=Label(root,font=("Times New Roman",10,"bold"),text="Decision Tree",height=1,bg="red"
         ,width=30,fg="white",textvariable=pred1,relief="sunken").grid(row=17, column=1, padx=8)

t2=Label(root,font=("Times New Roman",10,"bold"),text="Random Forest",height=1,bg="dark blue"
         ,width=30,fg="white",textvariable=pred2,relief="sunken").grid(row=19, column=1, padx=8)

t3=Label(root,font=("Times New Roman",10,"bold"),text="Naive Bayes",height=1,bg="dark green"
         ,width=30,fg="white",textvariable=pred3,relief="sunken").grid(row=21, column=1, padx=8)

t4=Label(root,font=("Times New Roman",10,"bold"),text="KNN",height=1,bg="olive"
         ,width=30,fg="white",textvariable=pred4,relief="sunken").grid(row=23, column=1, padx=8)


# CALLING the below function
root.mainloop()
