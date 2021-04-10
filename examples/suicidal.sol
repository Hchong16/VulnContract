pragma solidity 0.8.1;

contract Contract{
    function protected_kill() public{
        require(msg.sender == owner);
        selfdestruct(msg.sender);
    }
}

contract Test{
    function bad_kill() public{
        address a = msg.sender;
        require(a == owner);


        selfdestruct(msg.sender);
    }
}
