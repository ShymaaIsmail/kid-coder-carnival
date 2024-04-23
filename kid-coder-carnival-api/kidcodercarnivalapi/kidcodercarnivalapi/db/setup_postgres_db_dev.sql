-- prepare  posetgres
-- dev Environment
CREATE DATABASE kidcodecarnival_dev;
CREATE USER kidcodecarnival_user WITH PASSWORD 'kidcodecarnival_123';
GRANT ALL PRIVILEGES ON DATABASE kidcodecarnival_dev TO kidcodecarnival_user;
