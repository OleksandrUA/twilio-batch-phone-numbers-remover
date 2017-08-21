# twilio-batch-phone-numbers-remover
Small CLI-tool that removes reserved Twilio.com phone numbers in batch mode

Unfortunately Twilio doesn't allow you to remove phone numbers in batch mode using web-interface and it is getting really tough to remove all of them if you have thousands of them.
This tool deletes all incoming phone numbers reserved/linked to Twilio account.
You will have to provide Twilio credentials (Account SID and Auth Token).

## Use pre-built container from Dockerhub
```
docker pull oleksandrua/twilio-batch-phone-numbers-remover
docker run -e "twilio_account_sid=REPLACE_WITH_YOUR_TWILIO_ACCOUNT_SID" -e "twilio_auth_token=REPLACE_WITH_YOUR_TWILIO_AUTH_TOKEN" -it --rm oleksandrua/twilio-batch-phone-numbers-remover
```

## Or use image that was built locally
```
docker build -t twilio-batch-phone-numbers-remover .
docker run -e "twilio_account_sid=REPLACE_WITH_YOUR_TWILIO_ACCOUNT_SID" -e "twilio_auth_token=REPLACE_WITH_YOUR_TWILIO_AUTH_TOKEN" -it --rm twilio-batch-phone-numbers-remover
```
