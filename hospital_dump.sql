-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital_db
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `patients`
--

DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patients` (
  `pid` int NOT NULL AUTO_INCREMENT,
  `pname` varchar(100) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `blood_group` varchar(5) DEFAULT NULL,
  `mobile` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patients`
--

LOCK TABLES `patients` WRITE;
/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
INSERT INTO `patients` VALUES (1,'Ayaan Khan',35,'123 Main St, Delhi','Male','O+','9876543210'),(2,'Fatima Ali',28,'456 Lake Rd, Mumbai','Female','A-','9123456780'),(3,'Rohan Mehta',42,'789 Hill View, Pune','Male','B+','9988776655'),(4,'Zara Sheikh',31,'15 Garden Ave, Bangalore','Female','AB+','9001122334'),(5,'Imran Patel',24,'88 Station Rd, Hyderabad','Male','B-','9811223344'),(6,'Mehak Sharma',29,'21 Lotus Lane, Jaipur','Female','O-','9810011223'),(7,'Arjun Verma',38,'77 River Rd, Lucknow','Male','A+','9908765432'),(8,'Nazia Khan',26,'32 MG Road, Bhopal','Female','B+','9898989898'),(9,'Rahul Das',45,'9 South St, Kolkata','Male','AB-','9123451234'),(12,'MD SHAKIR KHAN',21,'PATNA BIHAR 801505','Male','B+','7764932253');
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` enum('admin','viewer') NOT NULL DEFAULT 'viewer',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'MD SHAKIR','khan9211','viewer'),(2,'lolo','khan78945','viewer'),(3,'adminuser','admin123','admin'),(4,'vieweruser','viewer123','viewer'),(5,'Shakir','Khan723492','admin'),(6,' shakir','$2b$12$5Nv2l8jBFVBq0xZy3EGLdeS3I5r3jfVYADdSOVGo0CjHI89dkpcD6','admin'),(7,'viewer1','viewer123','viewer'),(8,'admin','$2b$12$6g0mtaFR9JInrVyKxzy3pu4EOVobKJEBHFC.lLWjtVOnO4Pq9Fefy','admin');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-30 17:01:41
