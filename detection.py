import argparse
import logging
import configparser
from declarations.solidityFile import SolidityFile
from detectors.suicidal import Suicidal

def detection(directory, contract_name):
    logger.debug("Starting detection in detection.py")
    contract_path = directory + '/' + contract_name

    # Create status file to track if detection is still operating, done, or encountered an error.
    status_path = directory + '/' + 'status.txt'
    f = open(status_path, 'w')
    f.close()
    
    status = configparser.RawConfigParser()
    status.read(status_path)
    status.add_section('Status')
    status.set('Status', 'done', '0')
    status.set('Status', 'error', '0')
    
    with open(status_path, 'w') as file:
        status.write(file)
        
    # Perform detection
    try:
        # Setup and parse out smart contract
        smart_contract = SolidityFile(contract_name, contract_path)
        smart_contract.parse_top_level()

        # Perform vulnerability detectors on smart contract 
        output = Suicidal().detect_driver(smart_contract)

        # Write results to file
        with open(directory + '/results.txt', 'w') as f:
            for issue in output:
                f.write(str(issue) + "\n")

        # Update status file
        status.set('Status', 'done', '1')
        with open(status_path, 'w') as file:
            status.write(file)
    except Exception as e: 
        # Update status file
        status.set('Status', 'error', '1')
        status.set('Status', 'message', e)
        with open(status_path, 'w') as file:
            status.write(file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Perform detections on contract.")
    parser.add_argument("-d", "--directory", help="directory containing model, weight, and config files")
    parser.add_argument("-c", "--contract", help=".sol format file of contract")
    args = parser.parse_args()
    
    directory = getattr(args, "directory")
    contract = getattr(args, "contract")

    logging.basicConfig(filename=directory + '/log/detection.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(funcName)s:%(lineno)d:%(message)s')
    logger = logging.getLogger(name="root")
    
    detection(directory, contract)
