from flask import Flask, jsonify, render_template
import socket, psutil

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

#Function that get system cpu and memory usage
def app_health():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    message = None
    if cpu_percent > 85 or mem_percent > 70:
        message = "High CPU and Memory utilization, scale up"
    return str(cpu_percent), (mem_percent)

@app.route("/details")
def details():
    cpu_percent, mem_percent = app_health()
    hostname, ip_address = get_host_details()
    return render_template('index.html', HOSTNAME=hostname, IP=ip_address, CPU=cpu_percent, MEM=mem_percent)


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)