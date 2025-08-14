# Automate Citrix Login

Easily log in to Citrix Workspace by automating clicks and entering your email and password. MFA is not automated. Tested on macOS 15 only. Email and password are stored securely in the macOS Keychain.

## Download the code

```bash
git clone https://github.com/gungorbudak/automate-citrix-login.git
cd automate-citrix-login
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Set email and password

```bash
python -m keyring set citrix-login email
python -m keyring set citrix-login password
```

## Execute

```bash
python main.py
```

## Optionally assign keyboard shortcut

You can run this script with a global keyboard shortcut using Automator and macOS Services:

1. **Create a Quick Action:**
   - Open **Automator** and select **Quick Action**.
   - Set "Workflow receives" to "no input" in "any application".
   - Add a **Run Shell Script** action.
   - Enter the following command, replacing the Python path if needed:
     ```bash
     /path/to/.pyenv/versions/3.x.x/bin/python /path/to/automate-citrix-login/main.py
     ```
     *(Find your Python path with `pyenv which python` if using pyenv.)*
   - Save the Quick Action (e.g., "Run Citrix Login").

2. **Assign a Keyboard Shortcut:**
   - Open **System Settings** > **Keyboard** > **Keyboard Shortcuts**.
   - Go to **Services**.
   - Find your Quick Action under "General" or "Services".
   - Add a shortcut, e.g., `Control + Option + Command + L` (`⌃⌥⌘L`).

Now, pressing your chosen shortcut will run the Citrix login script
