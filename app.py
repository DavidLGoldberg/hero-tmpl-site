import os
from flask import Flask
from werkzeug import SharedDataMiddleware

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__,
            static_folder=os.path.join(PROJECT_ROOT, 'public'),
            static_url_path='/public')

app.wsgi_app = SharedDataMiddleware(app.wsgi_app, 
    {'/': os.path.join(os.path.dirname(__file__), 'public') })

#Routes:
#====================================
@app.route('/index.html')
@app.route('/', alias=True)
def index(): pass


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
