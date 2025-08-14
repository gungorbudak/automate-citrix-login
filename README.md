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
