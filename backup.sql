-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: user_infodb
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.20.04.1

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
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category` text,
  `job_ad_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `categories_ibfk_1` (`job_ad_id`),
  CONSTRAINT `categories_ibfk_1` FOREIGN KEY (`job_ad_id`) REFERENCES `job_ads` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (7,'39c2620b-4dde-47a1-a87c-bda3c2488705','19823574-b8be-4c12-9e1e-d5802141ee78'),(8,'0cbb015a-04c0-4d65-b636-003f24b9d4c4','960bc7b6-a254-4ab6-9f6b-11817e3db74a');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `companies`
--

DROP TABLE IF EXISTS `companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `companies` (
  `name` varchar(100) DEFAULT NULL,
  `logo_url` varchar(255) DEFAULT NULL,
  `id` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companies`
--

LOCK TABLES `companies` WRITE;
/*!40000 ALTER TABLE `companies` DISABLE KEYS */;
INSERT INTO `companies` VALUES ('Schneider Electric Nordics','https://d1guu6n8gz71j.cloudfront.net/system/asset/logos/6858702/logo.png?1680005440','629fa5ca-f3ac-43cf-a6de-5b86c604f882'),('u-blox','https://d1guu6n8gz71j.cloudfront.net/system/asset/logos/6590049/logo.png?1669915315','cfbaf89c-8e3a-46b9-b894-99ae3f35eccc');
/*!40000 ALTER TABLE `companies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_ads`
--

DROP TABLE IF EXISTS `job_ads`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_ads` (
  `title` varchar(100) DEFAULT NULL,
  `description` text,
  `location` varchar(100) DEFAULT NULL,
  `work_experience` text,
  `company_id` varchar(100) DEFAULT NULL,
  `contract_type` varchar(100) DEFAULT NULL,
  `id` varchar(100) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `job_ads_ibfk_1` (`company_id`),
  CONSTRAINT `job_ads_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `companies` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_ads`
--

LOCK TABLES `job_ads` WRITE;
/*!40000 ALTER TABLE `job_ads` DISABLE KEYS */;
INSERT INTO `job_ads` VALUES ('Master Thesis','We want to find a use case and theory for Data Integrity between our softwares together with Aalto University. Thesis can focus be either on discrete manufacturing or Process.','Finland','young_graduate','629fa5ca-f3ac-43cf-a6de-5b86c604f882','thesis','19823574-b8be-4c12-9e1e-d5802141ee78','2023-11-24 10:03:22'),('GNSS Test Engineer','As a GNSS Test Engineer at u-blox you are responsible for the heart of u-blox’s cutting-edge positioning devices. You are responsible for test development and verification of positioning techniques based on GNSS.&nbsp; This role aims to acquire good knowledge of embedded software, GNSS and Sensor Fusion. You capture the test needs and bring them to definition, implementation, and execution. Understanding the new requirements and knowing how to verify functionalities and characterize navigation performance by continuous integration testing is part of your work. This role requires close collaboration with our test hardware and infrastructure team as well as our platform development teams for the overall goal of delivering high-quality positioning products for our customers. In this role, you will enjoy working in a highly skilled and motivated, international team engineering the next generation of u-blox’s innovative and competitive navigation systems.&nbsp; The role is located in Espoo , Finland. Your Responsibilities Understanding the requirements of new features and how to verify and test them. Define, implement, document, and maintain test cases enabling automated and continuous integration testing Execute and review tests for verification of requirements and specifications. Report on accuracy and integrity of automated test results, identify and fix defects and non-compliances.&nbsp; Your Skills and Experience Experienced with automated tests and with Robot test framework. Programming skills: Python or similar Software Version Control (GIT or other) Continuous integration testing Strong team player with good communication skills (English) Bonus Point&nbsp; Embedded software development Experience with agile Software development (SCRUM) What are your perks?&nbsp; A multicultural and international company with over 60 different nationalities &nbsp; Project-based activities working with colleagues across the globe&nbsp; A start-up and innovation mindset while in the process of scaling-up processes and efficiencies&nbsp; Hybrid working model &amp; flexible working hours&nbsp; A strong learning environment and regular career discussions&nbsp; Company Performance Bonus and RSU&nbsp; Easy access location in Perkkaa, Espoo&nbsp; Modern office premises&nbsp; Good basic benefits (commuting, lunch, sports &amp; culture etc.)&nbsp; Sport activities, Team events&nbsp; … and discover even more by talking with us! We see diversity as a strength and promote a culture of inclusion among our employees. Our varied backgrounds, ideas and experiences are critical to our success. We strive to become a strong learning organization and are committed to provide our employees with equal opportunities regardless of differences such as gender, race, ethnicity, generations, belief.','Finland','young_graduate','cfbaf89c-8e3a-46b9-b894-99ae3f35eccc','cdi','960bc7b6-a254-4ab6-9f6b-11817e3db74a','2023-11-24 10:03:22');
/*!40000 ALTER TABLE `job_ads` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `search_preferences`
--

DROP TABLE IF EXISTS `search_preferences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `search_preferences` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `contract_type` text,
  `location` varchar(100) DEFAULT NULL,
  `work_experience` int DEFAULT NULL,
  `categories` text,
  `company_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `search_preferences_ibfk_1` (`company_id`),
  CONSTRAINT `search_preferences_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `companies` (`id`),
  CONSTRAINT `search_preferences_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `search_preferences`
--

LOCK TABLES `search_preferences` WRITE;
/*!40000 ALTER TABLE `search_preferences` DISABLE KEYS */;
/*!40000 ALTER TABLE `search_preferences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `language_code` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=866414624 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (866414623,'Sviat',NULL,'TroyeKizzz','en');
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

-- Dump completed on 2023-12-07 21:28:35
