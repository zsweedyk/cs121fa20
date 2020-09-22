from app import app

@app.route('/')
@app.route('/index')
def index():
	return "Hello, CS121 World!"
