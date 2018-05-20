from app import create_app

# See README.md how to run the flask app on your local computer.
# this is if you will run this one a wsgi server for instance on docker.
if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8000)