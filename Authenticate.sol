pragma solidity ^0.5.0;
contract Auth{
    uint public count = 0;
    struct productDetail{
        string id;
        string username;
        string date;
        string time;
        string city;
        string country;
    }
    mapping( uint => productDetail  ) public productList;
    function register(string memory _id,string memory _username,string memory _date,string memory _time,string memory _city,string memory _country) public {
        count++;
        productList[count] = productDetail( _id,_username,_date,_time,_city,_country );                
    }
}