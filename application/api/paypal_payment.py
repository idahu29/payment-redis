# facebook/views/profile.py

from flask import Blueprint, render_template
import paypalrestsdk
import logging
import config

paypalrestsdk.configure({
  "mode": config.PAYPAL_MODE, # sandbox or live
  "client_id": config.PAYPAL_CLIENT_ID,
  "client_secret": config.PAYPAL_CLIENT_SECRET })

paypal = Blueprint('paypal', __name__, url_prefix='/api/paypal')

@paypal.route('/payment/create', methods=["GET"])
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
    logging.debug("Payment created successfully")
  else:
    logging.error(payment.error)
    return jsonify('ABC')
    


@paypal.route('/payment/execute', methods=["POST"])
def about(user_url_slug):
    # Do some stuff
    return render_template('profile/about.html')