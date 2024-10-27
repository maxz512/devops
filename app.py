from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Adjust region if needed
table = dynamodb.Table('Patients')

@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.json
    table.put_item(Item={
        'patient_id': data['id'],
        'name': data['name'],
        'age': data['age'],
        'diagnosis': data['diagnosis']
    })
    return jsonify({"message": "Patient added!"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
