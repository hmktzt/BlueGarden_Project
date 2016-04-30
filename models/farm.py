from shared import db


class Farm(db.Model):
    __tablename__ = 'farms'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(255), nullable=False)
    address_id = db.Column('address_id', db.Integer, db.ForeignKey('addresses.id'), nullable=False)
    #produce_id = db.Column('produce_id', db.Integer, db.ForeignKey('produces.id'))

    def __init__(self, name, address_id):#, produce_id):
        self.name = name
        self.address_id = address_id
        #self.produce_id = produce_id