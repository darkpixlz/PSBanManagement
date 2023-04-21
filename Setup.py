import time, subprocess, sys
packages = [
    "termcolor",
    "flask",
    "getpass4",
    "bcrypt"
]
start_time = time.time()
for package in packages:
    print(f"Resolving package {package}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
print(
    f"Resolved {len(packages)} packages in {time.time() - start_time} seconds")
import os, string, collections, requests, bcrypt
from getpass4 import getpass
from termcolor import colored, cprint
from pathlib import Path
cprint("PreloadService", "blue", attrs=["bold"])
cprint("Advanced Ban Pro Web Management Setup", "red")

print("""
Welcome to the PreloadService Advanced Ban Pro Setup Manager!

This will assist you in setting up your website, and getting it ready.

Note: Continuting with setup will overwrite existing configuration data

Are you sure you would like to continue with setup? If you continue, all previous setup info will be wiped [y/n].
""")
data = Path(__file__).with_name('userinfo')
remove_consent = input("> ")

while not remove_consent == "y" and not remove_consent == "n":
    print("Try again. (expected y/n)")
    remove_consent = input("> ")

if remove_consent == "n":
    exit("setup cancelled by user")
else:
    cprint("Overwriting userinfo...", "red")
    try:
        with data.open("w") as file:
            file.write("")
            file.close()
    except Exception as e:
        cprint(f"{'-'*25} Error! {'-'*25} ", 'red')
        print(f"Could not overwrite data with exception {e}, exiting...\n")
        exit("Something went wrong and the code had to exit, try again later.")

cprint("Success!\n\n", "green")

supplied_data = {}

print("What is your Universe ID? (https://create.roblox.com/dashboard/creations/experiences/xxxxxxxxxxx/overview)")
supplied_data["universe_id"] = input("> ")

print("What is your open cloud API key?")
supplied_data["api_key"] = input("> ")

print("What port should your app run on?")
supplied_data["port"] = input("> ")

print("What should your app's login username be?")
supplied_data["username"] = input("> ")


def check_password():
    issues = False
    common_passwords = str(requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt").content)
    if supplied_data["password"] in common_passwords:
        cprint("Error: Password is in top 10000 most common passwords. Pick a better password.", "red")
        issues = True
    if len(supplied_data["password"]) < 10:
        cprint("Error: Your password must not be less than 10 characters", "red")
        issues = True
    
    return issues
def prompt_password():
    print("What should your app's login password be?")
    supplied_data["password"] = getpass("> ")
prompt_password()
while check_password():
    prompt_password()

print("All data collected! Hashing password and saving...")
# hashing is disabled rn bc its shit 
#salt = bcrypt.gensalt()
#hashed = bcrypt.hashpw(supplied_data["password"], salt)
cprint("Successfully generated a password hash!", "green")
try:
    with data.open("a") as file:
        for entry in supplied_data:
            file.write(supplied_data[entry] + "\n")
    file.close()
except Exception as e:
    cprint(f"Failed to save userdata with exception {e}. Are you admin/root?")

cprint("Saved!", "green")
print("""
From now, you're all good to go. To start the server, just run:

python3 main.py

Exiting with success...
""")