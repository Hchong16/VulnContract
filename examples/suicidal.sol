pragma solidity 0.8.1;

contract Contract{
    constructor() public {
        data = 1;
    }
    
    function kill() public{
        selfdestruct(msg.sender);
    }
}

contract Test{
    function test() public{
        return 1;
    }
}