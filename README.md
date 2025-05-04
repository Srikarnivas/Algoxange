
# 📘 AlgoRack – A Book-Selling NFT Marketplace on Algorand

AlgoRack is a decentralized NFT marketplace where authors can mint and sell digital books (eBooks, articles, research papers) as Non-Fungible Tokens (NFTs) on the Algorand blockchain. It leverages smart contracts written in `algopy` to securely manage book listings and purchases, with NFT creation handled on the frontend using `algosdk`.

---

## 🚀 Features

- ✅ **NFT Creation (Frontend)**
  - Authors mint NFTs for their books using the frontend.
  - Each book is represented as an ASA (Algorand Standard Asset) with:
    - Total supply of 1 (NFT)
    - Asset name, unit name, metadata link (e.g., IPFS)
    - Zero decimals (indivisible)

- ✅ **List Book for Sale**
  - After creating the NFT, the author lists it for sale by deploying the smart contract using `create_application(asset_id, price)`.

- ✅ **Opt-In to Asset**
  - The smart contract can opt-in to hold the NFT before sales begin.

- ✅ **Buy Book (NFT)**
  - Buyers pay in ALGO and receive the NFT directly via the `buy()` function in the smart contract.

- ✅ **Close Sale**
  - Authors can delete the contract, reclaim unsold NFTs and earned ALGO via `delete_application()`.

---

## 🔗 Workflow

1. **NFT Creation (Frontend)**  
   The author uploads a book and metadata. The frontend uses `algosdk` to call a `createNFT()` function that mints an ASA with a total supply of 1.

2. **Smart Contract Deployment**  
   The NFT’s asset ID is passed to the smart contract’s `create_application(asset_id, unitary_price)` method.

3. **Opt-In to the Asset**  
   The contract opts in to hold and sell the book NFT using `opt_in_to_asset()`.

4. **Purchase**  
   Buyers interact with the `buy()` method, pay the specified amount in ALGO, and receive the NFT.

5. **Close & Reclaim**  
   When the sale is over, the author can close the contract with `delete_application()` to recover all remaining assets.

---

## 💻 Technologies Used

| Layer          | Technology                         |
|----------------|------------------------------------|
| Blockchain     | [Algorand](https://www.algorand.com/) |
| Smart Contract | [`algopy`](https://github.com/algorandfoundation/algopy) |
| ABI Interface  | ARC4                               |
| NFT Minting    | [`algosdk`](https://github.com/algorand/js-algorand-sdk) (frontend) |
| Wallets        | MyAlgo Wallet / AlgoSigner         |
| Storage        | IPFS / Pinata (for book files)     |

---

## 📂 Project Structure

```
/contracts
  └── DigitalMarket.py         # ARC4 smart contract code
/frontend
  └── createNFT.js             # Function to mint ASA (NFT)
  └── App.js                   # UI for uploading books and interacting with the contract
```

---

## 🧠 Smart Contract Functions

| Function | Description |
|---------|-------------|
| `create_application(asset_id, unitary_price)` | Initialize the marketplace app for a book NFT |
| `set_price(new_price)` | Update the unit price |
| `opt_in_to_asset()` | Smart contract opts in to receive the NFT |
| `buy(payment_txn, quantity)` | Buyer sends ALGO and receives the book NFT |
| `delete_application()` | Author deletes the contract and reclaims funds and unsold NFTs |

---

## 🛠 Prerequisites

- Python + Algopy installed for contract deployment
- Node.js + algosdk for frontend
- Testnet ALGO from [Algorand Faucet](https://bank.testnet.algorand.network/)
- Wallet setup (MyAlgo, AlgoSigner, or PeraWallet)

---

## 📦 Installation & Setup

```bash
# Install dependencies for frontend
cd frontend
npm install

# Install Algopy for contract
pip install algopy
```

---

## 📌 Future Improvements

- User dashboards for buyers and sellers
- Search and filter by genre or price
- Royalty support for secondary sales
- Add metadata standards (ARC3, ARC69)
- Secure file delivery post-purchase

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ✨ Authors

- **Srikarnivas** – Full-stack Developer, AlgoRack Creator  
- Connect: [srikarnivas.24@gmail.com](mailto:srikarnivas.24@gmail.com)

---

## 💡 Inspiration

This project combines the speed of Algorand with the rising demand for digital collectibles and eBooks, enabling authors to earn fairly and transparently through decentralized distribution.
