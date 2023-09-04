from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, I am Nelson Osagie, a Cloud / DevOps Engineer.</p>"

#App health endpoint
@app.route("/status")
def app_status():
    return jsonify(
        status="RUNNING"
    )

#Function for fetching host name and ip add
def get_host_details():
    # Get the hostname
    hostname = socket.gethostname()
    # Get the IP address
    ip_address = socket.gethostbyname(hostname)
    return str(hostname), str(ip_address)

@app.route("/details")
def details():
    hostname, ip_address = get_host_details()
    return render_template('index.html', HOSTNAME=hostname, IP=ip_address)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)