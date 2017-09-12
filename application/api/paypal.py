# facebook/views/profile.py

from flask import Blueprint, render_template
import paypalrestsdk
import logging
import config

paypalrestsdk.configure({
  "mode": config.PAYPAL_MODE, # sandbox or live
  "client_id": config.PAYPAL_CLIENT_ID,
  "client_secret": config.PAYPAL_CLIENT_SECRET })

paypal = Blueprint('paypal', __name__)

@paypal.route('/payment/create')
def create():
    # Do some stuff
  payment = paypalrestsdk.Payment({
      "intent": "sale",
      "payer": {
          "payment_method": "paypal"},
      "redirect_urls": {
          "return_url": "http://localhost:3000/payment/execute",
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
    logging.info("Payment created successfully")
  else:
    logging.info(payment.error)
    


@paypal.route('/payment/execute')
def about(user_url_slug):
    # Do some stuff
    return render_template('profile/about.html')