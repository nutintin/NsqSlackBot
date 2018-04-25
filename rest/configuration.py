import os

from dotenv import load_dotenv, find_dotenv

# from pymongo.read_preferences import ReadPreference

# Load environment
load_dotenv(find_dotenv())

# logging formatter based on
# https://docs.python.org/2/howto/logging-cookbook.html#an-example-dictionary-based-configuration
logconfiguration = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(levelname)s] %(asctime)s - %(name)s - %(filename)s:%(lineno)d: %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'verbose',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['logstash', 'console']
    }
}


class Configuration(object):
    # DB SETTINGS
    MANAGIX_DB_HOST = os.getenv("MANAGIX_DB_HOST", "mongodb://localhost:27017/managix_nsq")
    MANAGIX_DB = "managix_nsq"

    # PYMONGO NEW DB CONFIGURATION
    MONGO_URI = os.getenv("MONGO_URI", MANAGIX_DB_HOST)
    # MONGO_READ_PREFERENCE = ReadPreference.SECONDARY_PREFERRED

    # Url for access static file, best practice is using file server like nginx
    FILE_SERVER = os.getenv("FILE_SERVER", "http://127.0.0.1:5000/static")

    # Log
    LOG_CONFIGURATION = logconfiguration

    # uglify json flask
    JSONIFY_PRETTYPRINT_REGULAR = False

    # Flask compress setting
    COMPRESS_MIN_SIZE = 50

    PROJECT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    # Admin secret key
    APP_SECRET_KEY = os.getenv("APP_SECRET_KEY")
    
    # NSQ
    NSQD_HTTP_ADDRESS = os.getenv("NSQD_HTTP_ADDRESS", "nsq.managix.id:4151")

    # SLACK
    SLACK_CLIENT_ID = os.getenv("SLACK_CLIENT_ID")
    SLACK_VERIFICATION_TOKEN = "leIQIpxq12xdFvv3ohctuB15"
    SLACK_TEAM_ID = "T07U44ADA"
    SLACK_CLIENT_SECRET = os.getenv("SLACK_CLIENT_SECRET")
    SLACK_HOST = os.getenv("SLACK_HOST", "https://slack.com/api")
    SLACK_REQUEST_TIMEOUT = 60
