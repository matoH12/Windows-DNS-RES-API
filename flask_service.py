import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import os
import subprocess

class FlaskService(win32serviceutil.ServiceFramework):
    _svc_name_ = "FlaskDNSService"
    _svc_display_name_ = "Flask DNS Service"
    _svc_description_ = "A service that runs a Flask application to manage DNS records."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ""))
        self.main()

    def main(self):
        # Change directory to where the Flask app is located
        os.chdir(r"C:\api-app")
        # Run the Flask app
        subprocess.call(["python", "dns_api.py"])

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(FlaskService)
