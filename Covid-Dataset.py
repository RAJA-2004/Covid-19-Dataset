import pandas as pd
import matplotlib.pyplot as plt               

print(" ")
print("       *****  WELCOME TO COVID-19 DATASET  *****       ")
print(" ")
print(" ")

def csv():
    print("---------------------------------")
    print("!  READ DATA IN DIFFERENT WAYS  !")
    print("---------------------------------")
    print("1. Read complete csv file")
    print("2. Reading file without index")
    print("-------------------")
    print("!  DATA ANALYSIS  !")
    print("-------------------")
    print("3. Sorting data as per your choice ")
    print("4. Read Top and Bottom Records as per your choice")
    print("5. Read file with specified columns")
    print("------------------------")
    print("!  DATA VISUALIZATION  !")
    print("------------------------")
    print("6. Line Chart")
    print("7. Bar Chart")
    print(" ")
    print("===================================================")
csv()

def read_csv():
    print("Reading Data From csv")
    print(" ")
    df = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv")
    print(df)

def no_index():
    print("Reading Data From csv file without index values")
    print(" ")
    df = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv", index_col=0)
    print(df)

def data_sorting():
    df = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv")
    print("     -------------------------------     ")
    print("     !  COVID-19 OVERALL ANALYSIS  !     ")
    print("     -------------------------------     ")
    print(" ")
    print(">> To display record in Descending Order")
    print(" ")
    print("Press 1 to arrange the record as per TOTAL CASES")
    print("Press 2 to arrange the record as per TOTAL DEATHS")
    print("Press 3 to arrange the record as per ACTIVE CASES")
    print("Press 4 to arrange the record as per TOTAL RECOVERED")
    print(" ")
    print("****************************************************")
    print(" ")
    print(">> To display record in Ascending Order")
    print(" ")
    print("Press 5 to arrange the record as per TOTAL CASES")
    print("Press 6 to arrange the record as per TOTAL DEATHS")
    print("Press 7 to arrange the record as per ACTIVE CASES")
    print("Press 8 to arrange the record as per TOTAL RECOVERED")

    print(" ")

    sr = int(input("Enter Your Choice : "))

    print(" ")
    if sr == 1:
        df1 = df.sort_values(by=["Total Cases"], ascending=[False])
        print(df1)
    elif sr == 2:
        df1 = df.sort_values(by=["Active Cases"], ascending=[False])
        print(df1)
    elif sr == 3:
        df1 = df.sort_values(by=["Total Deaths"], ascending=[False])
        print(df1)
    elif sr == 4:
        df1 = df.sort_values(by=["Total Recovered"], ascending=[False])
        print(df1)
    elif sr == 5:
        df1 = df.sort_values(by=["Total Cases"])
        print(df1)
    elif sr == 6:
        df1 = df.sort_values(by=["Active Cases"])
        print(df1)
    elif sr == 7:
        df1 = df.sort_values(by=["Total Deaths"])
        print(df1)
    elif sr == 8:
        df1 = df.sort_values(by=["Total Recovered"])
        print(df1)
    else:
        print("       ####### Enter a valid input #######       ")

print(" ")

def read_top_and_bottom():
    df = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv")
    print("Press 1 to extract records from top")
    print("Press 2 to extrcat records from bottom")

    print(" ")

    ch = int(input("Enter your choice : "))

    print(" ")

    if ch == 1:
        top = int(input("Enter How Many Records You want To Display From Top : "))
        df1 = df.head(top)
        print(df1)
    elif ch == 2:
        bottom = int(input("Enter How Many Records You want To Display From Bottom : "))
        df2 = df.tail(bottom)
        print(df2)
    else:
        print("       ####### Enter a valid input #######       ")

def read_specified_col():
    df = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv")
    print("Press 1 to print COUNTRIES & VACCINATION RATE")
    print("Press 2 to print COUNTRIES & DEATH RATE")
    print("Press 3 to print COUNTRIES & RECOVERY RATE")
    print("Press 4 to print INDIA's COVID ANALYSIS ")
    print("Press 5 to print COUNTRIES & ACTIVE CASES")
    print("Press 6 to print COUNTRIES & TOTAL DEATHS")
    print("Press 7 to print COUNTRIES & TOTAL TESTS")
    print("Press 8 to print COUNTRIES HAVING 60% & ABOVE RECOVERY RATE")

    print(" ")

    rs = int(input("Enter your choice : "))

    print(" ")

    if rs == 1:
        df1 = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv", usecols=["Country", "Vaccines Rate"])
        print(df1)
    elif rs == 2:
        df1 = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv", usecols=["Country", "Death Rate"])
        print(df1)
    elif rs == 3:
        df1 = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv", usecols=["Country", "Recovery Rate"])
        print(df1)
    elif rs == 4:
        df1 = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv")
        ind = df1.iloc[1]
        print(ind)
    elif rs == 5:
        df1 = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv", usecols=["Country", "Active Cases"])
        print(df1)
    elif rs == 6:
        df1 = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv", usecols=["Country", "Total Deaths"])
        print(df1)
    elif rs == 7:
        df1 = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv", usecols=["Country", "Total Tests"])
        print(df1)
    elif rs == 8:
        df1 = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv")
        mvp = df1[df1["Recovery Rate"] > 60]
        print(mvp)
    else:
        print("       ####### Enter a valid input #######       ")

def line_chart():
    lc = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv")
    ct = lc["Country"]
    tc = lc["Total Cases"]
    td = lc["Total Deaths"]
    tr = lc["Total Recovered"]
    ac = lc["Active Cases"]
    tt = lc["Total Tests"]
    vr = lc["Vaccines Rate"]
    dr = lc["Death Rate"]
    rr = lc["Recovery Rate"]
    plt.xlabel("COUNTRY")
    plt.xticks(rotation="vertical")

    print("Select Specific LINE CHART as given below :-")
    print(" ")
    print("Press 1 to print COUNTRY vs TOTAL CASES")
    print("Press 2 to print COUNTRY vs TOTAL RECOVERED")
    print("Press 3 to print COUNTRY vs ACTIVE CASES")
    print("Press 4 to print COUNTRY vs TOTAL TESTS")
    print("Press 5 to print COUNTRY vs VACCINE RATE")
    print("Press 6 to print COUNTRY vs DEATH RATE")
    print("Press 7 to print COUNTRY vs RECOVERY RATE")

    print(" ")

    ip = int(input("Enter your choice : "))
    if ip == 1:
        plt.ylabel("TOTAL CASES")
        plt.title("COUNTRY vs TOTAL CASES")
        plt.plot(ct.head(20), tc.head(20))
        plt.show()
    elif ip == 2:
        plt.ylabel("TOTAL RECOVERED")
        plt.title("COUNTRY vs TOTAL RECOVERED ")
        plt.plot(ct.tail(20), tr.tail(20))
        plt.show()
    elif ip == 3:
        plt.ylabel("TOTAL CASES")
        plt.title("COUNTRY vs ACTIVE CASES")
        plt.plot(ct.head(20), ac.head(20))
        plt.show()
    elif ip == 4:
        plt.ylabel("TOTAL CASES")
        plt.title("COUNTRY vs TOTAL TESTS")
        plt.plot(ct.tail(20), tt.tail(20))
        plt.show()
    elif ip == 5:
        plt.ylabel("VACCINE RATE")
        plt.title("COUNTRY vs VACCINE RATE")
        plt.plot(ct.head(20), vr.head(20))
        plt.show()
    elif ip == 6:
        plt.ylabel("DEATH RATE")
        plt.title("COUNTRY vs DEATH RATE")
        plt.plot(ct.tail(20), dr.tail(20))
        plt.show()
    elif ip == 7:
        plt.ylabel("RECOVERY RATE")
        plt.title("COUNTRY vs RECOVERY RATE")
        plt.plot(ct.head(20), rr.head(20))
        plt.show()
    else:
        print("       ####### Enter a valid input #######       ")

def bar_chart():
    br = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv")
    ct = br["Country"]
    tc = br["Total Cases"]
    td = br["Total Deaths"]
    tr = br["Total Recovered"]
    ac = br["Active Cases"]
    tt = br["Total Tests"]
    vr = br["Vaccines Rate"]
    dr = br["Death Rate"]
    rr = br["Recovery Rate"]
    plt.xticks(rotation="vertical")

    print("Select Specific BAR CHART as given below :-")
    print(" ")
    print("Press 1 to print COUNTRY vs TOTAL CASES")
    print("Press 2 to print COUNTRY vs TOTAL RECOVERED")
    print("Press 3 to print COUNTRY vs ACTIVE CASES")
    print("Press 4 to print RECOVERY RATE vs DEATH RATE")
    print("Press 5 to print COUNTRY vs VACCINE RATE")
    print("Press 6 to print COUNTRY vs DEATH RATE")
    print("Press 7 to print COUNTRY vs RECOVERY RATE")

    print(" ")

    ip = int(input("Enter your choice : "))
    if ip == 1:
        plt.xlabel("COUNTRY")
        plt.ylabel("TOTAL CASES")
        plt.title("COUNTRY vs TOTAL CASES")
        plt.bar(ct.head(10), tc.tail(10), color=["g", "gold"])
        plt.show()
    elif ip == 2:
        plt.xlabel("COUNTRY")
        plt.ylabel("TOTAL RECOVERED")
        plt.title("COUNTRY vs TOTAL RECOVERED ")
        plt.bar(ct.head(20), tr.head(20), color=["r", "gold"])
        plt.show()
    elif ip == 3:
        plt.xlabel("COUNTRY")
        plt.ylabel("TOTAL CASES")
        plt.title("COUNTRY vs ACTIVE CASES")
        plt.bar(ct.head(20), ac.head(20), color=["g", "r"])
        plt.show()
    elif ip == 4:
        plt.ylabel("DEATH RATE")
        plt.xlabel("RECOVERY RATE")
        plt.title("RECOVERY RATE vs DEATH RATE")
        plt.bar(rr.head(20), dr.head(20), color=["k", "gold"])
        plt.show()
    elif ip == 5:
        plt.xlabel("COUNTRY")
        plt.ylabel("VACCINE RATE")
        plt.title("COUNTRY vs VACCINE RATE")
        plt.bar(ct.head(20), vr.head(20), color=["orange", "k"])
        plt.show()
    elif ip == 6:
        plt.xlabel("COUNTRY")
        plt.ylabel("DEATH RATE")
        plt.title("COUNTRY vs DEATH RATE")
        plt.bar(ct.head(20), dr.head(20), color=["orange", "blue"])
        plt.show()
    elif ip == 7:
        plt.xlabel("COUNTRY")
        plt.ylabel("RECOVERY RATE")
        plt.title("COUNTRY vs RECOVERY RATE")
        plt.bar(ct.head(20), rr.head(20), color=["orange", "silver", "g"])
        plt.show()
    else:
        print("       ####### Enter a valid input #######       ")

op = int(input("Enter your choice : "))
print(" ")
if op == 1:
    read_csv()
elif op == 2:
    no_index()
elif op == 3:
    data_sorting()
elif op == 4:
    read_top_and_bottom()
elif op == 5:
    read_specified_col()
elif op == 6:
    line_chart()
elif op == 7:
    bar_chart()
else:
    print("       ####### Enter a valid input #######       ")

print("")
print("   ------------------------------------------   ")
print("   !   THANK-YOU FOR VISITING THE DATASET   !   ")
print("   ------------------------------------------   ")