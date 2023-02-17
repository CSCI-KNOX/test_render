from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
  
# test route to show prefix settings
@app.route('/prefix_url')  
def prefix_url():
    return 'The URL for this page is {}'.format(url_for('prefix_url'))

###############################################################################
## Required Routes from Flask Tutorial for Lab include:
##     1. static text page, "index"   @app.route('/')
##     2. static text page, "hello"   @app.route('/hello')
##     3. static text page, "project" @app.route('/projects/')
##     4. static text page, "about"   @app.route('/about')
##     5. dynamic text, route parameter, string  @app.route('/user/<username>')
##     6. dynamic text, route parameter, int     @app.route('/post/<int:post_id>')
##     7. dynamic text, route parameter, subpath @app.route('/path/<path:subpath>')
##
## Place your required routes here
##

###############################################################################
## Place your optional routes here
