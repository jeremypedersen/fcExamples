import logging
import os

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
  # Write auth and cleanup shellscripts to disk, for use
  # in subsequent call to certbot
  #
  auth = '''
#!/bin/bash

echo "============ BEGIN AUTH OUTPUT ============="
echo $CERTBOT_DOMAIN
echo $CERTBOT_VALIDATION
echo $CERTBOT_TOKEN
echo "============ END AUTH OUTPUT ============="
  '''

  try:
    f = open('auth.sh', 'w')
    f.write(auth)
    f.close()
  except:
    response = 'ERROR: Failed to write auth script to local environment in FC'
    return response

  cleanup = '''
#!/bin/bash

echo "============ BEGIN CLEANUP OUTPUT ============="
echo $CERTBOT_AUTH_OUTPUT
echo "============ END CLEANUP OUTPUT ============="
  '''

  try:
    f = open('cleanup.sh', 'w')
    f.write(cleanup)
    f.close()
  except:
    response = 'ERROR: Failed to write cleanup script to local environment in FC'
    return response

  #
  # Make shellscripts executable
  # 
  os.system('chmod ugo+x auth.sh')
  os.system('chmod ugo+x cleanup.sh')

  #
  # Make call to certbot
  # 
  certCommand = '''
  certbot certonly --manual --preferred-challenges http --agree-tos --manual-public-ip-logging-ok --config-dir . --work-dir . --logs-dir . -n --manual-auth-hook ./auth.sh --manual-cleanup-hook ./cleanup.sh -m dummyemail@dummy.com -d somedomain.com --dry-run
  '''
  os.system(certCommand)

  #
  # Send certbot log file to Log Service
  #
  try:
    f = open('letsencrypt.log', 'r')
    raw_logs = f.read()
    f.close()
    logger.info(raw_logs)
  except:
    response = 'Function completed, but unable to write letsencrypt.log out to log service'
    return response

  return 'Certificate renewal complete! Check logs for details'
