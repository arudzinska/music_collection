"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import AlbumForm
from app.models import Album
# import sqlite3

###
# Routing for your application.
###

@app.route('/')
def root():
    """Render website's home page."""
    return render_template('root.html')


# @app.route('/about/')
# def about():
#     """Render the website's about page."""
#     return render_template('about.html', name="Mary Jane")

@app.route('/albums', methods=['POST', 'GET'])
# def show_albums():
#     albums = db.session.query(Album).all() # or you could have used User.query.all()
#
#     return render_template('show_albums.html', albums=albums)

###########################################################################################
def show_albums():
    album = AlbumForm()
    albums = db.session.query(Album).all()  # or you could have used User.query.all()

    if request.method == 'POST':
        if album.validate_on_submit():
            # Get validated data from form
            artist = album.artist.data # You could also have used request.form['name']
            name = album.name.data # You could also have used request.form['email']
            release_date = album.release_date.data

            # save user to database
            new_album = Album(artist, name, release_date)
            db.session.add(new_album)
            db.session.commit()

            flash('Album successfully added')
            return render_template('show_albums.html', albums=albums)
    return render_template('show_albums.html', albums=albums)

# @app.route('/add-user', methods=['POST', 'GET'])
# def add_user():
#     user_form = UserForm()
#
#     if request.method == 'POST':
#         if user_form.validate_on_submit():
#             # Get validated data from form
#             name = user_form.name.data # You could also have used request.form['name']
#             email = user_form.email.data # You could also have used request.form['email']
#
#             # save user to database
#             user = User(name, email)
#             db.session.add(user)
#             db.session.commit()
#
#             flash('User successfully added')
#             return redirect(url_for('show_users'))
#
#     flash_errors(user_form)
#     return render_template('add_user.html', form=user_form)

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))

###
# The functions below should be applicable to all Flask apps.
###

# @app.route('/<file_name>.txt')
# def send_text_file(file_name):
#     """Send your static text file."""
#     file_dot_text = file_name + '.txt'
#     return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
