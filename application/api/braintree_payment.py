# facebook/views/profile.py

from flask import Blueprint, render_template, jsonify, request
import braintree
import logging
import config

mode = braintree.Environment.Sandbox if config.PAYMENT_MODE == 'sandbox' else braintree.Environment.Production
braintree.Configuration.configure(
  mode, **config.BRAINTREE)

braintree_payment = Blueprint('braintree_payment', __name__, url_prefix='/api/braintree')

@braintree_payment.route('/payment/create', methods=["GET"])
def create():
  return braintree.ClientToken.generate()


@braintree_payment.route('/payment/execute', methods=["GET"])
def execute():
    # Do some stuff
  # test nonce: fake-valid-nonce  
  nonce_from_the_client = request.args.get("payment_method_nonce")

  result = braintree.Transaction.sale({
    "amount": "10.00",
    "payment_method_nonce": nonce_from_the_client,
    "options": {
      "submit_for_settlement": True
    }
  })
  if result.is_success or result.transaction:
    return jsonify(result.transaction.id)
  else:
    x = result.errors.deep_errors[0]
    raise Exception('Error: %s: %s' % (x.code, x.message))
  #   raise result.errors.deep_errors
  #     for x in result.errors.deep_errors: flash('Error: %s: %s' % (x.code, x.message))
  #     return redirect(url_for('new_checkout'))
  # return jsonify(result.transaction.id)
