from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import AlbumForm
from app.models import Album


@app.route('/')
def root():
    return render_template('root.html')


@app.route('/albums', methods=['GET', 'POST'])
def show_albums():

    album_form = AlbumForm()

    if request.method == 'POST':
        if album_form.validate_on_submit():
            artist = album_form.artist.data
            name = album_form.name.data
            release_date = album_form.release_date.data

            # dumping data to the database
            album = Album(artist, name, release_date)
            db.session.add(album)
            db.session.commit()

            flash('Album successfully added')
            return redirect(url_for('show_albums'))

    albums = db.session.query(Album).all()

    flash_errors(album_form)
    return render_template('show_albums.html', form=album_form, albums=albums)


@app.route('/albums/<int:id>', methods=['GET', 'DELETE'])
def describe(id):

    album = Album.query.get(id)

    if request.method == 'DELETE':
        Album.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect(url_for('show_albums'))

    return render_template('describe_album.html', album=album)


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="127.0.0.1",port="8080")
