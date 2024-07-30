from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class StopwatchApp(App):
    """A Textual App to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the App."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An Action to toggle dark mode."""
        self.dark = not self.dark

if __name__ == "__main__":
    app = StopwatchApp()
    app.run