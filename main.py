import json
from declarations.solidityFile import SolidityFile

if __name__ == "__main__":
    filename = 'test.sol'
    file_path = './examples/{}'.format(filename)

    # Setup and parse out smart contract
    smart_contract = SolidityFile(filename, file_path)
    smart_contract.parse_top_level()

    with open('data/parsed.json', 'w') as outfile:
        json.dump(smart_contract.source_unit, outfile, indent=4)
        json.dump(smart_contract.source_unit, outfile)

    # [To do] Perform vulnerability detectors on smart contract
