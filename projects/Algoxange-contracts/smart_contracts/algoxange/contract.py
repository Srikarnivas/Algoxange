from algopy import ARC4Contract, String
from algopy.arc4 import abimethod, Address
from algopy import ARC4Contract, arc4, UInt64, String, Bytes, itxn, Global, Asset, Txn, gtxn

class Algoxange(ARC4Contract):
    assetid: UInt64
    unitaryprice: UInt64

    @abimethod()
    def create_nft( self, asset_name: String, unit_name: String, url: String ) -> UInt64:
        
        itxn_result = itxn.AssetConfig(
            total= 1,
            decimals= 0,
            unit_name=unit_name,
            asset_name=asset_name,
            url=url,
            manager=Global.current_application_address,
            reserve=Global.current_application_address,
            freeze=Global.current_application_address,
            clawback=Global.current_application_address,
        ).submit()

        return itxn_result.created_asset.id
    #create the app
    @abimethod(allow_actions=["NoOp"], create="require")
    def create_application(self, asset_id: Asset, unitary_price: UInt64) -> None:
        self.assetid = asset_id.id
        self.unitaryprice = unitary_price
    @abimethod()
    def update_asset_id(self, asset_id: Asset) -> None:
        assert Txn.sender == Global.creator_address

        self.assetid = asset_id.id
    

    #update the listing price
    @abimethod()
    def set_price(self, unitary_price: UInt64) -> None:
        assert Txn.sender == Global.creator_address
        self.unitaryprice = unitary_price

    # opt in to the asset that will be sold
    @abimethod()
    def opt_in_to_asset(self, mbrpay: gtxn.PaymentTransaction) -> None:
        assert Txn.sender == Global.creator_address
        assert not Global.current_application_address.is_opted_in(Asset(self.assetid))

        assert mbrpay.receiver == Global.current_application_address

        assert mbrpay.amount == Global.min_balance + Global.asset_opt_in_min_balance

        itxn.AssetTransfer(
            xfer_asset= self.assetid,
            asset_receiver= Global.current_application_address,
            asset_amount= 0,
        ).submit()

    @abimethod()
    def debug_buy_check(self, buyerTxn: gtxn.PaymentTransaction) -> UInt64:
        if buyerTxn.sender != Txn.sender:
            return UInt64(1)
        if buyerTxn.receiver != Global.current_application_address:
            return UInt64(2)
        if buyerTxn.amount != self.unitaryprice:
            return UInt64(3)
        return UInt64(0)  # All good

    # buy the asset
    @abimethod()
    def buy(self, buyerTxn: gtxn.PaymentTransaction) -> None:

        assert(buyerTxn.sender == Txn.sender )
        assert(buyerTxn.receiver == Global.current_application_address )
        assert(buyerTxn.amount == self.unitaryprice )

    # Perform asset transfer
        itxn.AssetTransfer(
            xfer_asset=self.assetid,
            asset_receiver=Txn.sender,
            asset_amount=1,
        ).submit()

    @abimethod(allow_actions=["DeleteApplication"])
    def delete_application(self) -> None:

        assert Txn.sender == Global.creator_address

        # Send all the unsold assets to the creator
        itxn.AssetTransfer(
            xfer_asset=self.assetid,
            asset_receiver=Global.creator_address,
            # The amount is 0, but the asset_close_to field is set
            # This means that ALL assets are being sent to the asset_close_to address
            asset_amount=0,
            # Close the asset to unlock the 0.1 ALGO that was locked in opt_in_to_asset
            asset_close_to=Global.creator_address,
            fee=1_000,
        ).submit()

        # Send the remaining balance to the creator
        itxn.Payment(
            receiver=Global.creator_address,
            amount=0,
            # Close the account to get back ALL the ALGO in the account
            close_remainder_to=Global.creator_address,
            fee=1_000,
        ).submit()


