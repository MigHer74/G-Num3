import ttkbootstrap as ttk


class MainPanel(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title("G-Num3")
        self.theme_use("nord-dark")
        self.geometry("800x600")
        self.place_window_center()

        self.main_panes()
        self.game_type_panel()
        self.game_play_panel()
        self.game_button_panel()

    def main_panes(self):
        self.action_panel = ttk.Frame(self, width=100, bootstyle="bordered")
        self.action_panel.pack(padx=(10), pady=(10), side="left", fill="y")
        self.action_panel.rowconfigure([0, 1, 2], weight=1)

        self.content_panel = ttk.Frame(self, bootstyle="bordered")
        self.content_panel.pack(padx=(10), pady=(10), side="right",
                                fill="both", expand=True)

    def game_type_panel(self):
        self.type_panel = ttk.Frame(self.action_panel)
        self.type_panel.grid(row=0, column=0, padx=(5), sticky="w")

        self.radio_short = ttk.Radiobutton(self.type_panel, text="Short Game",
                                           value="Short")
        self.radio_short.pack(padx=(10), pady=(10, 0))

        self.radio_long = ttk.Radiobutton(self.type_panel, text="Long Game",
                                          value="Long")
        self.radio_long.pack(padx=(10), pady=(10, 10))

    def game_play_panel(self):
        self.play_panel = ttk.Frame(self.action_panel)
        self.play_panel.grid(row=1, column=0, padx=(5), sticky="w")

        self.radio_play = ttk.Radiobutton(self.play_panel, text="Play Game",
                                          value="Play")
        self.radio_play.grid(row=0, column=0, padx=(10), pady=(10, 0),
                             sticky="w")

        self.radio_replay = ttk.Radiobutton(self.play_panel,
                                            text="Replay Game", value="Replay")
        self.radio_replay.grid(row=1, column=0, padx=(10), pady=(10, 10),
                               sticky="w")

    def game_button_panel(self):
        self.button_panel = ttk.Frame(self.action_panel)
        self.button_panel.grid(row=2, column=0, padx=(5), sticky="w")

        self.go_button = ttk.Button(self.button_panel, width=15, text="Go!",
                                    bootstyle="success")
        self.go_button.grid(row=0, column=0, padx=(10), pady=(10, 0))

        self.cancel_button = ttk.Button(self.button_panel, width=15,
                                        text="Cancel", bootstyle="warning")
        self.cancel_button.grid(row=1, column=0, padx=(10), pady=(15, 0))

        self.archive_button = ttk.Button(self.button_panel, width=15,
                                         text="Archive", bootstyle="info")
        self.archive_button.grid(row=2, column=0, padx=(10), pady=(15, 0))

        self.close_button = ttk.Button(self.button_panel, width=15,
                                       text="Close",
                                       bootstyle="danger-outline",
                                       command=self.destroy)
        self.close_button.grid(row=3, column=0, padx=(10), pady=(15, 10))
