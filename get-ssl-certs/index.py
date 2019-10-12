# Libraries for error reporting and event parsing
import logging
import json

# Libraries needed to make ACME work (so we can get our 
# nice new SSL cert)
from contextlib import contextmanager
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import OpenSSL

from acme import challenges
from acme import client
from acme import crypto_util
from acme import errors
from acme import messages
from acme import standalone
import josepy as jose

#
# Let's Encrypt SSL Certificate Handler
#
# Purpose: Create an easy way to renew SSL certificates
# bound to a static site hosted in an Alibaba Cloud OSS 
# bucket, without the need to leave a server running 
# all the time
#
# What it does:
# 1 - Create account on Let's Encrypt, and get an account key
# 2 - Generate a challenge file (HTTP-01 ACME challenge)
# 3 - Place challenge file into OSS bucket hosting our website
# 4 - Get certificate (private key, full chain)
# 5 - Install certificate
# 6 - Clean up ACME challenge files by deleting them from OSS bucket
#
# Code borrows heavily from the HTTP-01 challenge example code here:
# https://github.com/certbot/certbot/blob/master/acme/examples/http01_example.py
def handler(event, context):

  # Get logging info
  logger = logging.getLogger()

  # Log entire raw event in case we need to do troubleshooting later
  logger.info(event)

  # Load event string
  try:
    params_raw = str(event.decode()).strip()
  except:
    response = 'ERROR: Failed to decode event string passed to FC'
    return response

  # Parse event JSON
  try:
    params_json = json.loads(params_raw)
  except:
    response = 'ERROR: Unable to convert event string to valid JSON'
    return response

  # 
  # Determine whether or not a certificate has already been generated, 
  # and if yes, whether it needs to be renewed
  #

  #
  # Begin certificate challenge process
  #

  #
  # Install certificates
  #

  #
  # Remove files created by HTTP-01 challenge
  # 


  return response