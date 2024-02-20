from pynput import keyboard
import time

typed_keys = []
start_time = None
total_characters = 0
total_time = 0
last_key_time = None
is_logging = True
double_tab_interval = 0.5  # Adjust this interval as needed

def on_press(key):
    global typed_keys, total_characters, last_key_time, start_time, total_time, is_logging

    try:
        char_key = key.char
    except AttributeError:
        char_key = str(key)

    # Record the pressed key
    typed_keys.append(char_key)
    total_characters += 1

    # Check for double-press of Tab key
    if char_key == 'tab':
        current_time = time.time()
        if last_key_time is not None and current_time - last_key_time < double_tab_interval:
            # Stop the listener and return all typed keys
            stop_logging()
            return False
        last_key_time = current_time

def on_release(key):
    global is_logging

    if key == keyboard.Key.esc:
        # Stop the listener and return all typed keys
        stop_logging()
        return False

def calculate_typing_stats():
    global start_time, total_time, typed_keys

    # Filter out non-alphanumeric keys for velocity calculation
    alphanumeric_chars = [char for char in typed_keys if char.isalnum()]

    for i in range(1, len(alphanumeric_chars)):
        # Calculate the time between consecutive alphanumeric key presses
        time_between_keys = time_between_presses(alphanumeric_chars[i - 1], alphanumeric_chars[i])
        total_time += time_between_keys

def time_between_presses(first_char, second_char):
    # Simple function to return the time between consecutive key presses
    # You can customize this based on your requirements
    return 0.1  # Placeholder value, replace with your own calculation

def stop_logging():
    global total_characters, total_time, is_logging

    avg_typing_speed = (
        total_characters / max(total_time, 1) if total_characters > 0 else 0
    )
    avg_velocity = (
        total_time / max(total_characters - 1, 1) if total_characters > 1 else 0
    )

    print(f'Average Typing Speed: {avg_typing_speed:.2f} characters per second')
    print(f'Average Velocity: {avg_velocity:.4f} seconds per keystroke')
    print("All Typed Keys:", " ".join(typed_keys))
    is_logging = False

def start_logging():
    global start_time

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        start_time = time.time()
        listener.join()

# Main program

start_logging()
calculate_typing_stats()
stop_logging()
