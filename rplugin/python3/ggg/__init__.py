import neovim
import time
import os

@neovim.plugin
class ggg(object):
  def __init__(self, nvim):
    self.nvim = nvim
    self.nvim.command("echo '非同期でgggプラグインが有効になりました'")

  @neovim.command("Gecho")
  def echo(self):
    self.nvim.command("echo '[Echo Test]'")
  
  @neovim.command("Pwd")
  def echo(self):
    pwd = os.popen('pwd').read()
    self.nvim.command("echo '[PWD@GGG]={}'".format(pwd))
