pragma solidity 0.8.1;

contract Contract_v1{
    function protected_kill_1() public{
        require(msg.sender == owner);
        selfdestruct(msg.sender);
    }
}

contract Contract_v2{
    function bad_kill_1() public{
        address a = msg.sender;
        require(a == owner);

        selfdestruct(msg.sender);
    }
}

contract Contract_v3{
    function bad_kill_2() public{
        suicide(msg.sender);
    }
}

contract Contract_v4{
    function protected_kill_2() private{
        selfdestruct(msg.sender);
    }
}
