#!/bin/sh

celery -A corec.endpoints.ping --config=celeryconfig  worker -l INFO
