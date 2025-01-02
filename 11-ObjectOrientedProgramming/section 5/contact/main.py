from contact_list import ContactList

# John Brown     brown@onet.pl       555234000
# Anna May   	   am@o2.pl            232000199
# George Small   smallg@google.pl    222999100
# Paola Big      bigpaola@poczta.pl  100200300

def main():
    contacts = ContactList()
    
    contacts.add_contact("John Brown", "brown@onet.pl", "555234000")
    contacts.add_contact("Anna May", "am@o2.pl", "232000199")
    contacts.add_contact("George Small", "smallg@google.pl", "222999100")
    contacts.add_contact("Paola Big", "bigpaola@poczta.pl", "100200300")
    
    contacts.display_all()
    
    print("\nSearching for Anna May:")
    contact = contacts.find_contact("Anna May")
    if contact:
        contact.display_info()
    
    print("\nRemoving George Small...")
    contacts.remove_contact("George Small")
    
    contacts.display_all()

if __name__ == "__main__":
    main()