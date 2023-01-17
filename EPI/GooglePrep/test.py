
''' Unique email addresses google interview preparation'''

def unikemails(email):
    # First we need to create a set in which we will store the unik emails
    uniqmail = set()

    for mail in email:
        # we are seprating the domain name from the local name
        name, domain = mail.split('@')

        # we need to clean the local of the + and .
        local = name.split('+')[0].replace('.', '')

        # add the email addresses to how set
        uniqmail.add(local + '@' + domain)
    return len(uniqmail)
