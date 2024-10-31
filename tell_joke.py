import tkinter as tk
from pyjokes import get_joke

# Set up the window
root = tk.Tk()
root.title("You're Gonna Laugh")
root.geometry("600x400")
root.configure(bg="#1e1e1e")

# Header label
header_label = tk.Label(root, text="Need a Laugh?", font=("Helvetica", 28, "bold"), bg="#1e1e1e", fg="#ffffff")
header_label.pack(pady=20)

# Joke label to display the joke
display_label = tk.Label(root, text="Click the button to hear a joke!", font=("Helvetica", 16), bg="#1e1e1e", fg="#dcdcdc", wraplength=500, justify="center")
display_label.pack(pady=40)

# Function to get and display a joke
def tell_joke():
    joke = get_joke()
    display_label.configure(text=joke)

# Button to get the joke
joke_button = tk.Button(root, text="Click Only If You're a Programmer", fg="#ffffff", bg="#007acc", font=("Helvetica", 14, "bold"), command=tell_joke, padx=20, pady=10, relief="flat", bd=0)
joke_button.pack(pady=20)

# Add a quit button 
quit_button = tk.Button(root, text="Exit", fg="#ffffff", bg="#d9534f", font=("Helvetica", 14, "bold"), command=root.quit, padx=20, pady=10, relief="flat", bd=0)
quit_button.pack(pady=20)

# Run the application
root.mainloop()