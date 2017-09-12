#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paypalrestsdk
import logging
import config

paypalrestsdk.configure({
  "mode": config.PAYPAL_MODE, # sandbox or live
  "client_id": config.PAYPAL_CLIENT_ID,
  "client_secret": config.PAYPAL_CLIENT_SECRET })

def pay(payment_id, payer_id):
  payment = paypalrestsdk.Payment.find(payment_id)

  if payment.execute({"payer_id": payer_id}):
    logging.info("Payment execute successfully")
  else:
    logging.info(payment.error) # Error Hash
