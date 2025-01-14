import pyautogui
from pynput.mouse import Controller, Button
import win32gui
import win32con

# Set the pixel position to monitor (x, y)
PIXEL_POSITION = (442, 399)  # Updated position

# Define RGB values for red and green
RED_RGB = (255, 0, 0)
GREEN_RGB = (106, 219, 75)  # Updated green color

# Initialize mouse controller
mouse = Controller()

# Toggle this to True to print the mouse position
gettingPixelPosition = False

def get_pixel_color(x, y):
    # Get the handle of the screen
    hwnd = win32gui.GetDesktopWindow()
    
    # Get the device context for the screen
    hdc = win32gui.GetWindowDC(hwnd)
    
    # Get the pixel color at the specified location
    color = win32gui.GetPixel(hdc, x, y)
    
    # Convert color from hex (BGR) to RGB
    b = color & 0xFF
    g = (color >> 8) & 0xFF
    r = (color >> 16) & 0xFF
    return (r, g, b)

def print_mouse_position():
    print("Move your mouse to see its position. Press Ctrl+C to stop.")
    while True:
        position = pyautogui.position()
        print(f"Mouse position: {position}", end="\r")

def monitor_pixel():
    print(f"Monitoring pixel at position {PIXEL_POSITION}...")
    while True:
        # Get the current color of the pixel using pywin32 (direct access)
        current_color = get_pixel_color(*PIXEL_POSITION)
        
        # Debugging: Print current pixel color
        print(f"Current color: {current_color}", end="\r")
        
        # Check if the pixel color has changed to green
        if current_color == GREEN_RGB:
            print("\nPixel changed to green! Clicking the mouse...")
            
            # Perform the mouse click using pyautogui
            pyautogui.click(*PIXEL_POSITION)
            
            # Debugging: Confirm the click action
            print("Mouse click performed!")

def main():
    global gettingPixelPosition
    
    if gettingPixelPosition:
        print_mouse_position()
    else:
        monitor_pixel()

if __name__ == "__main__":
    main()