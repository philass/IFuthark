"""
Futhark Wrapper Kernel
"""

import re

from ipykernel.kernelbase import Kernel
from pexpect.replwrap import REPLWrapper

class FutharkKernel(Kernel):
  """
  Implementation of the Method and Attributes
  for the FutharkKernel
  """

  implementation = 'Futhark'
  implementation_version = '1.0'
  language = "Futhark"
  language_info = {
    'name': "Futhark",
    'codemirror_mode': 'haskell',
    'mimetype': 'text/plain',
    'file_extension': '.fut'
  }

  banner = "Futhark Kernel"

  def __init__(self, **kwargs):
    Kernel.__init__(self, **kwargs)
    self._repl()

  def _repl(self):
    self.repl = REPLWrapper("futhark repl", "]>", None)
    
  def do_execute(self, code, silent, store_history=True, user_expressions=None,
                 allow_stdin=False):
    if not silent:

      output = self.repl.run_command(code)
      output = re.sub(r'\r\n\[\d+', '\n', output)
      output = re.sub(r'\r\[\d+', '\n', output)
      stream_content = {'name': 'stdout', 'text': output}
      self.send_response(self.iopub_socket, 'stream', stream_content)

    return {'status': 'ok',
              # The base class increments the execution count
              'execution_count': self.execution_count,
              'payload': [],
              'user_expressions': {},
             }

if __name__ == '__main__':
  from ipykernel.kernelapp import IPKernelApp
  IPKernelApp.launch_instance(kernel_class=FutharkKernel)
