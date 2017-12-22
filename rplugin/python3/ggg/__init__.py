import neovim
import time
import os
'''examples'''
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
  def git(self):
    add = os.popen('git add *').read()
    commit = os.popen('git commit -m "add"').read()
    self.nvim.command("echo '[Load Git Repo function@GGG]\n{add}\n{commit}'".format(add=add, commit=commit))
    #self.nvim.command("echo '{}'".format(commit))
    #push = os.popen('git push').read()
    #self.nvim.command("echo '{}'".format(push))


