from celery import Celery

app = Celery('endpoints')

app.conf.update(
    result_expires=240,
)

if __name__ == '__main__':
    app.start()
