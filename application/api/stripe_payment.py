# facebook/views/profile.py

from flask import Blueprint, render_template, jsonify, request
import stripe
import logging
import config


stripe.api_key = config.STRIPE['api_key']
stripe.api_version = config.STRIPE['api_version']

stripe_payment = Blueprint('stripe_payment', __name__, url_prefix='/api/stripe')

@stripe_payment.route('/user/create', methods=["GET"])
def create_customer():
  user = request.args.get('user')
  customer = stripe.Customer.create(**{
    'description': 'user contact method is %s'%(user)
    })
  return jsonify(customer.id)


@stripe_payment.route('/payment/create', methods=["GET"])
def create():
    # Do some stuff
  customer_id = request.args.get('customer_id')
  key = stripe.EphemeralKey.create(customer=customer_id, api_version=VERSION)
  return jsonify(key)
    

@stripe_payment.route('/payment/execute', methods=["GET"])
def execute():
  # test token: tok_visa
  token = request.args.get('stripe_token')
  customer_id = request.args.get('customer_id', None)
  result = pay('123', 'HKD', 200, token, '123', customer_id)
  
  return jsonify(result)

def pay(tx_id, currency, amount, token, idempotency_key, customer_id=None,retries=10):

  result = None
  message = ''
  try:
    result = stripe.Charge.create(
      currency=currency, 
      amount=int(amount*100), 
      source=token,
      customer=customer_id,
      description=config.PROJECT_NAME,
      statement_descriptor=config.PROJECT_NAME,
      idempotency_key=idempotency_key,
      metadata={'transaction_id': tx_id})


  except stripe.error.CardError as e:
    # Since it's a decline, stripe.error.CardError will be caught
    body = e.json_body
    err  = body.get('error', {})
    message= u'''
            Status is: %s ,
            Type is: %s ,
            Code is: %s ,
            Param is: %s ,
            Message is: %s
          '''.format(e.http_status, err.get('type'), err.get('code'), err.get('param'), err.get('message'))
    logging.debug(message)          
    
  except stripe.error.RateLimitError as e:
    # Too many requests made to the API too quickly
    pass
  except stripe.error.InvalidRequestError as e:
    # Invalid parameters were supplied to Stripe's API
    pass
  except stripe.error.AuthenticationError as e:
    # Authentication with Stripe's API failed
    # (maybe you changed API keys recently)
    pass
  except stripe.error.APIConnectionError as e:
    # Network communication with Stripe failed
    if retries > 0:
      pay(tx_id, currency, amount, token, idempotency_key, retries=retries-1)

  except stripe.error.StripeError as e:
    # Display a very generic error to the user, and maybe send
    # yourself an email
    pass
  except Exception as e:
    # Something else happened, completely unrelated to Stripe
    pass
  else:
    logging.debug('success')
    logging.debug(result)
    return result
  logging.debug('fail stripe')

  # err = e.json_body.get('error', {})
  
  # error_type = 'STRIPE_%s' % (err.get('type').upper())
  logging.error(message or e.message)
 
  return jsonify(e)   