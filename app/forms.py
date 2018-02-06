from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class AlbumForm(FlaskForm):
    artist = StringField('Artist name', validators=[InputRequired()])
    name = StringField('Album name', validators=[InputRequired()])
    release_date = StringField('Release date', validators=[InputRequired()])
