from mongoengine import Document
from mongoengine.fields import (
    BooleanField,
    StringField,
    EmailField,
)


class Contact(Document):
    fullname = StringField()
    email = EmailField()
    sent = BooleanField(default=False)
    meta = {'collection': 'contacts'}
