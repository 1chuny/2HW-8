import mongoengine as me

me.connect('contacts_db')

class Contact(me.Document):
    full_name = me.StringField(required=True)
    email = me.EmailField(required=True)
    email_sent = me.BooleanField(default=False)
    additional_info = me.StringField()

    def __str__(self):
        return f"{self.full_name} <{self.email}>"