[![Python 3.7](https://img.shields.io/badge/Python-3.6-blue.svg)](https://www.python.org/downloads/release/python-374/)

# BestBuy Price Alert

Script that emails price alerts for a given item(s) on Bestbuy.com using Bestbuy API



#### Usage

- Script can be deployed on a Raspberry Pi 
  - User can setup `cronjob` to run every hour to check for price
  - Uses `SendGrid` to send the email alerts
  - Can use `.env` or system defined environment variables



##### The script requires the following environment variables

| Environment Variable Name | Example             | Notes                                                        |
| ------------------------- | ------------------- | ------------------------------------------------------------ |
| SKUS                      | 5706672, 5543401    | Bestbuy product SKUs as a comma separated list               |
| BESTBUY_KEY               | *API key*           | Bestbuy API key *get one from Bestbuy developer portal*      |
| MAX_PRICE                 | 399.00              | Price that will trigger the alert email                      |
| EMAIL_FROM                | example@example.com | The email sender for the alert email                         |
| EMAIL_TO                  | example@example.com | The email that will receive the price alert. Can be a comma separated list of emails |
| EMAIL_NAME                | BestBuy Price Alert | Name that will appear as senders name in your inbox          |
| SENDGRID_API_KEY          | *API key*           | API key from [SendGrid](https://sendgrid.com/)               |

