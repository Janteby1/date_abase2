Next steps - 

also took a look at your couch app.  I think that it the next step, to try and add tags instead of categories and then model the db that way

"""
class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # tags have many logs
    logs = db.relationship(
        'Log',
        secondary='log_tag_link')
"""


yeah you could add a tag table to the db, and then you could presumably populate that list of checkboxes directly from the db -- this isn't necessarily better or worse, just an alternate method


two new items - 
I found out two other cool things reading up on this. The first is these Q objects, which you might find interesting 
--> https://docs.djangoproject.com/es/1.9/topics/db/queries/#complex-lookups-with-q-objects

the second is this .raw() method on the ORM 
--> https://docs.djangoproject.com/es/1.9/topics/db/sql/