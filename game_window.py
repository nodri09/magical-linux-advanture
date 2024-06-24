import re
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit
from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import Qt, QTimer
from game_logic import handle_command
from text_loader import load_texts

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.texts = load_texts()
        self.command_keywords = ['ls', 'cd', 'mkdir', 'touch', 'cat', 'help']
        self.typing_index = 0
        self.current_text = ""
        self.typing_timer = QTimer(self)
        self.typing_timer.timeout.connect(self.type_text)
        self.initUI()
        self.setupBlinkingCursor()
        self.pause_duration = 0
        #self.show_dialog_text("Welcome to the game! Type ' help to see available commands or start a conversation.")

    def initUI(self):
        self.setWindowTitle('Magical Linux Adventure')
        self.setGeometry(100, 100, 800, 600)
        
        # Set the background color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(0, 0, 0))
        self.setPalette(palette)
        
        self.layout = QVBoxLayout()
        
        # Set the text area
        self.story_text = QTextEdit(self)
        self.story_text.setReadOnly(True)
        self.story_text.setStyleSheet("""
            background-color: black; 
            color: green; 
            border: none;
            font-family: Courier;
            font-size: 12px;
        """)
        font = QFont("Courier", 12)
        self.story_text.setFont(font)
        self.layout.addWidget(self.story_text)

        # Set the input area
        self.command_input = QLineEdit(self)
        self.command_input.setStyleSheet("""
            background-color: black; 
            color: green; 
            border: none;
            font-family: Courier;
            font-size: 12px;
        """)
        self.command_input.setFont(font)
        self.command_input.setPlaceholderText("Enter command...")
        self.command_input.returnPressed.connect(self.execute_command)
        self.layout.addWidget(self.command_input)

        self.setLayout(self.layout)
        self.start_game()

    def setupBlinkingCursor(self):
        self.cursor_visible = True
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blinkCursor)
        self.timer.start(500)

    def blinkCursor(self):
        if self.cursor_visible:
            self.command_input.setStyleSheet("""
                background-color: black; 
                color: green; 
                border: none;
                font-family: Courier;
                font-size: 12px;
            """)
        else:
            self.command_input.setStyleSheet("""
                background-color: black; 
                color: green; 
                border: none;
                font-family: Courier;
                font-size: 12px;
                selection-background-color: black;
                selection-color: green;
            """)
        self.cursor_visible = not self.cursor_visible

    def start_game(self):
        self.typing_index = 0
        self.current_text = "\n".join(self.texts["intro"])
        self.story_text.clear()
        self.command_input.setDisabled(True)
        self.typing_timer.start(50)

    def type_text(self):
        if self.pause_duration > 0:
            self.pause_duration -= 50
            return

        if self.typing_index < len(self.current_text):
            match = re.match(r'\{pause:(\d+)\}', self.current_text[self.typing_index:])
            if match:
                self.pause_duration = int(match.group(1)) * 1000
                self.typing_index += match.end()
                return
            
            self.story_text.insertPlainText(self.current_text[self.typing_index])
            self.typing_index += 1
        else:
            self.typing_timer.stop()
            self.command_input.setDisabled(False)

    def execute_command(self):
        command = self.command_input.text().strip()
        self.story_text.append(f'\n>>> {command}')

        if command.split()[0] in self.command_keywords:
            result = handle_command(command)
            self.show_dialog_text(result)
        else:
            self.handle_conversation(command)
        
        self.command_input.clear()
    
    def handle_conversation(self, message):
        message = message.lower()
        responses = {
            'hi': 'Hello, young magician!',
            'hello': 'Greetings! How can I assist you on your journey?',
            'buy': 'Firewell! Until next time.',
        }
        response = responses.get(message.lower(), "I'm not sure how to respond to that.")
        self.show_dialog_text(response)

    def show_dialog(self, character):
        self.typing_index = 0
        self.current_text = "\n".join(self.texts["dialogs"][character])
        self.story_text.append("\n")
        self.typing_timer.start(50)

    def show_dialog_text(self, text):
        self.typing_index = 0
        self.current_text = text
        self.story_text.append("\n")
        self.typing_timer.start(50)
