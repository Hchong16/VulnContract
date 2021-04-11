import os
import sys
import logging
import configparser
import subprocess
import time
import uuid 
import os.path
from flask import Flask, render_template, make_response, request, redirect, send_file, send_from_directory
from werkzeug.utils import secure_filename

# [Setup Debug Log]
logging.basicConfig(filename='./log/temp.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(funcName)s:%(lineno)d:%(message)s')
logger = logging.getLogger(name="root")

UPLOAD_FOLDER = './output'

# [Setup Application]
app = Flask(__name__, template_folder='interface/templates', static_folder="interface/static")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# App route to Home Page
@app.route('/')
def home():
    today = time.strftime('%Y-%m-%d:%H%M%S')

    # Record User IP visiting webtool
    ip_addr = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    with open("./log/track.log", 'a') as f:
        f.write("(Home) Requester IP: {} on {}\n".format(ip_addr, today))    
    
    return render_template("main.html")

# App route to save input files.
@app.route('/save', methods = ['POST'])
def save():
    if request.method == 'POST':
        # language_choice = request.form.get('contract_language') No use currently
        # Generate job ID
        job_id = str(uuid.uuid4().hex)
        
        # Create main directory named after job ID for detection results
        directory = app.config['UPLOAD_FOLDER'] + '/{}'.format(job_id)
        os.makedirs(directory)
        
        # Setup detection log directory
        log_directory = directory + '/log'
        os.makedirs(log_directory)
        
        time.sleep(2)
       
        # Grab and save file
        solidity_file = request.files['contract_file']
        solidity_file.save(os.path.join(directory, secure_filename(solidity_file.filename)))

        # If files saved successfully, call detection function
        response = detection(directory, solidity_file.filename, job_id)

        if response:
            return response
    else: # Prevent user from accessing this route manually.
        return "Error: Invalid Access"

@app.route('/progress', methods = ['POST'])
def progress():
    time.sleep(3)
    directory = request.get_json()["directory"]

    done, error = 0, 0
    status_path = directory + '/' + 'status.txt'
    status = configparser.RawConfigParser()

    # Keep reading file until either status updates
    while done == 0 and error == 0:
        status.read(status_path)
        done = int(status.get('Status', 'done'))
        error = int(status.get('Status', 'error'))
        
    return # Job completed

@app.route('/result')
def result():
    directory = request.args.get('directory')
    contract = request.args.get('contract')
    job_id = request.args.get('jobID') 
    today = time.strftime("%Y-%m-%d:%H%M%S")
      
    # Parse detection log for output data.
    detection_log = directory + "/log/detection.log"
       
    results = []

    # Record User IP initiating detection
    ip_addr = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    with open("./log/track.log", 'a') as f:
        f.write("(Detection) Requester IP: {} on {}\n".format(ip_addr, today)) 
    
    try: 
        # [To do] Parse results.
        pass
    except:
        pass

    # Grab error message if exist
    status_path = directory + '/' + 'status.txt'
    status_file = configparser.RawConfigParser()
    status_file.read(status_path)
    
    try:
        error_message = str(status_file.get('Status', 'message'))
    except:
        error_message = ''
        pass
    
    status = 1
    
    return render_template("result.html", status=status, directory=directory, contract=contract, jobID=job_id, error=error_message, detection_results=results)

# Function to initiate detection.py script to run scans 
def detection(directory, solidity_file, job_id):
    command = [sys.executable, './detection.py', '--directory', directory, '--contract', solidity_file]
    
    f = open(directory + "/log/detection.log", "a")
    response = make_response(redirect('/progress'))
    pid = subprocess.Popen(command, stdout=f, stderr=f)
    logger.debug("Launching detection in app.py with PID:{}".format(str(pid.pid)))
    
    response = render_template('progress.html', directory=directory, contract=solidity_file, jobID=job_id)
    return response

if __name__ == "__main__":
    app.run(host="localhost", port=8001, debug=True)
