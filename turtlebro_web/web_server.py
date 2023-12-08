from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World1!"

def main():
  app.run(host="0.0.0.0", port=8080, threaded=True)

if __name__ == "__main__":
  main()