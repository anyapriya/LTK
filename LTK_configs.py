import logging
import logging.handlers
import logging.config
import sys




logging_config = { 
    'version': 1,
    'disable_existing_loggers': True,

    'formatters': { 
        'standard': { 'format': '%(asctime)s %(levelname)s [%(module)s:%(lineno)d]: %(message)s'},
        'multiprocessing': {'format': '%(asctime)s %(levelname)s [%(module)s:%(lineno)d] (%(process)d): %(message)s'},
    },


    'handlers': { 
        'print': { 
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,  
        },
        'file': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'LTK.log',
            'when': 'W6',
            'interval': 1,
            'backupCount': 5
        },
    },


    'loggers': { 
        'default': {  
            'handlers': ['print', 'file'],
            'level': 'DEBUG',
            'propagate': False
        },
    } 


}



logging.config.dictConfig(logging_config)


