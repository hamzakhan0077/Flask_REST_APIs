
from REST_APIs import app




if __name__ == "__main__":
    with app.app_context():
        app.run(host="0.0.0.0",port=5000,debug=True,use_reloader = True)