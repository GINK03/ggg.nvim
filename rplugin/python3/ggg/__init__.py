import neovim
import time

@neovim.plugin
class ggg(object):
  def __init__(self, nvim):
    self.nvim = nvim
  
  @neovim.command("GGGEcho")
  def echo(self):
    self.nvim.command("echo '[Echo Test]'")
