import os

#backend here
# no no touch sa accounts.txt

class UserAccount:
    def __init__(self, filename="accounts.txt"):
        self.filename = filename
        self.accounts = {}
        self.current_user = None

        self.create_file() 
        self.load_accounts()

    def create_file(self):
        if not os.path.exists(self.filename):
            open(self.filename, "w").close()

    def load_accounts(self):
        with open(self.filename, "r") as f:
            for line in f:
                u, p = line.strip().split(",")
                self.accounts[u] = p

    def save_account(self, username, password):
        with open(self.filename, "a") as f:
            f.write(f"{username},{password}\n")

    def register(self, username, password):
        if len(password) < 6:
            return "Password should be at least 6 characters"
        if username in self.accounts:
            return "User already exists"

        self.accounts[username] = password
        self.save_account(username, password)
        return "Registration successful"

    def login(self, username, password):
        if username in self.accounts and self.accounts[username] == password:
            self.current_user = username
            return "Login successful"
        elif username in self.accounts:
            return "Wrong password"
        else:
            return "User not found"

