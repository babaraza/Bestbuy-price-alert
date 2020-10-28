from utilities.mail import send_mail
from dotenv import load_dotenv
import requests
import os

load_dotenv()


class Product:
    """
    Class to hold the product data for each product result
    """

    def __init__(self, title, image, product_link_api, product_link, cart_link, price):
        self.title = title
        self.image = image
        self.product_api = product_link_api
        self.link = product_link
        self.cart = cart_link
        self.price = price

    def create_link(self):
        """
        Returns the formatted url for Product link
        """
        return f"<a href='{self.link}'>Link</a>"

    def add_to_cart(self):
        """
        Returns the formatted url for Add to Cart link
        """
        return f"<a href='{self.cart}'>Add to Cart</a>"


skus = os.getenv('SKUS')
api_url = f'https://api.bestbuy.com/beta/products/openBox(sku%20in({skus}))'
headers = {'Content-Type': 'application/json'}
params = {'apiKey': os.getenv('BESTBUY_KEY')}

# List to hold all the Product results
products = []


def get_data():
    s = requests.Session()
    r = s.get(api_url, headers=headers, params=params)

    results = r.json()

    for result in results['results']:
        prices = []
        for offer in result['offers']:
            prices.append(offer['prices']['current'])
        if min(prices) < os.getenv('MAX_PRICE'):
            product_raw = Product(title=result['names']['title'],
                                image=result['images']['standard'],
                                product_link_api=result['links']['product'],
                                product_link=result['links']['web'],
                                cart_link=result['links']['addToCart'],
                                price=min(prices))
            products.append(product_raw)


def prepare_data():
    raw_string = ''

    # Iterating over product list
    for product in products:
        raw_string += f'<tr><td><img src="{product.image}" style="width:40%;height:40%;"></td>' \
                      f'<td>{product.title}</td>' \
                      f'<td>${product.price}</td>' \
                      f'<td>{product.create_link()}</td>' \
                      f'<td>{product.add_to_cart()}</td></tr>'
    return raw_string


def prepare_email(final_string):
    # Preparing the email through SendGrid
    sender = os.getenv('EMAIL_FROM')
    recipient = os.getenv('EMAIL_TO')
    name = os.getenv('EMAIL_NAME')
    subject = 'Best Buy Deal'
    message = """
    <!DOCTYPE html>
    <html>
    
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link href="https://fonts.googleapis.com/css?family=M+PLUS+Rounded+1c:700&display=swap" rel="stylesheet">
    
        <style type="text/css">
            body, table, div {
                font-family: 'M PLUS Rounded 1c', sans-serif !important;
            }
    
            table.wrapper {
            width: 100% !important;
            table-layout: fixed;
            text-align:center; 
            }
            
            table, th, td {
              border: 1px solid black;
              border-collapse: collapse; 
            }
    
            @media screen and (max-width: 600px) {
                table, div {
                width: 100%;
                }
                body, table, div {
                color: #ffffff !important;
                }
            }
        </style>
    </head>
    
    <body>
        <div style="font-size: 22px;"> BEST BUY DEAL </div>&nbsp;&nbsp;&nbsp;
        <div>
            <table border="0" class="wrapper">
                """ + final_string + """
            </table>
        </div>
    </body>
    
    </html>
    """

    return sender, recipient, name, subject, message


if __name__ == '__main__':
    get_data()
    email_body = prepare_data()
    if email_body:
        print("Got latest prices and email sent")
        send_mail(*prepare_email(email_body))
    else:
        print("None of the results matched criteria")
