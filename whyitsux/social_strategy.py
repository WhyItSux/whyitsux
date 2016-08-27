from social.strategies.django_strategy import DjangoStrategy
import os

class EnvDjangoStrategy(DjangoStrategy):
	def get_setting(self, name):
		val = os.getenv(name)
		if val:
			return val
		else:
			return super().get_setting(name)
