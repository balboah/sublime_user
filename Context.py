import subprocess
import os.path
import sublime
import sublime_plugin
import logging

log = logging.getLogger()

class ContextPreview(sublime_plugin.WindowCommand):
	def run(self):
		src = self.window.active_view().file_name()
		dst = "%s.pdf" % ''.join(src.split('.')[:-1])
		pipe = subprocess.Popen(
			args=["/Users/johnny/Documents/context/tex/texmf-osx-64/bin/context", src],
			env={"PATH": "/Users/johnny/Documents/context/tex/texmf-osx-64/bin"},
			cwd=os.path.dirname(src),
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE)
		stdout, stderr = pipe.communicate()
		print("waiting for context")
		ret = pipe.wait()
		print("done")

		if ret != 0:
			print("ERROR: ", stderr)
		else:
			subprocess.check_call(["open", dst])
			print(stdout)