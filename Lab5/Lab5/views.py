from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'Lab5'}

@view_config(route_name='color', renderer='templates/mytemplate.jinja2')
def text_color(request):
	mydict = request.matchdict
	print mydict['color']
	return {'color':mydict['color']}

@view_config(route_name='weight', renderer='templates/mytemplate.jinja2')
def font_weight(request):
	mydict = request.matchdict
	print mydict['weight']
	return {'weight':mydict['weight']}