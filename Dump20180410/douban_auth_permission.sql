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
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',2,'add_logentry'),(2,'Can change log entry',2,'change_logentry'),(3,'Can delete log entry',2,'delete_logentry'),(4,'Can add permission',3,'add_permission'),(5,'Can change permission',3,'change_permission'),(6,'Can delete permission',3,'delete_permission'),(7,'Can add group',4,'add_group'),(8,'Can change group',4,'change_group'),(9,'Can delete group',4,'delete_group'),(10,'Can add content type',5,'add_contenttype'),(11,'Can change content type',5,'change_contenttype'),(12,'Can delete content type',5,'delete_contenttype'),(13,'Can add session',6,'add_session'),(14,'Can change session',6,'change_session'),(15,'Can delete session',6,'delete_session'),(16,'Can add User',1,'add_user'),(17,'Can change User',1,'change_user'),(18,'Can delete User',1,'delete_user'),(19,'Can add article',7,'add_article'),(20,'Can change article',7,'change_article'),(21,'Can delete article',7,'delete_article'),(22,'Can add comment_article',8,'add_comment_article'),(23,'Can change comment_article',8,'change_comment_article'),(24,'Can delete comment_article',8,'delete_comment_article'),(25,'Can add captcha store',9,'add_captchastore'),(26,'Can change captcha store',9,'change_captchastore'),(27,'Can delete captcha store',9,'delete_captchastore'),(28,'Can add 图书',10,'add_book'),(29,'Can change 图书',10,'change_book'),(30,'Can delete 图书',10,'delete_book'),(31,'Can add 评论',11,'add_comment'),(32,'Can change 评论',11,'change_comment'),(33,'Can delete 评论',11,'delete_comment'),(34,'Can add 评论点赞',12,'add_praise'),(35,'Can change 评论点赞',12,'change_praise'),(36,'Can delete 评论点赞',12,'delete_praise'),(37,'Can add 收藏管理',13,'add_collection'),(38,'Can change 收藏管理',13,'change_collection'),(39,'Can delete 收藏管理',13,'delete_collection'),(40,'Can add 父标签',14,'add_flabel'),(41,'Can change 父标签',14,'change_flabel'),(42,'Can delete 父标签',14,'delete_flabel'),(43,'Can add 子标签',15,'add_slabel'),(44,'Can change 子标签',15,'change_slabel'),(45,'Can delete 子标签',15,'delete_slabel'),(46,'Can add article_save',16,'add_article_save'),(47,'Can change article_save',16,'change_article_save'),(48,'Can delete article_save',16,'delete_article_save');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-10  6:20:18
