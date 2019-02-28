
from rq import Queue
from rq.job import Job
from rq.decorators import job
from worker import conn
from flask import Flask
from function import *
app = Flask(__name__)

q = Queue(connection=conn)

def add(x):
    return x+x 

@app.route('/', methods=['GET', 'POST'])
def index():
    value = 10
    job = q.enqueue_call(
    func=increment, args=(value,), result_ttl=5000
    )
    print(job.get_id())
    return "Added Job "+job.get_id() 

@app.route("/results/<job_key>", methods=['GET'])
def get_results(job_key):
    job = Job.fetch(job_key, connection=conn)

    if job.is_finished:
        return str(job.result), 200
    else:
        return "Nay!", 202


if __name__ == '__main__':
    app.run()
