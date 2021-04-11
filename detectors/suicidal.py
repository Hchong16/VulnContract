""" 
Module detecting unprotected suicidal contract

A contract is suicidal if the selfdestruct or suicide function is called 
without any protection.
"""

class Suicidal():
    def detect_driver(self, smart_contract):
        """Driver code to detect for suicidal functions""" 
        results = []
        underlying_contracts = smart_contract.underlying_contracts
        
        # Iterate through all defined contracts in the Solidity File
        for contract_obj in underlying_contracts.values():
            functions = self.detect_suicidal(contract_obj)
            for function_obj in functions:
                info = [function_obj.name, " allows anyone to terminate the contract"]
                results.append(info)

        return results

    def detect_suicidal(self, contract):
        """
        Iterate through all defined functions within the contract and flag any functions 
        suspectable to a suicidal attack.

        Returns:
            (bool): True if the function is suicidal
        """
        suspectible_functions = []
        for function_obj in contract.functions.values():
            if self.detect_suicidal_function(function_obj):
                suspectible_functions.append(function_obj)
        
        return suspectible_functions

    def detect_suicidal_function(self, f):
        if f.visibility not in ["public", "external"]:
           return False

        calls = [c.name for c in f.identifiers]
        if not ("suicide" in calls or "selfdestruct" in calls):
            return False
        
        if f.is_protected:
            return False

        return True
