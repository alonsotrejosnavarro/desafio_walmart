from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField
from wtforms.validators import DataRequired

class searchForm(FlaskForm):
    search = StringField('')
    submit = SubmitField('Buscar')
