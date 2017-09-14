# facebook/views/profile.py

from flask import Blueprint, render_template, jsonify, request
import paypalrestsdk
import logging
import config
import json

paypalrestsdk.configure(**config.PAYPAL)

paypal_payment = Blueprint('paypal_payment', __name__, url_prefix='/api/paypal')

@paypal_payment.route('/payment/create', methods=["POST"])
def create():
    # Do some stuff

  data = json.loads(request.form['data'])  
  payment = paypalrestsdk.Payment({
      "intent": "sale",
      "payer": {
          "payment_method": "paypal"},
      "redirect_urls": {
          "return_url": "http://localhost:8080/",
          "cancel_url": "http://localhost:3000/"},
      "transactions": [{
          "item_list": {
              "items": data['items']},
          "amount": data['amount'],
          "description": "This is the payment transaction description."}]})
  if payment.create():
    resp = {}
    resp['paymentID'] = payment.id
    for link in payment.links:
        if link.rel == "approval_url":
          resp["approval_url"]= str(link.href)
    return jsonify(resp)
  else:
    return jsonify(payment.error)
    


@paypal_payment.route('/payment/execute', methods=["POST"])
def execute():
  payment_id = request.form['paymentID']
  payer_id = request.form['payerID']

  payment = paypalrestsdk.Payment.find(payment_id)

  if payment.execute({"payer_id": payer_id}):
    return jsonify("Payment execute successfully")
  else:
    return jsonify(payment.error) # Error Hash
  