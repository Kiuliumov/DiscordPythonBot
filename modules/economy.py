import json
class Economy:
    async def add_coins(user_id, coins_to_add):
    
     with open('bank.json', 'r') as f:
        users = json.load(f)
        users[str(user_id)]['bank'] += coins_to_add
     with open('bank.json', 'w') as f:
        json.dump(users, f, indent=2)
     return users[str(user_id)]['bank']
    
    async def open_account(user_id):
     with open('bank.json', 'r') as f:
        users = json.load(f)

     if str(user_id) in users:
        return False
     else:
        users[str(user_id)] = {'bank': 500}

     with open('bank.json', 'w') as f:
        json.dump(users, f)
     return True
    
    async def get_bank_data():
     with open('bank.json', 'r') as f:
        users = json.load(f)
     return users