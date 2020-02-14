from app import celery

@celery.task()
def make_file(fname, content):
    return(str(fname)+str(content))
