import mongoengine as me

me.connect(host="mongodb+srv://koufeed:bqgxVc8aP2o8Juiy@cluster0.tti5h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

class Author(me.Document):
    fullname = me.StringField(required=True)
    born_date = me.StringField()
    born_location = me.StringField()
    description = me.StringField()

    def __str__(self):
        return self.fullname

class Quote(me.Document):
    tags = me.ListField(me.StringField())
    author = me.ReferenceField(Author, reverse_delete_rule=me.CASCADE)
    quote = me.StringField(required=True)

    def __str__(self):
        return self.quote