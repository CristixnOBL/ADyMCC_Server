from flask.scaffold import F


class Config:
    HOST = "0.0.0.0"
    DEBUG = True
    PORT = 80

    TEMPLATE_FOLDER = "views/templates"
    STATIC_FOLDER = "views/static"
    CAP_IMG_FOLDER = "Cap/img"
    CAP_VID_FOLDER = "Cap/vid"
