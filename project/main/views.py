# project/main/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, request, flash, redirect, url_for

from forms import SignUpForm
from project import db
from project.models import UserData


################
#### config ####
################

main_blueprint = Blueprint('main', __name__,)


################
#### routes ####
################


@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    """Landing page for users to enter emails."""
    form = SignUpForm(request.form)
    if form.validate_on_submit():
        test = UserData.query.filter_by(email=form.email.data).first()
        if test:
            flash('Sorry that email aleady exists!', 'danger')
        else:
            email = UserData(email=form.email.data,name=form.name.data,phone=form.phone.data)
            db.session.add(email)
            db.session.commit()
            flash('Thank you for your interest!', 'success')
            return redirect(url_for('main.index'))
    return render_template('main/index.html', form=form)
