-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: localhost    Database: douban
-- ------------------------------------------------------
-- Server version	5.7.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-04-04 22:08:24.913472'),(2,'contenttypes','0002_remove_content_type_name','2018-04-04 22:08:24.964261'),(3,'auth','0001_initial','2018-04-04 22:08:25.088903'),(4,'auth','0002_alter_permission_name_max_length','2018-04-04 22:08:25.112444'),(5,'auth','0003_alter_user_email_max_length','2018-04-04 22:08:25.118859'),(6,'auth','0004_alter_user_username_opts','2018-04-04 22:08:25.125455'),(7,'auth','0005_alter_user_last_login_null','2018-04-04 22:08:25.132265'),(8,'auth','0006_require_contenttypes_0002','2018-04-04 22:08:25.135699'),(9,'auth','0007_alter_validators_add_error_messages','2018-04-04 22:08:25.147120'),(10,'auth','0008_alter_user_username_max_length','2018-04-04 22:08:25.153258'),(11,'users','0001_initial','2018-04-04 22:08:25.312947'),(12,'admin','0001_initial','2018-04-04 22:08:25.379308'),(13,'admin','0002_logentry_remove_auto_add','2018-04-04 22:08:25.399694'),(14,'book','0001_initial','2018-04-04 22:08:25.462024'),(15,'book','0002_auto_20180404_2208','2018-04-04 22:08:25.545573'),(16,'captcha','0001_initial','2018-04-04 22:08:25.562755'),(17,'main','0001_initial','2018-04-04 22:08:25.578174'),(18,'main','0002_article_author','2018-04-04 22:08:25.622021'),(19,'sessions','0001_initial','2018-04-04 22:08:25.649563'),(20,'main','0003_comment_article','2018-04-04 22:12:31.364038'),(21,'main','0004_auto_20180406_1412','2018-04-06 14:12:26.929004'),(22,'main','0005_article_image','2018-04-07 21:18:06.966329');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-08 21:05:47
