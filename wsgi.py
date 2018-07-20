import logging
from slack import app

if __name__ == "__main__":
  app.run()
else:
  try:
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
  except NameError:
    pass

application = app
