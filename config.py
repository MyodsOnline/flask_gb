class Config:
    DEBUG = False


class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db_test.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '^tg7ucgfpv3xtk83%tol5f!*^6&r#(k66sak$&e!+616o$cq=$'
