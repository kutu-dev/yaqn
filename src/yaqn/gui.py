import tkinter
import tkinter.font
from pathlib import Path
from datetime import datetime
import sys

class Gui(tkinter.Tk):
    def __init__(self, notes_path: Path, extension: str) -> None:
        super().__init__()

        self.notes_dir_path: Path = notes_path
        self.extension = extension

        self.title('YAQN')
        self.bind_all('<Control-Return>', self.save_note_and_exit)

        # Set the widgets
        self.set_widgets()
        self.input.focus_set()
        self.scrollbar_loop()
        
        self.mainloop()
    
    def set_widgets(self) -> None:

        font_size: tkinter.font.Font = tkinter.font.Font(size=20)

        # Input widget
        self.input = tkinter.Text(
            self,
            highlightthickness=0,
            padx=20,
            pady=20,
            font= font_size,
            height=9,
            width=30,
            )
        self.input.pack(side=tkinter.LEFT)

        # Scrollbar widget
        self.scrollbar = tkinter.Scrollbar()

        # Set the relation between the textbox and the scrollbar
        self.input.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.input.yview)

        # Clean the menu bar
        self.menu = tkinter.Menu()
        self.config(menu=self.menu)

    def scrollbar_loop(self):
        """
        Check if the number of lines has exceeded the maximum of the textbox and show or hide a scrollbar as appropriate.
        """
        number_of_lines: int = self.input.get('1.0', 'end-1c').count('\n')

        if number_of_lines > 8:
            self.scrollbar.pack(side=tkinter.RIGHT, fill='y')
        else:
            self.scrollbar.pack_forget()

        self.after(1, self.scrollbar_loop)

    def save_note_and_exit(self, event: tkinter.Event) -> None:
        # Set the note file
        self.notes_dir_path.mkdir(parents=True, exist_ok=True)

        datetime_file_name: str = datetime.now().strftime('%H%M%S-%d%m%Y')
        note_path: Path = Path(self.notes_dir_path, f'{datetime_file_name}.{self.extension}')

        # Get the textbox data and save it
        note:str = self.input.get('1.0', 'end-1c')

        note_path.touch()
        with open(note_path, 'w') as file:
            file.write(note)
        
        sys.exit(0)
