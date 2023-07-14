from REST_APIs import db
Model = db.Model


class Customer(Model):
    id = db.Column(db.Integer,unique = True, nullable=False,primary_key = True,autoincrement=True)
    name = db.Column(db.String(100), nullable=False,default='')
    email = db.Column(db.String(100), nullable=False,default='')
    note = db.Column(db.String(100),nullable=False,default='')

    def __repr__(self):
        return f"Customer({self.id}, {self.name},{self.email},{self.note})"