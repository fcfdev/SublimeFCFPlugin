import sublime
import sublime_plugin
import os
import sys
import subprocess
__dir__ = os.path.dirname(os.path.realpath(__file__));
sys.path.insert(1, __dir__)
import pyperclip


class FcfGetPathCommand(sublime_plugin.TextCommand):
  def run(self, edit, **args):  
    path = None

    try:
      if len(args["dirs"]) != 0:
          path = args["dirs"][0]
      elif len(args["files"]) != 0:
        path = args["files"][0]
    except:
      return

    if path == None:
      return
    pyperclip.copy(path)


    

class FcfNewTemplateCommand(sublime_plugin.TextCommand):
  directory = None
  args      = None
  template  = None

  def run(self, edit, **args):
    try:
      self.directory = ""
      self.args      = {"file": ""}
      self.template  = args["template"]
      if len(args["dirs"]) != 0:
          self.directory = args["dirs"][0]
      elif len(args["files"]) != 0:
        self.directory = os.path.dirname(args["files"][0])
    except:
      return;

    if self.directory == None:
      return


    self.view.window().show_input_panel("Enter file name:", "",
                                 self.onDoneInput, None, None)

  def onDoneInput(self, inputString):
    self.args["file"] = inputString.strip();
    self.action();


  def action(self):
    try:
      if len(self.directory) == 0:
        return
      if len(self.args["file"]) == 0:
        return
      subprocess.Popen(["fcfmngr", "c", self.template, self.args["file"]], cwd=self.directory)
    except e:
      print(e)
