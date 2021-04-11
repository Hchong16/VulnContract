# VulnContract - CertiK Take Home Assignment (Project B)

VulnContract is a security analysis web tool for smart contracts. It detects security vulnerabilities in Ethereum smart contracts programmed in Solidity. 

Currently, the webtool detects only for **unprotected Suicidal contracts**.

## Installation and setup
Download dependencies using:
```
pip install -r requirements.txt
```
Run the webtool:
```
python3 app.py
```

## Usage
Once the terminal is running the Flask application, visit http://localhost:8001/ to access the webtool. 

To use the tool, please follow these steps:
1. Select a contract language (Solidity supported. Golang and Rust planned for future release).
2. Press the browse button to upload a `.sol` contract file.
3. Press the `Run Detections` button.

Once the detection is completed, you will be transferred to the result screen. If you wish to perform detections on another file, return to the home screen by pressing the `Home` button.

### Example Files
All test inputs can be found in the `examples` folder.

## Video Demo
Please find a video demonstration of the webtool here: [Youtube](https://youtu.be/dPqfdtKCCeE)

## Documentation
Please find design and implementation documentation here: [Google Doc](https://docs.google.com/document/d/1ChN1sSe9viZSnBZN61JOiARuszOb4u3eG0Py4BbbHfA/edit?usp=sharing)
