#!/usr/bin/env python3
"""
Small CLI-tool that removes reserved Twilio.com phone numbers in batch mode
"""
import os
import sys
import time
import twilio
import traceback
from twilio.rest import Client

__author__ = 'Oleksandr Tsurenko (tsurenko@gmail.com)'
__version__ = '0.1'


def main():
    twilio_account_sid = os.environ['twilio_account_sid']
    twilio_auth_token = os.environ['twilio_auth_token']

    try:
        client = Client(twilio_account_sid, twilio_auth_token)
        numbers = client.incoming_phone_numbers.list()
    except twilio.base.exceptions.TwilioException as e:
        raise NameError('Twillio fatal error: "%s"' % getattr(e, 'message', repr(e)))

    if len(numbers) > 0:
        print("""
!!! WARNING WARNING WARNING!!!
====================================================
In 60 seconds I'm going to delete %s phone number(s).
Ctrl/Cmd+C if you want to cancel the removal process")
====================================================
""" % (len(numbers)))
        time.sleep(60)

        for number in numbers:
            print(number.phone_number, "has been successfully deleted" if number.delete() else "!!! can't delete")
    else:
        print("No phone numbers to delete")

    print("Done")


if __name__ == '__main__':
    try:
        main()
        sys.exit(0)

    except KeyboardInterrupt as e:
        raise e

    except SystemExit as e:
        raise e

    except Exception as e:
        print('ERROR, UNEXPECTED EXCEPTION')
        print(getattr(e, 'message', repr(e)))
        traceback.print_exc()
        sys.exit(1)
