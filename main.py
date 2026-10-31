import ui
import src


if __name__ == "__main__":
    src.database_exists()

    app = ui.MainPanel()
    app.mainloop()
