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


# Form for submitting online
"""
SUBMIT A CLAIM WITHOUT COMMENTS
PLEASE SELECT THE NAME OF THE PERSON WHO THE CLAIM IS BEING FILED FOR, YEAR CLAIM WAS SERVICED AND ENTER THE CORRESPONDING FSBP MEMBER ID/LAST 4 OF THE SSN NUMBER. NEXT, BROWSE FOR THE DOCUMENT(S) YOU WISH TO UPLOAD AND CLICK "SUBMIT CLAIM" TO SEND YOUR CLAIM. NOTE: ALL PDF FILE SUBMISSIONS ARE CONVERTED TO GRAYSCALE. PLEASE MAKE SURE THE DOCUMENT UPLOADED IS IN PORTABLE DOCUMENT FORMAT (PDF).
PLEASE FILL IN ALL MANDATORY FIELDS MARKED WITH AN ASTERISK (*)

*This claim is for: 

* Service year on Claim/Invoice:  2019 (1/1/2019 - 12/31/2019 )       2018 (1/1/2018 - 12/31/2018)

*Please enter corresponding FSBP Member ID/or the last 4 of your SSN for Aetna identification: 

*Diagnosis or Reason for Visit:

*Please select the document(s) you wish to upload and click "Submit Claim" to send your claim.




*I certify the information in this claim submission is complete and accurate.
WARNING: Any intentional false statement in this application or willful misrepresentation is a violation of the law punished by a fine not more than 10,000, or imprisonment of not more than five years, or both. (18 U.S.C. 1001).
"""