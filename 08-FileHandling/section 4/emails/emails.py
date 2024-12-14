import re

def email_sender(email_text):
    match = re.search(r'From:\s*([^<]+<(\S+@\S+)>)', email_text)
    if match:
        return match.group(1)
    return None

def email_recipient(email_text):
    match = re.search(r'To:\s*([^<]+<(\S+@\S+)>)', email_text)
    if match:
        return match.group(1)
    return None

def email_title(email_text):
    match = re.search(r'Subject:\s*(.*)', email_text)
    if match:
        return match.group(1)
    return None

def email_body(email_text):
    match = re.search(r'\r?\n\r?\n(.*)', email_text, re.DOTALL)
    if match:
        return match.group(1)
    return None