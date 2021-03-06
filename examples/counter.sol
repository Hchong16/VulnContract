pragma solidity 0.8.1;

contract Counter_v1 {
    uint count = 0;
    
    event Increment(uint value);
    event Decrement(uint value);
    
    function getCount() view public returns(uint) {
        return count;
    }
    
    function increment() public {
        count += 1;
        emit Increment(count);
    }
    
    function decrement() public {
        count -= 1;
        emit Decrement(count);
    }
}

contract Counter_v2 {
    uint count = 0;
    
    event Increment(uint value);
    event Decrement(uint value);
    
    function getCount() view public returns(uint) {
        return count;
    }
    
    function increment() public {
        count += 1;
        emit Increment(count);
    }
    
    function decrement() public {
        count -= 1;
        emit Decrement(count);
    }

    function good_suicide() public{
        require(msg.sender == owner);
        selfdestruct(msg.sender);
    }
}
