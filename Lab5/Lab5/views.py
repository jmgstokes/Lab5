from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'Lab5', 'bgcolor': '#bc2131'}

@view_config(route_name='color', renderer='templates/mytemplate.jinja2')
def text_color(request):
	mydict = request.matchdict
	print mydict['color']
	return {'color':mydict['color'], 'bgcolor': '#bc2131'}

@view_config(route_name='weight', renderer='templates/mytemplate.jinja2')
def font_weight(request):
	mydict = request.matchdict
	print mydict['weight']
	return {'weight':mydict['weight'], 'bgcolor': '#bc2131'}

@view_config(route_name='new_bg', renderer='templates/background.jinja2')
def new_bg(request):
    return {'project': 'Lab5'}

@view_config(request_method='POST', route_name='bg_change', renderer='templates/mytemplate.jinja2')
def change_bg(request):
    return {'bgcolor': request.POST['bgcolor']}
