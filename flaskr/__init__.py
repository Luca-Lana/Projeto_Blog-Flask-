import os

from flask import Flask


def create_app(test_config=None):
    # instance_relative_config isso fala que os arquivos de configuração  são relativos a pasta instance
    app = Flask(__name__, instance_relative_config=True)
    # seta algumas configurações padrões que o app vai usar
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # vai sobrescrever algumas configs padrao que vão ser pegadas do config.py se existir
        app.config.from_pyfile('config.py', silent=True)
    else:
        # carrega a configuração passada
        app.config.from_mapping(test_config)

    # garante que a pasta instance seja criada
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # registrando as funções referente ao db
    from . import db
    db.init_app(app)

    # registando bp de autenticação
    from . import auth
    app.register_blueprint(auth.bp)

    # registrando bp do blog
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app