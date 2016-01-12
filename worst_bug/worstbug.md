# WORST.BUG.EVER.
## *__A tale of the trickiest bug I've ever found__*

^ I don't know about you but I've been asked a few times in interviews:

^ "What's the worst bug you've ever found?"

^ Usually I try to block those memories out and don't have a good answer

^ But last month, I found it: the worst bug I've ever squashed

---

# Background:

* **Picwell**: a recommendation engine for health care plans (and a corresponding API)
* **Recommendation**: a ranking for a given set of health care plans

^ Picwell's clients use their API to give them a list of plans, and get a ranking

^ Picwell's clients are major health insurance companies: Aon, Cigna, etc.

---

# The problem:

"As part of our client deliverables, we have been providing reporting derived from our recommendation logging service on a weekly basis... For the past week or so, we've noticed rather low throughput (as recorded by this service)"

^ This was the problem that Picwell approached us with

^ (in reality, this bug had existed for months)

---

# What they're actually saying:

* "We've been parsing our logs to create reports for clients."
* "One of our clients decided to double-check our numbers."
* "And we've been kinda underreporting recommendations."
* "We don't know how that happened."
* "Help."

^ So I'm going to give you three clues that I found and see if you can figure it out

---

# Clue #1: Logstash

^ Logstash bills itself as a tool to "collect, enrich & transport data"

^ Picwell uses Logstash to back up the log files from production to S3

^ They are stored in S3 until needed for something, or just for posterity

---

# Clue #1: Logstash
## `chef/templates/logstash.conf.erb`:

```ruby
input {
  file {
    path => "<%= @recommendations_path %>"
    tags => ["recommendations"]
    codec => "json"
  }
}
```

^ This is the chef template for the logstash.conf file

^ We see it's being given a path for a "recommendations" log file

---

# Clue #1: Logstash
## `chef/templates/logstash.conf.erb`:


```ruby
output {
  s3 {
    tags => ["recommendations"]
    region => "us-east-1"
    bucket => "picwell.recommendationlogs"
    prefix => "<%= @app_name %>/<%= @env_name %>/recommendations/"
    codec => "json_lines"
    size_file => 500000
    time_file => 15
  }
```

^ This is the other part of that config file

^ We see that logstash is being set to output the recommendation log to s3

^ It outputs the log every 15 minutes, or every half-megabyte, whichever is first

---

# Clue #1: Logstash
## `chef/recipies/logstash.rb`:

```ruby
template "/etc/logstash/conf.d/logstash.conf" do
  source "logstash.conf.erb"
  owner "deploy"
  group "deploy"
  variables({
    :recommendations_path =>
        node['logstash']['recommendations_path'] +
        "recommendations.log",
  })
end
```

^ Here's the chef recipie which fills that embedded ruby file

^ We see that the file that logstash is backing up is `recommendations.log`

---

# Clue #2: `RotatingFileHandler`

^ The rotatingfilehandler is a class in pythons logging module

^ It supports the rotation of disk log files

---

# Clue #2: `RotatingFileHandler`
## `commercial-api/log_helpers.py`:

```python
from logging.handlers import RotatingFileHandler
...
handler = RotatingFileHandler(
    log_path + name + '.log',
    maxBytes=10000000,
    backupCount=10
)
...
logger.addHandler(handler)
```

^ Here's how Picwell was configuring their rotatingfilehandler

^ When `recommendations.log` exceeds 10MB, it gets moved to `recommendaitons.log.1`

^ Then a new `recommendations.log` file is created

^ It does this up until `recommendations.log.10`, after which it starts throwing away files

---

# *"Ah hah!"*

^ At this point you might say "ah ha!" log files were being rotated before backed up

^ But i would say "you are right, but wrong"

^ There is a small possibility that a log will be written and rotated before logstash can get to it

^ But it would lose at most 0.5 mb of logs -- only 5% of logs

^ And picwell's traffic is not really high enough for 0.5mb of logs to be written in less than 15 minutes

---

# Clue #3: Apache

^ Picwell uses Apache as their web server, like almost everyone else

---

# Clue #3: Apache
## `apache2/sites-available/commercial.conf`:

```xml
<VirtualHost *:80>
  ServerName commercial-api.picwell.net
  WSGIDaemonProcess commercial processes=8
    threads=1 display-name=commercial
  WSGIProcessGroup commercial
  WSGIScriptAlias / /home/deploy/commercial.wsgi
  ...
</VirtualHost>
```

^ This is the relevant section of the apache config for the API

^ It's important to undertand why we have one thread and 8 processes here

^ Also to understand the difference between threads and processes

^ Picwell's applicaiton is not thread-safe, so to be performant, they run 8 separate processes

^ Threads share memory -- processes do not

---

# Any guesses?

^ I've given you all the clues. Any guesses?

---

# Hint: A Rollover in Action

^ Here's a hint. I forced a rollover to happen and observed the results

---

# Hint: A Rollover in Action

```
$ ls -lah /var/log/picwell/recommendations
total 20M
drwxr-xr-x 2 www-data www-data 4.0K Dec 14 21:59 .
drwxr-xr-x 4 deploy   deploy   4.0K Nov 11 02:10 ..
-rw-r--r-- 1 www-data www-data 9.9M Dec 14 21:59 recommendations.log
-rw-r--r-- 1 www-data www-data  38K Dec  2 17:18 recommendations.log.1
-rw-r--r-- 1 www-data www-data  59K Dec  2 17:17 recommendations.log.2
-rw-r--r-- 1 www-data www-data  80K Dec  2 17:18 recommendations.log.3
-rw-r--r-- 1 www-data www-data  30K Dec  2 17:18 recommendations.log.4
-rw-r--r-- 1 www-data www-data  47K Dec  2 17:18 recommendations.log.5
-rw-r--r-- 1 www-data www-data  99K Dec  2 17:18 recommendations.log.6
-rw-r--r-- 1 www-data www-data  43K Dec  2 17:18 recommendations.log.7
-rw-r--r-- 1 www-data www-data 9.6M Dec  2 15:28 recommendations.log.8 
.
.
```

^ I modified `recommendations.log` to be 9.9M

^ then ran a script which would make recommendations over and over

^ At first, it looks like this

^ Kind of weird all those small logs rolled in the same minute

---

# Hint: A Rollover in Action

```
$ ls -lah /var/log/picwell/recommendations
total 20M
drwxr-xr-x 2 www-data www-data 4.0K Dec 14 22:19 .
drwxr-xr-x 4 deploy   deploy   4.0K Nov 11 02:10 ..
-rw-r--r-- 1 www-data www-data 1.6K Dec 14 22:19 recommendations.log
-rw-r--r-- 1 www-data www-data 9.9M Dec 14 21:59 recommendations.log.1
-rw-r--r-- 1 www-data www-data  38K Dec  2 17:18 recommendations.log.2
-rw-r--r-- 1 www-data www-data  59K Dec  2 17:17 recommendations.log.3
-rw-r--r-- 1 www-data www-data  80K Dec  2 17:18 recommendations.log.4
-rw-r--r-- 1 www-data www-data  30K Dec  2 17:18 recommendations.log.5
-rw-r--r-- 1 www-data www-data  47K Dec  2 17:18 recommendations.log.6
-rw-r--r-- 1 www-data www-data  99K Dec  2 17:18 recommendations.log.7
-rw-r--r-- 1 www-data www-data  43K Dec  2 17:18 recommendations.log.8
-rw-r--r-- 1 www-data www-data 9.6M Dec  2 15:28 recommendations.log.9 
.
```

^ Then, it rolls over.

^ It successfully moves `recommendations.log` to `recommendations.log.1`,

^ so on and so forth. great

---

# Hint: A Rollover in Action

```
$ ls -lah /var/log/picwell/recommendations
total 11M
drwxr-xr-x 2 www-data www-data 4.0K Dec 14 22:20 .
drwxr-xr-x 4 deploy   deploy   4.0K Nov 11 02:10 ..
-rw-r--r-- 1 www-data www-data 3.2K Dec 14 22:21 recommendations.log
-rw-r--r-- 1 www-data www-data 8.0K Dec 14 22:21 recommendations.log.1
-rw-r--r-- 1 www-data www-data  12K Dec 14 22:21 recommendations.log.2
-rw-r--r-- 1 www-data www-data  18K Dec 14 22:21 recommendations.log.3
-rw-r--r-- 1 www-data www-data  42K Dec 14 22:21 recommendations.log.4
-rw-r--r-- 1 www-data www-data 9.9M Dec 14 21:59 recommendations.log.5
-rw-r--r-- 1 www-data www-data  38K Dec  2 17:18 recommendations.log.6
-rw-r--r-- 1 www-data www-data  59K Dec  2 17:17 recommendations.log.7
-rw-r--r-- 1 www-data www-data  80K Dec  2 17:18 recommendations.log.8
-rw-r--r-- 1 www-data www-data  30K Dec  2 17:18 recommendations.log.9
-rw-r--r-- 1 www-data www-data  47K Dec  2 17:18 recommendations.log.10
```

^ But then it continues moving the ~10M file to `recomendations.log.2`,

^ then `recommendations.log.3`, and so on

^ This might not seem so bad, but at this point, it's simultaneously writing to all the new files at once!

---

# Why?

^ So, why is this happening?

---

# Answer: inodes

---

# Answer: inodes

"In a Unix-style file system, the inode is a data structure used to represent a filesystem object, which can be one of various things including a file or a directory. Each inode stores the attributes and disk block location(s) of the filesystem object's data."

---

# Answer: inodes

* When you open the file `recommendations.log`, you're following a pointer in the inode table to a file descriptor
* When your script has a file open, and the pointer in the inode table changes, you're still writing to the same file descriptor

---

# Answer: inodes

At first, when the server starts, all eight processes are looking at the file called `recommendations.log`, which points to file descriptor *A*;

---

![inline](img1.pdf)

---

# Answer: inodes

Then, one process tries to write a log at the max size:

  * It closes the file;
  * It moves the file from `recommendations.log` to `recommendations.log.1`;
  * Then it opens a new file, `recommendations.log`, which points to file descriptor *B*;
  * And writes the log to the file.

^ This just updates the pointer in the inode table;

^ The data is still in the same place on disk, with the same file descriptor (*A*);

^ This means the other seven processes are now looking at `recommendations.log.1`

^ AKA "the file formerly known as `recommendations.log`

---

![inline](img2.pdf)

---

![inline](img3.pdf)

---

![inline](img4.pdf)

---

# Answer: inodes

Eventually, all eight processes are writing to eight different files on disk, but only *one* is getting backed up to S3!

---

![inline](img5.pdf)

---

![inline](img6.pdf)

---

# Estimating data loss

I estimated the % of logs lost to be 7/8ths, or 87.5%; the actual stats:

* Total recommendations recorded in logs: 42,509
* Total recommendations actually made: 323,603
* Percent lost: ~86.9%

^ We had elastic load balancer logs which showed us the actual number of responses

---

# Takeaways:
* Maybe log files shouldn't be relied on to be the end-all-be-all source of important data
* Maybe don't hire short-term contractors who don't know what they're doing
* Definitely keep hiring PromptWorks, though!
