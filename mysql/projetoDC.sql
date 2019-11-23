CREATE DATABASE IF NOT EXISTS projetoDC;

USE projetoDC;

CREATE TABLE IF NOT EXISTS Alunos (
	RM INT(10) PRIMARY KEY, 
	NOME VARCHAR(100) NOT NULL,
	IDADE INT(2),
	CURSO VARCHAR (100) NOT NULL,
	TURMA VARCHAR (10) NOT NULL);

INSERT INTO Alunos
VALUES 
(333305, "Matheus Moreti Felizardo", 24, "Big Data", "41BDT"),
(333765, "Ligia Araujo Hinniger", 26, "Big Data", "41BDT"),
(333927, "Rodrigo Rossi", 35, "Marketing", "70MKT"),
(333856, "Lionel Messi", 32, "Marketing", "70MKT"),
(333956, "Kim Kawasaki", 28, "Arquitetura de Solucoes", "37AQS");
