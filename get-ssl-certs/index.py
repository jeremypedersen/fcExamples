import logging

# A simple Function Compute function to renew Let's Encrypt
# certificates using certbot, and bind them to an OSS bucket
def handler(event, context):

  # Get logging info
  logger = logging.getLogger()

  # Log entire raw event in case we need to do troubleshooting later
  logger.info(event)

  # Load event string
  try:
    params_raw = str(event.decode()).strip()
  except DecodeEventString:
    response = "ERROR: Failed to decode event string passed to FC"

  # Parse event JSON
  try:
    params_json = json.loads(params_raw)
  except DecodeEventJSON:
    response = "ERROR: Unable to convert event string to valid JSON"

  # TODO: Add code to perform challenge (by placing file on OSS), get certs, and subsequently install them
  
  return response