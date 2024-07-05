CREATE DATABASE  IF NOT EXISTS `slsm_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `slsm_db`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: slsm_db
-- ------------------------------------------------------
-- Server version	8.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `avances_usuarios`
--

DROP TABLE IF EXISTS `avances_usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `avances_usuarios` (
  `id_avance` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  `pregunta1_sec1` int DEFAULT NULL,
  `notas1_sec1` varchar(200) DEFAULT NULL,
  `notas2_sec1` varchar(200) DEFAULT NULL,
  `pregunta1_sec2` int DEFAULT NULL,
  `notas1_sec2` varchar(200) DEFAULT NULL,
  `notas2_sec2` varchar(200) DEFAULT NULL,
  `pregunta1_sec3` int DEFAULT NULL,
  `notas1_sec3` varchar(200) DEFAULT NULL,
  `notas2_sec3` varchar(200) DEFAULT NULL,
  `pregunta1_sec4` int DEFAULT NULL,
  `notas1_sec4` varchar(200) DEFAULT NULL,
  `notas2_sec4` varchar(200) DEFAULT NULL,
  `pregunta1_sec5` int DEFAULT NULL,
  `notas1_sec5` varchar(200) DEFAULT NULL,
  `notas2_sec5` varchar(200) DEFAULT NULL,
  `pregunta1_sec6` int DEFAULT NULL,
  `notas1_sec6` varchar(200) DEFAULT NULL,
  `notas2_sec6` varchar(200) DEFAULT NULL,
  `pregunta1_sec7` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_avance`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `avances_usuarios`
--

LOCK TABLES `avances_usuarios` WRITE;
/*!40000 ALTER TABLE `avances_usuarios` DISABLE KEYS */;
INSERT INTO `avances_usuarios` VALUES (1,1,'2023-10-23',5,'EGXRDHFCGV','XRDFCGH',5,'fsgdxhfcjg','zsxdfcg',5,'fxgchj','tcyhvj',5,'xtfcygvjhbk','szxdfcgh',5,'yhvjbk','xrdtcfgvhb',5,'xdfgch','drxtfcvg','dfghj'),(2,1,'2023-10-23',5,'bien','si',5,'bien','si',5,'bien','si',5,'bien','si',5,'bien','si',5,'bien','si','si'),(3,1,'2023-10-17',10,'bien','si',7,'mejor','si',8,'mucho mejor','si',2,'muy bien','si',10,'bien','si',2,'si','si','mejor'),(4,6,'2023-10-18',2,'dsfghjk','fghjk',6,'fghj','tfyguio',2,'fgh','fghjkl',6,'fghjkl','dfghj',3,'yui','gfhjkl',2,'fdghjklñ','gfhjkl','dfghjkl'),(5,11,'2023-11-04',9,'mejor','sí,  he sentido menos cansancio',7,'mejor','he notado mejoras',6,'bien','poco a poco he ido progresando',10,'mejor','siento que he descansado más',10,'bien','he comido mejor',6,'bien','aún tomo 3 veces por semana','en cuanto a alimentación y conciliación del sueño he mejorado ');
/*!40000 ALTER TABLE `avances_usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historiales_medicos`
--

DROP TABLE IF EXISTS `historiales_medicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historiales_medicos` (
  `id_historial` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `altura` float DEFAULT NULL,
  `numero_telefono` varchar(20) DEFAULT NULL,
  `genero` varchar(15) DEFAULT NULL,
  `peso` float DEFAULT NULL,
  `pregunta1_sec2` varchar(2) DEFAULT NULL,
  `pregunta2_sec2` int DEFAULT NULL,
  `pregunta3_sec2` varchar(2) DEFAULT NULL,
  `pregunta4_sec2` float DEFAULT NULL,
  `pregunta5_sec2` int DEFAULT NULL,
  `pregunta6_sec2` varchar(2) DEFAULT NULL,
  `pregunta7_sec2` varchar(200) DEFAULT NULL,
  `pregunta8_sec2` int DEFAULT NULL,
  `pregunta9_sec2` int DEFAULT NULL,
  `pregunta10_sec2` varchar(200) DEFAULT NULL,
  `pregunta11_sec2` varchar(200) DEFAULT NULL,
  `pregunta12_sec2` varchar(200) DEFAULT NULL,
  `pregunta13_sec2` varchar(200) DEFAULT NULL,
  `pregunta1_sec3` varchar(2) DEFAULT NULL,
  `pregunta2_sec3` int DEFAULT NULL,
  `pregunta3_sec3` varchar(2) DEFAULT NULL,
  `pregunta4_sec3` varchar(200) DEFAULT NULL,
  `pregunta5_sec3` varchar(2) DEFAULT NULL,
  `pregunta6_sec3` int DEFAULT NULL,
  `pregunta7_sec3` varchar(2) DEFAULT NULL,
  `pregunta8_sec3` varchar(200) DEFAULT NULL,
  `pregunta9_sec3` varchar(2) DEFAULT NULL,
  `pregunta10_sec3` int DEFAULT NULL,
  `pregunta11_sec3` varchar(2) DEFAULT NULL,
  `pregunta12_sec3` varchar(200) DEFAULT NULL,
  `pregunta13_sec3` varchar(2) DEFAULT NULL,
  `pregunta14_sec3` int DEFAULT NULL,
  `pregunta15_sec3` varchar(2) DEFAULT NULL,
  `pregunta16_sec3` varchar(200) DEFAULT NULL,
  `pregunta17_sec3` varchar(200) DEFAULT NULL,
  `pregunta1_sec4` varchar(2) DEFAULT NULL,
  `pregunta2_sec4` varchar(2) DEFAULT NULL,
  `pregunta3_sec4` varchar(2) DEFAULT NULL,
  `pregunta4_sec4` varchar(2) DEFAULT NULL,
  `pregunta5_sec4` varchar(200) DEFAULT NULL,
  `pregunta6_sec4` varchar(2) DEFAULT NULL,
  `pregunta7_sec4` varchar(2) DEFAULT NULL,
  `pregunta8_sec4` varchar(2) DEFAULT NULL,
  `pregunta9_sec4` varchar(2) DEFAULT NULL,
  `pregunta10_sec4` varchar(2) DEFAULT NULL,
  `pregunta11_sec4` varchar(2) DEFAULT NULL,
  `pregunta12_sec4` varchar(2) DEFAULT NULL,
  `pregunta13_sec4` varchar(2) DEFAULT NULL,
  `pregunta14_sec4` varchar(200) DEFAULT NULL,
  `pregunta15_sec4` varchar(2) DEFAULT NULL,
  `pregunta16_sec4` varchar(2) DEFAULT NULL,
  `pregunta17_sec4` varchar(2) DEFAULT NULL,
  `pregunta18_sec4` varchar(2) DEFAULT NULL,
  `pregunta19_sec4` varchar(2) DEFAULT NULL,
  `pregunta20_sec4` varchar(2) DEFAULT NULL,
  `pregunta21_sec4` varchar(2) DEFAULT NULL,
  `pregunta22_sec4` varchar(200) DEFAULT NULL,
  `pregunta1_sec5` varchar(2) DEFAULT NULL,
  `pregunta2_sec5` varchar(200) DEFAULT NULL,
  `pregunta3_sec5` varchar(2) DEFAULT NULL,
  `pregunta4_sec5` varchar(40) DEFAULT NULL,
  `pregunta5_sec5` varchar(2) DEFAULT NULL,
  `pregunta6_sec5` varchar(2) DEFAULT NULL,
  `pregunta7_sec5` varchar(40) DEFAULT NULL,
  `pregunta1_sec6` int DEFAULT NULL,
  `pregunta2_sec6` varchar(40) DEFAULT NULL,
  `pregunta3_sec6` varchar(2) DEFAULT NULL,
  `pregunta4_sec6` varchar(2) DEFAULT NULL,
  `pregunta5_sec6` varchar(2) DEFAULT NULL,
  `pregunta6_sec6` varchar(2) DEFAULT NULL,
  `pregunta1_sec7` varchar(2) DEFAULT NULL,
  `pregunt2_sec7` varchar(2) DEFAULT NULL,
  `pregunta3_sec7` varchar(200) DEFAULT NULL,
  `pregunta4_sec7` varchar(2) DEFAULT NULL,
  `pregunta1_ext` varchar(2) DEFAULT NULL,
  `pregunta2_ext` varchar(200) DEFAULT NULL,
  `pregunta3_ext` varchar(200) DEFAULT NULL,
  `pregunta4_ext` varchar(200) DEFAULT NULL,
  `pregunta5_ext` varchar(200) DEFAULT NULL,
  `pregunta6_ext` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_historial`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historiales_medicos`
--

LOCK TABLES `historiales_medicos` WRITE;
/*!40000 ALTER TABLE `historiales_medicos` DISABLE KEYS */;
INSERT INTO `historiales_medicos` VALUES (1,6,'2023-10-01',0.01,'1235689','Femenino',0.1,'No',1,'No',0.1,1,'No','dfghj',1,1,'fghj','ftyguh','fghjk','tyui','No',1,'No','rtyui','No',1,'No','fghuj','No',1,'No','tyuio','No',1,'No','yguio','dfghjk','No','No','No','No','fghjk','No','No','No','No','No','No','No','No','dfghj','No','No','No','No','No','No','No','sedrtfgyuh','No','fghjk','No','Duermo más de lo normal','No','No','4 a 6 horas',1,'Omnívoro','No','No','No','No','No','No','dfghjk','No','No','sdfghj','No','fghj','No','Mejor nutrición'),(2,1,'2023-10-10',1,'23456','Femenino',1,'Si',1,'Si',1,1,'Si','rxdcftgvhbjnk',1,1,'rdfxgcfhv','tyvuj','gchvjchg','cgfvh','Si',0,'Si','rxdtgfchvj','Si',0,'Si','gxfchv','Si',0,'Si','xfgfchgjv','Si',0,'Si','tdyfcguvjh','rxdtfchg','Si','Si','Si','Si','rtcyvu','Si','Si','Si','Si','Si','Si','Si','Si','txfcgh','Si','Si','Si','Si','Si','Si','Si','gchv','Si','xdfcghbj','Si','Me quitan el sueño','Si','Si','4 o menos',0,'Vegetariano','Si','Si','Si','Si','Si','Si','xdgcfhj','Si','Sí','xgfchvj','Sí','xfgchvjj','Sí','Mejor nutrición'),(3,10,'1980-08-11',0.01,'235678','Femenino',0.1,'No',1,'No',0.1,1,'No','rety',1,1,'gfhjk','fghjk','gfhjk','gfhjk','No',1,'No','gfhj','No',1,'No','tygjk','No',1,'No','trfyui','No',1,'No','ytui','fghij','No','No','No','No','fghjk','No','No','No','No','No','No','No','No','fghjk','No','No','No','No','No','No','No','gfhj','No','gfhjk','No','Duermo más de lo normal','No','No','6 a 8 horas',1,'Vegetariano','No','No','No','No','No','No','fdghjkl','No','No','fghj','No','tyuio','No','Salud emocional'),(4,11,'2000-11-04',1.65,'9981234567','Femenino',68.5,'Si',2,'No',3.5,0,'No','ninguna',40,2,'mejorar mi condición','falta de tiempo','ninguno','me duele la cabeza','No',0,'No','ninguna','No',0,'No','ninguna','No',0,'No','ninguna','No',0,'No','ninguna','ninguna','No','No','No','No','sin frecuencia','No','No','No','No','No','No','Si','No','despejarme un rato','No','Si','Si','Si','Si','Si','Si','muy buena','No','ninguna','No','Ninguna de las anteriores','No','No','6 a 8 horas',13,'Omnívoro','Si','Si','No','No','No','No','3 veces a la semana','No','No','ninguna limitación','mucha confianza','la motivación','falta de tiempo, compromiso y disciplina','Mejor nutrición, Peso ideal, Dormir mejor');
/*!40000 ALTER TABLE `historiales_medicos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hojas_evolucion_medico`
--

DROP TABLE IF EXISTS `hojas_evolucion_medico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hojas_evolucion_medico` (
  `id_hojas` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  `peso` float DEFAULT NULL,
  `IMC` float DEFAULT NULL,
  `grasa_viseral` float DEFAULT NULL,
  `porcentaje_musculo` float DEFAULT NULL,
  `abdomen` float DEFAULT NULL,
  `ejercicio` int DEFAULT NULL,
  `horas_sueno` int DEFAULT NULL,
  `talla` float DEFAULT NULL,
  `grasa_corporal` float DEFAULT NULL,
  `edad_metabolica` int DEFAULT NULL,
  `calorias` int DEFAULT NULL,
  `glucosa` float DEFAULT NULL,
  `comida_chatarra` varchar(12) DEFAULT NULL,
  `calidad_sueno` varchar(12) DEFAULT NULL,
  `notas` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_hojas`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hojas_evolucion_medico`
--

LOCK TABLES `hojas_evolucion_medico` WRITE;
/*!40000 ALTER TABLE `hojas_evolucion_medico` DISABLE KEYS */;
INSERT INTO `hojas_evolucion_medico` VALUES (1,2,'2023-10-23',0.02,0.01,0.01,0.01,0.01,2,2,0,0.01,2,1001,1001,'Poca','Mala','dfghjk'),(2,9,'2023-10-23',60,20,2,20,20,20,8,20,20,20,1200,1200,'Casi nada','Buena','rzdhxfcgvjbk'),(3,6,'2023-10-23',0.01,0.01,0.01,0.01,0.01,2,2,1,0.01,2,1001,1001,'Poca','Buena','gfhj'),(4,1,'2023-10-23',60,25,2,20,70,40,7,70,20,25,1700,1200,'Mucha','Buena','va bien'),(5,3,'2023-10-23',0.01,0.01,0.01,0.01,0.01,2,2,1,0.01,2,1001,1001,'Poca','Buena','ertyui'),(6,3,'2023-10-16',0.01,0.01,0.01,0.01,0.01,2,2,1,0.01,2,1001,1001,'Poca','Buena','retyui'),(7,3,'2023-10-17',69,30,2,40,80,120,6,30,20,20,2000,1300,'Poca','Buena','El paciente no a hecho caso a sus medicaciones, se a vuelto un adicto a la mota.'),(8,3,'2023-10-17',60,23,30,45,67,200,3,32,32,30,1200,1300,'Poca','Mala','Esta muertisimo'),(9,1,'2023-10-17',62,25,20,25,70,30,7,80,20,25,1500,1200,'Poca','Buena','va bien'),(10,1,'2023-10-17',61,20,20,20,60,30,7,70,20,20,1300,1100,'Poca','Mala','ta bien'),(12,11,'2023-08-05',70,27,4,45,80,20,6,11,25,26,1800,77,'Poca','Buena','El paciente requiere de determinados ejercicios para mantenerlo en forma'),(13,11,'2023-09-02',69,26,3.5,44.5,79,25,8,10,24.5,25,1720,76,'Poca','Buena','El paciente esta teniendo un ligero progreso, se requiere hacer cambios en su alimentación'),(14,11,'2023-10-07',68,26,2.99,44.6,79,30,7,10,24,25,1728,76,'Poca','Buena','El paciente esta progresando a un buen ritmo, no requiere cambios en su plan de alimentación'),(15,11,'2023-11-04',67,24,2,43.5,78,35,7,9,23.9,25,1600,75,'Poca','Buena','El paciente va progresando considerablemente');
/*!40000 ALTER TABLE `hojas_evolucion_medico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id_rol` int NOT NULL AUTO_INCREMENT,
  `nombre_rol` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Especialista'),(2,'Paciente');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(80) DEFAULT NULL,
  `apellidos` varchar(80) DEFAULT NULL,
  `correo` varchar(80) DEFAULT NULL,
  `id_rol` int DEFAULT NULL,
  `contrasena` varchar(100) DEFAULT NULL,
  `contrasena_hash` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'GUADALUPE','GUINTO','guadalupe.guinto@gmail.com',2,'12345','$2b$12$NffuYu0ZnORLiM/PObslrugmyRsFz0V8sPArMW2HK7Lu3VYawhb7.'),(2,'AMAYRANI','GOMEZ','170300079@ucaribe.edu.mx',1,'12345','$2b$12$q1ROBA.geON5Ll9PvyD.ROHVtBTqyKXwEfSPzeIFZb.vz2PiKUAEm'),(3,'ADOLFO','TUN DZUL','170300124@ucaribe.edu.mx',2,'12345','$2b$12$7dYcrIuYsYl8Rg769cLTzeL0WHxbsq5RBuWsq1JuLqd8UmozirYD2'),(4,'KARLA','GUINTO','karla.guinto@gmail.com',2,'12345','$2b$12$M9BpQ4wQCB6pbiLrodDkjuvkCejCoH..F1AN8ZD6aoblpNHxbikqO'),(5,'GUADALUPE','SALINAS','guadalupe.salinas@gmail.com',1,'12345','$2b$12$6QnmWuNG1RQoHh6rwcch5.eCZTvKiHKgJx3WkCR9FZNwEUl7giADy'),(6,'AMAYRANI','GOMEZ','amayraniigomez@gmail.com',2,'12345','$2b$12$o8uAScdMsXi8ZXT8R9ZmyOXzcaVYN5X31MTQts2ktwNVgeiJ0NEfO'),(8,'ASHWIN','CARDENAS BOBADILLA','170300113@ucqribe.edu.mx',2,'adolfoestahermoso','$2b$12$kAIM7Q.WT63FbO7tVUV9ceTRejMI4N1NkTrHWKkMY6cUu99JG5fJC'),(9,'KARLA','GUINTO','180300325@ucaribe.edu.mx',1,'12345','$2b$12$reF50MVExOP9n7f2PmtUeuEQSP3381EN1vW8KUcrAdzegS9nXU/Om'),(10,'AMAYRANI','GOMEZ','herg08@hotmail.com',2,'12345','$2b$12$PS1TC7UO8EVD92ieJ0xZO.TlyK5BhF1r4eEiNQrnDD2Me3.siz3ie'),(11,'MARIA','GONZALEZ','maria.gonzalez@gmail.com',2,'12345','$2b$12$gNB02tuQG26gLokrYEcW6euYOMVYtn08CZdhm9hN4NSVJ0fweapb6'),(14,'ADOLFO','TUN DZUL','adolfo.mx99@gmail.com',1,'12345','$2b$12$3OZU1s7rtpknJ4dmhAsRweG2dfYRXRzltmbdqWnf9B07pVCcxA9su');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'slsm_db'
--

--
-- Dumping routines for database 'slsm_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-04  2:30:18
