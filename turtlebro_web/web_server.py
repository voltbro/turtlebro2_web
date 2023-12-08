from flask import Flask, send_from_directory, send_file, request, jsonify, render_template
app = Flask(__name__)

www_path = "../resource/web"
app = Flask(__name__, static_folder=www_path + '/static', template_folder=www_path)

@app.route("/")
def serve_index():
  return render_template('index.html', ros_host = "192.168.0.148")
#   return "Hello World1!"

def main():
  app.run(host="0.0.0.0", port=8080, threaded=True)

if __name__ == "__main__":
  main()