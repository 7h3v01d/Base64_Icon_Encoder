import base64
import os
import sys
import mimetypes
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD

def get_base64_data(input_path):
    """Core logic to convert image to Data URI."""
    input_path = input_path.strip('{}').strip('"') 
    
    if not os.path.exists(input_path):
        return f"Error: File '{input_path}' not found."

    mime_type, _ = mimetypes.guess_type(input_path)
    if not mime_type:
        mime_type = 'image/png'

    try:
        with open(input_path, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return f"data:{mime_type};base64,{encoded_string}"
    except Exception as e:
        return f"Error: {e}"

class EncoderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Base64 Icon Studio")
        self.root.geometry("500x480")
        
        self.history = [] 
        
        # --- UI Setup ---
        tk.Label(root, text="Base64 Image Encoder", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Drop Zone
        self.drop_label = tk.Label(
            root, text="\nDROP IMAGE HERE\n", 
            relief="groove", bd=2, bg="#f8f9fa", fg="#666",
            font=("Arial", 10, "italic")
        )
        self.drop_label.pack(fill="x", padx=40, pady=10)
        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind('<<Drop>>', self.handle_drop)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Select File", command=self.handle_click, width=15).grid(row=0, column=0, padx=5)
        self.copy_btn = tk.Button(btn_frame, text="Copy Current", command=self.copy_latest, width=15, state="disabled", bg="#e3f2fd")
        self.copy_btn.grid(row=0, column=1, padx=5)

        # --- History Section ---
        tk.Label(root, text="Recent History (Double-click to copy):", font=("Arial", 9, "bold")).pack(anchor="w", padx=40, pady=(10, 0))
        
        self.history_listbox = tk.Listbox(root, height=6, font=("Consolas", 9))
        self.history_listbox.pack(fill="both", expand=True, padx=40, pady=5)
        self.history_listbox.bind('<Double-1>', self.copy_from_history)

        self.status_label = tk.Label(root, text="Ready", fg="gray", font=("Arial", 9, "bold"))
        self.status_label.pack(pady=10)

    def process_file(self, file_path):
        data_uri = get_base64_data(file_path)
        
        if data_uri.startswith("Error"):
            messagebox.showerror("Encoding Error", data_uri)
        else:
            filename = os.path.basename(file_path).strip('{}').strip('"')
            
            # Update History
            self.history.insert(0, (filename, data_uri))
            self.history = self.history[:10] 
            self.update_history_ui()
            
            # Save to fallback file
            with open("encoded_output.txt", "w") as f:
                f.write(data_uri)
            
            # UI Feedback
            self.status_label.config(text=f"✅ Successfully Encoded: {filename}", fg="#2e7d32")
            self.copy_btn.config(state="normal")
            
            # THE Pop-Up
            messagebox.showinfo("Success", f"'{filename}' has been encoded!\n\nIt is saved to history and 'encoded_output.txt'.\n\nYou can now click 'Copy Current' to use it.")

    def update_history_ui(self):
        self.history_listbox.delete(0, tk.END)
        for name, _ in self.history:
            self.history_listbox.insert(tk.END, f" 📄 {name}")
    
    def handle_drop(self, event):
        self.process_file(event.data)

    def handle_click(self):
        path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg *.svg *.gif *.ico")])
        if path: self.process_file(path)

    def copy_latest(self):
        if self.history:
            self.copy_text(self.history[0][1])

    def copy_from_history(self, event):
        selection = self.history_listbox.curselection()
        if selection:
            index = selection[0]
            self.copy_text(self.history[index][1])

    def copy_text(self, text):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.status_label.config(text="📋 Copied to Clipboard!", fg="#1976d2")
        # Temporary status change to show it worked
        self.root.after(2000, lambda: self.status_label.config(text="Ready", fg="gray"))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # CLI Mode
        print(get_base64_data(sys.argv[1]))
    else:
        # GUI Mode
        root = TkinterDnD.Tk()
        app = EncoderApp(root)
        root.mainloop()