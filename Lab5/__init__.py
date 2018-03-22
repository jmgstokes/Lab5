from pyramid.config import Configurator


def main(global_config, **settings):
    """ 
    This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    config.add_route('color','color/{color}')
    config.add_route('weight', 'weight/{weight}')

    config.add_route('bg_change', '/bg_change')
    config.add_route('new_bg', '/new_bg')

    config.scan()
    return config.make_wsgi_app()
