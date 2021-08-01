from .models import Tenant
from requests.structures import CaseInsensitiveDict
import requests
import africastalking

# Initialize SDK
username = "sandbox"    
api_key = "YOUR API KEY" 
africastalking.initialize(username, api_key)

sms = africastalking.SMS

def send_reminders():
    tenants=Tenant.objects.all()
    for tenant in tenants:
        invoice_message=f'Hello, {tenant.name}, your rent payment of shs 10,000 is due on demand. Please plan to pay before 5th.'
        response =sms.send(invoice_message, [str(tenant.phone)]) 
        print(response)
