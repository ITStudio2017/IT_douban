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
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-04-08 21:06:49.255788'),(2,'contenttypes','0002_remove_content_type_name','2018-04-08 21:06:49.291931'),(3,'auth','0001_initial','2018-04-08 21:06:49.425580'),(4,'auth','0002_alter_permission_name_max_length','2018-04-08 21:06:49.447133'),(5,'auth','0003_alter_user_email_max_length','2018-04-08 21:06:49.453604'),(6,'auth','0004_alter_user_username_opts','2018-04-08 21:06:49.461319'),(7,'auth','0005_alter_user_last_login_null','2018-04-08 21:06:49.476692'),(8,'auth','0006_require_contenttypes_0002','2018-04-08 21:06:49.478940'),(9,'auth','0007_alter_validators_add_error_messages','2018-04-08 21:06:49.484516'),(10,'auth','0008_alter_user_username_max_length','2018-04-08 21:06:49.491176'),(11,'users','0001_initial','2018-04-08 21:06:49.639975'),(12,'admin','0001_initial','2018-04-08 21:06:49.703278'),(13,'admin','0002_logentry_remove_auto_add','2018-04-08 21:06:49.725430'),(14,'book','0001_initial','2018-04-08 21:06:49.741345'),(15,'book','0002_auto_20180317_1534','2018-04-08 21:06:49.780492'),(16,'book','0003_auto_20180323_1835','2018-04-08 21:06:49.815059'),(17,'book','0004_comment','2018-04-08 21:06:49.846060'),(18,'book','0005_auto_20180331_1027','2018-04-08 21:06:49.889120'),(19,'book','0006_auto_20180331_1037','2018-04-08 21:06:49.931161'),(20,'book','0007_auto_20180405_1420','2018-04-08 21:06:50.202427'),(21,'book','0008_auto_20180405_1424','2018-04-08 21:06:50.251801'),(22,'book','0009_auto_20180405_1429','2018-04-08 21:06:50.310928'),(23,'book','0010_auto_20180405_1430','2018-04-08 21:06:50.359284'),(24,'book','0011_auto_20180406_1405','2018-04-08 21:06:50.698842'),(25,'book','0012_collection','2018-04-08 21:06:50.759901'),(26,'book','0013_auto_20180406_2014','2018-04-08 21:06:50.861965'),(27,'book','0014_auto_20180406_2019','2018-04-08 21:06:50.916583'),(28,'book','0015_auto_20180408_1755','2018-04-08 21:06:51.087548'),(29,'book','0016_auto_20180408_1829','2018-04-08 21:06:51.148198'),(30,'book','0017_book_score','2018-04-08 21:06:51.174414'),(31,'book','0018_auto_20180408_1924','2018-04-08 21:06:51.210289'),(32,'captcha','0001_initial','2018-04-08 21:06:51.229460'),(33,'main','0001_initial','2018-04-08 21:06:51.269704'),(34,'main','0002_article_author','2018-04-08 21:06:51.312923'),(35,'main','0003_comment_article','2018-04-08 21:06:51.377484'),(36,'main','0004_auto_20180406_1412','2018-04-08 21:06:51.404030'),(37,'main','0005_article_image','2018-04-08 21:06:51.441098'),(38,'main','0006_auto_20180408_2104','2018-04-08 21:06:51.456446'),(39,'sessions','0001_initial','2018-04-08 21:06:51.479101'),(40,'main','0007_article_save','2018-04-09 15:29:46.856507'),(41,'main','0002_auto_20180410_0030','2018-04-10 00:30:15.218691');
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

-- Dump completed on 2018-04-10  6:20:19
