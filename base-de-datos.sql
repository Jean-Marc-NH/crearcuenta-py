CREATE DATABASE IF NOT EXISTS project_001;
use project_001;

CREATE TABLE usuarios(
    id      int(25) auto_increment not null,
    nombre  varchar(100),
    apellidos varchar(255),
    email varchar(255) not null,
    password varchar(255) not null,
    fecha date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=INNODB;

CREATE TABLE notas(
    id int(25) auto_increment not null,
    usuario_id int(25) not null,
    titulo varchar(255) not null,
    nota text not null,
    fecha date not null,

    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT uq_titulo UNIQUE(titulo),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=INNODB