from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

root = Tk()
root.title('Language Translator')
root.geometry("880x300")

def translate_it():
    # Delete any previous translation
    translated_text.delete(1.0, END)
    try:
        # Get Languages from Dictionary Keys
        # Get the from Language Keys
        for key, value in languages.items():
            if(value == original_combo.get()):
                from_language_key = key

        # Get the Language Key
        for key, value in languages.items():
            if(value == translated_combo.get()):
                to_language_key = key


        # Turn original text into a TextBlob
        words = textblob.TextBlob(original_text.get(1.0, END))

        # Translate text
        words = words.translate(from_lang = from_language_key, to = to_language_key)

        # Output Translated text to screen
        translated_text.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Translator", e)

def clear():
    # Clear the text buttons
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

# language_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27)

# Grab Language List from GoogleTrans
languages = googletrans.LANGUAGES

# print(languages)

# Convert to list
language_list = list(languages.values())
print(language_list)


# Text Boxes
original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(root, text="Translate", font=("Helvetica", 24), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, pady=20, padx=10)

# Combo boxes
original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1, column=2)

# Clear button
clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()