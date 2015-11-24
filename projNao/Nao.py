import time
import sys

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

class Nao:
    # Classe représentant Nao
    def __init__(self, ip="127.0.0.1", port=5995):
        self.ip = ip
        self.port = port

        self.proxies = {}

    def add_proxy(self, name, proxy_name):
        """Ajoute un proxy a la liste des proxy, avec l'adresse IP et le port."""
        self.proxies[name] = ALProxy(proxy_name, self.ip, self.port)

    def __getattr__(self, item):
        """Redirection de 'nao.item' sur 'nao.proxies["item"]' pour l'accès à la valeur"""
        if self.proxies.has_key(item):
            return self.proxies[item]

        raise NameError("Parameter {0} is not in self.proxies.".format(item))

    def __setattr__(self, item, value):
        """Redirection de 'nao.item' sur 'nao.proxies["item"]' pour l'affectation de valeurs."""
        if self.proxies.has_key(item):
            self.proxies[item] = value

        raise NameError("Parameter {0} is not in self.proxies.".format(item))

    def __delattr__(self, item):
        """Redirection de 'nao.item' sur 'nao.proxies["item"]' pour la suppression."""
        if self.proxies.has_key(item):
            del self.proxies[item]

        raise NameError("Parameter {0} is not in self.proxies.".format(item))
