import smartpy as sp

class Crowfounding(sp.Contract):
    def __init__(self, tokenPrice: int, adminAddress: str) -> None: # Constructor
        self.init(
            price = tokenPrice, # token price
            adminAddress = adminAddress,
            investors = sp.big_map() # Liste des investisseurs et de leurs jetons
        )

    @sp.entry_point
    def buy_tokens(self, value: int) -> None:
        # Vérifier que l'acheteur n'est pas l'administrateur
        #sp.verify(sp.sender != role, message="Admin ne peut pas acheter des jetons")
        sp.verify(value > 0,message="403|The amount must be greater than 0")
        totalPrice = self.data.price * value
        '''sp.verify(
            value == sp.utils.nat_to_tez(totalPrice),
            message="400|The amount is incorrect"
        )'''
        # Mettre à jour le solde de l'investisseur
        self.data.investors[sp.sender] = self.data.investors.get(sp.sender, 0) + value

    @sp.entry_point
    def update_price(self, value: int) -> None:
        # Vérifier que l'expéditeur est l'administrateur
        #sp.verify(sp.sender == self.data.admin, message="Seul l'admin peut mettre à jour le prix de l'énergie")
        self.data.price = value

    @sp.entry_point
    def transfer(self, _to: str, value: int) -> None:
        sp.verify(
            sp.sender != _to,
            message="403|Operation forbidden"
        )
        sp.verify(
            self.data.investors[sp.sender] >= value,
            message="400|Insufficient tokens"
        )
        self.data.investors[sp.sender] = sp.as_nat(self.data.investors[sp.sender] - value)
        self.data.investors[_to] = self.data.investors.get(_to, 0) + value

@sp.add_test(name="Crowfounding")
def test():
    scenario = sp.test_scenario() # Creation of a test scenario
    
    admin = sp.test_account("admin")
    investors = [sp.test_account("Pierre"), sp.test_account("Paul"), sp.test_account("Jacsque")]
    
    cost = 200 
    contract = Crowfounding(cost, admin.address) # Créer une instance du contrat
    
    scenario += contract
    scenario += contract.buy_tokens(5).run(sender=investors[0])
    scenario += contract.update_price(3).run(sender=admin)
    scenario += contract.transfer(investors[0].address, sp.nat(2)).run(sender=investors[1])

