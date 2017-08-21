# twilio-batch-phone-numbers-remover
Small CLI-tool that removes reserved Twilio.com phone numbers in batch mode

Unfortunately Twilio doesn't allow you to remove phone numbers in batch mode and it is getting really tough to remove all of them if you thousands of them

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
