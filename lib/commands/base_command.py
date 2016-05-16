"""The base command."""

class BaseCommand(object):
	"""A base command."""

	def __init__(self, options, *args, **kwargs):
		self.options = options
		self.args = args
		self.kwargs = kwargs

	def run(self):
		raise NotImplementedError('Run method must be implemented on inheritors!')
