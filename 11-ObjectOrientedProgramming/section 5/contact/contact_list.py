from contact import Contact

class ContactList:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
    
    def remove_contact(self, name):
        contact_to_remove = self.find_contact(name)
        if contact_to_remove:
            self.contacts.remove(contact_to_remove)
            del contact_to_remove
    
    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None
    
    def display_all(self):
        if not self.contacts:
            print("No contacts found.")
            return
        
        print("\nAll Contacts:")
        print("=" * 20)
        for contact in self.contacts:
            contact.display_info()