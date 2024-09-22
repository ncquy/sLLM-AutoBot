import tkinter as tk
from tkinter import messagebox, ttk
from googletrans import Translator
from PIL import Image, ImageTk  # Importing the necessary classes from Pillow

# Khởi tạo Google Translator
translator = Translator()

# Hàm để dịch văn bản bằng Google Translate
def translate_text(text, source_lang, target_lang):
    try:
        translated = translator.translate(text, src=source_lang, dest=target_lang)
        return translated.text
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {str(e)}")
        return None

# Hàm để xử lý khi người dùng nhấn nút "Translate"
def handle_translate():
    text_to_translate = input_text.get("1.0", tk.END).strip()  # Lấy nội dung từ ô nhập
    if not text_to_translate:
        messagebox.showwarning("Input Error", "Please enter some text to translate.")
        return

    # Lấy ngôn ngữ từ menu lựa chọn
    source_lang = source_lang_var.get()
    target_lang = target_lang_var.get()

    translated_text = translate_text(text_to_translate, source_lang, target_lang)
    
    if translated_text:
        output_text.delete("1.0", tk.END)  # Xóa nội dung cũ
        output_text.insert(tk.END, translated_text)  # Hiển thị nội dung dịch

# Tạo GUI bằng Tkinter
root = tk.Tk()
root.title("Korean-English Translation Tool")
root.geometry("500x500")
root.configure(bg="#f0f0f0")  # Set background color

# Style configuration
label_font = ("Arial", 12, "bold")
text_font = ("Arial", 10)
button_font = ("Arial", 11, "bold")

# Load and display the image at the top of the window
image = Image.open("img.png")  # Replace with the path to your image file
image = image.resize((100, 100), Image.Resampling.LANCZOS)  # Resize the image

photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo, bg="#f0f0f0")
image_label.pack(pady=10)

# Nhãn tiêu đề
title_label = tk.Label(root, text="Translator", font=("Arial", 16), bg="#f0f0f0")
title_label.pack(pady=10)

# Menu lựa chọn ngôn ngữ
language_frame = tk.Frame(root, bg="#f0f0f0")
language_frame.pack(pady=10)

source_lang_label = tk.Label(language_frame, text="Source Language:", font=label_font, bg="#f0f0f0")
source_lang_label.pack(side=tk.LEFT, padx=10)

source_lang_var = tk.StringVar(value="ko")  # Mặc định là Korean
source_lang_menu = ttk.Combobox(language_frame, textvariable=source_lang_var, values=["ko", "en"], state="readonly", font=text_font)
source_lang_menu.pack(side=tk.LEFT, padx=10)

target_lang_label = tk.Label(language_frame, text="Target Language:", font=label_font, bg="#f0f0f0")
target_lang_label.pack(side=tk.LEFT, padx=10)

target_lang_var = tk.StringVar(value="en")  # Mặc định là English
target_lang_menu = ttk.Combobox(language_frame, textvariable=target_lang_var, values=["en", "ko"], state="readonly", font=text_font)
target_lang_menu.pack(side=tk.LEFT, padx=10)

# Khung nhập liệu
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

input_label = tk.Label(input_frame, text="Input Text:", font=label_font, bg="#f0f0f0")
input_label.pack(side=tk.LEFT, padx=10)

input_text = tk.Text(input_frame, height=5, width=40, font=text_font, bd=2, relief="solid")
input_text.pack(side=tk.LEFT, padx=10)



# Nút Translate
translate_button = tk.Button(root, text="Translate", command=handle_translate, font=button_font, bg="#4CAF50", fg="white", width=15, bd=0)
translate_button.pack(pady=10)

# Khung hiển thị kết quả dịch
output_label = tk.Label(root, text="Translated Text:", font=label_font, bg="#f0f0f0")
output_label.pack(pady=5)

output_text = tk.Text(root, height=5, width=40, font=text_font, bd=2, relief="solid")
output_text.pack(pady=10)

# Khởi động ứng dụng
root.mainloop()
