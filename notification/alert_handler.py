import os
import base64
import boto3
import gzip
import json
import logging
import os

from botocore.exceptions import ClientError
from template import Template

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def getBatchId(ERROR_MESSAGE):
    ERROR_MESSAGE = ERROR_MESSAGE.replace("\n","")

    if  ERROR_MESSAGE.find("BatchId") != -1:
        searchWord = ERROR_MESSAGE.find("BatchId")
        lengthWord = len(ERROR_MESSAGE)

        ERROR_MESSAGE = ERROR_MESSAGE[searchWord:lengthWord]
        ERROR_MESSAGE = ERROR_MESSAGE.replace("'", "")
        ERROR_MESSAGE = ERROR_MESSAGE.replace(",", "")
        ERROR_MESSAGE = ERROR_MESSAGE.replace("]", "")
        ERROR_MESSAGE = ERROR_MESSAGE.replace("BatchId:", "")
        return ERROR_MESSAGE
    else:
        return ''

def logpayload(event):
    logger.setLevel(logging.DEBUG)
    logger.debug(event['awslogs']['data'])
    compressed_payload = base64.b64decode(event['awslogs']['data'])
    uncompressed_payload = gzip.decompress(compressed_payload)
    log_payload = json.loads(uncompressed_payload)
    return log_payload


def error_details(payload):
    error_msg = ""
    log_events = payload['logEvents']
    logger.debug(payload)
    loggroup = payload['logGroup']
    logstream = payload['logStream']
    lambda_func_name = loggroup.split('/')
    logger.debug(f'LogGroup: {loggroup}')
    logger.debug(f'Logstream: {logstream}')
    logger.debug(f'Function name: {lambda_func_name[3]}')
    logger.debug(log_events)
    for log_event in log_events:
        error_msg += log_event['message']
    logger.debug('Message: %s' % error_msg.split("\n"))
    return loggroup, logstream, error_msg, lambda_func_name


def publish_message_sns(loggroup, logstream, error_msg, lambda_func_name):
    sns_arn = os.environ['snsARN']  # Getting the SNS Topic ARN passed in by the environment variables.

    snsclient = boto3.client('sns')
    try:
        message = ""
        message += "\nLambda error  summary" + "\n\n"
        message += "##########################################################\n"
        message += "# LogGroup Name:- " + str(loggroup) + "\n"
        message += "# LogStream:- " + str(logstream) + "\n"
        message += "# Log Message:- " + "\n"
        message += "# \t\t" + str(error_msg.split("\n")) + "\n"
        message += "##########################################################\n"

        # Sending the notification...
        snsclient.publish(
            TargetArn=sns_arn,
            Subject=f'Execution error for Lambda - {lambda_func_name[3]}',
            Message=message
        )
    except ClientError as e:
        logger.error("An error occured: %s" % e)

def publish_message_ses(loggroup, logstream, error_msg, lambda_func_name, templateType):
    # The character encoding for the email.
    CHARSET = "UTF-8"
    RECIPIENT = os.environ['RECIPIENT_ALERT']
    SENDER = os.environ['SENDER_ALERT']
    SUBJECT = f'Execution error for Lambda - {lambda_func_name[3]}'
    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Lambda error  \r\n"
                " error "
                " summary "
                )

    logger.info("Message-Error-22: %s" % str(error_msg.split("\n")))

    ERROR_MESSAGE = str(error_msg.split("\n"))
    # BATCH_ID = getBatchId(ERROR_MESSAGE)

    BODY_HTML_TEMPLATE = ""
    templateMail = Template(templateType)
    if templateType == 'Price':        
        BODY_HTML_TEMPLATE = templateMail.getHtmlMailBrandliveRed(ERROR_MESSAGE)
    elif templateType == 'Inventory':
        BODY_HTML_TEMPLATE = templateMail.getHtmlMailBrandliveGray(ERROR_MESSAGE)
    else :
        BODY_HTML_TEMPLATE = templateMail.getHtmlMailInfracommerceCherry(ERROR_MESSAGE)

    # BODY_HTML_TEMPLATE = Template. (123459789, ERROR_MESSAGE)

    sesclient = boto3.client('ses')
    try:
        # Sending the notification...
        sesclient.send_email(
            Source=SENDER,
            Destination={
                'ToAddresses': [
                    RECIPIENT
                   ],
                },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML_TEMPLATE,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
        )

    except ClientError as e:
        logger.error("An error occured: %s" % e)
    else:
        logger.info("Email sent!")


def user_scan_log(event, context):
    logger.info("user_scan_log event")
    pload = logpayload(event)
    lgroup, lstream, errmessage, lambdaname = error_details(pload)
    publish_message_ses(lgroup, lstream, errmessage, lambdaname, "Inventory")

def profile_scan_log(event, context):
    logger.info("profile_scan_log event")
    pload = logpayload(event)
    lgroup, lstream, errmessage, lambdaname = error_details(pload)
    publish_message_ses(lgroup, lstream, errmessage, lambdaname, "Price")

# def orders_hook_scan_log(event, context):
#     logger.info("orders_hook_scan_log event")
#     pload = logpayload(event)
#     lgroup, lstream, errmessage, lambdaname = error_details(pload)
#     publish_message_ses(lgroup, lstream, errmessage, lambdaname, "Order")