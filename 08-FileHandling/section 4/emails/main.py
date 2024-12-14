import emails

with open('email.txt', 'r', encoding='utf-8') as file:
    email_text = file.read()

print('Email sender:', emails.email_sender(email_text))
print('Email recipient:', emails.email_recipient(email_text))
print('Email title:', emails.email_title(email_text))
print('Email body:', emails.email_body(email_text))