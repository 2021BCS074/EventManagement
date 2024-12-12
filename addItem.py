import tkinter as tk
from tkinter import messagebox

def add_product():
    product_name = entry_product_name.get()
    product_price = entry_product_price.get()
    product_image = entry_product_image.get()
    if product_name and product_price and product_image:
        messagebox.showinfo("Success", "Product Added Successfully!")
    else:
        messagebox.showwarning("Error", "All fields are required!")

def delete_product():
    messagebox.showinfo("Delete", "Product Deleted Successfully!")

def update_product():
    messagebox.showinfo("Update", "Product Updated Successfully!")

# Main window
root = tk.Tk()
root.title("Vendor Panel")
root.geometry("800x600")
root.configure(bg="lightblue")

# Header
header = tk.Frame(root, bg="blue", height=50)
header.pack(fill=tk.X)
tk.Label(header, text="Welcome  'Vendor Name'", bg="blue", fg="white", font=("Arial", 14)).pack(side=tk.LEFT, padx=10)

# Navigation Buttons
nav_frame = tk.Frame(header, bg="blue")
nav_frame.pack(side=tk.RIGHT, padx=10)
for btn_text in ["Product Status", "Request Item", "View Product", "Log Out"]:
    tk.Button(nav_frame, text=btn_text, bg="white", font=("Arial", 10), padx=5).pack(side=tk.LEFT, padx=5)

# Add Product Section
add_frame = tk.Frame(root, bg="lightblue")
add_frame.pack(pady=20)
tk.Label(add_frame, text="Product Name", bg="lightblue", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
tk.Label(add_frame, text="Product Price", bg="lightblue", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
tk.Label(add_frame, text="Product Image", bg="lightblue", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5)

entry_product_name = tk.Entry(add_frame, width=30, font=("Arial", 12))
entry_product_name.grid(row=0, column=1, padx=10, pady=5)
entry_product_price = tk.Entry(add_frame, width=30, font=("Arial", 12))
entry_product_price.grid(row=1, column=1, padx=10, pady=5)
entry_product_image = tk.Entry(add_frame, width=30, font=("Arial", 12))
entry_product_image.grid(row=2, column=1, padx=10, pady=5)

tk.Button(add_frame, text="Add The Product", bg="blue", fg="white", font=("Arial", 12), command=add_product).grid(row=3, columnspan=2, pady=10)

# Product List Section
list_frame = tk.Frame(root, bg="lightblue")
list_frame.pack(pady=20)
columns = ["Product Image", "Product Name", "Product Price", "Action"]
for col_index, col_name in enumerate(columns):
    tk.Label(list_frame, text=col_name, bg="blue", fg="white", font=("Arial", 12), width=20).grid(row=0, column=col_index, padx=5, pady=5)

# Sample Data Row
sample_image = tk.Label(list_frame, text="Image", bg="white", font=("Arial", 10))
sample_image.grid(row=1, column=0, padx=5, pady=5)
sample_name = tk.Label(list_frame, text="Sample Name", bg="white", font=("Arial", 10))
sample_name.grid(row=1, column=1, padx=5, pady=5)
sample_price = tk.Label(list_frame, text="Rs/-", bg="white", font=("Arial", 10))
sample_price.grid(row=1, column=2, padx=5, pady=5)

action_frame = tk.Frame(list_frame, bg="lightblue")
action_frame.grid(row=1, column=3, padx=5, pady=5)

tk.Button(action_frame, text="Delete", bg="red", fg="white", font=("Arial", 10), command=delete_product).pack(side=tk.LEFT, padx=5)
tk.Button(action_frame, text="Update", bg="green", fg="white", font=("Arial", 10), command=update_product).pack(side=tk.LEFT, padx=5)

root.mainloop()