import os
import threading
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import fitz
from tkinterdnd2 import TkinterDnD, DND_FILES
import io
import webbrowser

# =========================================================
# Smart PDF Compressor
# Developed by Ali Zangeneh
# GitHub: https://github.com/alizangeneh
# License: MIT
# =========================================================

# ---------- Detect if PDF is Raster or Vector ----------
def is_raster_pdf(path):
    """
    Detects whether a PDF is raster (image-based) or vector (text-based).
    Returns True for raster PDFs.
    """
    try:
        doc = fitz.open(path)
        for page in doc:
            if page.get_text("text").strip():
                doc.close()
                return False
        doc.close()
        return True
    except:
        return True

# ---------- Compress Raster (Image-based) PDFs ----------
def compress_raster_pdf(input_path, output_path, dpi, cancel_flag):
    """
    Compresses raster PDFs by re-rendering each page as a lower-DPI image.
    """
    try:
        doc = fitz.open(input_path)
        new_pdf = fitz.open()
        for page in doc:
            if cancel_flag():
                doc.close()
                new_pdf.close()
                return False
            zoom = dpi / 72.0
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat, alpha=False)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            buf = io.BytesIO()
            img.save(buf, format="PDF", quality=85)
            buf.seek(0)
            img_pdf = fitz.open(stream=buf.read(), filetype="pdf")
            new_pdf.insert_pdf(img_pdf)
            buf.close()
            img_pdf.close()
        new_pdf.save(output_path, garbage=4, deflate=True)
        doc.close()
        new_pdf.close()
        return True
    except Exception as e:
        print(f"Error compressing raster PDF {input_path}: {e}")
        return False

# ---------- Compress Vector PDFs using Ghostscript ----------
def compress_vector_pdf(input_path, output_path, cancel_flag, quality="ebook"):
    """
    Compresses vector (selectable text) PDFs using Ghostscript.
    """
    try:
        if cancel_flag():
            return False
        gs_command = [
            "gswin64c",  # Use "gs" on Linux/Mac
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            f"-dPDFSETTINGS=/{quality}",
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            f"-sOutputFile={output_path}",
            input_path
        ]
        subprocess.run(gs_command, check=True)
        return True
    except Exception as e:
        print(f"Error compressing vector PDF {input_path}: {e}")
        return False

# ---------- Main Application Class ----------
class PDFCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart PDF Compressor - by Ali Zangeneh")
        self.root.geometry("550x520")
        self.root.resizable(False, False)
        self.pdf_files = []
        self.cancel_flag = False

        # --- File Selection Section ---
        file_frame = tk.LabelFrame(root, text="Select or Drop PDF Files")
        file_frame.pack(fill="x", padx=10, pady=5)
        self.listbox = tk.Listbox(file_frame, height=6, selectmode=tk.EXTENDED)
        self.listbox.pack(fill="both", expand=True, padx=5, pady=5)
        self.listbox.drop_target_register(DND_FILES)
        self.listbox.dnd_bind("<<Drop>>", self.on_drop)

        btn_frame = tk.Frame(file_frame)
        btn_frame.pack(fill="x")
        tk.Button(btn_frame, text="Browse", command=self.add_files_dialog).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete Selected", command=self.delete_selected).pack(side="left", padx=5)

        # --- DPI Options ---
        dpi_frame = tk.LabelFrame(root, text="DPI Settings")
        dpi_frame.pack(fill="x", padx=10, pady=5)
        self.dpi_choice = tk.StringVar(value="Screen 72 dpi")
        self.dpi_value = tk.IntVar(value=72)
        options = {"Screen 72 dpi": 72, "eBook 150 dpi": 150, "Printer 300 dpi": 300, "Manual": None}
        for text, val in options.items():
            tk.Radiobutton(dpi_frame, text=text, variable=self.dpi_choice,
                           value=text, command=lambda t=text, v=val: self.update_dpi(t, v)).pack(anchor="w")
        self.slider = tk.Scale(dpi_frame, from_=50, to=300, orient="horizontal", resolution=10,
                               label="Manual DPI", state="disabled", command=self.set_manual_dpi)
        self.slider.pack(fill="x", padx=10)

        # --- Control Buttons and Progress Bar ---
        control = tk.Frame(root)
        control.pack(fill="x", padx=10, pady=10)
        self.process_btn = tk.Button(control, text="Process", command=self.start_process)
        self.process_btn.pack(side="left", fill="x", expand=True, padx=5)
        self.cancel_btn = tk.Button(control, text="Cancel", state="disabled", command=self.cancel_process)
        self.cancel_btn.pack(side="left", fill="x", expand=True, padx=5)
        self.progress = ttk.Progressbar(root, mode="determinate")
        self.progress.pack(fill="x", padx=10, pady=10)
        self.status = tk.Label(root, text="Ready", anchor="w")
        self.status.pack(fill="x", padx=10)

        # --- GitHub Info Label (Help Button) ---
        help_label = tk.Label(root, text="❓", fg="blue", cursor="hand2", font=("Arial", 14))
        help_label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
        help_label.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/alizangeneh"))

    # ---------- File Handling ----------
    def add_files_dialog(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        self.add_files(files)

    def add_files(self, files):
        for f in files:
            if f not in self.pdf_files:
                self.pdf_files.append(f)
                self.listbox.insert(tk.END, os.path.basename(f))

    def delete_selected(self):
        selected = list(self.listbox.curselection())
        for i in reversed(selected):
            self.listbox.delete(i)
            del self.pdf_files[i]

    def on_drop(self, event):
        paths = self.root.tk.splitlist(event.data)
        files = [p for p in paths if p.lower().endswith(".pdf")]
        self.add_files(files)

    # ---------- DPI Control ----------
    def update_dpi(self, text, val):
        if text == "Manual":
            self.slider.config(state="normal")
            self.dpi_value.set(self.slider.get())
        else:
            self.slider.config(state="disabled")
            self.dpi_value.set(val)

    def set_manual_dpi(self, val):
        if self.dpi_choice.get() == "Manual":
            self.dpi_value.set(int(val))

    # ---------- Processing ----------
    def start_process(self):
        if not self.pdf_files:
            messagebox.showwarning("No files", "Please add PDF files first.")
            return
        self.cancel_flag = False
        self.process_btn.config(state="disabled")
        self.cancel_btn.config(state="normal")
        self.progress["value"] = 0
        self.status.config(text="Processing...")
        threading.Thread(target=self.process_all).start()

    def process_all(self):
        out_dir = os.path.join(os.getcwd(), "compressed_pdf")
        os.makedirs(out_dir, exist_ok=True)
        total = len(self.pdf_files)
        done = 0
        dpi = self.dpi_value.get()

        for pdf in self.pdf_files:
            if self.cancel_flag:
                break
            fname = os.path.basename(pdf)
            out_path = os.path.join(out_dir, fname)

            if is_raster_pdf(pdf):
                success = compress_raster_pdf(pdf, out_path, dpi, lambda: self.cancel_flag)
            else:
                success = compress_vector_pdf(pdf, out_path, lambda: self.cancel_flag, quality="ebook")

            if success:
                done += 1
            self.root.after(0, lambda d=done, t=total, f=fname: self.update_progress(d, t, f))

        self.root.after(0, lambda: self.finish(done, total))

    def update_progress(self, done, total, fname):
        self.progress["value"] = int((done / total) * 100)
        self.status.config(text=f"Processed {fname} ({done}/{total})")

    def finish(self, done, total):
        self.process_btn.config(state="normal")
        self.cancel_btn.config(state="disabled")
        self.status.config(text=f"Done: {done}/{total} files compressed.")
        messagebox.showinfo("Finished", f"Compressed {done}/{total} files.\nSaved in 'compressed_pdf' folder.")

    def cancel_process(self):
        self.cancel_flag = True
        self.status.config(text="Cancelling...")

# ---------- Run Application ----------
if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = PDFCompressorApp(root)
    root.mainloop()
