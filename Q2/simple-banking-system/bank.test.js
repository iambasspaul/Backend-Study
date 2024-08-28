const { Account, Bank } = require('./server'); // Ensure correct path

test('Account should not allow negative balance', () => {
    const account = new Account('Alice', 100);
    expect(() => account.withdraw(150)).toThrow('Insufficient balance');
});

test('Bank should create an account', () => {
    const bank = new Bank();
    bank.createAccount('Bob', 200);
    expect(bank.getAccount('Bob').balance).toBe(200);
});