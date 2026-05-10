import tkinter as tk
from tkinter import ttk
import descriptive

class DataLabWindow(tk.Toplevel):
    def __init__(root, parent):
        super().__init__(parent)
        # --- Create main window ---
        root.title("Statistics Calculator") 

        # Window size
        window_width = 1000
        window_height = 600

        # Get screen size
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Compute center position
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))

        # Set window position
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # --- UI Layout ---
        nav_frame = tk.Frame(root, bg="#6c0987", height=60)
        nav_frame.pack(side="top", fill="x")
        nav_frame.pack_propagate(False)

      
        tk.Label(nav_frame, text="Statistics Calc",font=("Georgia",10,"bold"),fg="white", bg="#6c0987", padx=20).pack(side="left")

        data_lab_btn = tk.Button(nav_frame, text="Data Lab", relief="flat",font=("Verdana",10,"bold"), fg="white", bg="#6c0987")
        data_lab_btn.pack(side="right", padx=15)

        data_lab_btn = tk.Button(nav_frame, text="Stats Basics", relief="flat",font=("Verdana",10,"bold"), fg="white", bg="#6c0987")
        data_lab_btn.pack(side="right", padx=15)

        data_lab_btn = tk.Button(nav_frame, text="Home", relief="flat",font=("Verdana",10,"bold"), fg="white", bg="#6c0987", command=root.destroy)
        data_lab_btn.pack(side="right", padx=15)


        main_content = tk.Frame(root, bg="#d871f5")
        main_content.pack(expand=True, fill="both")

        tk.Label(main_content, bg="#d871f5").pack(expand=True)
        tk.Label(main_content, text="Statistics Calc", font=("Georgia", 50, "bold"), fg="white", bg="#d871f5").pack()
        tk.Label(main_content, bg="#d871f5").pack(pady=10)
        tk.Button(main_content, text="Descriptive Statistics",fg = "white",bg = "#6c0987",font=("Verdana",10,"bold"), padx=10, pady=10,command=lambda: descriptive.Descriptive(root)).pack()
        tk.Label(main_content, bg="#d871f5").pack(pady=1)
        tk.Button(main_content, text="Inferential Statistics",fg = "white",bg = "#6c0987",font=("Verdana",10,"bold"), padx=11, pady=10).pack()
        tk.Label(main_content, bg="#d871f5").pack(expand=True)

    

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    root.mainloop()

