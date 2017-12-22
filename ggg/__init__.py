import neovim
import time
from .api import TogglAPI
from requests.exceptions import ConnectionError

@neovim.plugin
class GGG(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command("GGGEcho")
    def echo(self, msg):
      self.nvim.command("echo '[Toggl.nvim] {}'".format(msg))
