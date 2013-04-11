import sublime, sublime_plugin

class SplitFileCommand(sublime_plugin.TextCommand):
	"""
	Split current file with new view into another group
	"""
	def run(self, edit):
		window = self.view.window()
		window.run_command("set_layout", {
			"cols": [0.0, 1.0],
			"rows": [0.0, 0.5, 1.0],
			"cells": [[0, 0, 1, 1], [0, 1, 1, 2]]})
		window.run_command("clone_file")
		window.run_command("move_to_group", { "group": 1 })