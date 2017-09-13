# facebook/views/profile.py

from flask import Blueprint, render_template, jsonify, request
import paypalrestsdk
import logging
import config

paypalrestsdk.configure(**config.PAYPAL)

paypal_payment = Blueprint('paypal_payment', __name__, url_prefix='/api/paypal')

@paypal_payment.route('/payment/create', methods=["GET"])
def create():
    # Do some stuff
  payment = paypalrestsdk.Payment({
      "intent": "sale",
      "payer": {
          "payment_method": "paypal"},
      "redirect_urls": {
          "return_url": "http://localhost:3000/payment",
          "cancel_url": "http://localhost:3000/"},
      "transactions": [{
          "item_list": {
              "items": [{
                  "name": "item",
                  "sku": "item",
                  "price": "5.00",
                  "currency": "USD",
                  "quantity": 1}]},
          "amount": {
              "total": "5.00",
              "currency": "USD"},
          "description": "This is the payment transaction description."}]})

  if payment.create():
    return jsonify("Payment created successfully")
  else:
    return jsonify(payment.error)
    


@paypal_payment.route('/payment/execute', methods=["POST"])
def execute():
  payment_id = request.args.get('payment_id')
  payer_id = request.args.get('payer_id')

  payment = paypalrestsdk.Payment.find(payment_id)

  if payment.execute({"payer_id": payer_id}):
    return jsonify("Payment execute successfully")
  else:
    return jsonify(payment.error) # Error Hash
  