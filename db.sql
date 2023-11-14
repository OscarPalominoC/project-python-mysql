CREATE DATABASE IF NOT EXISTS project_py_mysql;
USE project_py_mysql;

CREATE TABLE IF NOT EXISTS users(
    id              int(25) AUTO_INCREMENT NOT NULL,
    name            VARCHAR(100),
    lastname        VARCHAR(255),
    email           CHAR(255) NOT NULL,
    password        VARCHAR(255) NOT NULL,
    creation_date   date NOT NULL,
    CONSTRAINT pk_users PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS notes(
    id              INT(25) AUTO_INCREMENT NOT NULL,
    user_id         INT(25) NOT NULL,
    title           VARCHAR(255) NOT NULL,
    description     MEDIUMTEXT,
    creation_date   date NOT NULL,
    CONSTRAINT pk_notes PRIMARY KEY(id),
    CONSTRAINT fk_note_user FOREIGN KEY(user_id) REFERENCES users(id)
)ENGINE=InnoDb;