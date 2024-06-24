import re
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit
from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import QTimer
from game_logic import GameLogic
from text_loader import load_texts

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.texts = load_texts()  # Load game texts from external source
        self.logic = GameLogic()  # Initialize game logic
        self.typing_index = 0  # Current index for typing animation
        self.current_text = ""  # Text to be typed out
        self.typing_timer = QTimer(self)  # Timer for typing effect
        self.typing_timer.timeout.connect(self.type_text)  # Connect timer to typing method
        self.initUI()  # Initialize user interface
        self.setupBlinkingCursor()  # Setup blinking cursor effect
        self.pause_duration = 0  # Duration to pause during typing

    def initUI(self):
        self.setWindowTitle('Magical Linux Adventure')  # Set window title
        self.setGeometry(100, 100, 800, 600)  # Set window size and position
        
        # Set the background color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(0, 0, 0))  # Set window background to black
        self.setPalette(palette)
        
        self.layout = QVBoxLayout()  # Create vertical layout
        
        # Set up the text area for story output
        self.story_text = QTextEdit(self)
        self.story_text.setReadOnly(True)  # Make the text area read-only
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

        # Set up the input area for user commands
        self.command_input = QLineEdit(self)
        self.command_input.setStyleSheet("""
            background-color: black; 
            color: green; 
            border: none;
            font-family: Courier;
            font-size: 12px;
        """)
        self.command_input.setFont(font)
        self.command_input.setPlaceholderText("Enter command...")  # Placeholder text for input field
        self.command_input.returnPressed.connect(self.execute_command)  # Connect enter key to command execution
        self.layout.addWidget(self.command_input)

        self.setLayout(self.layout)  # Set layout for the main window
        self.start_game()  # Start the game

    def setupBlinkingCursor(self):
        self.cursor_visible = True  # Initial cursor visibility state
        self.timer = QTimer(self)  # Timer for blinking cursor
        self.timer.timeout.connect(self.blinkCursor)  # Connect timer to cursor blinking method
        self.timer.start(500)  # Set timer interval to 500ms

    def blinkCursor(self):
        # Toggle the cursor visibility and update the style accordingly
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
        self.cursor_visible = not self.cursor_visible  # Toggle visibility

    def start_game(self):
        self.typing_index = 0  # Reset typing index
        self.current_text = "\n".join(self.texts["intro"])  # Load intro text
        self.story_text.clear()  # Clear the story text area
        self.command_input.setDisabled(True)  # Disable input until typing is done
        self.typing_timer.start(50)  # Start typing timer with 50ms interval

    def type_text(self):
        # Handle pause duration during typing
        if self.pause_duration > 0:
            self.pause_duration -= 50
            return

        # Continue typing text if more characters remain
        if self.typing_index < len(self.current_text):
            # Check for input marker and handle it
            if self.current_text[self.typing_index:self.typing_index + 7] == '{input}':
                self.typing_timer.stop()
                self.command_input.setDisabled(False)  # Enable user input
                self.typing_index += 7
                return

            # Check for pause tags and handle them
            match = re.match(r'\{pause:(\d+)\}', self.current_text[self.typing_index:])
            if match:
                self.pause_duration = int(match.group(1)) * 1000
                self.typing_index += match.end()
                return
            
            # Insert character by character into the story text area
            self.story_text.insertPlainText(self.current_text[self.typing_index])
            self.typing_index += 1
        else:
            self.typing_timer.stop()  # Stop timer when done typing
            self.command_input.setDisabled(False)  # Enable user input

    def execute_command(self):
        command = self.command_input.text().strip()  # Get and trim user input
        self.story_text.append(f'\n>>> {command}')  # Display user command in story text area

        result = self.logic.handle_command(command)  # Process command using game logic
        self.show_dialog_text(result)  # Display result
        
        self.command_input.clear()  # Clear input field
    
    def handle_conversation(self, message):
        message = message.lower()  # Convert message to lowercase
        # Predefined responses for conversation
        responses = {
            'hi': 'Hello, young magician!',
            'hello': 'Greetings! How can I assist you on your journey?',
            'buy': 'Farewell! Until next time.',
        }
        response = responses.get(message, "I'm not sure how to respond to that.")  # Get response or default message
        self.show_dialog_text(response)  # Display response

    def show_dialog(self, character):
        self.typing_index = 0  # Reset typing index
        self.current_text = "\n".join(self.texts["dialogs"][character])  # Load dialog text for character
        self.story_text.append("\n")  # Add a newline for formatting
        self.typing_timer.start(50)  # Start typing timer

    def show_dialog_text(self, text):
        self.typing_index = 0  # Reset typing index
        self.current_text = text  # Set current text to the provided text
        self.story_text.append("\n")  # Add a newline for formatting
        self.typing_timer.start(50)  # Start typing timer
