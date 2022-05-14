from app.__init__ import create_app
from flask_wtf.csrf import CSRFProtect

if __name__ == "__main__":
    app = create_app()
    csrf = CSRFProtect()
    csrf.init_app(app)
    app.run(port = 4000)
