/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - charity
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`charity` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `charity`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add department_table',7,'add_department_table'),
(26,'Can change department_table',7,'change_department_table'),
(27,'Can delete department_table',7,'delete_department_table'),
(28,'Can view department_table',7,'view_department_table'),
(29,'Can add foodchart_table',8,'add_foodchart_table'),
(30,'Can change foodchart_table',8,'change_foodchart_table'),
(31,'Can delete foodchart_table',8,'delete_foodchart_table'),
(32,'Can view foodchart_table',8,'view_foodchart_table'),
(33,'Can add login_table',9,'add_login_table'),
(34,'Can change login_table',9,'change_login_table'),
(35,'Can delete login_table',9,'delete_login_table'),
(36,'Can view login_table',9,'view_login_table'),
(37,'Can add order_table',10,'add_order_table'),
(38,'Can change order_table',10,'change_order_table'),
(39,'Can delete order_table',10,'delete_order_table'),
(40,'Can view order_table',10,'view_order_table'),
(41,'Can add product_table',11,'add_product_table'),
(42,'Can change product_table',11,'change_product_table'),
(43,'Can delete product_table',11,'delete_product_table'),
(44,'Can view product_table',11,'view_product_table'),
(45,'Can add inventory_table',12,'add_inventory_table'),
(46,'Can change inventory_table',12,'change_inventory_table'),
(47,'Can delete inventory_table',12,'delete_inventory_table'),
(48,'Can view inventory_table',12,'view_inventory_table'),
(49,'Can add need_table',13,'add_need_table'),
(50,'Can change need_table',13,'change_need_table'),
(51,'Can delete need_table',13,'delete_need_table'),
(52,'Can view need_table',13,'view_need_table'),
(53,'Can add orderdetail_table',14,'add_orderdetail_table'),
(54,'Can change orderdetail_table',14,'change_orderdetail_table'),
(55,'Can delete orderdetail_table',14,'delete_orderdetail_table'),
(56,'Can view orderdetail_table',14,'view_orderdetail_table'),
(57,'Can add user_table',15,'add_user_table'),
(58,'Can change user_table',15,'change_user_table'),
(59,'Can delete user_table',15,'delete_user_table'),
(60,'Can view user_table',15,'view_user_table'),
(61,'Can add needresponse',16,'add_needresponse'),
(62,'Can change needresponse',16,'change_needresponse'),
(63,'Can delete needresponse',16,'delete_needresponse'),
(64,'Can view needresponse',16,'view_needresponse'),
(65,'Can add inventoryrequest_table',17,'add_inventoryrequest_table'),
(66,'Can change inventoryrequest_table',17,'change_inventoryrequest_table'),
(67,'Can delete inventoryrequest_table',17,'delete_inventoryrequest_table'),
(68,'Can view inventoryrequest_table',17,'view_inventoryrequest_table'),
(69,'Can add fooddonation',18,'add_fooddonation'),
(70,'Can change fooddonation',18,'change_fooddonation'),
(71,'Can delete fooddonation',18,'delete_fooddonation'),
(72,'Can view fooddonation',18,'view_fooddonation'),
(73,'Can add volunteers_table',19,'add_volunteers_table'),
(74,'Can change volunteers_table',19,'change_volunteers_table'),
(75,'Can delete volunteers_table',19,'delete_volunteers_table'),
(76,'Can view volunteers_table',19,'view_volunteers_table'),
(77,'Can add patientinfo_table',20,'add_patientinfo_table'),
(78,'Can change patientinfo_table',20,'change_patientinfo_table'),
(79,'Can delete patientinfo_table',20,'delete_patientinfo_table'),
(80,'Can view patientinfo_table',20,'view_patientinfo_table');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$720000$pIIQsBDhx5kHBjzFnhEw9q$r2sF1etzIgywXPKf5Hjxd0YLjZiZNfulUsyuiQkRa8g=','2024-05-05 09:14:01.539435',1,'admin','','','admin@gmail.com',1,1,'2024-04-13 11:05:18.637617');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `charity_scheme_department_table` */

DROP TABLE IF EXISTS `charity_scheme_department_table`;

CREATE TABLE `charity_scheme_department_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `d_name` varchar(100) NOT NULL,
  `Details` longtext NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Charity_Scheme_depar_LOGIN_id_3bf76ce6_fk_Charity_S` (`LOGIN_id`),
  CONSTRAINT `Charity_Scheme_depar_LOGIN_id_3bf76ce6_fk_Charity_S` FOREIGN KEY (`LOGIN_id`) REFERENCES `charity_scheme_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `charity_scheme_department_table` */

insert  into `charity_scheme_department_table`(`id`,`d_name`,`Details`,`LOGIN_id`) values 
(2,'Palliative care unit','A palliative care unit provides specialized medical care focused on improving the quality of life for patients with serious illnesses, focusing on pain and symptom management, emotional support, and holistic care.',7),
(3,'Dialysis unit','Specialized medical facility providing renal replacement therapy, such as hemodialysis or peritoneal dialysis, to patients with kidney failure.',8),
(4,'Destitute home','A destitute home is a shelter or dwelling where impoverished individuals or families lacking basic necessities, such as food, clothing, and proper housing, seek refuge and assistance.',9),
(5,'Rehabilitation services','\"Rehabilitation services focus on restoring and improving an individual\'s physical, mental, or emotional well-being through targeted therapies, interventions, and support programs.\"',10),
(6,'Harmony Village','Harmony Village is a serene and picturesque community nestled amidst lush greenery, offering a tranquil living environment for residents seeking peace and harmony.',11);

/*Table structure for table `charity_scheme_foodchart_table` */

DROP TABLE IF EXISTS `charity_scheme_foodchart_table`;

CREATE TABLE `charity_scheme_foodchart_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `day` varchar(100) NOT NULL,
  `daytime` varchar(100) NOT NULL,
  `daytype` varchar(100) NOT NULL,
  `amount` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `charity_scheme_foodchart_table` */

insert  into `charity_scheme_foodchart_table`(`id`,`day`,`daytime`,`daytype`,`amount`) values 
(1,'','BreakFast','Normal',2000),
(2,'','BreakFast','Special',4000),
(3,'','Lunch','Normal',4500),
(4,'','Lunch','Special',7500),
(5,'','Evening','Normal',1000),
(6,'','Evening','Special',1500),
(7,'','Dinner','Normal',1500),
(8,'','Dinner ','Special',3000);

/*Table structure for table `charity_scheme_fooddonation` */

DROP TABLE IF EXISTS `charity_scheme_fooddonation`;

CREATE TABLE `charity_scheme_fooddonation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `amount` double NOT NULL,
  `foodchart_id` bigint NOT NULL,
  `userid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Charity_Scheme_foodd_foodchart_id_41f47584_fk_Charity_S` (`foodchart_id`),
  KEY `Charity_Scheme_foodd_userid_id_e9c4488b_fk_Charity_S` (`userid_id`),
  CONSTRAINT `Charity_Scheme_foodd_foodchart_id_41f47584_fk_Charity_S` FOREIGN KEY (`foodchart_id`) REFERENCES `charity_scheme_foodchart_table` (`id`),
  CONSTRAINT `Charity_Scheme_foodd_userid_id_e9c4488b_fk_Charity_S` FOREIGN KEY (`userid_id`) REFERENCES `charity_scheme_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `charity_scheme_fooddonation` */

insert  into `charity_scheme_fooddonation`(`id`,`date`,`status`,`amount`,`foodchart_id`,`userid_id`) values 
(1,'2024-03-31','paid',2000,1,1),
(2,'2024-03-31','paid',4500,3,1),
(3,'2024-04-01','pending',3000,8,1),
(4,'2024-04-03','paid',2000,1,1),
(5,'2024-04-03','paid',4500,3,1),
(6,'2024-04-02','pending',4000,2,1),
(7,'2024-04-18','paid',3000,8,1),
(8,'2024-04-28','paid',2000,1,1),
(9,'2024-04-28','paid',4500,3,1),
(10,'2024-04-28','paid',1000,5,1),
(11,'2024-04-28','paid',1500,7,1),
(12,'2024-04-29','paid',3000,8,2);

/*Table structure for table `charity_scheme_inventory_table` */

DROP TABLE IF EXISTS `charity_scheme_inventory_table`;

CREATE TABLE `charity_scheme_inventory_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `inventory` varchar(100) NOT NULL,
  `description` varchar(300) NOT NULL,
  `stock` int NOT NULL,
  `department_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Charity_Scheme_inven_department_id_d441d301_fk_Charity_S` (`department_id`),
  CONSTRAINT `Charity_Scheme_inven_department_id_d441d301_fk_Charity_S` FOREIGN KEY (`department_id`) REFERENCES `charity_scheme_department_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `charity_scheme_inventory_table` */

insert  into `charity_scheme_inventory_table`(`id`,`inventory`,`description`,`stock`,`department_id`) values 
(1,'Wheelchairs','A wheelchair is a mobility device with a seat, backrest, wheels, and sometimes armrests and footrests, designed to assist individuals with mobility impairments in moving around independently.',20,2),
(2,'Wheelchairs',' A lift chair is a type of recliner that is designed to assist individuals with mobility challenges in standing up or sitting down comfortably. ',15,2),
(3,'Hospital beds','specialized bed used in healthcare facilities that can be adjusted in height, head and foot positions',15,3),
(4,'Water beds','A waterbed is a type of mattress filled with water, providing support and comfort by distributing body weight evenly.',18,2),
(5,'Therapy equipment','Therapy equipment refers to devices and tools designed to aid in physical, occupational, or psychological therapy, helping individuals improve their health, mobility, or well-being.',8,6);

/*Table structure for table `charity_scheme_inventoryrequest_table` */

DROP TABLE IF EXISTS `charity_scheme_inventoryrequest_table`;

CREATE TABLE `charity_scheme_inventoryrequest_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `stock` int NOT NULL,
  `reason` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `inventory_id` bigint NOT NULL,
  `userid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Charity_Scheme_inven_inventory_id_5e976353_fk_Charity_S` (`inventory_id`),
  KEY `Charity_Scheme_inven_userid_id_4ac16eae_fk_Charity_S` (`userid_id`),
  CONSTRAINT `Charity_Scheme_inven_inventory_id_5e976353_fk_Charity_S` FOREIGN KEY (`inventory_id`) REFERENCES `charity_scheme_inventory_table` (`id`),
  CONSTRAINT `Charity_Scheme_inven_userid_id_4ac16eae_fk_Charity_S` FOREIGN KEY (`userid_id`) REFERENCES `charity_scheme_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `charity_scheme_inventoryrequest_table` */

insert  into `charity_scheme_inventoryrequest_table`(`id`,`date`,`stock`,`reason`,`status`,`inventory_id`,`userid_id`) values 
(1,'2024-03-31',1,'personal issues\r\n','pending',1,1),
(2,'2024-04-01',5,'fdfdvfsdff','accept',1,1),
(3,'2024-04-01',8,'nhgyt','accept',2,1),
(4,'2024-04-02',1,'fdgtrt','pending',5,1);

/*Table structure for table `charity_scheme_login_table` */

DROP TABLE IF EXISTS `charity_scheme_login_table`;

CREATE TABLE `charity_scheme_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `charity_scheme_login_table` */

insert  into `charity_scheme_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','Admin@123','admin1'),
(6,'kiran','Kiran@123','volunteer'),
(7,'dep1','Dep1@123','department'),
(8,'dep2','Dep2@123','department'),
(9,'dep3','Dep3@123','department'),
(10,'dep4','Dep4@123','department'),
(11,'dep5','Dep5@123','department'),
(12,'nihal','Nihal@123','volunteer'),
(13,'finu','Finu@123','volunteer'),
(14,'muhammed','Muhammed@123','volunteer'),
(15,'aysha','Aysha@123','user'),
(16,'shaha','Shaha@1234','user'),
(18,'fathima','Fathima@123','user');

/*Table structure for table `charity_scheme_need_table` */

DROP TABLE IF EXISTS `charity_scheme_need_table`;

CREATE TABLE `charity_scheme_need_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `needs` varchar(100) NOT NULL,
  `details` varchar(300) NOT NULL,
  `amount` double NOT NULL,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `department_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Charity_Scheme_need__department_id_759cde39_fk_Charity_S` (`department_id`),
  CONSTRAINT `Charity_Scheme_need__department_id_759cde39_fk_Charity_S` FOREIGN KEY (`department_id`) REFERENCES `charity_scheme_department_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `charity_scheme_need_table` */

insert  into `charity_scheme_need_table`(`id`,`needs`,`details`,`amount`,`date`,`status`,`department_id`) values 
(1,'Medical Supplies','First aid kits, bandages, over-the-counter medications, and health-related items.',10000,'2024-03-31','pending',2),
(2,'Seasonal Items',' Warm clothing, blankets, and winter accessories during colder months; fans, sunscreen, and hydration supplies during hotter months.',19900,'2024-03-31','verified',2),
(3,'Mobility Aids','Wheelchairs, walkers, canes, and crutches for individuals with mobility challenges.',0,'2024-03-31','verified',3),
(4,'Counseling Services','Funding or resources for mental health counseling and support programs.',600,'2024-03-31','verified',4);

/*Table structure for table `charity_scheme_needresponse` */

DROP TABLE IF EXISTS `charity_scheme_needresponse`;

CREATE TABLE `charity_scheme_needresponse` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `amount` double NOT NULL,
  `needid_id` bigint NOT NULL,
  `userid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Charity_Scheme_needr_needid_id_5c5af50f_fk_Charity_S` (`needid_id`),
  KEY `Charity_Scheme_needr_userid_id_9c3694f1_fk_Charity_S` (`userid_id`),
  CONSTRAINT `Charity_Scheme_needr_needid_id_5c5af50f_fk_Charity_S` FOREIGN KEY (`needid_id`) REFERENCES `charity_scheme_need_table` (`id`),
  CONSTRAINT `Charity_Scheme_needr_userid_id_9c3694f1_fk_Charity_S` FOREIGN KEY (`userid_id`) REFERENCES `charity_scheme_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `charity_scheme_needresponse` */

insert  into `charity_scheme_needresponse`(`id`,`date`,`status`,`amount`,`needid_id`,`userid_id`) values 
(1,'2024-03-31','paid',200,3,1),
(2,'2024-03-31','paid',5000,2,1),
(3,'2024-03-31','paid',100,3,1),
(4,'2024-04-02','paid',700,3,1),
(5,'2024-04-02','paid',2000,3,1),
(6,'2024-04-02','paid',100,2,1),
(7,'2024-04-02','paid',100,4,1),
(8,'2024-04-18','paid',100,4,1),
(9,'2024-04-18','paid',100,4,1),
(10,'2024-05-05','paid',100,4,1);

/*Table structure for table `charity_scheme_order_table` */

DROP TABLE IF EXISTS `charity_scheme_order_table`;

CREATE TABLE `charity_scheme_order_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `amount` double NOT NULL,
  `status` varchar(100) NOT NULL,
  `userid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Charity_Scheme_order_userid_id_39698c56_fk_Charity_S` (`userid_id`),
  CONSTRAINT `Charity_Scheme_order_userid_id_39698c56_fk_Charity_S` FOREIGN KEY (`userid_id`) REFERENCES `charity_scheme_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `charity_scheme_order_table` */

insert  into `charity_scheme_order_table`(`id`,`date`,`amount`,`status`,`userid_id`) values 
(1,'2024-04-01',350,'ORDER',1),
(2,'2024-04-01',1050,'PAID',1),
(3,'2024-04-01',350,'ORDER',1),
(4,'2024-04-06',700,'PAID',1),
(5,'2024-04-08',1050,'PAID',1),
(6,'2024-04-08',1050,'PAID',1),
(7,'2024-04-08',350,'ORDER',1),
(8,'2024-04-08',700,'PAID',1),
(9,'2024-04-08',800,'PAID',1),
(10,'2024-04-08',200,'ORDER',1),
(11,'2024-04-08',700,'PAID',1),
(12,'2024-04-09',400,'PAID',1),
(13,'2024-04-18',1050,'CART',1),
(14,'2024-04-18',1750,'ORDER',1),
(15,'2024-04-18',300,'ORDER',1),
(16,'2024-04-18',700,'ORDER',2),
(17,'2024-04-18',700,'PAID',2),
(18,'2024-04-18',350,'ORDER',1),
(19,'2024-04-18',350,'ORDER',1),
(20,'2024-04-18',350,'ORDER',1),
(21,'2024-04-18',350,'ORDER',1),
(22,'2024-04-18',350,'ORDER',1),
(23,'2024-04-18',350,'ORDER',1),
(24,'2024-04-18',200,'ORDER',1),
(25,'2024-04-18',200,'ORDER',1),
(26,'2024-04-18',400,'ORDER',1),
(27,'2024-04-18',400,'ORDER',1),
(28,'2024-04-18',400,'ORDER',1),
(29,'2024-04-18',400,'ORDER',1),
(30,'2024-04-18',400,'ORDER',1),
(31,'2024-04-18',400,'ORDER',1),
(32,'2024-04-18',400,'ORDER',1),
(33,'2024-04-18',200,'ORDER',1),
(34,'2024-04-18',400,'ORDER',1),
(35,'2024-04-18',800,'ORDER',1),
(36,'2024-04-18',800,'ORDER',1),
(37,'2024-05-05',400,'ORDER',1);

/*Table structure for table `charity_scheme_orderdetail_table` */

DROP TABLE IF EXISTS `charity_scheme_orderdetail_table`;

CREATE TABLE `charity_scheme_orderdetail_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `price` int NOT NULL,
  `order_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Charity_Scheme_order_order_id_66c9b548_fk_Charity_S` (`order_id`),
  KEY `Charity_Scheme_order_product_id_98b75dd4_fk_Charity_S` (`product_id`),
  CONSTRAINT `Charity_Scheme_order_order_id_66c9b548_fk_Charity_S` FOREIGN KEY (`order_id`) REFERENCES `charity_scheme_order_table` (`id`),
  CONSTRAINT `Charity_Scheme_order_product_id_98b75dd4_fk_Charity_S` FOREIGN KEY (`product_id`) REFERENCES `charity_scheme_product_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `charity_scheme_orderdetail_table` */

insert  into `charity_scheme_orderdetail_table`(`id`,`quantity`,`price`,`order_id`,`product_id`) values 
(1,1,350,1,1),
(2,3,2100,2,1),
(3,1,350,3,1),
(4,2,700,4,1),
(5,3,1050,5,1),
(8,3,1050,6,1),
(9,1,350,7,1),
(10,2,700,8,1),
(11,2,800,9,2),
(12,1,200,10,3),
(13,2,700,11,1),
(14,2,400,12,3),
(15,3,1050,13,1),
(18,5,1750,14,1),
(19,5,300,15,4),
(20,2,700,16,1),
(21,2,700,17,1),
(22,1,350,18,1),
(23,1,350,19,1),
(24,1,350,20,1),
(25,1,350,21,1),
(26,1,350,22,1),
(27,1,350,23,1),
(28,1,200,24,3),
(29,1,200,25,3),
(30,1,400,26,2),
(31,1,400,27,2),
(32,1,400,28,2),
(33,1,400,29,2),
(34,1,400,30,2),
(35,1,400,31,2),
(36,1,400,32,2),
(37,1,200,33,3),
(38,1,400,34,2),
(39,2,800,35,2),
(40,2,800,36,2),
(41,1,400,37,2);

/*Table structure for table `charity_scheme_patient_enable` */

DROP TABLE IF EXISTS `charity_scheme_patient_enable`;

CREATE TABLE `charity_scheme_patient_enable` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `reson` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `patient_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Charity_Scheme_patie_patient_id_id_2953d211_fk_Charity_S` (`patient_id_id`),
  CONSTRAINT `Charity_Scheme_patie_patient_id_id_2953d211_fk_Charity_S` FOREIGN KEY (`patient_id_id`) REFERENCES `charity_scheme_patientinfo_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `charity_scheme_patient_enable` */

/*Table structure for table `charity_scheme_patientinfo_table` */

DROP TABLE IF EXISTS `charity_scheme_patientinfo_table`;

CREATE TABLE `charity_scheme_patientinfo_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `phone` bigint NOT NULL,
  `disease` varchar(100) NOT NULL,
  `Image` varchar(100) NOT NULL,
  `idproof` varchar(100) NOT NULL,
  `volunteer_id` bigint NOT NULL,
  `sdate` date NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Charity_Scheme_patie_volunteer_id_2cdbbf44_fk_Charity_S` (`volunteer_id`),
  CONSTRAINT `Charity_Scheme_patie_volunteer_id_2cdbbf44_fk_Charity_S` FOREIGN KEY (`volunteer_id`) REFERENCES `charity_scheme_volunteers_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `charity_scheme_patientinfo_table` */

insert  into `charity_scheme_patientinfo_table`(`id`,`fname`,`lname`,`gender`,`dob`,`phone`,`disease`,`Image`,`idproof`,`volunteer_id`,`sdate`,`status`) values 
(1,'vishnu','','Male','1938-06-06',9898989898,'Parkinson disease\r\n','mmm.jpeg','Blue And White Modern Effective Leadership In Business Presentation (1).pdf',3,'2024-03-31','enabled'),
(2,'aruthathi','mk','Female','1979-06-12',9876765454,'Heart Disease','www.jpeg','Blue And White Modern Effective Leadership In Business Presentation (1) (1)_VRILj2m.pdf',3,'2024-03-31','enabled');

/*Table structure for table `charity_scheme_product_table` */

DROP TABLE IF EXISTS `charity_scheme_product_table`;

CREATE TABLE `charity_scheme_product_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `productname` varchar(100) NOT NULL,
  `Description` longtext NOT NULL,
  `image` varchar(100) NOT NULL,
  `stock` int NOT NULL,
  `price` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `charity_scheme_product_table` */

insert  into `charity_scheme_product_table`(`id`,`productname`,`Description`,`image`,`stock`,`price`) values 
(1,'Handmade Umbrella',' This may include initiatives such as creating handmade umbrellas tailored to their specific needs, ensuring they have access to essential tools for protection and mobility despite their physical challenges.','umberlla_yqSSiqr.webp',3,350),
(2,' Handmade chalk','These chalk sticks are used for writing or drawing on surfaces like chalkboards or sidewalks, offering a smooth and erasable medium for artistic or educational purposes.','chalk_AjepzJJ.jpeg',6,400),
(3,'Handmade candles ',' crafted by melting wax, adding fragrance or color, pouring the wax into molds with a wick, and allowing it to cool and solidify.','candles_UmuDrZ4.jpg',23,200),
(4,' Handmade soap',' Additional ingredients like essential oils or herbs are often added for fragrance and benefits such as moisturizing or exfoliating.','soap_G7F5OBr.jpg',15,60);

/*Table structure for table `charity_scheme_user_table` */

DROP TABLE IF EXISTS `charity_scheme_user_table`;

CREATE TABLE `charity_scheme_user_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Charity_Scheme_user__LOGIN_id_60ca5a0d_fk_Charity_S` (`LOGIN_id`),
  CONSTRAINT `Charity_Scheme_user__LOGIN_id_60ca5a0d_fk_Charity_S` FOREIGN KEY (`LOGIN_id`) REFERENCES `charity_scheme_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `charity_scheme_user_table` */

insert  into `charity_scheme_user_table`(`id`,`fname`,`lname`,`gender`,`address`,`phone`,`email`,`LOGIN_id`) values 
(1,'Aysha','shahana','Female','kazhuthidukkil house muriyanal po kunnamagalam',8075301075,'ayshashana@gmail.com',15),
(2,'shaha','muhikha','Female','arakkal house\r\nmukkam\r\nmukkam',8089315707,'shaha@gmail.com',16),
(4,'fathima','','Female','koolikkal house\r\nnarikuuni\r\n',9878767656,'fathimasana83785@gmail.com',18);

/*Table structure for table `charity_scheme_volunteers_table` */

DROP TABLE IF EXISTS `charity_scheme_volunteers_table`;

CREATE TABLE `charity_scheme_volunteers_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `aadharno` bigint NOT NULL,
  `status` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Charity_Scheme_volun_LOGIN_id_24a44437_fk_Charity_S` (`LOGIN_id`),
  CONSTRAINT `Charity_Scheme_volun_LOGIN_id_24a44437_fk_Charity_S` FOREIGN KEY (`LOGIN_id`) REFERENCES `charity_scheme_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `charity_scheme_volunteers_table` */

insert  into `charity_scheme_volunteers_table`(`id`,`fname`,`lname`,`gender`,`place`,`post`,`pin`,`phone`,`email`,`photo`,`aadharno`,`status`,`LOGIN_id`) values 
(1,'kiran','kumar','Male','kollam','kollam',898989,9898989898,'kirankumar@gmail.com','candles_DNjBWoL.jpg',787878787878,'enabled',6),
(2,'nihal','baker','Male','ap hourse','mukkam',654543,9876765454,'nihal@gmail.com','men_uHbMmDo.png',767676554543,'',12),
(3,'finu','fathima','Female','arakkal hourse','koduvally',655433,9878788788,'finu@gmail.com','women_FVP0KC9.jpeg',765432121212,'',13),
(4,'muhammed','','Male','kk hourse','kunnamagalm',676767,9898989898,'muhammed@gmail.com','men_QyhsW3I.png',765454343232,'enabled',14);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(7,'Charity_Scheme','department_table'),
(8,'Charity_Scheme','foodchart_table'),
(18,'Charity_Scheme','fooddonation'),
(12,'Charity_Scheme','inventory_table'),
(17,'Charity_Scheme','inventoryrequest_table'),
(9,'Charity_Scheme','login_table'),
(13,'Charity_Scheme','need_table'),
(16,'Charity_Scheme','needresponse'),
(10,'Charity_Scheme','order_table'),
(14,'Charity_Scheme','orderdetail_table'),
(20,'Charity_Scheme','patientinfo_table'),
(11,'Charity_Scheme','product_table'),
(15,'Charity_Scheme','user_table'),
(19,'Charity_Scheme','volunteers_table'),
(5,'contenttypes','contenttype'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'Charity_Scheme','0001_initial','2024-03-30 12:17:32.033196'),
(2,'contenttypes','0001_initial','2024-03-30 12:17:32.118261'),
(3,'auth','0001_initial','2024-03-30 12:17:32.911882'),
(4,'admin','0001_initial','2024-03-30 12:17:33.110617'),
(5,'admin','0002_logentry_remove_auto_add','2024-03-30 12:17:33.128959'),
(6,'admin','0003_logentry_add_action_flag_choices','2024-03-30 12:17:33.141513'),
(7,'contenttypes','0002_remove_content_type_name','2024-03-30 12:17:33.254114'),
(8,'auth','0002_alter_permission_name_max_length','2024-03-30 12:17:33.327558'),
(9,'auth','0003_alter_user_email_max_length','2024-03-30 12:17:33.355484'),
(10,'auth','0004_alter_user_username_opts','2024-03-30 12:17:33.366220'),
(11,'auth','0005_alter_user_last_login_null','2024-03-30 12:17:33.429409'),
(12,'auth','0006_require_contenttypes_0002','2024-03-30 12:17:33.434757'),
(13,'auth','0007_alter_validators_add_error_messages','2024-03-30 12:17:33.447375'),
(14,'auth','0008_alter_user_username_max_length','2024-03-30 12:17:33.539013'),
(15,'auth','0009_alter_user_last_name_max_length','2024-03-30 12:17:33.624497'),
(16,'auth','0010_alter_group_name_max_length','2024-03-30 12:17:33.635098'),
(17,'auth','0011_update_proxy_permissions','2024-03-30 12:17:33.666814'),
(18,'auth','0012_alter_user_first_name_max_length','2024-03-30 12:17:33.765410'),
(19,'sessions','0001_initial','2024-03-30 12:17:33.801064');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('vdpgm6ciktvnddnl44zfno5a8uccv0cr','.eJxVjrkOwjAQRP_FNbJ8xQclPd8Qeb1rHIhsKUeF-HdiKQW082ae5s3GuG9l3FdaxgnZlUl2-c0gphfVDvAZ66Px1Oq2TMB7hZ905feGNN_O7p-gxLUcawItSNmohEPjEXS22mgRNCaDyVtSalAZIgyWJGEIwWgKToJP0ojsD-nc_7nPF6wIOfA:1s3X4F:3TslA0VkoXtM3aVsiNYac8znPLn1G6H8S74_u6wMI_Q','2024-05-19 08:17:55.163054'),
('zzkfvvztmly1vnq7k1x9vvd09dj2abov','.eJxVjjsOwjAQRO-ytWX5F8dOSc8ZItu7JoEQo3wqxN2JpRTQjWbejOYNfdi3od9XWvoRoQMJ7NeLIT1orgHew3wrPJV5W8bIK8LPdOXXgjRdTvZvYAjrcLQpakHKBiVaNA6jzlYbLbzGZDA5S0o1KscQG0uS0HtvNPlWRpekEdkdo1P9JxsGr6UqxSA8N-icEAxydbT9fAGpUEF0:1rxRBa:8Rl6EOI9DvDm_Fgp6Ai4GXQYnX9luDK5YjH1cavDcgo','2024-05-02 12:48:18.081867');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
