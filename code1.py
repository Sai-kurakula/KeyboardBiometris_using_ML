from pynput import keyboard
import time

class KeyLogger:
    def __init__(self):
        self.start_time = None
        self.total_characters = 0
        self.total_time = 0

    def on_press(self, key):
        try:
            # Record the pressed key
            char_key = key.char
            self.total_characters += 1
            print(f'Key Pressed: {char_key}')
        except AttributeError:
            # Handle special keys
            char_key = str(key)
            print(f'Key Pressed: {char_key}')

        # Calculate typing speed and velocity of keystrokes
        if self.start_time is None:
            self.start_time = time.time()
        else:
            elapsed_time = time.time() - self.start_time
            self.total_time += elapsed_time
            if self.total_characters > 0:
                typing_speed = self.total_characters / self.total_time
                velocity = self.total_time / self.total_characters
                print(f'Typing Speed: {typing_speed:.2f} characters per second')
                print(f'Keystroke Velocity: {velocity:.4f} seconds per keystroke')

    def on_release(self, key):
        if key == keyboard.Key.esc:
            # Stop the listener
            avg_typing_speed = (
                self.total_characters / max(self.total_time, 1) if self.total_characters > 0 else 0
            )
            print(f'Average Typing Speed: {avg_typing_speed:.2f} characters per second')
            return False

    def start_logging(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
            

if __name__ == "__main__":
    logger = KeyLogger()
    logger.start_logging()

