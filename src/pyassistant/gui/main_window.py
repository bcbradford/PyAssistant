''' Main Window '''

import tkinter as tk
from tkinter import filedialog
from pyassistant.model import init_model

class MainWindow(tk.Tk):

    def __init__(self, config, logger):
        super().__init__()
        self.app_config = config
        self.logger = logger
        self.model = None
        self.title(self.app_config.get("window_title", "PyAssitant"))
        self.geometry(self.app_config.get("geometry", "800x600"))
        self.init_menu()
        self.init_widgits()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def init_menu(self):
        self.menu_bar = tk.Menu(self)
        self.model_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Models", menu=self.model_menu)
        
        self.diffuser_menu = tk.Menu(self.model_menu, tearoff=0)
        self.model_menu.add_cascade(label="Diffuser", menu=self.diffuser_menu)
        self.nlp_menu = tk.Menu(self.model_menu, tearoff=0)
        self.model_menu.add_cascade(label="NLP", menu=self.nlp_menu)

        # Add Models to menu
        for key in self.app_config["MODELS"].keys():
            if self.app_config["MODELS"][key]["TYPE"] == "diffuser":
                self.diffuser_menu.add_command(label=key, 
                        command=lambda m=key: self.load_model(m))
            else:
                self.nlp_menu.add_command(label=key,
                        command=lambda m=key: self.load_model(m))
        
        self.config(menu=self.menu_bar)

    def init_widgits(self):
        self.text = tk.Text(self)
        self.text.grid(row=0, column=0, sticky='nsew')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.text.config(state=tk.DISABLED)

        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=0, sticky='ew')
        self.entry.bind("<Return>", self.on_submit)

    def load_model(self, model_name):
        self.model = init_diffuser_model(self.app_config["MODELS"][model_name],
                model_name, self.logger)
    
    def save_image(self, image):
        file_path = filedialog.asksaveasfilename(
                title="Save Image",
                initialdir=self.app_config["OUTPUT_PATH"],
                filetypes=(("PNG Files", "*.png"), ("JPEG Files", "*.jpg"), ("All Files", "*.*")),
                defaultextension=".png"
        )
        if file_path:
            try:
                image.save(file_path)
            except Exception as e:
                self.logger.error(f"Failed to save image '{file_path}': {e}")
        
    def on_submit(self, event):
        pass
    
    def on_closing(self):
        self.destroy()

    def run(self):
        self.mainloop()
    
def init_main_window(config, logger):
    window = MainWindow(config, logger)
    return window
