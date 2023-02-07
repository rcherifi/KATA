from flask import Flask, request, jsonify
import bank_app

app = Flask(__name__)

@app.route('/api/v1/create_account', methods=['POST'])
def create_account_route():
    name = request.json['name']
    balance = request.json['balance']
    account_id = bank_app.create_account(name, balance)
    if account_id is None:
        return "Account could not be created", 500
    return jsonify({'account_id': account_id}), 201


@app.route('/api/v1/deposit', methods=['POST'])
def deposit_route():
    account_id = request.json['account_id']
    amount = request.json['amount']
    success = bank_app.deposit(account_id, amount)
    if not success:
        return "Deposit could not be made", 500
    return jsonify({'message': 'Deposit successful'}), 200

@app.route('/api/v1/retrieve_account', methods=['GET'])
def retrieve_account_route():
    account_id = request.args.get('account_id')
    if account_id is None:
        return "Missing account_id parameter", 400
    account = bank_app.retrieve_account(account_id)
    if account is None:
        return "Account not found", 404
    return jsonify(account), 200

if __name__ == '__main__':
    app.run(debug=True)
