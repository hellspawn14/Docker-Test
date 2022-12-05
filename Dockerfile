# Install linux os
FROM debian:latest

# Copy script files 
COPY Script /usr/local/Script
COPY crontab /etc/cron.d/crontab

# Install dependencies 
RUN apt-get update 
RUN apt-get -y install cron 
RUN apt-get -y install nano
RUN apt-get -y install python3.9
RUN apt-get -y install python3-pip
RUN apt-get -y install python3-venv

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab

# Run process 
CMD ["cron", "-f"]
