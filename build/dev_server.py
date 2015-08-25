import argparse
import os
import sys

from paste import fileapp
from paste import httpserver

import webapp2
from webapp2 import Route

import game_project

class SourcePathsHandler(webapp2.RequestHandler):
  def get(self, *args, **kwargs):  # pylint: disable=unused-argument
    top_path = os.path.abspath(kwargs.pop('_top_path', None))
    path = os.path.join(top_path, os.path.relpath(self.request.path, '/'))
    if os.path.exists(path):
      app = fileapp.FileApp(path)
      app.cache_control(no_cache=True)
      return app
    self.abort(404)

def CreateApp():
  project = game_project.GameProject()
  routes = [Route('/<:.+>', SourcePathsHandler,
  	  defaults={'_top_path': project.source_path})]
  app = webapp2.WSGIApplication(routes=routes, debug=True)
  return app

def _AddPleaseExitMixinToServer(server):
  # Shutting down httpserver gracefully and yielding a return code requires
  # a bit of mixin code.

  exitCodeAttempt = []
  def please_exit(exitCode):
    if len(exitCodeAttempt) > 0:
      return
    exitCodeAttempt.append(exitCode)
    server.running = False

  real_serve_forever = server.serve_forever

  def serve_forever():
    try:
      real_serve_forever()
    except KeyboardInterrupt:
      # allow CTRL+C to shutdown
      return 255

    if len(exitCodeAttempt) == 1:
      return exitCodeAttempt[0]
    # The serve_forever returned for some reason separate from
    # exit_please.
    return 0

  server.please_exit = please_exit
  server.serve_forever = serve_forever

def Main(argv):
  parser = argparse.ArgumentParser(description='Run development server')
  parser.add_argument('-p', '--port', default=8003, type=int)
  args = parser.parse_args(args=argv[1:])

  app = CreateApp()

  server = httpserver.serve(app, host='127.0.0.1', port=args.port,
                            start_loop=False)

  _AddPleaseExitMixinToServer(server)
  app.server = server

  sys.stderr.write('Now running on http://127.0.0.1:%i\n' % server.server_port)

  return server.serve_forever()