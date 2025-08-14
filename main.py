import pywinctl
import pyautogui
import pyperclip
import keyring


SIGNIN_BUTTON_PATH = "images/signin_button.png"
EMAIL_TEXTBOX_PATH = "images/email_textbox.png"
PASSWORD_TEXTBOX_PATH = "images/password_textbox.png"
EMAIL = keyring.get_password("citrix-login", "email")
PASSWORD = keyring.get_password("citrix-login", "password")


def activate_window(window_title):
    try:
        window = pywinctl.getWindowsWithTitle(window_title)[0]
        window.activate()
    except IndexError:
        print(f"Window with title '{window_title}' not found.")
        return False
    return True


def locate(image_path):
    try:
        return pyautogui.locateOnScreen(
            image_path,
            grayscale=True,
            confidence=0.8
        )
    except pyautogui.ImageNotFoundException:
        print(f"Image not found: {image_path}")
        return None


def click(image_path):
    try:
        while not locate(image_path):
            print(f"Waiting for image: {image_path}")
            pyautogui.sleep(1)
        button = pyautogui.center(locate(image_path))
        pyautogui.click(button.x, button.y)
    except pyautogui.ImageNotFoundException:
        print(f"Image not found: {image_path}")
        return


def enter_text(image_path, text):
    click(image_path)
    pyperclip.copy(text)
    pyautogui.sleep(2)
    pyautogui.hotkey("command", "v")
    pyautogui.press("enter")
    pyautogui.sleep(1)


def main():
    if not activate_window("Citrix Workspace"):
        return

    click(SIGNIN_BUTTON_PATH)
    enter_text(EMAIL_TEXTBOX_PATH, EMAIL)
    enter_text(PASSWORD_TEXTBOX_PATH, PASSWORD)


if __name__ == "__main__":
    main()
