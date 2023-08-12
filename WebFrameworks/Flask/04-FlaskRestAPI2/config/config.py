from dotenv import dotenv_values

config = dotenv_values(".env")

dbconfig = {
    "hostname":config.get('HOSTNAME', 'localhost'),
    "username":config.get('USER', 'root'),
    "password":config.get('PASSWORD', '12345678'),
    "database":config.get('DATABASE', 'flask_tutorial_1'),
}