from flask import Flask, request, jsonify

app = Flask(__name__)

workAccount = [
	{
		'id': '001',
		'name':{
			'firstName': 'jon',
			'lastName': 'doe'
		}
	}
]

@app.route('/workAccount')
def get_accounts():
	return jsonify({'workAccount': workAccount})

@app.route('/workAccount/<string:id>')
def get_account(id):
	for account in workAccount:
		if account['id'] == id:
			return jsonify(account)
	return jsonify({'message': 'Account not found'})

@app.route('/workAccount/<string:id>/name')
def get_account_name(id):
	for account in workAccount:
		if account['id'] == id:
			return jsonify({'name': account['name']})
	return jsonify({'message': 'Account not found'})

@app.route('/workAccount', methods=['POST'])
def create_work_account():
	request_data = request.get_json()
	new_account = {
		'id': request_data['id'],
		'name': {}
	}
	workAccount.append(new_account)
	return jsonify(new_account)

@app.route('/workAccount/<string:id>/name', methods=['POST'])
def create_name_in_work_account(id):
	request_data = request.get_json()
	for account in workAccount:
		if account['id'] == id:
			new_name = {
				'firstName': request_data['firstName'],
				'lastName': request_data['lastName']
			}
			account['name'] = new_name
			return jsonify(new_name)
	return jsonify({'message': 'Account not found'})
	

app.run(port=5000)