## Steps to get started
1. download and install redis
   - `wget http://download.redis.io/releases/redis-5.0.3.tar.gz`
   - `tar xzf redis-3.0.5.tar.gz`
   - `cd redis-3.0.5`
   - `make`
2. run redis server
   - `redis-server`
3. install requirements
   - `pip install -r requirements.txt`
4. run worker
   - `python worker.py`
5. run app 
   - `python app.py`

## To Test
1. make a `GET` request to `localhost:5000`
2. make a `GET` request to `localhost:5000/results/<job_id>`
