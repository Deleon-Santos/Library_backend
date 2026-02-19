from app import appCreate


app = appCreate()
CORS = app()

if __name__ == '__main__':
    app.run(debug=True)