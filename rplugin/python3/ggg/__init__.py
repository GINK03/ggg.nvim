import neovim
import time
import os

@neovim.plugin
class ggg(object):
  def __init__(self, nvim):
    self.nvim = nvim
    self.nvim.command("echo '非同期でgggプラグインが有効になりました'")

  @neovim.command("Gecho")
  def gecho(self):
    self.nvim.command("echo '[Echo Test]'")
  
  @neovim.command("Pwd")
  def pwd(self):
    pwd = os.popen('pwd').read()
    self.nvim.command("echo '[PWD@GGG]={}'".format(pwd))
  
  @neovim.command("Git")
  def pwd(self):
    add = os.popen('git add *').read()
    commit = os.popen('git commit -m "add"').read()
    push = os.popen('git push').read()
    self.nvim.command("echo {}".format(add))
    self.nvim.command("echo {}".format(commit))
    self.nvim.command("echo {}".format(push))


