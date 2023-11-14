CREATE DATABASE IF NOT EXISTS proyecto_py_mysql;
USE proyecto_py_mysql;

CREATE TABLE IF NOT EXISTS usuarios(
    id          int(25) AUTO_INCREMENT NOT NULL,
    nombre      VARCHAR(100),
    apellidos   VARCHAR(255),
    email       VARCHAR(255) NOT NULL,
    password    VARCHAR(255) NOT NULL,
    fecha       date NOT NULL,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS notas(
    id          INT(25) AUTO_INCREMENT NOT NULL,
    usuario_id  INT(25) NOT NULL,
    titulo      VARCHAR(255) NOT NULL,
    descripcion MEDIUMTEXT,
    fecha       date NOT NULL,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;