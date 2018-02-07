from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import InputRequired

class AlbumForm(FlaskForm):
    artist = StringField('Artist name', validators=[InputRequired()])
    name = StringField('Album name', validators=[InputRequired()])
    release_date = DateField('Release date', validators=[InputRequired()])
