import time, subprocess, sys
from flask import Flask, render_template, request, redirect, abort, make_response, send_file
from termcolor import cprint
from pathlib import Path
cprint("Starting...", "blue")
app = None
start_time = time.time()
data = {}
userinfofile = Path(__file__).with_name('userinfo')
try:
    print("Making new Flask app...")
    app = Flask(__name__)
    print("Reading userdata...")
    with open(userinfofile) as file:
        data = userinfofile.read()
except Exception as e:
    pass