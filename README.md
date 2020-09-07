# Stock price tracker
Tracking stock price of interest in real time. Unike web applications, refreshing happens often and no input is ever required. Application is for a raspberry pi feeding data into a led matrix display that can be installed anywhere within the house.

### 3rd party dependencies:
- [dotenv](https://pypi.org/project/python-dotenv/)

### To generate token:
Go to [Finnhub](https://finnhub.io/) and sign up with an account. Doing so will generate a token for generating api calls. Include this in an .env file within the same foloder using the following structure:

> FINNHUB_TOKEN=yourToken

### TODOs:
- switch over to webhooks to avoid api calls overhead and get real time results
- include alarm triggers for breakpoints (ie min/max target values)
- add integration with led matrix display and raspberry pi