from api import create_app

app = create_app("Development")
if __name__ == '__main__':
    app.run()
