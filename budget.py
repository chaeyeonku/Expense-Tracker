#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:03:24 2020

@author: student
"""

from pymongo import MongoClient
import pandas as pd
import tkinter as tk
from tkcalendar import DateEntry, Calendar
import datetime
#from datetime import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Retrieve documents from MongoDB database

cluster = MongoClient("mongodb+srv://admin:dsgs2020@cluster0.avwzd.mongodb.net/expense_analysis?retryWrites=true&w=majority")
db = cluster["expense_analysis"]
collection = db["expense"]
collection_fixed = db["fixed"]

exp_data = []
col_names = ['Date', 'Category', 'Amount']
col_names_fixed = ['Rent', 'Health Insurance', 'Mobile Fee']

results = collection.find()
new_id = collection.find().count()

for result in results:
    # print(result["Date"])
    values = [result["Date"], result["Category"], result["Amount"]]
    zipped = zip(col_names, values)
    a_row = dict(zipped)
    # print(a_row)
    exp_data.append(a_row)

exp_rec = pd.DataFrame(exp_data, columns=col_names)
print(exp_rec)


# Retrieve fixed expenses

result_f = collection_fixed.find({"_id": 0})
fixed_data = []

for result in result_f:
    values_fixed = [result["Rent"], result["HealthInsurance"], result["MobileFee"]]
    zipped_fixed = zip(col_names_fixed, values_fixed)
    row_fixed = dict(zipped_fixed)
    fixed_data.append(row_fixed)
    

fixed_exp = pd.DataFrame(fixed_data, columns=col_names_fixed)

fixed_total = fixed_exp.Rent[0] + fixed_exp['Health Insurance'][0] + fixed_exp['Mobile Fee'][0]



# Old csv file retrieval

# exp_rec = pd.read_csv('/Users/student/Desktop/CS-learning/Python/Python-Stats/expense.csv')
# print(exp_rec)

#exp_rec = exp_rec.drop(exp_rec[exp_rec.Category == "Rent"].index)
#exp_rec.to_csv('/Users/student/Desktop/CS-learning/Python/Python-Stats/expense.csv', index=False)

# ---- NEW INPUT TEMPLATE ---

#test = {'Date': ['2020-10-24'], 'Category': ['Grocery'], 'Amount': [49.14]}
#test_df = pd.DataFrame(test, columns=col_names)
#combined = test_df.append(exp_rec, ignore_index=True)
#print(combined.head())
#test_df.to_csv('/Users/student/Desktop/CS-learning/Python/Python-Stats/expense.csv', index=False)

# --- VARIABLES ----
#amount = 0
#subcategory = ''
dateChosen = datetime.date.today()
today = datetime.date.today()

HEIGHT = 650
WIDTH = 750

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#003399', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')



frame2 = tk.Frame(root, bg='#ebc6d9', bd=5)
frame2.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')

frame3 = tk.Frame(root, bg="#efc6d9", bd=5)
frame3.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')

# frame: current_statement
frame4 = tk.Frame(root, bg="#efc6d9", bd=5)
frame4.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')

# frame: previous_statement
frame5 = tk.Frame(root, bg="#efc6d9", bd=5)
frame5.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')

# frame: calendar
frame_cal = tk.Frame(root, bg="#efc6d9", bd=5)
frame_cal.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')

# frame: statistics
frame_stat = tk.Frame(root, bg="#efc6d9", bd=5)
frame_stat.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')

# frame: setting
frame_setting = tk.Frame(root, bg="#efc6d9", bd=5)
frame_setting.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')


#calendar = DateEntry(frame2)
calendar = Calendar(frame_cal, year=today.year, month=today.month, day=today.day)
calendar.place(relx=0.5, rely=0.3, relwidth=0.7, anchor='n')



def calPage():
    calendar.place(relx=0.5, rely=0.3, relwidth=0.7, anchor='n')
    frame_cal.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')
    frame_cal.tkraise()

def expPage():
    #-- Test: date chosen from calendar received properly --
    #input_date = calendar.get_date()
    #print(input_date)
    #datetimetgt = datetime.datetime.strptime(input_date, '%m/%d/%y')
    #dateChosen = datetimetgt.date()
    #print(dateChosen)
    var_amount.set("")
    
    frame2.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')
    #calendar.place(relx=0.2, rely=0.3, relwidth=0.3, anchor='n')
    frame2.tkraise()
    
def mainPage():
    frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')
    frame.tkraise()
    
def subcatPage():
    #print(amount)
    frame3.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')
    frame3.tkraise()
    
def quitApp():
    root.quit()

# Check if the input is a number
def check_exp_val():
    text_exception = tk.StringVar()
    entry_exception = tk.Entry(frame2, text=text_exception)
    entry_exception.place(relx=0.5, rely=0.7, relwidth=0.7, anchor='n')
    
    boolean = False
    try:
        exp_int = float(entry_amount.get())
        boolean = True
    except ValueError:
        text_exception.set("* WARNING: Please enter a number")
        
    if (boolean):
        subcatPage()
    
def subcatValue(val):
    global new_id
    global exp_rec
    
    input_date = calendar.get_date()
    print(input_date)
    datetimetgt = datetime.datetime.strptime(input_date, '%m/%d/%y')
    dateChosen = datetimetgt.date()
    
    subcategory = val
    print(subcategory)
    amount = float(entry_amount.get())
    print(amount)
    
    #store to to database
    new_post = {"_id": new_id, 'Date': str(dateChosen), 'Category': subcategory, 'Amount': amount}
    new_row = {'Date': [dateChosen], 'Category': [subcategory], 'Amount': [amount]}
    collection.insert_one(new_post)
    new_id +=1
    new_df = pd.DataFrame(new_row, columns=col_names)
    exp_rec = new_df.append(exp_rec, ignore_index=True)
    print(exp_rec)
    mainPage()
   
    
    # Old code: store to csv
    # combined.to_csv('/Users/student/Desktop/CS-learning/Python/Python-Stats/expense.csv', index=False)
    
    

def statsPage():
    frame_stat.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')
    frame_stat.tkraise()
    

def stat_basic_current():
    global exp_rec
    global fixed_exp
    global fixed_total
    
    #decide which month's statement to present
    
    month_chosen = today.month
    
        
    print(month_chosen)
    
    frame4.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')
    frame4.tkraise()
    
    # exp_rec = pd.read_csv('/Users/student/Desktop/CS-learning/Python/Python-Stats/expense.csv')
    
    start_date = datetime.datetime(today.year, month_chosen, 1)
    
    if (month_chosen != 12):
        next_month = month_chosen+1
        next_year = today.year
    else:
        next_month = 1
        next_year = today.year+1
        
    end_date = datetime.datetime(next_year, next_month, 1)
    # Expense filtered by month
    exp_filtered = exp_rec[ (exp_rec['Date'] >= start_date.strftime('%Y-%m-%d')) 
                           & (exp_rec['Date'] < end_date.strftime('%Y-%m-%d'))]
    
    
    # Expense grouped by Category
    exp_categorized = exp_filtered.groupby(by=['Category'])['Amount'].sum()
    
    fig_exp = plt.Figure(figsize=(6,5), dpi=100)
    
    # Pie chart
    ax2 = fig_exp.add_subplot(221)
    pie_exp = FigureCanvasTkAgg(fig_exp, frame4)
    pie_exp.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    exp_categorized.plot.pie(y='Amount', figsize=(6,6), ax=ax2)
    ax2.set_title('Exepnse by Category')
    
    
    # Create new column: day (in date) for bar graph
    exp_filtered['Day'] = exp_filtered.Date.apply(lambda x: x[8:])
    print(exp_filtered)
    
    
    # Expense grouped by Date
    exp_grouped = exp_filtered.groupby(by=['Day'])['Amount'].sum()
    
    # Bar graph
    ax1 = fig_exp.add_subplot(223)
    bar_exp = FigureCanvasTkAgg(fig_exp, frame4)
    bar_exp.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    exp_grouped.plot(kind='bar', x="Date", y="Amount", figsize=(5,4), ax=ax1)
    ax1.set_title('Monthly Expense Trend- Month: ' + str(month_chosen))
    
    # Retrieve fixed expense
    # fixed_exp = pd.read_csv('/Users/student/Desktop/CS-learning/Python/Python-Stats/fixed.csv')
    
    
    var_exp = exp_filtered['Amount'].sum()
    

    # Summary stats
    label_total = tk.Label(frame4, text="Total Amount: $ "
                           +str(round(fixed_total + var_exp ,2)))
    label_total.place(relx=0.8, rely=0.1, anchor='n')
    label_fixed = tk.Label(frame4, text="Fixed Expense: $ " + str(fixed_total))
    label_fixed.place(relx=0.8, rely=0.2, anchor='n')
    label_variable = tk.Label(frame4, text="Variable Expense: $ " + str(round(var_exp)))
    label_variable.place(relx=0.8, rely=0.3, anchor='n')
    
    btn_backtoprev_stat2 = tk.Button(frame4, text="BACK", highlightbackground='#b3e6ff', 
              highlightthickness=50, command=statsPage)
    btn_backtoprev_stat2.place(relx=0.1, rely=0, anchor='n', relwidth=0.1, relheight=0.05)

    btn_backToMain_stat2 = tk.Button(frame4, text="HOME", highlightbackground='#b3e6ff', 
              highlightthickness=50, command=mainPage)
    btn_backToMain_stat2.place(relx=0.9, rely=0, anchor='n', relwidth=0.1, relheight=0.05)


def stat_basic_prev():
    global exp_rec
    global fixed_rec
    global fixed_total
    
    month_chosen = today.month-1
    
    frame5.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')
    frame5.tkraise()
    # exp_rec_2 = pd.read_csv('/Users/student/Desktop/CS-learning/Python/Python-Stats/expense.csv')
    
    start_date = datetime.datetime(today.year, month_chosen, 1)
    
    if (month_chosen != 12):
        next_month = month_chosen+1
        next_year = today.year
    else:
        next_month = 1
        next_year = today.year+1
        
    end_date = datetime.datetime(next_year, next_month, 1)
    
    # Expense filtered by month
    exp_filtered_2 = exp_rec[ (exp_rec['Date'] >= start_date.strftime('%Y-%m-%d')) 
                           & (exp_rec['Date'] < end_date.strftime('%Y-%m-%d'))]
    
    
    # Expense grouped by Category
    exp_categorized_2 = exp_filtered_2.groupby(by=['Category'])['Amount'].sum()
    
    fig_exp_2 = plt.Figure(figsize=(6,5), dpi=100)
    
    # Pie chart
    ax4 = fig_exp_2.add_subplot(221)
    pie_exp_2 = FigureCanvasTkAgg(fig_exp_2, frame5)
    pie_exp_2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    exp_categorized_2.plot.pie(y='Amount', figsize=(6,6), ax=ax4)
    ax4.set_title('Exepnse by Category')
    
    
    # Create new column: day (in date) for bar graph
    exp_filtered_2['Day'] = exp_filtered_2.Date.apply(lambda x: x[8:])
    print(exp_filtered_2)
    
    
    # Expense grouped by Date
    exp_grouped_2 = exp_filtered_2.groupby(by=['Day'])['Amount'].sum()
    
    # Bar graph
    ax3 = fig_exp_2.add_subplot(223)
    bar_exp_2 = FigureCanvasTkAgg(fig_exp_2, frame5)
    bar_exp_2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    exp_grouped_2.plot(kind='bar', x="Date", y="Amount", figsize=(5,4), ax=ax3)
    ax3.set_title('Monthly Expense Trend- Month: ' + str(month_chosen))
    
    # Retrieve fixed expense
    # fixed_exp_2 = pd.read_csv('/Users/student/Desktop/CS-learning/Python/Python-Stats/fixed.csv')
    # fixed_total_2 = fixed_exp_2.Rent[0] + fixed_exp_2['Health Insurance'][0] 
    # + fixed_exp_2['Mobile Fee'][0]
     
    var_exp_2 = exp_filtered_2['Amount'].sum()
    
    # Summary stats
    label_total_2 = tk.Label(frame5, text="Total Amount: $ "
                           +str(round(fixed_total + var_exp_2 ,2)))
    label_total_2.place(relx=0.8, rely=0.1, anchor='n')
    label_fixed_2 = tk.Label(frame5, text="Fixed Expense: $ " + str(fixed_total))
    label_fixed_2.place(relx=0.8, rely=0.2, anchor='n')
    label_variable_2 = tk.Label(frame5, text="Variable Expense: $ " + str(round(var_exp_2)))
    label_variable_2.place(relx=0.8, rely=0.3, anchor='n')
    
    btn_backtoprev_stat2_2 = tk.Button(frame5, text="BACK", highlightbackground='#b3e6ff', 
              highlightthickness=50, command=statsPage)
    btn_backtoprev_stat2_2.place(relx=0.1, rely=0, anchor='n', relwidth=0.1, relheight=0.05)

    btn_backToMain_stat2_2 = tk.Button(frame5, text="HOME", highlightbackground='#b3e6ff', 
              highlightthickness=50, command=mainPage)
    btn_backToMain_stat2_2.place(relx=0.9, rely=0, anchor='n', relwidth=0.1, relheight=0.05)

    
    

def setting_page():
    frame_setting.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')
    frame_setting.tkraise()
    

def check_setting(rent, insurance, mobile):
    #Error message
    
    text_exception = tk.StringVar()
    entry_exception = tk.Entry(frame_setting, text=text_exception)
    entry_exception.place(relx=0.5, rely=0.9, relwidth=0.7, anchor='n')
    
    check_1 = False
    check_2 = False
    check_3 = False
    
    try:
        rent_int = int(rent)
        check_1 = True
    except ValueError:
        text_exception.set("* WARNING: Please type a number for the rent amount")
    
    try:
        insurance_int = int(insurance)
        check_2 = True
    except ValueError:
        text_exception.set("* WARNING: Please type a number for the insurance amount")
    
    try:
        mobile_int = int(mobile)
        check_3 = True
    except ValueError:
        text_exception.set("* WARNING: Please type a number for the mobile fee")
        
    if (check_1 & check_2 & check_3):
        save_setting(rent_int, insurance_int, mobile_int)
        
        
def save_setting(rent, insurance, mobile):
    global col_names_fixed
    global collection_fixed
    global fixed_total
    #print(rent)
    #print(insurance)
    #print(mobile)
    
    # Old csv file
    
    # fixed = {'Rent': [rent], 'Health Insurance': [insurance], 'Mobile Fee': [mobile]}
    # fixed_df = pd.DataFrame(fixed, columns=col_names_fixed)
    # fixed_df.to_csv('/Users/student/Desktop/CS-learning/Python/Python-Stats/fixed.csv', index=False)
    # print(fixed_df)
    # check = pd.read_csv('/Users/student/Desktop/CS-learning/Python/Python-Stats/fixed.csv')
    # print(check.head())
    
    collection_fixed.update_one({"_id": 0}, {"$set": {"Rent": rent, 
                                                      "HealthInsurance": insurance, 
                                                      "MobileFee": mobile}})
    fixed_total = rent + insurance + mobile
    mainPage()
            
        


btn_backToMain_exp1 = tk.Button(frame2, text="BACK", highlightbackground='#b3e6ff', 
              highlightthickness=50, command=mainPage)
btn_backToMain_exp1.place(relx=0.1, rely=0, anchor='n', relwidth=0.1, relheight=0.05)

btn_backToMain_exp2 = tk.Button(frame3, text="BACK", highlightbackground='#b3e6ff', 
              highlightthickness=50, command=expPage)
btn_backToMain_exp2.place(relx=0.1, rely=0, anchor='n', relwidth=0.1, relheight=0.05)


# Expense Value Page
var_amount = tk.StringVar()
label_amount = tk.Label(frame2, text=" $ ")
entry_amount = tk.Entry(frame2, textvariable=var_amount)
label_amount.place(relx=0.55, rely=0.3, anchor='n')
entry_amount.place(relx=0.8, rely=0.3, anchor='n')

btn_next = tk.Button(frame2, text='NEXT', highlightbackground='#b3e6ff', 
                  highlightthickness=50, command=check_exp_val)
btn_next.place(relx=0.9, rely=0, anchor='n', relwidth=0.1, relheight=0.05)


# Calendar Page
btn_cal_exp = tk.Button(frame_cal, text='NEXT', highlightbackground='#b3e6ff', 
                  highlightthickness=50, command=expPage)
btn_cal_exp.place(relx=0.9, rely=0, anchor='n', relwidth=0.1, relheight=0.05)
btn_backToMain_cal = tk.Button(frame_cal, text='BACK', highlightbackground='#b3e6ff', 
              highlightthickness=50, command=mainPage)
btn_backToMain_cal.place(relx=0.1, rely=0, anchor='n', relwidth=0.1, relheight=0.05)



#btn_quit = tk.Button(frame, text='QUIT', highlightbackground='#b366ff', 
#                  highlightthickness=40, command=quitApp)
#btn_quit.place(relx=0.9, rely=0, relwidth=0.08, relheight=0.08)

btn_1 = tk.Button(frame, text='EXPENSE', highlightbackground='#b3e6ff', 
               highlightthickness=50, command=calPage)
btn_1.place(relx=0.5, rely=0.1, relwidth=0.35, relheight=0.2, anchor='n')


# btn_2 = tk.Button(frame, text='INCOME', highlightbackground='#b3e6ff', 
#                   highlightthickness=50)
# btn_2.place(relx=0.51, rely=0.1, relwidth=0.3, relheight=0.2)


btn_3 = tk.Button(frame, text='REPORT', highlightbackground='#c299ff', 
                  highlightthickness=50, command=statsPage)
btn_3.place(relx=0.5, rely=0.35, relwidth=0.35, relheight=0.2, anchor='n')


btn_4 = tk.Button(frame, text='SETTINGS', highlightbackground='#ffb3d9', 
                  highlightthickness=50, command=setting_page)
btn_4.place(relx=0.5, rely=0.6, relwidth=0.35, relheight=0.2, anchor='n')


#sub category page
btn_c1 = tk.Button(frame3, text='Grocery', highlightbackground='#c299ff', 
                  highlightthickness=40, command = lambda *args:subcatValue('Grocery'))
btn_c1.place(relx=0.1, rely=0.3, relwidth=0.15, relheight=0.15)
btn_c2 = tk.Button(frame3, text='Cafe', highlightbackground='#c299ff', 
                  highlightthickness=40, command = lambda *args:subcatValue('Cafe'))
btn_c2.place(relx=0.3, rely=0.3, relwidth=0.15, relheight=0.15)

# Moved to Fixed Expense
# btn_c3 = tk.Button(frame3, text='Rent', highlightbackground='#c299ff', 
#                   highlightthickness=40, command = lambda *args:subcatValue('Rent'))
# btn_c3.place(relx=0.5, rely=0.3, relwidth=0.15, relheight=0.15)

btn_c4 = tk.Button(frame3, text='Restaurant', highlightbackground='#c299ff', 
                  highlightthickness=40, command = lambda *args:subcatValue('Restaurant'))
btn_c4.place(relx=0.5, rely=0.3, relwidth=0.15, relheight=0.15)
btn_c5 = tk.Button(frame3, text='Necessities', highlightbackground='#c299ff', 
                  highlightthickness=40, command = lambda *args:subcatValue('Necessities'))
btn_c5.place(relx=0.1, rely=0.5, relwidth=0.15, relheight=0.15)

btn_c6 = tk.Button(frame3, text='Health', highlightbackground='#c299ff', 
                  highlightthickness=40, command = lambda *args:subcatValue('Health'))
btn_c6.place(relx=0.3, rely=0.5, relwidth=0.15, relheight=0.15)


# Moved to Fixed Expense
# btn_c7 = tk.Button(frame3, text='Mobile', highlightbackground='#c299ff', 
#                   highlightthickness=40, command = lambda *args:subcatValue('Mobile'))
# btn_c7.place(relx=0.5, rely=0.5, relwidth=0.15, relheight=0.15)


#stat page
btn_current = tk.Button(frame_stat, text='This Statement', highlightbackground='#c299ff', 
                  highlightthickness=40, command = stat_basic_current)
btn_current.place(relx=0.1, rely=0.3, relwidth=0.30, relheight=0.15)
btn_prev = tk.Button(frame_stat, text='Last Statement', highlightbackground='#c299ff', 
                  highlightthickness=40, command = stat_basic_prev)
btn_prev.place(relx=0.6, rely=0.3, relwidth=0.30, relheight=0.15)

btn_backtoprev_stat = tk.Button(frame_stat, text="BACK", highlightbackground='#b3e6ff', 
              highlightthickness=50, command=mainPage)
btn_backtoprev_stat.place(relx=0.1, rely=0, anchor='n', relwidth=0.1, relheight=0.05)


#stat-2 page



#setting page
label_rent = tk.Label(frame_setting, text="Rent")
label_rent.place(relx=0.25, rely=0.1, relwidth=0.2, relheight=0.15)
entry_rent = tk.Entry(frame_setting)
entry_rent.place(relx=0.55, rely=0.1, relwidth=0.2, relheight=0.15)
label_ins = tk.Label(frame_setting, text="Health Insurance")
label_ins.place(relx=0.25, rely=0.3, relwidth=0.2, relheight=0.15)
entry_ins = tk.Entry(frame_setting)
entry_ins.place(relx=0.55, rely=0.3, relwidth=0.2, relheight=0.15)
label_mobile = tk.Label(frame_setting, text="Mobile Fee")
label_mobile.place(relx=0.25, rely=0.5, relwidth=0.2, relheight=0.15)
entry_mobile = tk.Entry(frame_setting)
entry_mobile.place(relx=0.55, rely=0.5, relwidth=0.2, relheight=0.15)


btn_save_setting = tk.Button(frame_setting, text="SAVE", highlightbackground='#c299ff', 
                  highlightthickness=40, command= lambda *args: 
                      check_setting(entry_rent.get(), entry_ins.get(), 
                                    entry_mobile.get()))
btn_save_setting.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.15, anchor='n')

btn_back_setting = tk.Button(frame_setting, text="BACK", highlightbackground='#b3e6ff', 
              highlightthickness=50, command=mainPage)
btn_back_setting.place(relx=0.1, rely=0, anchor='n', relwidth=0.1, relheight=0.05)




frame.tkraise()
root.mainloop()




