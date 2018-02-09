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

@app.route('/albums', methods=['GET', 'POST'])
def show_albums():
    album_form = AlbumForm()

    if request.method == 'POST':
        if album_form.validate_on_submit():
            # Get validated data from form
            artist = album_form.artist.data # You could also have used request.form['name']
            name = album_form.name.data # You could also have used request.form['email']
            release_date = album_form.release_date.data

            # save user to database
            album = Album(artist, name, release_date)
            db.session.add(album)
            db.session.commit()

            flash('Album successfully added')
            return redirect(url_for('show_albums'))

    albums = db.session.query(Album).all()

    flash_errors(album_form)
    return render_template('show_albums.html', form=album_form, albums=albums)

@app.route('/albums/<int:id>', methods=['GET', 'POST'])
def describe(id):
    if request.method == 'POST':
        album = Album.query.get(id)
        Album.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect(url_for('show_albums'))

    album = Album.query.get(id)
    return render_template('describe_album.html', album=album)


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
