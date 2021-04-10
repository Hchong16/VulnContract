import json
from declarations.solidityFile import SolidityFile
from detectors.suicidal import Suicidal

if __name__ == "__main__":
    filename = 'suicidal.sol'
    file_path = './examples/{}'.format(filename)

    results = []

    # Setup and parse out smart contract
    smart_contract = SolidityFile(filename, file_path)
    smart_contract.parse_top_level()

    # Perform vulnerability detectors on smart contract 
    output = Suicidal().detect_driver(smart_contract)











    # with open('data/parsed.json', 'w') as outfile:
    #     json.dump(smart_contract.source_unit, outfile, indent=4)
    #     json.dump(smart_contract.source_unit, outfile)
