import json
import pprint

from declarations.solidityFile import SolidityFile

if __name__ == "__main__":
    filename = 'suicidal.sol'
    file_path = './examples/{}'.format(filename)

    # Setup and parse out smart contract
    smart_contract = SolidityFile()
    smart_contract.filename = filename
    smart_contract.file_path = file_path
    smart_contract.parse_top_level()

    # Run vulnerability detectors on smart contract

    # pprint.pprint(sourceUnitObject.imports)
    # pprint.pprint(sourceUnitObject.contracts["Contract"].functions.keys())  # Get all functions in contract: "contractName"
    # pprint.pprint(sourceUnitObject.contracts["Counter_v1"].functions["getCount"].visibility)  # get "kill"s visibility (or stateMutability)

    # print("Arguments:")
    # pprint.pprint(sourceUnitObject.contracts["Counter_v1"].functions["kill"].arguments)   

    # print("Declarations:")
    # pprint.pprint(sourceUnitObject.contracts["Counter_v1"].functions["kill"].declarations)

    # print("Identifiers:")
    # pprint.pprint(sourceUnitObject.contracts["Counter_v1"].functions["kill"].identifiers.idents)

    # print("Returns:")
    # pprint.pprint(sourceUnitObject.contracts["Counter_v1"].functions["kill"].returns)

    # print("State Mutability:")
    # pprint.pprint(sourceUnitObject.contracts["Counter_v1"].functions["kill"].stateMutability)
    #print(dir(sourceUnitObject.contracts["Counter_v1"].functions["kill"])) # get "kill"s

    # with open('data/parsed.json', 'w') as outfile:
    #     #json.dump(smart_contract.source_unit, outfile, indent=4)
    #     json.dump(smart_contract.source_unit, outfile)

