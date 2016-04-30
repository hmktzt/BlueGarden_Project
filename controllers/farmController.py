from flask import request, render_template, redirect, url_for, flash, session
from models.user import *
from models.works import *
from models.farm import *
#from models.produce import *
from models.address import *

class FarmController:
 
    @staticmethod
    def farms_view():
        errors = []
        myfarms = []
        user = User.query.get(User.query.filter_by(email=session['email']).first().id)
        
        if user.type == 'C':
            for farm in Works.query.filter_by(user_id=user.id).all():
                myfarms.append(Farm.query.get(farm.farm_id).name)


        if request.method == 'POST':
            name = request.form.get('name', '')
            address1 = request.form.get('address1', '')
            address2 = request.form.get('address2', '')
            city = request.form.get('city', '')
            state = request.form.get('state', '')
            country = request.form.get('country', '')
            postcode = request.form.get('postcode', '')
            
            #add farm address:
            address = Address(address1,address2,city,state,country,postcode)
            db.session.add(address)
            db.session.commit()
            #add new farm:
            address_id = db.session.query(Address).order_by(Address.id.desc()).first().id
            farm = Farm(name,address_id)
            db.session.add(farm)
            db.session.commit()
            #add farm worker and change user type flag:
            farm_id = db.session.query(Farm).order_by(Farm.id.desc()).first().id
            db.session.add(Works(user.id,farm_id))
            User.set_user_farmer(user)
            db.session.commit()
            return redirect(url_for('sell'))
        else:
            errors.append("You dont have any farms yet. Please add a farm.")
            return render_template("sell.html", errors=errors, myfarms=myfarms)
            
        return render_template("sell.html", errors=errors, myfarms=myfarms)    
        
