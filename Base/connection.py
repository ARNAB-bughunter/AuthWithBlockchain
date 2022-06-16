from datetime import datetime
from web3 import Web3
import json
from django.conf import settings

class myBlockchain():
    def __init__(self):
        self.BLOCKCHAIN_URL = settings.BLOCKCHAIN_URL
        self.contract = None
        self.web = None
        
    def deployContract(self):
        self.web = Web3(Web3.HTTPProvider(self.BLOCKCHAIN_URL))
        
        self.web.eth.default_account = self.web.eth.accounts[0]

        abi = json.loads('[{"constant":true,"inputs":[],"name":"count","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"productList","outputs":[{"internalType":"string","name":"id","type":"string"},{"internalType":"string","name":"username","type":"string"},{"internalType":"string","name":"ownerType","type":"string"},{"internalType":"string","name":"date","type":"string"},{"internalType":"string","name":"time","type":"string"},{"internalType":"string","name":"city","type":"string"},{"internalType":"string","name":"country","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"_id","type":"string"},{"internalType":"string","name":"_username","type":"string"},{"internalType":"string","name":"_ownerType","type":"string"},{"internalType":"string","name":"_date","type":"string"},{"internalType":"string","name":"_time","type":"string"},{"internalType":"string","name":"_city","type":"string"},{"internalType":"string","name":"_country","type":"string"}],"name":"register","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
        bytecode = '0x60806040526000805534801561001457600080fd5b50610e51806100246000396000f3fe608060405234801561001057600080fd5b50600436106100415760003560e01c806306661abd14610046578063528c87d2146100645780639d0c9fca14610393575b600080fd5b61004e6107d8565b6040518082815260200191505060405180910390f35b6100906004803603602081101561007a57600080fd5b81019080803590602001909291905050506107de565b604051808060200180602001806020018060200180602001806020018060200188810388528f818151815260200191508051906020019080838360005b838110156100e85780820151818401526020810190506100cd565b50505050905090810190601f1680156101155780820380516001836020036101000a031916815260200191505b5088810387528e818151815260200191508051906020019080838360005b8381101561014e578082015181840152602081019050610133565b50505050905090810190601f16801561017b5780820380516001836020036101000a031916815260200191505b5088810386528d818151815260200191508051906020019080838360005b838110156101b4578082015181840152602081019050610199565b50505050905090810190601f1680156101e15780820380516001836020036101000a031916815260200191505b5088810385528c818151815260200191508051906020019080838360005b8381101561021a5780820151818401526020810190506101ff565b50505050905090810190601f1680156102475780820380516001836020036101000a031916815260200191505b5088810384528b818151815260200191508051906020019080838360005b83811015610280578082015181840152602081019050610265565b50505050905090810190601f1680156102ad5780820380516001836020036101000a031916815260200191505b5088810383528a818151815260200191508051906020019080838360005b838110156102e65780820151818401526020810190506102cb565b50505050905090810190601f1680156103135780820380516001836020036101000a031916815260200191505b50888103825289818151815260200191508051906020019080838360005b8381101561034c578082015181840152602081019050610331565b50505050905090810190601f1680156103795780820380516001836020036101000a031916815260200191505b509e50505050505050505050505050505060405180910390f35b6107d6600480360360e08110156103a957600080fd5b81019080803590602001906401000000008111156103c657600080fd5b8201836020820111156103d857600080fd5b803590602001918460018302840111640100000000831117156103fa57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f8201169050808301925050505050505091929192908035906020019064010000000081111561045d57600080fd5b82018360208201111561046f57600080fd5b8035906020019184600183028401116401000000008311171561049157600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290803590602001906401000000008111156104f457600080fd5b82018360208201111561050657600080fd5b8035906020019184600183028401116401000000008311171561052857600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f8201169050808301925050505050505091929192908035906020019064010000000081111561058b57600080fd5b82018360208201111561059d57600080fd5b803590602001918460018302840111640100000000831117156105bf57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f8201169050808301925050505050505091929192908035906020019064010000000081111561062257600080fd5b82018360208201111561063457600080fd5b8035906020019184600183028401116401000000008311171561065657600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290803590602001906401000000008111156106b957600080fd5b8201836020820111156106cb57600080fd5b803590602001918460018302840111640100000000831117156106ed57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f8201169050808301925050505050505091929192908035906020019064010000000081111561075057600080fd5b82018360208201111561076257600080fd5b8035906020019184600183028401116401000000008311171561078457600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290505050610c48565b005b60005481565b6001602052806000526040600020600091509050806000018054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561088a5780601f1061085f5761010080835404028352916020019161088a565b820191906000526020600020905b81548152906001019060200180831161086d57829003601f168201915b505050505090806001018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156109285780601f106108fd57610100808354040283529160200191610928565b820191906000526020600020905b81548152906001019060200180831161090b57829003601f168201915b505050505090806002018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156109c65780601f1061099b576101008083540402835291602001916109c6565b820191906000526020600020905b8154815290600101906020018083116109a957829003601f168201915b505050505090806003018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610a645780601f10610a3957610100808354040283529160200191610a64565b820191906000526020600020905b815481529060010190602001808311610a4757829003601f168201915b505050505090806004018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610b025780601f10610ad757610100808354040283529160200191610b02565b820191906000526020600020905b815481529060010190602001808311610ae557829003601f168201915b505050505090806005018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610ba05780601f10610b7557610100808354040283529160200191610ba0565b820191906000526020600020905b815481529060010190602001808311610b8357829003601f168201915b505050505090806006018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610c3e5780601f10610c1357610100808354040283529160200191610c3e565b820191906000526020600020905b815481529060010190602001808311610c2157829003601f168201915b5050505050905087565b60008081548092919060010191905055506040518060e001604052808881526020018781526020018681526020018581526020018481526020018381526020018281525060016000805481526020019081526020016000206000820151816000019080519060200190610cbc929190610d77565b506020820151816001019080519060200190610cd9929190610d77565b506040820151816002019080519060200190610cf6929190610d77565b506060820151816003019080519060200190610d13929190610d77565b506080820151816004019080519060200190610d30929190610d77565b5060a0820151816005019080519060200190610d4d929190610d77565b5060c0820151816006019080519060200190610d6a929190610d77565b5090505050505050505050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f10610db857805160ff1916838001178555610de6565b82800160010185558215610de6579182015b82811115610de5578251825591602001919060010190610dca565b5b509050610df39190610df7565b5090565b610e1991905b80821115610e15576000816000905550600101610dfd565b5090565b9056fea265627a7a72315820041cbfc8eb9aea601f529dfb4a87e9866701e77da3f891eaef65bf5910dbfc5264736f6c63430005110032'
        
        Auth = self.web.eth.contract(abi=abi,bytecode=bytecode)
        tx_hash = Auth.constructor().transact()
        tx_receipt = self.web.eth.waitForTransactionReceipt(tx_hash)
        self.contract=self.web.eth.contract(
            address=tx_receipt.contractAddress,
            abi=abi
        )

    def setAccount(self,useraddress):
        self.web.eth.default_account = Web3.toChecksumAddress(useraddress)

    def setDefaultAccount(self):
        self.web.eth.default_account = self.web.eth.accounts[0]


    def registerProduct(self,id,username,ownerType,city,country):
        tx_hash=self.contract.functions.register(id,username,ownerType,datetime.now().strftime('%d:%m:%y'),datetime.now().strftime('%H:%M:%S'),city,country).transact()
        return self.web.toHex(tx_hash)

    def aboutProduct(self,id):
        productList=[]
        for i in range(1,self.contract.functions.count().call()+1):
            if self.contract.functions.productList(i).call()[0]==str(id):
                productList.append(self.contract.functions.productList(i).call())
        return productList

