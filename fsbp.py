import configparser

"""
Required Input

If the bill you have from your foreign provider is not fully itemized, please
provide the following information with your claim. Please try not to write
information on the bill.

Patient name
Subscriber ID number
Provider name and address
Dates of service
Diagnosis or a description of your symptoms (not required for prescription medicine receipts)
A brief description of each service or supply
Charge for each service or supply


For massages:

Here are some general tips regarding the submission of massage claims.
The following information is needed:
• Patient’s name and
• Patient’s date of birth
• Patient’s ID number
• Provider/Massage Therapist
name, address, and
license or certification number
(where applicable)
• Date of each service
• Description of service rendered
• Cost for each service
• Federal Tax identification
number, if
available (for providers in the
United States)
Note: If you paid for the services, please provide your paid receipt. 


"""

# import configuration variables
config = configparser.ConfigParser()
config.read('.env')
account = {}
account['member_name'] = config.get('ACCOUNT','MEMBER_NAME')
account['member_email'] = config.get('ACCOUNT','MEMBER_EMAIL')
account['member_id_number'] = config.get('ACCOUNT','MEMBER_ID_NUMBER')
account['member_no_dependents'] = config.get('ACCOUNT','MEMBER_NO_DEPENDENTS')
for i in range(int(account['member_no_dependents'])):
    account['dependent_'+str(i+1)+'_name'] = config.get('ACCOUNT','DEPENDENT_'+str(i+1)+'_NAME')

print(account)