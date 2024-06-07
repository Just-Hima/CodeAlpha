# Importing Libraries
import tkinter as tk
from nltk import download
from nltk.corpus import wordnet
from tkinter import ttk, messagebox
from langdetect import DetectorFactory
from googletrans import Translator, LANGUAGES

#Translation Tool Body
class Translator_Tool:
    def __init__(self, master):
        self.master = master
        master.title("Language Translator")

        self.translator = Translator()
        self.supported_languages = dict(zip(LANGUAGES.values(), LANGUAGES.keys()))
        self.languages_list = list(LANGUAGES.values())
        self.user_input = tk.StringVar()
        self.target_lang_code = None

        self.create_widgets()

    def create_widgets(self):
        # Input
        self.label_input = ttk.Label(self.master, text="Input Text:", font=("Arial", 18))
        self.label_input.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.entry_input = ttk.Entry(self.master, textvariable=self.user_input, width=50, font=("Arial", 18))
        self.entry_input.grid(row=0, column=1, padx=10, pady=5)
        self.entry_input.bind('<Return>', lambda Enter_Typed: self.translate_text())

        # Output
        self.label_output = ttk.Label(self.master, text="Translated Text:", font=("Arial", 18))
        self.label_output.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.output_text_label = ttk.Label(self.master, text="", font=("Arial", 18), wraplength=500, anchor="w")
        self.output_text_label.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="w")

        # Language Menu
        self.output_lang_menu = ttk.Combobox(self.master, values=self.languages_list, state="readonly", font=("Arial", 18))
        self.output_lang_menu.grid(row=0, column=2, padx=10, pady=5)
        self.output_lang_menu.current(0)
        self.output_lang_menu.bind("<<ComboboxSelected>>", lambda selected: self.translate_text())

        # Translate Button
        self.translate_button = ttk.Button(self.master, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=2, column=1, padx=10, pady=5, sticky="e")

    # Error Handling
    def translate_text(self):
        user_text = self.user_input.get().strip()
        if not user_text:
            messagebox.showerror("Error", "Please enter some text.")
            return

        try:
            target_lang_code = self.supported_languages[self.output_lang_menu.get()]
        except KeyError:
            messagebox.showerror("Error", "Please select an output language.")
            return

        try:
            translation = self.translator.translate(user_text, dest=target_lang_code)
            self.output_text_label.config(text=f"{LANGUAGES[target_lang_code]} Translation:\n{translation.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Translation error: {str(e)}")

#Translation Function
def translate():
    download('punkt')
    download('wordnet')

    # Avoid Randomness
    DetectorFactory.seed = 0

    root = tk.Tk()
    app = Translator_Tool(root)
    root.mainloop()

#Start
translate()