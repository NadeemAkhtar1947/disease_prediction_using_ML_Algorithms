pred1 = StringVar()
def DecisionTree():
    if len(NameEn.get()) == 0:
        pred1.set(" ")
        comp = messagebox.askokcancel("System", "Kindly Fill the Name")
        if comp:
            root.mainloop()
    elif len(AddressEn.get()) == 0:
        pred1.set(" ")
        comp = messagebox.askokcancel("System", "Kindly Fill the Address")
        if comp:
            root.mainloop()
    elif len(MobileEn.get()) == 0:
        pred1.set(" ")
        comp = messagebox.askokcancel("System", "Kindly Fill the Contact details")
        if comp:
            root.mainloop()
    elif ((Symptom1.get() == "Select Here") or (Symptom2.get() == "Select Here") or (Symptom3.get() == "Select Here")):
        pred1.set(" ")
        sym = messagebox.askokcancel("System", "Kindly Fill atleast first three Symptoms")
        if sym:
            root.mainloop()
    else:
        print(NameEn.get())
        from sklearn import tree

        clf3 = tree.DecisionTreeClassifier()
        clf3 = clf3.fit(X, y)

        from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
        y_pred = clf3.predict(X_test)
        print("Decision Tree")
        print("Accuracy")
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred, normalize=False))
        print("Confusion matrix")
        conf_matrix = confusion_matrix(y_test, y_pred)
        print(conf_matrix)

        psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

        for k in range(0, len(l1)):
            for z in psymptoms:
                if (z == l1[k]):
                    l2[k] = 1

        inputtest = [l2]
        predict = clf3.predict(inputtest)
        predicted = predict[0]

        h = 'no'
        for a in range(0, len(disease)):
            if (predicted == a):
                h = 'yes'
                break

        if (h == 'yes'):
            pred1.set(" ")
            pred1.set(disease[a])
        else:
            pred1.set(" ")
            pred1.set("Not Found")


pred2 = StringVar()
def randomforest():
    if len(NameEn.get()) == 0:
        pred1.set(" ")
        comp = messagebox.askokcancel("System", "Kindly Fill the Name")
        if comp:
            root.mainloop()
    elif len(AddressEn.get()) == 0:
        pred1.set(" ")
        comp = messagebox.askokcancel("System", "Kindly Fill the Address")
        if comp:
            root.mainloop()
    elif len(MobileEn.get()) == 0:
        pred1.set(" ")
        comp = messagebox.askokcancel("System", "Kindly Fill the Contact details")
        if comp:
            root.mainloop()
    elif ((Symptom1.get() == "Select Here") or (Symptom2.get() == "Select Here") or (Symptom3.get() == "Select Here")):
        pred1.set(" ")
        sym = messagebox.askokcancel("System", "Kindly Fill atleast first three Symptoms")
        if sym:
            root.mainloop()
    else:
        from sklearn.ensemble import RandomForestClassifier
        clf4 = RandomForestClassifier(n_estimators=100)
        clf4 = clf4.fit(X, np.ravel(y))

        # calculating accuracy
        from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
        y_pred = clf4.predict(X_test)
        print("Random Forest")
        print("Accuracy")
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred, normalize=False))
        print("Confusion matrix")
        conf_matrix = confusion_matrix(y_test, y_pred)
        print(conf_matrix)

        psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

        for k in range(0, len(l1)):
            for z in psymptoms:
                if (z == l1[k]):
                    l2[k] = 1

        inputtest = [l2]
        predict = clf4.predict(inputtest)
        predicted = predict[0]

        h = 'no'
        for a in range(0, len(disease)):
            if (predicted == a):
                h = 'yes'
                break
        if (h == 'yes'):
            pred2.set(" ")
            pred2.set(disease[a])
        else:
            pred2.set(" ")
            pred2.set("Not Found")


pred4 = StringVar()
def KNN():
    if len(NameEn.get()) == 0:
        pred1.set(" ")
        comp = messagebox.askokcancel("System", "Kindly Fill the Name")
        if comp:
            root.mainloop()
    elif len(AddressEn.get()) == 0:
        pred1.set(" ")
        comp = messagebox.askokcancel("System", "Kindly Fill the Address")
        if comp:
            root.mainloop()
    elif len(MobileEn.get()) == 0:
        pred1.set(" ")
        comp = messagebox.askokcancel("System", "Kindly Fill the Contact details")
        if comp:
            root.mainloop()
    elif ((Symptom1.get() == "Select Here") or (Symptom2.get() == "Select Here") or (Symptom3.get() == "Select Here")):
        pred1.set(" ")
        sym = messagebox.askokcancel("System", "Kindly Fill atleast first three Symptoms")
        if sym:
            root.mainloop()
    else:
        from sklearn.neighbors import KNeighborsClassifier
        knn = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
        knn = knn.fit(X, np.ravel(y))

        from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
        y_pred = knn.predict(X_test)
        print("KNN")
        print("Accuracy")
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred, normalize=False))
        print("Confusion matrix")
        conf_matrix = confusion_matrix(y_test, y_pred)
        print(conf_matrix)

        psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

        for k in range(0, len(l1)):
            for z in psymptoms:
                if (z == l1[k]):
                    l2[k] = 1

        inputtest = [l2]
        predict = knn.predict(inputtest)
        predicted = predict[0]

        h = 'no'
        for a in range(0, len(disease)):
            if (predicted == a):
                h = 'yes'
                break

        if (h == 'yes'):
            pred4.set(" ")
            pred4.set(disease[a])
        else:
            pred4.set(" ")
            pred4.set("Not Found")


pred3 = StringVar()
def NaiveBayes():
    if len(NameEn.get()) == 0:
        pred1.set(" ")
        comp = messagebox.askokcancel("System", "Kindly Fill the Name")
        if comp:
            root.mainloop()
    elif len(AddressEn.get()) == 0:
        pred1.set(" ")
        comp = messagebox.askokcancel("System", "Kindly Fill the Address")
        if comp:
            root.mainloop()
    elif len(MobileEn.get()) == 0:
        pred1.set(" ")
        comp = messagebox.askokcancel("System", "Kindly Fill the Contact details")
        if comp:
            root.mainloop()
    elif ((Symptom1.get() == "Select Here") or (Symptom2.get() == "Select Here") or (Symptom3.get() == "Select Here")):
        pred1.set(" ")
        sym = messagebox.askokcancel("System", "Kindly Fill atleast first three Symptoms")
        if sym:
            root.mainloop()
    else:
        from sklearn.naive_bayes import GaussianNB
        gnb = GaussianNB()
        gnb = gnb.fit(X, np.ravel(y))

        from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
        y_pred = gnb.predict(X_test)
        print("Naive Bayes")
        print("Accuracy")
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred, normalize=False))
        print("Confusion matrix")
        conf_matrix = confusion_matrix(y_test, y_pred)
        print(conf_matrix)

        psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]
        for k in range(0, len(l1)):
            for z in psymptoms:
                if (z == l1[k]):
                    l2[k] = 1

        inputtest = [l2]
        predict = gnb.predict(inputtest)
        predicted = predict[0]

        h = 'no'
        for a in range(0, len(disease)):
            if (predicted == a):
                h = 'yes'
                break
        if (h == 'yes'):
            pred3.set(" ")
            pred3.set(disease[a])
        else:
            pred3.set(" ")
            pred3.set("Not Found")
