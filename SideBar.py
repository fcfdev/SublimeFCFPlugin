import sublime
import sublime_plugin
import os
import subprocess

class FcfNewTemplateCommand(sublime_plugin.TextCommand):
  directory = None
  args      = None
  template  = None

  def run(self, edit, **args):
    self.directory = ""
    self.args      = {"file": ""}
    self.template  = args["template"]

    if len(args["dirs"]) != 0:
      self.directory = args["dirs"][0]
    elif len(args["files"]) != 0:
      self.directory = os.path.dirname(args["files"][0])
      pass

    if self.directory == None:
      return


    self.view.window().show_input_panel("Enter file name:", "",
                                 self.onDoneInput, None, None)

  def onDoneInput(self, inputString):
    self.args["file"] = inputString.strip();
    self.action();


  def action(self):
    if len(self.directory) == 0:
      return
    if len(self.args["file"]) == 0:
      return
    try:
      subprocess.Popen(["fcfmngr", "c", self.template, self.args["file"]], cwd=self.directory)
    except e:
      print(e)
