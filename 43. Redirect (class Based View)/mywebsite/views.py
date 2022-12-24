from django.views.generic.base import RedirectView, TemplateView

class HomeView(RedirectView):
	# url = '/'
	pattern_name = 'index'

class HomeUserView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, *args, **kwargs):
		print(kwargs)
		if self.request.GET.__contains__('Ptes'):
			kwargs['Ptes']=self.request.GET['Ptes']
		print(kwargs)
		context=kwargs
		return context
		# return super().get_context_data(*args, **kwargs) ini sama dengan yang diatas

# inheritance hanya dari base view
class HomeRedirectView(RedirectView):
	pattern_name = 'user'
	permanent = False
	query_string = True


	def get_redirect_url(self, *args, **kwargs):
		print(kwargs)
		if kwargs['user'] == 'ali':
			print('ubah data')
			kwargs['user']='musthofa'

		return super().get_redirect_url(*args, **kwargs)