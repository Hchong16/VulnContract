pragma solidity 0.8.1;

contract Contract{
    function kill() public{
        require(msg.sender == owner);
        selfdestruct(msg.sender);
    }
}

contract Test{
    function bad_kill() public{
        selfdestruct(msg.sender);
    }
}
