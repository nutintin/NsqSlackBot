from optparse import OptionParser
from rest import configuration
from rest import http
from werkzeug.serving import run_simple
import os

parser = OptionParser()
parser.add_option("-p", "--port", help="Port Number", dest="portnumber",
                  action="store", type="int", default=6002)

(options, args) = parser.parse_args()

application = http.create_app(configuration.Configuration)

port = int(os.environ.get('PORT', options.portnumber))

# openshift entry point
if __name__ == "__main__":

    run_simple('0.0.0.0', port, application, threaded=True, use_reloader=True)
