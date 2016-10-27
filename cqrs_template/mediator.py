from cqrs_template.helpers.singleton import SingletonMetaClass


class Mediator(object):
    __metaclass__ = SingletonMetaClass

    def __init__(self):
        self.signals = {}

    def signal(self, signal_name, *args, **kwargs):
        for handler in self.signals.get(signal_name, []):
            handler(*args, **kwargs)

    def connect(self, signal_name, receiver):
        handlers = self.signals.setdefault(signal_name, [])
        handlers.append(receiver)

    def disconnect(self, signal_name, receiver):
        handlers = self.signals.setdefault(signal_name, [])
        handlers[signal_name].remove(receiver)
