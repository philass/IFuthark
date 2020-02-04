"""
Futhark Wrapper Kernel
"""

from ipykernel.kernelbase import Kernel

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

 
  def do_execute(self, code, silent, store_history=True, user_expressions=None,
                 allow_stdin=False):
    if not silent:
      stream_content = {'name': 'stdout', 'text': code}
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
