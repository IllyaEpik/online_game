import http.client
conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
print(conn.getresponse().read())
import modules.main_window
if __name__ == "__main__":
    modules.main_window.screen.run()
# 46.98.108.205