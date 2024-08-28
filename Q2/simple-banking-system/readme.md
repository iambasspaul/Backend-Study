You can use tools like Postman or curl to test the API endpoints.

### **Download File**

- ** use `git clone` to download the file.


### **Example API Calls**

1. **Create an account:**
   ```bash
   curl -X POST http://localhost:3000/accounts -H "Content-Type: application/json" -d '{"name": "Alice", "balance": 100}'
   ```

2. **Deposit money:**
   ```bash
   curl -X POST http://localhost:3000/accounts/Alice/deposit -H "Content-Type: application/json" -d '{"amount": 50}'
   ```

3. **Withdraw money:**
   ```bash
   curl -X POST http://localhost:3000/accounts/Alice/withdraw -H "Content-Type: application/json" -d '{"amount": 30}'
   ```

4. **Transfer money:**
   ```bash
   curl -X POST http://localhost:3000/accounts/Alice/transfer/Bob -H "Content-Type: application/json" -d '{"amount": 50}'
   ```

5. **Get transaction logs:**
   ```bash
   curl http://localhost:3000/accounts/Alice/logs
   ```


### **Build and Run the Docker Container**

1. **Build the Docker image:**
   ```bash
   docker build -t simple-banking-system .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 3000:3000 simple-banking-system
   ```