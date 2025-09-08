import sys
from pathlib import Path

# Resolve the folder containing tictactoe.py
base_dir = Path(__file__).parent.resolve()

# Add student_code and default_code to sys.path
sys.path.insert(0, str(base_dir))  # student_code folder
sys.path.insert(1, str(base_dir.parent / 'default_code'))  # fallback

# Now imports work
from play_game import play_game

play_game()