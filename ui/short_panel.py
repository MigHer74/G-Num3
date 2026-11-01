import ttkbootstrap as ttk


class ShortPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.short_panel()
        self.short_entries_definition()

    def short_panel(self):
        self.short_frame = ttk.Frame(self.parent, bootstyle="bordered")
        self.short_frame.grid(row=0, column=0, padx=(10), pady=(10),
                              sticky="ew")
        self.short_frame.rowconfigure([0, 1], weight=1)
        self.short_frame.columnconfigure([0, 6], weight=1)

        self.short_label = ttk.Label(self.short_frame, text="Short Game",
                                     bootstyle="inverse-primary")
        self.short_label.grid(row=0, column=0, columnspan=7,
                              padx=(10), pady=(10))

        self.game_label = ttk.Label(self.short_frame, text="Game #1")
        self.game_label.grid(row=1, column=0, padx=(10), pady=(10))

    def short_entries_definition(self):
        self.entry_list = []

        self.entry_01 = ttk.Entry(self.short_frame, width=3, justify="center")
        self.entry_02 = ttk.Entry(self.short_frame, width=3, justify="center")
        self.entry_03 = ttk.Entry(self.short_frame, width=3, justify="center")
        self.entry_04 = ttk.Entry(self.short_frame, width=3, justify="center")
        self.entry_05 = ttk.Entry(self.short_frame, width=3, justify="center")
        self.entry_06 = ttk.Entry(self.short_frame, width=3, justify="center")

        self.entry_list = ([self.entry_01, self.entry_02, self.entry_03,
                            self.entry_04, self.entry_05, self.entry_06])

        for item in self.entry_list:
            item.grid(row=1, column=self.entry_list.index(item) + 1,
                      padx=(10), pady=(10))
