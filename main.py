import tkinter
from tkinter import messagebox
import base64

def encode(key, clear):
    enc_bytes = bytearray()
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc_bytes.append(ord(enc_c))
    return base64.urlsafe_b64encode(bytes(enc_bytes)).decode('utf-8')

def decode(key, enc):
    dec_bytes = bytearray()
    enc_bytes = base64.urlsafe_b64decode(enc.encode('utf-8'))
    enc_str = enc_bytes.decode('utf-8', errors='ignore') # Base64 çözüldü ve stringe çevrildi
    for i in range(len(enc_str)):
        key_c = key[i % len(key)]
        dec_c_ord = (256 + ord(enc_str[i]) - ord(key_c)) % 256
        dec_bytes.append(dec_c_ord)
    return bytes(dec_bytes).decode('utf-8', errors='ignore')

def save_and_encrypt():
    title = title_entry.get()
    message = note_text.get("1.0", tkinter.END)
    master_secret = key_entry.get()

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showerror(title="Error", message="Please enter all info")
    else:
        message_encrypted = encode(master_secret, message)
        try:
            with open("mysecret.txt", "a") as data_file:
                data_file.write(f"\n{title} \n{message_encrypted}")
        except FileNotFoundError:
            with open("mysecret.txt", "w") as data_file:
                data_file.write(f"\n{title} \n{message_encrypted}")
        finally:
            title_entry.delete(0, tkinter.END)
            note_text.delete("1.0", tkinter.END)
            key_entry.delete(0, tkinter.END)

def decrypt_notes():
    message_encrypted = note_text.get("1.0", tkinter.END)
    master_secret = key_entry.get()

    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showerror(title="Error", message="Please enter all info")
    else:

        # decrypted_message = decode(master_secret, message_encrypted)
        # note_text.delete("1.0", tkinter.END)
        # note_text.insert("1.0", decrypted_message)

        try:
            decrypted_message = decode(master_secret, message_encrypted)
            note_text.delete("1.0", tkinter.END)
            note_text.insert("1.0", decrypted_message)
        except:
            messagebox.showerror(title="Error", message="Please enter encrypted text!")

window = tkinter.Tk()
window.title("Secret Notes")
window.geometry("400x700")

image = tkinter.PhotoImage(file="topsecret.png")
new_image = image.subsample(4,4)
image_label = tkinter.Label(image=new_image)
image_label.pack()

title_label = tkinter.Label(text="Enter your title", font=("montserrat", 15, "normal"))
title_label.pack()

title_entry = tkinter.Entry(font=("montserrat", 15, "normal"))
title_entry.pack(pady=10)

note_label = tkinter.Label(text="Enter your secret", font=("montserrat", 15, "normal"))
note_label.pack(pady=1)

note_text = tkinter.Text(width=30, height=10, font=("montserrat", 15, "normal"))
note_text.pack(pady=10)

key_label = tkinter.Label(text="Enter your key", font=("montserrat", 15, "normal"))
key_label.pack()

key_entry = tkinter.Entry(font=("montserrat", 15, "normal"))
key_entry.pack(pady=10)

save_btn = tkinter.Button(text="Save & Encrypt", command=save_and_encrypt,fg="white",relief=tkinter.FLAT, font=("montserrat", 13, "bold"),cursor="hand2", bg="dark gray")
save_btn.pack(pady=10)

decrypt_btn = tkinter.Button(text="Decrypt", command=decrypt_notes, fg="white",relief=tkinter.FLAT, font=("montserrat", 13, "bold"),cursor="hand2", bg="dark gray")
decrypt_btn.pack(pady=5)

window.mainloop()