const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

class Account {
    constructor(name, balance) {
        this.name = name;
        this.balance = balance;
        this.transactionLogs = [];
    }
    deposit(amount) {
        this.balance += amount;
        this.logTransaction('Deposit', amount);
    }
    withdraw(amount) {
        if (this.balance >= amount) {
            this.balance -= amount;
            this.logTransaction('Withdraw', amount);
        } else {
            throw new Error('Insufficient balance');
        }
    }
    transfer(amount, toAccount) {
        this.withdraw(amount);
        toAccount.deposit(amount);
        this.logTransaction('Transfer', amount, toAccount.name);
    }
    logTransaction(type, amount, toAccountName) {
        this.transactionLogs.push({
            type,
            amount,
            toAccountName: toAccountName || null,
            date: new Date()
        });
    }
}

class Bank {
    constructor() {
        this.accounts = {};
    }
    createAccount(name, balance) {
        let account = new Account(name, balance);
        this.accounts[name] = account;
        return account;
    }
    getAccount(name) {
        return this.accounts[name];
    }
}

const bank = new Bank();

// RESTful API endpoints

app.post('/accounts', (req, res) => {
    const { name, balance } = req.body;
    const account = bank.createAccount(name, balance);
    res.status(201).json(account);
});

app.post('/accounts/:name/deposit', (req, res) => {
    const { name } = req.params;
    const { amount } = req.body;
    const account = bank.getAccount(name);
    account.deposit(amount);
    res.json(account);
});

app.post('/accounts/:name/withdraw', (req, res) => {
    const { name } = req.params;
    const { amount } = req.body;
    const account = bank.getAccount(name);
    try {
        account.withdraw(amount);
        res.json(account);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

app.post('/accounts/:from/transfer/:to', (req, res) => {
    const { from, to } = req.params;
    const { amount } = req.body;
    const fromAccount = bank.getAccount(from);
    const toAccount = bank.getAccount(to);

    if (!fromAccount || !toAccount) {
        return res.status(404).json({ error: 'One of the accounts does not exist' });
    }

    try {
        fromAccount.transfer(amount, toAccount);
        res.json(fromAccount);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

app.get('/accounts/:name/logs', (req, res) => {
    const { name } = req.params;
    const account = bank.getAccount(name);
    res.json(account.transactionLogs);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

module.exports = { Account, Bank };