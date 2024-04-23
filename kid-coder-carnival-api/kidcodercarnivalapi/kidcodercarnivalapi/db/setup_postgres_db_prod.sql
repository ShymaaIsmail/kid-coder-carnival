-- prepare  posetgres
-- prod Environment
CREATE DATABASE kidcodecarnival_prod;
CREATE USER kidcodecarnival_user WITH PASSWORD 'kidcodecarnival_123';
GRANT ALL PRIVILEGES ON DATABASE kidcodecarnival_prod TO kidcodecarnival_user;
