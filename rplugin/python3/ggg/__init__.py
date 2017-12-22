import neovim
import time
import os
import shlex
from datetime import datetime
import json
class Datastore(object):
  def __init__(self, kind):
    client = datastore.Client() 
    self.client = client
    self.kind = kind
  def put(self, key:str, value:str):
    key = self.client.key(self.kind, key)
    task = datastore.Entity(key=key)
    task['value'] = value
    self.client.put(task)
  def get(self, key:str):
    key = self.client.key(self.kind, key)
    #task = datastore.Entity(key=key)
    return self.client.get(key).get('value') 
  def delete(self, key:str):
    key = self.client.key(self.kind, key)
    self.client.delete(key)
try:
  from google.cloud import datastore
  datastoreInstance = Datastore('neovim')
except Exception as ex:
  ...

@neovim.plugin
class ggg(object):
  def __init__(self, nvim):
    self.nvim = nvim
    self.nvim.command("echo '非同期でgggプラグインが有効になりました'")
    self.zero_register = ''
    self.recover_from_gcp()

  def recover_from_gcp(self):
    self.nvim.vars['@0'] = "aaaaa"
 
  def enable(self):
    ...

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

  '''存在しないoptを適用する'''
  @neovim.command("Dot")
  def dot(self):
    git_opts = 'G=`git config --global credential.helper "cache --timeout=10000"`'
    go_opts = 'PATH=$HOME/go/bin:$PATH'
    gcloud_opts = 'PATH=$HOME/google-cloud-sdk/bin:$PATH'

    HOME = os.environ['HOME']
    lines = [ line.strip() for line in open(HOME + '/.bashrc').read().split('\n') ]

    opts = [ git_opts, go_opts, gcloud_opts ]
    opts = filter(lambda opt:opt not in lines, opts)

    f = open(HOME + '/.bashrc', 'a')
    for opt in opts:
      f.write( opt + '\n' )
  
  @neovim.autocmd("TextYankPost", pattern='*')
  def yank(self):
    ret = self.nvim.eval('@0')
    ''' zero_registerに保存して更新 '''
    if self.zero_register != ret:
      self.zero_register = ret
      
      '''escape処理(何をやってもうまくいかない)'''
      try:
        self.nvim.command( "echo '{r}' ".format(r=ret.replace('"','”').replace("'", "’") ) )
      except neovim.api.nvim.NvimError as ex:
        ...
      
      '''google data storeに保存する'''
      now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      datastoreInstance.put( now, ret ) 
