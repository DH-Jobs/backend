from flask import Flask

app = Flask(__name__)
app.debug = True
import src.adapters.middlewares.UsersMiddleware
import src.adapters.routers.User
