# Advanced Bank Account Management System 🏦

A professional backend Python application built to demonstrate advanced **Object-Oriented Programming (OOP)** concepts, specifically focusing on **Encapsulation** and **Object Interaction**.

## 🚀 Key Features
* **Data Encapsulation:** Secures the account balance using private variables (`__balance`), preventing direct external modification.
* **Transaction History:** Automatically tracks and records every deposit, withdrawal, and transfer in a dynamic history list.
* **Money Transfers:** Allows secure fund transfers between two completely separate `BankAccount` objects, reusing existing withdrawal and deposit methods.
* **Auto-Generated Accounts:** Automatically generates a unique 5-digit account number upon instantiation.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Core Concepts:** OOP, Encapsulation, Method Overloading (Concept), Code Reusability.

## 💻 How to Run
1. Clone this repository to your local machine.
2. Open your terminal or command prompt.
3. Run the following command:
   ```bash
   python bank_system.py

📊 Sample Output
Vimukthi account eke balance ek Rs:5000
Sade account eke balance ek Rs:1000

--- Transactions ---
Vimukthi Rs : 5000 k thenpath kara. Den balace eka:10000
Vimukthi Acconut eken Rs:6000 withdraw kara. den thiayana balance eka Rs:4000
Vimukthi account eke balance ek Rs:4000

--- Transfer Money ---
Vimukthi Acconut eken Rs:3000 withdraw kara. den thiayana balance eka Rs:1000
Sade Rs : 3000 k thenpath kara. Den balace eka:4000

transaction History | Vimukthi |
- Vimukthi account created with initial balance:  Rs: 5000
- Deposit amount Rs:5000
- Withdraw Rs:6000
- Withdraw Rs:3000
- Transferred Rs:3000 to Sade
