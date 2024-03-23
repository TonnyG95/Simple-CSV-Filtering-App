import pandas as pd
from tkinter import Tk, Label, Entry, filedialog, StringVar, Frame, messagebox
import tkinter.font as tkFont
from tkinter import ttk

def filter_csv():
    """
    Filter the loaded CSV file by the selected column and value.
    Saves the filtered data to a new CSV file.
    Shows a warning if any field is empty and an error if the filtering process fails.
    """
    input_csv = input_file.get()
    output_csv = output_file.get()
    column_name = filter_field.get()
    filter_value = filter_value_entry.get()

    if not input_csv or not output_csv or not column_name or not filter_value:
        messagebox.showwarning("Warning", "Please fill in all fields before filtering.")
        return
    
    try:
        df = pd.read_csv(input_csv)
        filtered_df = df[df[column_name] == filter_value]
        filtered_df.to_csv(output_csv, index=False)
        messagebox.showinfo("Success", "Filtering completed. Check the output file.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def choose_input_file():
    filename = filedialog.askopenfilename()
    if filename:
        input_file.set(filename)
        input_label.config(text=filename.split('/')[-1])
        update_columns(filename)
    update_filter_field()

def choose_output_file():
    filename = filedialog.asksaveasfilename(defaultextension=".csv")
    if filename:
        output_file.set(filename)
        output_label.config(text=filename.split('/')[-1])

def update_columns(file_path=None):
    """
    The function `update_columns` reads a CSV file, retrieves the column names, and updates a filter
    field with the column names as values.
    
    :param file_path: The `file_path` parameter is a string that represents the file path of a CSV file
    that you want to read and extract column names from
    """
    if file_path:
        try:
            df = pd.read_csv(file_path)
            columns = df.columns.tolist()
            filter_field['values'] = columns
            filter_field.set('')
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        update_filter_field()

def update_filter_field():
    """
    The function `update_filter_field` updates the values in a dropdown menu based on the columns of a
    CSV file selected by the user, handling errors if the file cannot be read.
    """
    if not input_file.get():
        filter_field['values'] = ['Input CSV not selected']
        filter_field.set('Input CSV not selected')
    else:
        try:
            df = pd.read_csv(input_file.get())
            columns = df.columns.tolist()
            filter_field['values'] = columns
            if not columns:
                filter_field.set('No columns found')
            else:
                filter_field.set('')
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

app = Tk()
app.title("CSV Filter Tool")
app.geometry("1000x550")

app.configure(background='#2C3E50')
app.title("CSV Filter Tool")

### Head Font Settings ###

title_font = tkFont.Font(family="Helvetica", size=24, weight="bold")  
subtitle_font = tkFont.Font(family="Helvetica", size=14)

### Title ###

title_label = Label(app, text="CSV Filter", font=title_font, bg="#2C3E50", fg="white")
title_label.pack(pady=20)

### Subtitle ###

subtitle_label = Label(app, text="Easily filter your CSV files and extract the data you need.", font=subtitle_font, bg="#2C3E50", fg="white")
subtitle_label.pack(pady=(0, 20))  

### Buttons Settings ###

style = ttk.Style(app)
style.configure("TButton", padding=10, relief="flat", font=('Helvetica', 12), background="#2C3E50", foreground="#417afa")
style.map("TButton", background=[('active', '#356eca'), ('pressed', '#417afa')])

### Frame Settings ###

frame = Frame(app, bg='#2C3E50')
frame.pack(padx=30, pady=30, fill="both", expand="yes")

input_file = StringVar()
output_file = StringVar()


### Input CSV ###

input_label = Label(frame, text="Select your CSV", bg="#34495E", fg="white", width=60, pady=10)
input_label.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
ttk.Button(frame, text="Select Your CSV", command=choose_input_file).grid(row=0, column=2, padx=10, pady=10, sticky="ew")

### Output CSV ###

output_label = Label(frame, text="Please select location and name for your filtered CSV", bg="#34495E", fg="white", width=60, pady=10)
output_label.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
ttk.Button(frame, text="Choose Output File", command=choose_output_file).grid(row=1, column=2, padx=10, pady=10, sticky="ew")

### Dropdown ###

Label(frame, text="Select a column to filter:", bg='#2C3E50', fg="white", font=('Helvetica', 12)).grid(row=2, column=0, pady=(20, 10), sticky='w')
filter_field = ttk.Combobox(frame, font=('Helvetica', 12), state="readonly")
filter_field.grid(row=2, column=1, padx=10, pady=(20, 10), sticky="ew", ipady=5)

### Filter Value ###

Label(frame, text="Enter the value to export to new CSV:", bg='#2C3E50', fg="white", font=('Helvetica', 12)).grid(row=3, column=0, pady=10, sticky='w')
filter_value_entry = StringVar()
filter_value = Entry(frame, textvariable=filter_value_entry, font=('Helvetica', 12), borderwidth=0, bg="#34495E", fg="white", insertbackground='white')
filter_value.grid(row=3, column=1, padx=10, pady=10, sticky="ew", ipady=5)

### Filter Button ###

filter_button = ttk.Button(frame, text="Filter", command=filter_csv)
filter_button.grid(row=4, column=1, pady=20, sticky='ew')

### Update Columns ###
update_filter_field()

### Run App ##
app.mainloop()