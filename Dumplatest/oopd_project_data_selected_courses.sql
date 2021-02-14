-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: oopd_project_data
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `selected_courses`
--

DROP TABLE IF EXISTS `selected_courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `selected_courses` (
  `roll_no` varchar(15) NOT NULL,
  `course_id` varchar(8) NOT NULL,
  `attendence` int NOT NULL,
  `grade` varchar(5) NOT NULL,
  `type` varchar(15) NOT NULL,
  `status` varchar(15) NOT NULL,
  `credits` int NOT NULL,
  KEY `course_id_idx` (`course_id`),
  KEY `roll_no_fk` (`roll_no`),
  CONSTRAINT `course_id_fk` FOREIGN KEY (`course_id`) REFERENCES `courses_info` (`course_id`),
  CONSTRAINT `roll_no_fk` FOREIGN KEY (`roll_no`) REFERENCES `student_info` (`roll_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `selected_courses`
--

LOCK TABLES `selected_courses` WRITE;
/*!40000 ALTER TABLE `selected_courses` DISABLE KEYS */;
INSERT INTO `selected_courses` VALUES ('MT20002','CSE525',0,'NULL','regular','current',4),('MT20114','CSE525',72,'NULL','regular','current',4),('MT20114','CSE200',70,'w','short','dropped',2),('MT20001','MGT100',0,'NULL','short','current',2),('MT20001','CSE200',0,'NULL','short','current',2),('MT20001','CSE100',0,'NULL','regular','current',4),('MT20114','CSE250',0,'NULL','regular','current',4),('MT20114','MGT100',75,'A2','short','completed',2),('MT20114','PSY200',0,'NULL','short','current',2),('MT20130','PSY200',0,'NULL','short','current',2),('MT20130','MGT100',77,'A1','short','completed',2),('MT20130','CSE200',65,'w','short','dropped',2),('MT20114','CSE100',0,'w','regular','dropped',4),('MT11150','CSE100',0,'NULL','regular','current',4),('mt20130','CSE100',0,'NULL','regular','current',4),('mt11150','MGT100',0,'NULL','short','current',2),('MT20114','MGT100',0,'NULL','Short','repeat',2),('MT20084','PSY200',0,'NULL','short','dropped',2),('MT20084','CSE200',0,'NULL','Short','dropped',2),('MT20130','MGT100',0,'NULL','Short','repeat',2),('MT20127','CSE100',0,'NULL','Regular','current',4),('MT20127','CSE200',0,'NULL','Short','current',2),('MT20127','MGT100',0,'NULL','Short','current',2),('MT20127','PSY200',0,'NULL','short','current',2),('MT20127','CSE250',0,'NULL','Regular','dropped',4),('MT20127','CSE525',0,'NULL','Regular','current',4),('MT135','CSE100',0,'NULL','Regular','dropped',4),('MT135','CSE200',0,'NULL','Short','current',2),('Mt135','MGT100',0,'NULL','Short','current',2),('MT135','CSE525',0,'NULL','Regular','current',4),('MT135','PSY200',0,'NULL','short','current',2),('MT20130','ECE100',0,'NULL','Regular','current',4),('MT20150','CSE100',0,'NULL','Regular','current',4),('MT20150','CSE200',0,'NULL','Short','current',2),('MT20150','CSE250',0,'NULL','Regular','current',4),('MT20150','CSE50',0,'NULL','Regular','current',4),('MT20003','CSE100',70,'NULL','Regular','current',4),('MT0001','CSE100',70,'NULL','Regular','dropped',4),('MT0001','CSE200',70,'NULL','Short','current',2),('MT20114','CSE800',70,'NULL','Short','current',2),('MT0002','CSE100',70,'NULL','Regular','dropped',4),('MT0002','CSE200',70,'NULL','Short','current',2),('MT0002','CSE250',70,'NULL','Regular','current',4),('MT0002','CSE50',70,'NULL','Regular','current',4),('mt0003','CSE100',70,'NULL','Regular','dropped',4),('mt0004','CSE100',70,'NULL','Regular','current',4),('mt0004','CSE200',70,'NULL','Short','current',2),('mt0004','CSE250',70,'NULL','Regular','current',4),('mt0004','CSE50',70,'NULL','Regular','current',4),('Mt0005','CSE100',70,'NULL','Regular','dropped',4),('Mt0005','CSE250',70,'NULL','Regular','current',4),('Mt0005','CSE50',70,'NULL','Regular','current',4);
/*!40000 ALTER TABLE `selected_courses` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-14 14:31:56
