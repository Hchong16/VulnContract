from declarations.solidityFile import SolidityFile

if __name__ == "__main__":
    filename = 'suicidal.sol'
    file_path = './examples/{}'.format(filename)

    # Setup and parse out smart contract
    smart_contract = SolidityFile()
    smart_contract.filename = filename
    smart_contract.file_path = file_path
    smart_contract.parse_top_level()

    # [To do] Run vulnerability detectors on smart contract
