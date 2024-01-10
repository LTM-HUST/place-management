-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 10, 2024 at 10:49 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `place_management`
--
CREATE DATABASE IF NOT EXISTS `place_management` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `place_management`;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `place_id` int(11) DEFAULT NULL,
  `category` enum('accounting','airport','amusement_park','aquarium','art_gallery','atm','bakery','bank','bar','beauty_salon','bicycle_store','book_store','bowling_alley','bus_station','cafe','campground','car_dealer','car_rental','car_repair','car_wash','casino','cemetery','church','city_hall','clothing_store','convenience_store','courthouse','dentist','department_store','doctor','drugstore','electrician','electronics_store','embassy','fire_station','florist','funeral_home','furniture_store','gas_station','gym','hair_care','hardware_store','hindu_temple','home_goods_store','hospital','insurance_agency','jewelry_store','laundry','lawyer','library','light_rail_station','liquor_store','local_government_office','locksmith','lodging','meal_delivery','meal_takeaway','mosque','movie_rental','movie_theater','moving_company','museum','night_club','painter','park','parking','pet_store','pharmacy','physiotherapist','plumber','police','post_office','primary_school','real_estate_agency','restaurant','roofing_contractor','rv_park','school','secondary_school','shoe_store','shopping_mall','spa','stadium','storage','store','subway_station','supermarket','synagogue','taxi_stand','tourist_attraction','train_station','transit_station','travel_agency','university','veterinary_care','zoo') DEFAULT NULL,
  `active` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `place_id`, `category`, `active`) VALUES
(1, 1, 'park', 1),
(2, 2, 'furniture_store', 1),
(3, 2, 'florist', 1),
(4, 4, 'doctor', 0),
(5, 5, 'book_store', 1),
(6, 6, 'book_store', 0),
(7, 7, 'embassy', 1),
(8, 8, 'physiotherapist', 0),
(9, 9, 'beauty_salon', 0),
(10, 10, 'hardware_store', 0),
(11, 11, 'furniture_store', 1),
(12, 12, 'laundry', 0),
(13, 13, 'funeral_home', 1),
(14, 14, 'mosque', 1),
(15, 15, 'hindu_temple', 1),
(16, 16, 'police', 0),
(17, 17, 'locksmith', 0),
(18, 18, 'bakery', 1),
(19, 19, 'city_hall', 1),
(20, 20, 'transit_station', 0),
(21, 21, 'train_station', 1),
(22, 22, 'taxi_stand', 1),
(23, 23, 'police', 1),
(24, 24, 'cemetery', 0),
(25, 25, 'hardware_store', 1),
(26, 26, 'doctor', 0),
(27, 27, 'beauty_salon', 1),
(28, 28, 'home_goods_store', 0),
(29, 29, 'train_station', 0),
(30, 30, 'hardware_store', 0),
(31, 31, 'car_wash', 1),
(32, 32, 'cafe', 1),
(33, 33, 'local_government_office', 1),
(34, 34, 'hair_care', 1),
(35, 35, 'movie_theater', 1),
(36, 36, 'park', 1),
(37, 37, 'mosque', 0),
(38, 38, 'veterinary_care', 1),
(39, 39, 'bank', 0),
(40, 40, 'post_office', 0),
(41, 41, 'cafe', 0),
(42, 88, NULL, 1),
(43, 88, NULL, 1),
(44, 88, NULL, 1),
(45, 91, NULL, 1),
(46, 91, NULL, 1),
(47, 91, NULL, 1),
(48, 92, 'accounting', 1),
(49, 92, 'aquarium', 0),
(50, 92, 'art_gallery', 1),
(51, 92, 'atm', 1),
(52, 93, 'amusement_park', 0),
(53, 93, 'aquarium', 0),
(54, 93, 'book_store', 1),
(55, 93, 'atm', 1),
(56, 93, 'bakery', 1),
(57, 93, 'bank', 1),
(58, 94, 'accounting', 0),
(59, 94, 'veterinary_care', 1),
(60, 94, 'zoo', 1),
(61, 94, 'bank', 1),
(62, 94, 'beauty_salon', 1),
(63, 95, 'art_gallery', 1),
(64, 97, 'atm', 1),
(65, 97, 'bank', 1),
(66, 97, 'beauty_salon', 1),
(67, 97, 'bicycle_store', 1),
(68, 98, 'atm', 1),
(69, 98, 'bank', 1),
(70, NULL, 'bowling_alley', 0),
(71, NULL, 'campground', 1),
(72, NULL, 'car_repair', 1),
(73, NULL, 'pet_store', 1),
(74, NULL, 'pharmacy', 1),
(75, NULL, 'zoo', 0),
(76, NULL, 'lodging', 1),
(77, NULL, 'meal_takeaway', 1);

-- --------------------------------------------------------

--
-- Table structure for table `friend`
--

CREATE TABLE `friend` (
  `id` int(11) NOT NULL,
  `source_friend_id` int(11) DEFAULT NULL,
  `target_friend_id` int(11) DEFAULT NULL,
  `status` enum('waiting','accepted','rejected') DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `active` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `friend`
--

INSERT INTO `friend` (`id`, `source_friend_id`, `target_friend_id`, `status`, `created_at`, `updated_at`, `active`) VALUES
(1, 1, 2, 'accepted', '1992-03-02 05:16:13', '2009-12-16 16:24:20', 1),
(2, 2, 3, 'accepted', '1984-03-13 00:31:34', '2024-01-10 08:49:25', 0),
(3, 2, 4, 'accepted', '1990-01-01 08:57:36', '1976-09-10 00:44:54', 0),
(4, 4, 5, 'waiting', '1999-02-14 09:55:39', '1982-03-30 22:00:49', 0),
(5, 5, 6, 'rejected', '1975-04-25 10:48:14', '1986-06-06 04:21:26', 0),
(6, 6, 9, 'accepted', '1971-09-17 16:29:03', '1971-05-16 22:44:37', 1),
(7, 7, 8, 'waiting', '1972-02-23 13:13:07', '1999-02-22 15:13:11', 0),
(8, 8, 5, 'rejected', '2006-03-04 00:23:53', '1972-11-14 21:05:26', 1),
(9, 9, 1, 'waiting', '1973-12-01 19:53:36', '2007-03-10 14:58:36', 1),
(10, 10, 11, 'accepted', '2015-04-04 12:57:45', '2004-06-15 14:26:49', 1),
(11, NULL, 1, 'accepted', '2024-01-03 17:57:33', '2024-01-03 17:58:04', 1),
(12, 2, NULL, 'waiting', '2024-01-03 18:29:25', '2024-01-03 18:29:25', 1),
(13, 3, 2, 'accepted', '2024-01-10 08:49:33', '2024-01-10 08:54:22', 1),
(14, 4, 2, 'waiting', '2024-01-10 08:50:55', '2024-01-10 08:50:55', 1),
(15, 5, 2, 'waiting', '2024-01-10 08:51:35', '2024-01-10 08:51:35', 1);

-- --------------------------------------------------------

--
-- Table structure for table `place`
--

CREATE TABLE `place` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `address` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `active` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `place`
--

INSERT INTO `place` (`id`, `name`, `address`, `description`, `user_id`, `created_at`, `updated_at`, `active`) VALUES
(1, 'voluptates', '48479 Baby Greens Suite 775\nSchambergertown, NC 74693', 'Sed aut explicabo enim sequi impedit. Ipsam in vel et recusandae.', 1, '2001-03-09 06:03:32', '1992-06-27 14:31:59', 1),
(2, 'sapiente', '99738 Wiegand Motorway\nO\'Keefeborough, NC 32010-5036', 'Ut nesciunt dolores quaerat maiores omnis quaerat numquam non. Similique voluptates nihil autem dolores esse odio qui. Temporibus eos repellendus vitae et delectus sed. Debitis rerum eum aut a itaque. Et occaecati rerum sed nisi quisquam.', 2, '1976-09-17 18:02:13', '2024-01-04 23:59:03', 1),
(3, 'pariatur', '44597 Nelle Harbors\nSouth Anahi, MD 65623-6538', 'Nihil qui dicta omnis officia. Consectetur in eos rerum odit non ullam et. Corrupti quidem modi et. Repellendus quibusdam aut et aut.', 3, '2019-01-28 19:48:35', '1987-10-14 15:57:14', 1),
(4, 'facere', '139 Hickle Gardens Apt. 025\nIsraelfurt, WV 72884', 'Nobis voluptatum et et autem neque. Voluptatem ut impedit consequatur. Et animi incidunt impedit officiis quos magni. Dolor et quam ea.', 4, '1994-11-01 21:47:15', '2000-07-30 03:28:42', 0),
(5, 'alias', '1374 Baumbach Grove Suite 694\nPort Marjolaine, CT 37525', 'Suscipit quae sint assumenda et mollitia in. Fuga repudiandae qui aut sunt magnam voluptas. Ipsam dolorem expedita molestias rerum eos.', 5, '1985-07-17 04:16:51', '2018-03-16 00:25:34', 1),
(6, 'ex', '152 Danyka Squares\nLake Kelliland, OK 35756-5551', 'Voluptas rerum esse facilis et et et dolorem nihil. Dolor repudiandae modi rerum commodi fugiat natus nihil omnis. Earum et ducimus et aliquam eum nihil.', 6, '2002-02-12 00:13:53', '2017-11-21 11:15:40', 0),
(7, 'et', '049 Keebler Roads\nNorth Woodrowfurt, DC 54847-2674', 'Hic sit distinctio vitae beatae repellendus magnam illum. Et iste laborum nisi repellendus non labore reprehenderit. Eligendi rem deleniti suscipit quidem ut accusamus. Voluptatibus perferendis ipsum tempora incidunt maxime nemo sed.', 7, '2005-07-18 23:50:12', '1970-10-10 02:49:04', 0),
(8, 'et', '33124 Okuneva Mountain\nLake Charityberg, AK 46479-6253', 'Ab cum quo officiis est. Harum quia modi aperiam voluptas qui accusantium ut. Eveniet recusandae laudantium eos. Id a et labore labore laborum et.', 8, '2020-12-27 00:22:14', '1997-04-15 23:38:35', 1),
(9, 'corporis', '617 Danielle Unions\nWillmsfurt, SD 83474-2679', 'Eos repellat molestiae recusandae sint. Cumque quis sunt facere sunt necessitatibus. Aut fugit dolor rem repellat id consequuntur fugiat facilis.', 9, '1994-06-24 09:33:15', '1982-04-08 10:42:19', 1),
(10, 'esse', '44889 Norris Stream\nSouth Wendell, ME 93839', 'Id natus aut voluptatem est veritatis quisquam optio. Impedit dolore in et saepe est illum. Et dolorem maxime optio corporis asperiores quia impedit.', 10, '2013-07-01 04:23:42', '2001-11-13 14:15:47', 1),
(11, 'qui', '6739 Kunde Pike\nNew Misael, NE 14215', 'Blanditiis quod odio eius dolorum. Iure est saepe est. Magnam vero exercitationem praesentium exercitationem optio aut. Consequuntur repellendus debitis laboriosam exercitationem nam sit enim.', 11, '1992-07-19 01:18:37', '1987-11-12 16:40:58', 0),
(12, 'non', '981 Belle Street\nSouth Sister, GA 83917', 'Natus non aut tempora iusto animi. Excepturi amet necessitatibus aut voluptatem voluptatem consequuntur possimus a. Sed fuga doloribus voluptatem possimus. Consectetur velit natus reprehenderit itaque ullam officia.', 12, '2016-04-01 22:13:12', '2019-03-24 05:36:28', 0),
(13, 'eum', '555 Buster Estates Apt. 830\nWest Kody, TN 46544-8874', 'Molestias ullam rerum vero voluptas aut repudiandae aut. Dolores ut accusamus ipsa vitae dolorem. Qui repellendus voluptas saepe optio quibusdam quisquam. Explicabo pariatur quis aspernatur sint assumenda inventore et.', 13, '1991-09-12 13:18:23', '2009-10-02 09:30:14', 0),
(14, 'ut', '7698 Katheryn Walks Suite 004\nPort Luther, OH 18224', 'Omnis soluta omnis incidunt. Sint expedita pariatur culpa inventore ut eligendi voluptates. Hic totam in vitae. Optio sit tenetur occaecati doloremque aut.', 14, '1972-01-25 18:10:47', '1973-04-28 13:27:49', 0),
(15, 'commodi', '91399 Remington Manor Suite 072\nNew Shanelle, AR 04512', 'Ipsum non id error omnis recusandae molestias. Est saepe facere nisi veniam reprehenderit. Est explicabo praesentium qui.', 15, '1985-11-12 21:54:56', '1993-05-08 02:30:42', 0),
(16, 'quia', '8788 Deonte Burg\nManuelafort, ND 25312', 'Et hic est a accusamus excepturi. Modi libero rerum quo quae praesentium voluptatem. Ex temporibus quibusdam velit beatae aliquid itaque. Ut error itaque est delectus tenetur enim magnam.', 16, '2009-02-18 02:34:02', '1988-05-18 04:38:39', 0),
(17, 'corrupti', '0439 Albina Flats\nHellerville, DE 35940', 'Voluptatem occaecati in fugiat aliquid. Quo quae quam porro assumenda officiis mollitia doloribus enim. Nihil facilis eligendi quo et facere provident alias. Consequuntur similique sapiente et dolore eaque mollitia sed. Voluptas eius vitae itaque.', 17, '2014-11-08 18:14:53', '1991-10-02 08:03:13', 0),
(18, 'vel', '0260 Hiram Unions\nJakobberg, NE 57546-0134', 'Tenetur commodi nihil quod suscipit aliquid aut. Velit quia est voluptas qui. Esse consequatur commodi aut.', 18, '2015-08-14 05:03:38', '2019-12-30 00:29:53', 0),
(19, 'aut', '9361 Marquardt Cliffs\nWest Chaya, AZ 85451-7930', 'Et est iure ut. Doloremque alias blanditiis saepe ea dolore ipsum. Animi consequuntur et praesentium voluptatum maiores ab.', 19, '2014-09-13 08:05:38', '1998-04-18 09:43:54', 1),
(20, 'minus', '1709 Friesen Inlet Suite 915\nVeumshire, MA 45889-0259', 'Voluptatem et explicabo tenetur aut. Quo soluta ipsum deserunt nisi. Quia ut in molestiae odit et. Error et reiciendis consequatur quidem natus aliquam cupiditate quia.', 20, '2020-12-13 15:46:19', '1972-03-15 06:32:09', 1),
(21, 'cupiditate', '4862 Bria Cove Suite 619\nSouth Valerieville, MI 03672-6169', 'Delectus quam hic sequi ea dolorem aperiam aut occaecati. Dolores molestiae cum qui est fugit numquam. Sequi unde quo voluptatem soluta aut voluptate nemo. Nisi occaecati consequatur illo.', 21, '1993-05-20 14:09:49', '2000-10-03 10:36:31', 0),
(22, 'sapiente', '36143 Dach Heights\nEichmannmouth, ID 13185-7004', 'Aliquam corrupti dolorum ratione officiis alias autem suscipit voluptatem. Tempora qui quia est ad molestiae id esse. Vitae quam quae sapiente officia.', 22, '1998-02-19 03:18:45', '1998-11-10 18:36:51', 0),
(23, 'placeat', '512 Urban Road Apt. 079\nLake Tanner, AZ 67065', 'Quia quaerat mollitia molestiae dolor dolores dolores. Sit voluptas occaecati natus dolorum quibusdam dolores est est.', 23, '1989-04-29 18:58:46', '2017-02-21 23:02:49', 1),
(24, 'molestiae', '32851 Trevion Heights\nNew Vincent, WI 39179', 'Ipsa nobis libero ut et et quod ad. Ut quo dolores repudiandae ut. Iusto quae sit pariatur.', 24, '2017-04-21 22:52:02', '2020-03-31 16:47:33', 1),
(25, 'aliquam', '818 Lilliana Shoals Suite 338\nVandervortmouth, MT 15030-4278', 'Eos velit natus tempora enim similique nostrum atque. Quasi et odit ut est perferendis consequatur molestias. Qui vel sed voluptatem maiores officiis voluptatem ea dolore.', 25, '1984-12-01 05:11:25', '2012-07-20 15:28:38', 0),
(26, 'et', '81093 Aufderhar Courts Suite 693\nLeuschkemouth, IN 34102-8821', 'Porro architecto velit quae aliquid consequatur ea. Officiis voluptas alias fuga libero. Unde aperiam repellat corporis soluta dolore.', 26, '2008-03-25 07:07:38', '1985-10-17 13:23:24', 1),
(27, 'sint', '2751 Green Skyway Suite 811\nBrowntown, ND 85384-3706', 'Autem asperiores et unde explicabo harum. Sint voluptas debitis aut tempore voluptatibus nesciunt est minima. Delectus labore temporibus magni odit neque hic. Adipisci consequatur sed non dolores error voluptatibus odit.', 27, '2008-10-18 16:52:41', '1994-02-19 10:12:55', 1),
(28, 'incidunt', '97464 Witting Ville Suite 642\nZacharychester, MN 72152', 'Voluptatem ullam cupiditate voluptatem tempore excepturi. Similique voluptatem eos sunt omnis accusantium odio aperiam. Quos qui veritatis quia sapiente sunt eius. Magnam veniam et voluptatem sequi necessitatibus perferendis.', 28, '2002-03-07 02:35:08', '2005-06-15 07:30:27', 0),
(29, 'et', '26541 Jo Island Suite 401\nIssacmouth, WY 86665', 'Recusandae aut distinctio non aut vel culpa velit. Et et eos ipsum aspernatur qui ducimus sed. Et suscipit ab reprehenderit. Ab numquam explicabo ducimus ipsam.', 29, '2020-07-23 04:30:35', '1985-12-16 01:23:28', 0),
(30, 'sapiente', '60859 Efrain Drive\nEast Ebonyfurt, NC 11108', 'Ipsum laborum doloribus aut excepturi itaque repudiandae voluptas ut. Distinctio qui maxime illo laborum aut sint et eaque. Et explicabo dolore voluptatem officia. Repellendus ut enim id aut consequatur.', 30, '1979-04-10 13:06:38', '1987-06-12 01:17:01', 0),
(31, 'sunt', '4661 Gutmann Pine\nLake Solon, IA 76818', 'Eum rerum blanditiis tempore quo quidem ullam. Consequatur culpa placeat perferendis. Aut iste ipsum similique inventore fuga rerum. Reprehenderit animi odit libero accusamus.', 31, '1984-05-31 10:27:40', '1999-08-05 10:19:11', 1),
(32, 'soluta', '628 Lamar Prairie\nFranciscaton, AK 24090-4177', 'Provident qui quod quis. Rem velit repudiandae ipsam. Quia inventore et unde aut provident odio. Et et earum et ut voluptatem.', 32, '1989-01-05 10:39:47', '2016-10-27 02:36:22', 0),
(33, 'perspiciatis', '6182 Koss Stravenue Apt. 038\nPfefferfurt, DE 53960', 'Qui ad fuga nihil et ipsum. Omnis quae qui laboriosam beatae aut est libero. Vero saepe vel ratione et nisi.', 33, '2000-07-15 13:21:37', '1995-01-16 09:41:53', 1),
(34, 'eaque', '940 Amy Drives Apt. 222\nLouisastad, TX 89551-2506', 'In deleniti voluptates minus ipsum necessitatibus qui. Velit non non hic corporis natus et unde. Ullam qui pariatur laboriosam officia natus. Officia excepturi reprehenderit sit reprehenderit doloremque.', 34, '1990-02-27 19:09:33', '2020-07-25 14:17:41', 1),
(35, 'ea', '914 Schumm Island\nNorth Dimitri, WA 61059-6812', 'Occaecati et numquam commodi id provident. Omnis facilis minus qui molestias aliquid debitis est. Qui corrupti molestias suscipit aut et eum maxime ipsam.', 35, '1996-06-21 07:27:03', '1997-03-29 01:15:29', 1),
(36, 'rem', '060 Gregoria Springs Apt. 672\nRachaelberg, LA 12127-5249', 'Corrupti iusto facere id blanditiis. Et ad quaerat voluptatem. Voluptas et aliquam non sint. Voluptatem voluptatem eius rerum impedit omnis.', 36, '1971-12-20 16:24:54', '2015-07-29 18:07:44', 0),
(37, 'magni', '209 Pfeffer Ferry\nGreenfelderside, NH 70792-1030', 'Consequuntur qui sed necessitatibus accusantium. Nemo sunt facilis illo. Dolor quis vitae ea dolor vel dicta accusamus iure.', 37, '1986-02-05 08:17:33', '2006-07-25 14:46:47', 0),
(38, 'dicta', '847 Lurline Corner\nPort Darwin, RI 03034-6408', 'Cum maxime illo id autem. Earum non reiciendis dolorem et illum eum et. Officia est commodi quos.', 38, '2010-10-06 17:07:57', '2021-05-30 07:14:04', 1),
(39, 'id', '1801 Joshua Springs Apt. 863\nSouth Kadenshire, MD 32183-4429', 'Explicabo iure et aliquid odio in qui aut. In qui architecto consequatur ratione praesentium neque nobis porro. Minima perferendis consequuntur quidem provident excepturi et.', 39, '2022-08-23 10:23:36', '1982-04-02 12:33:43', 0),
(40, 'et', '799 Mallie Forest\nLake Levi, MA 22577-6856', 'Rerum minus incidunt nihil non optio porro molestiae. Est ea sint magnam sunt qui ad fuga. Corporis iure consequuntur animi cum cum. Perferendis magnam quo voluptatibus rerum.', 40, '2013-05-15 04:09:11', '1997-11-10 04:36:09', 1),
(41, 'et', '19776 Keebler Inlet\nRusselfort, UT 30745', 'Consequuntur ut voluptas ut sed. Error soluta eos a quia nulla dolorem. Voluptatem quas tempore eaque et quo accusantium excepturi. Earum molestiae est et consequatur voluptates.', 41, '1980-03-25 06:03:06', '2020-04-11 10:39:20', 1),
(42, 'est', '166 Marjorie Spurs Suite 992\nRusselstad, HI 39571-1889', 'Cumque laudantium voluptatem similique exercitationem iusto error. Et autem aliquid nihil eos eveniet. Eum aspernatur autem iste doloribus quisquam libero laborum.', 42, '2015-11-14 17:27:03', '2005-08-14 09:58:17', 1),
(43, 'quis', '535 Alberta Manors\nBrookstad, IN 91168-4505', 'Ut aut et assumenda accusamus cumque perspiciatis ea. Error nulla ipsa deserunt nihil non. Id suscipit totam quidem architecto corporis quia. Quas quod quo qui at.', 43, '1975-12-19 18:14:53', '1996-03-18 22:25:06', 0),
(44, 'quia', '743 Betsy Forges\nNorth Caleberg, NJ 43135', 'Iste tenetur sint molestias qui debitis. Quia vero inventore et quia eos corporis. Harum non dolor facilis qui.', 44, '2011-10-20 01:09:07', '2007-05-04 04:44:59', 0),
(45, 'sint', '64220 Hank Ridges Suite 390\nOscarstad, ID 21969', 'Suscipit odio doloremque nesciunt rerum. Qui doloremque iusto quae suscipit eligendi qui. Et qui aut cupiditate. Maiores perferendis consequatur et.', 45, '2022-10-01 17:31:00', '1996-09-06 16:19:35', 1),
(46, 'ipsum', '400 Erin Branch\nEast Myrnashire, WY 98843', 'Distinctio debitis iure dolor necessitatibus. Natus doloremque nemo ipsum. Sed et et reprehenderit et quam earum quia.', 46, '1972-06-02 16:28:18', '2007-10-07 20:52:49', 1),
(47, 'quo', '158 Jerrold Lakes Apt. 559\nHandshire, NM 53522-4102', 'Deserunt hic saepe placeat dolorum et molestiae sint. Ipsa rerum veniam necessitatibus dolor facilis dolor repellat. Esse dolores iure quaerat id. Qui nesciunt qui sint aspernatur ut sit.', 47, '1987-02-27 12:34:03', '2000-03-22 03:59:17', 0),
(48, 'accusantium', '23299 Dereck Gateway Suite 107\nBartonton, KS 12276', 'Unde magni neque quia blanditiis natus. Perspiciatis id hic et eos. Ipsa quis aut recusandae debitis.', 48, '1985-05-09 21:52:19', '1981-06-14 15:21:25', 1),
(49, 'voluptatem', '814 Kaela Prairie\nBradtkeland, WV 99240', 'Doloremque deleniti cupiditate magnam hic reprehenderit quis error. In ratione voluptas est perspiciatis et. Voluptatum recusandae provident earum.', 49, '1984-10-09 04:18:09', '2004-06-30 10:03:20', 1),
(50, 'quam', '3967 Miller Highway Apt. 036\nWest Andreane, SC 35137-4096', 'Dolorem qui cupiditate eum assumenda voluptatum. Quos rerum eaque et eveniet voluptas. Qui deleniti aut est aliquid culpa omnis deleniti. Qui voluptas recusandae aut veniam maxime eveniet.', 50, '1977-07-14 05:46:51', '1995-03-28 13:05:25', 0),
(51, 'animi', '3202 Rippin Groves Suite 480\nEast Camden, CA 53026-8817', 'Atque excepturi atque nihil aut consequatur aspernatur. Aspernatur quas et optio doloribus maxime pariatur. Ipsum aspernatur totam voluptates adipisci nostrum. Qui cupiditate qui tenetur odio esse aut voluptatem.', 51, '1974-12-11 08:55:23', '1996-05-30 16:00:20', 1),
(52, 'et', '8486 Parker Ridge\nSouth Marquisview, DC 18050', 'Qui sunt pariatur modi a qui sed tempore. Impedit quibusdam sunt dolor voluptatem. Id ea fugit voluptatem est aliquid nulla. Libero architecto aperiam repudiandae blanditiis suscipit soluta nam.', 52, '2021-06-08 09:40:59', '1996-01-21 05:01:51', 0),
(53, 'deserunt', '2218 Joelle Rest Apt. 886\nNorth Regan, OK 39918-9973', 'Odit ad deserunt facere et ut sit. Delectus officiis itaque non ab. Incidunt aut est ratione qui et eos.', 53, '1987-01-29 02:06:12', '2006-08-22 18:09:29', 1),
(54, 'aut', '329 McGlynn Locks\nBlandaville, MA 70610', 'Incidunt in et accusantium perspiciatis enim ducimus. Aut exercitationem consequatur illum quia. Dolorum nemo distinctio aliquid. Qui incidunt eum saepe sunt consequatur nam. Expedita commodi ducimus quasi dolore ad.', 54, '1981-07-08 13:03:26', '1972-04-05 16:06:44', 0),
(55, 'eos', '0542 Hilpert Prairie Suite 767\nSouth Laurel, FL 29634', 'Tenetur suscipit quidem et et. Non rem sit magnam. Exercitationem totam rem non facilis natus ea. Beatae sed laudantium voluptatem consequatur eligendi fuga aliquid.', 55, '1983-05-27 22:05:31', '2018-02-11 13:40:32', 0),
(56, 'dolores', '0591 Schuster Via Suite 817\nNorth Marleefort, MS 45005', 'Numquam excepturi occaecati qui quo velit. Eos in neque sed ut qui. Impedit qui laborum provident est aut possimus dolor autem. Dicta aperiam nihil nobis omnis repellendus exercitationem recusandae.', 56, '1971-08-19 00:38:02', '2023-12-11 05:36:34', 0),
(57, 'ea', '9149 Chance Pike\nNew Joeton, MD 09166-4288', 'Magni ipsa mollitia officia voluptatem praesentium temporibus nam itaque. Repellendus suscipit numquam magni sed sint. Provident sed facere fugit harum magni autem libero.', 57, '2014-06-12 06:15:42', '2006-12-05 08:04:34', 1),
(58, 'accusamus', '32232 Isac Plains\nLindmouth, NE 30799', 'Repellat et earum est unde minima id. Qui et placeat eligendi fugiat eos. Veniam esse suscipit architecto dolorem et fugit qui eaque. Quia repellendus doloremque qui.', 58, '1979-12-16 01:19:30', '2011-05-26 18:41:29', 0),
(59, 'vero', '76339 Price Turnpike\nValeriemouth, WA 11104', 'Eos distinctio quas voluptates sit qui vel blanditiis. Saepe in corporis est consequatur. Debitis distinctio atque corrupti qui ut qui magni.', 59, '1984-01-13 15:46:53', '2021-04-18 04:05:14', 1),
(60, 'et', '50476 Clotilde Shoal Apt. 799\nVirgilside, IN 19463-0872', 'Neque ut dolorem maiores quia. Minus non assumenda quo nemo facilis odio. Quis modi rerum iusto officia quisquam magnam quis. Nemo maiores quibusdam consequatur alias ipsa nostrum.', 60, '2012-02-08 17:21:37', '1973-09-12 07:15:12', 1),
(61, 'odit', '229 Madisyn Ports\nNorth Kaciefort, MT 58085', 'Dicta excepturi voluptate accusantium temporibus. Aut qui suscipit sequi voluptatum inventore eligendi. Omnis laborum quo vel culpa tempora eos. Sit molestiae quia doloremque sunt a est qui alias. Est labore excepturi et enim ab debitis.', 61, '1978-01-15 18:44:16', '1971-12-10 13:41:47', 1),
(62, 'earum', '4113 Rutherford Spring\nPort Benniehaven, HI 26424-9102', 'Enim consequatur voluptatem nihil ea assumenda veniam non. Et excepturi exercitationem temporibus molestiae consequatur aut qui. Numquam qui voluptas accusamus sequi. Eius impedit ad dolorem.', 62, '2023-06-11 04:22:22', '2003-09-11 17:18:01', 0),
(63, 'architecto', '384 Kiara Overpass Apt. 604\nNew Mathew, MO 23375-4316', 'Corrupti nisi dicta voluptatem consectetur commodi. Veritatis qui autem facere quos. Ullam ut veritatis dolorem temporibus asperiores quia distinctio. Et earum et ea mollitia quisquam.', 63, '1999-06-30 07:29:02', '2010-01-26 11:08:17', 0),
(64, 'laborum', '510 Dorthy Expressway Apt. 627\nEast Favianchester, TN 53662', 'Ipsam neque iusto et saepe consequatur distinctio eum rerum. Excepturi explicabo ab totam vero quia consequatur. Voluptas vel eaque et modi illo. Assumenda consequatur dolorem laudantium voluptatem.', 64, '1982-07-08 17:49:21', '1974-06-07 06:03:32', 0),
(65, 'nam', '369 Ortiz Expressway Suite 226\nLake Herminaton, OH 55306', 'Sint placeat consequatur assumenda optio iure laborum. Harum ipsa qui veniam rem nihil maiores quam. Eos placeat officia corporis rerum sit voluptatem omnis consequatur. Officia et labore ut sit hic illum.', 65, '1995-01-08 19:56:51', '2012-09-16 14:25:22', 0),
(66, 'qui', '066 Ritchie Island\nEast Dayton, WI 93198-7564', 'Necessitatibus quod aut exercitationem voluptatem. Ut omnis sint hic veniam asperiores amet officia qui. Nisi similique aut atque quisquam aut. Quas non vero impedit sit ad.', 66, '1973-04-30 10:08:29', '1990-11-09 17:34:17', 0),
(67, 'autem', '902 Brandyn Ports Apt. 197\nWardburgh, KY 06105', 'Atque quo sint placeat tempora qui doloremque. Amet necessitatibus facilis consequuntur ut non est est saepe. Dolorum sunt consequatur eos temporibus et vitae.', 67, '1977-03-23 22:17:49', '1990-03-18 05:29:33', 1),
(68, 'voluptate', '452 Glenna Vista\nPort Albertochester, SC 05569', 'Est non voluptatem nulla rerum totam nihil. Eius ullam impedit eos qui dolorem. Ad maiores itaque excepturi est.', 68, '1999-07-18 09:16:42', '1979-10-14 13:46:06', 1),
(69, 'possimus', '51768 Isabelle Mall\nEast Elton, LA 09122', 'Eius quo ipsa alias iure odit voluptas magnam. Architecto at ratione itaque eum. Voluptate reprehenderit adipisci quisquam nobis commodi quia possimus soluta.', 69, '1996-12-29 15:41:39', '1973-03-16 14:01:34', 0),
(70, 'dolorem', '043 Sandrine Village\nDouglasmouth, IN 11377', 'Aut dolor earum consequatur impedit dolorum sed. Provident tempora dolores excepturi perferendis ut. Consequuntur harum voluptates aliquam. Repellendus exercitationem error doloribus rerum.', 70, '1986-10-26 14:50:21', '1996-12-07 06:26:56', 1),
(71, 'sed', '03928 Cummings Coves\nEast Tracyview, VA 61983-1198', 'Pariatur eum veniam ad quo voluptas earum ut eaque. Qui perferendis aut dolorem occaecati rem. Quasi deserunt pariatur quia omnis.', 71, '2019-08-07 04:44:38', '2015-11-24 15:12:46', 1),
(72, 'velit', '92177 Billy Mountain Apt. 687\nHagenesport, TX 03022', 'Et mollitia est quasi. Id qui non ipsum vel. Nisi vel qui laudantium quae itaque pariatur. Voluptas deleniti atque non et non nulla.', 72, '2016-09-07 06:43:05', '2015-02-25 23:06:20', 1),
(73, 'est', '28900 Norma Passage\nNew Dawnside, WI 49303-8661', 'Nihil aut minima occaecati libero. Dolore non est accusantium omnis ullam ad. Similique sit odit maxime consequatur modi. Suscipit molestias hic perferendis assumenda culpa magni.', 73, '1975-03-28 16:44:12', '2020-04-21 14:40:17', 0),
(74, 'eum', '4982 Charlotte Land\nKennaview, MI 75808-2806', 'Aspernatur quia voluptas optio impedit occaecati et. Optio optio modi ipsam deleniti culpa et quis. Ut voluptate quis temporibus dolorem consectetur quam. Rerum quas maiores est voluptatibus perferendis.', 74, '1971-11-21 17:46:53', '1983-10-04 18:35:35', 1),
(75, 'dolorem', '717 Kshlerin Green Apt. 964\nLake Eusebio, MT 89836', 'Voluptatibus autem nesciunt quidem. Quia provident cupiditate omnis earum sint unde nostrum sapiente. Repellendus consequatur necessitatibus sapiente a velit quis.', 75, '2012-05-30 01:18:38', '1986-08-09 06:09:54', 1),
(76, 'sint', '498 Maxwell Spurs\nNorth Narciso, IA 40483', 'Labore quia accusamus quis eveniet. Beatae nulla at sequi consequatur repudiandae. Nam ut vitae aut cumque. Officiis voluptas atque architecto est voluptatibus.', 76, '2020-01-08 23:58:14', '2003-11-23 09:11:08', 1),
(77, 'modi', '195 Ebert Groves\nJammiehaven, ND 13678-8935', 'Et dolore consequatur pariatur voluptatum enim. Eius impedit facilis ea soluta voluptatem. Qui deleniti nihil quos.', 77, '2015-01-14 21:47:43', '1985-07-22 03:49:37', 1),
(78, 'et', '12625 Carroll Shores\nGradyberg, NM 12530-6492', 'Et nisi adipisci delectus deleniti est. Impedit aut voluptatem neque vero reiciendis omnis. Quas rerum quis ipsam quo vitae et nesciunt odit. Consequatur iste cumque quam dolorum ducimus nihil expedita et.', 78, '2018-12-05 09:50:59', '2018-09-02 09:11:43', 0),
(79, 'iure', '7910 Reynolds Drive Suite 842\nLake Amosmouth, MO 69264', 'Voluptas dolores consequatur rerum incidunt ratione. Qui et quas et rerum nihil assumenda. Porro enim et amet accusantium.', 79, '1977-04-14 20:29:28', '2018-06-09 11:38:20', 1),
(80, 'voluptatum', '349 Elroy Track\nSchmittfort, IL 51888-7457', 'Dolorem expedita dolor ratione officia voluptate libero excepturi. Et quo neque odit repellendus et molestias aliquid sint. Iste facilis optio labore labore quibusdam.', 80, '2002-11-21 12:39:17', '1975-08-25 15:50:19', 0),
(81, 'et', '87856 Schultz Orchard Suite 295\nNorth Bartholomechester, NE 33863', 'Dolores repellendus est qui. Vel totam quia debitis voluptatibus hic et corporis vel.', 81, '1983-08-24 07:59:24', '2014-12-11 17:11:55', 1),
(82, 'quas', '4137 Barrows Plains\nKemmerton, WI 20595-1169', 'Quas voluptas quas ut vel laboriosam. Soluta error eos recusandae eum itaque explicabo. Pariatur aut voluptatum dolorum sint nesciunt id deserunt inventore.', 82, '2019-08-24 00:11:34', '1998-02-02 19:00:27', 1),
(83, 'voluptatibus', '12138 Jammie Square\nNew Alisa, CT 91215-3079', 'Tenetur veniam quia sed ullam quibusdam. Fugit et eos nihil magnam.', 83, '2015-07-06 08:07:14', '1994-02-17 06:16:32', 0),
(84, 'sed', '593 Sigurd Plains\nNorth Ruthshire, ME 86666-4367', 'Sunt harum est odit quis distinctio dolorum. Qui aut quidem sit consequatur sint sequi aut. Nihil natus impedit aut sint.', 84, '2000-06-23 10:53:50', '2008-05-20 19:08:03', 1),
(85, 'nihil', '6964 Little Alley\nSouth Solonville, NE 58945-5613', 'Quam aspernatur ea quia similique quod inventore dolore. Dolorem delectus vel possimus amet delectus corporis.', 85, '2012-06-18 06:01:21', '1984-01-15 19:32:34', 0),
(86, 'deserunt', '9858 Sasha Mission\nNew Stanleybury, OK 37275', 'Temporibus quos non alias tempora earum. Quisquam et aut repellendus omnis amet quas. Quo alias et cupiditate.', 86, '1993-06-09 00:45:46', '1979-08-25 11:32:26', 1),
(88, 'a', 'aa', '', 2, '2024-01-03 14:23:25', '2024-01-03 14:54:25', 0),
(89, 'ac', '', '', 2, '2024-01-03 14:27:26', '2024-01-03 14:54:34', 0),
(90, 'afvfgbdfgd', '', '', 2, '2024-01-03 14:32:31', '2024-01-03 14:54:41', 0),
(91, 'Hanoi', 'Hanoi', 'What a place~', 2, '2024-01-03 15:41:36', '2024-01-03 15:48:50', 0),
(92, 'a', 'aa', 'xd', 2, '2024-01-03 15:59:43', '2024-01-03 17:54:30', 0),
(93, 'Testing 333', 'None', 'Ok', 2, '2024-01-03 17:37:41', '2024-01-03 17:54:34', 0),
(94, 'Hanoi', 'Hanoi, Viet Nam', 'A nice place~', NULL, '2024-01-03 17:58:53', '2024-01-03 17:58:53', 1),
(95, 'a', 'a', 'aa', 2, '2024-01-03 18:24:28', '2024-01-03 18:24:31', 0),
(96, 'a', '', '', 2, '2024-01-03 18:27:09', '2024-01-03 18:27:15', 0),
(97, 'a', 'aa', 'a', 2, '2024-01-04 03:17:46', '2024-01-04 03:41:18', 0),
(98, 'Hanoi', 'Hanoi, Vietnam', 'Capital of Vietnam', 2, '2024-01-10 08:24:53', '2024-01-10 08:24:53', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tag`
--

CREATE TABLE `tag` (
  `id` int(11) NOT NULL,
  `place_id` int(11) DEFAULT NULL,
  `friend_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `friend_notification` tinyint(1) DEFAULT 0,
  `liked` tinyint(1) DEFAULT 0,
  `active` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tag`
--

INSERT INTO `tag` (`id`, `place_id`, `friend_id`, `created_at`, `updated_at`, `friend_notification`, `liked`, `active`) VALUES
(1, 1, 2, '2004-07-22 00:00:27', '2024-01-10 08:28:22', 1, 1, 1),
(2, 2, 1, '2004-05-17 08:11:04', '2024-01-10 08:52:17', 1, NULL, 1),
(3, 4, 5, '1994-05-09 07:01:34', '1981-09-27 03:09:20', NULL, NULL, 0),
(4, 5, 6, '1998-03-25 04:06:13', '1999-09-27 20:25:22', NULL, NULL, 1),
(5, 9, 6, '1979-05-18 19:43:31', '1992-12-26 00:16:54', NULL, NULL, 0),
(6, 2, 3, '2019-01-18 04:21:04', '2023-12-28 14:25:49', NULL, NULL, 1),
(7, 7, 8, '1972-04-11 09:04:34', '2023-01-22 02:25:09', NULL, NULL, 1),
(8, 8, 5, '1978-09-17 20:57:24', '2023-10-25 09:35:28', NULL, NULL, 0),
(9, 91, 3, '2024-01-03 15:41:36', '2024-01-03 15:41:36', 0, 0, 1),
(10, 92, 3, '2024-01-03 15:59:43', '2024-01-03 15:59:43', 0, 0, 1),
(12, 93, 3, '2024-01-03 17:37:41', '2024-01-03 17:37:41', 0, 0, 1),
(16, 97, 3, '2024-01-04 03:17:46', '2024-01-04 03:17:46', 0, 0, 1),
(18, NULL, 3, '2024-01-10 08:39:21', '2024-01-10 08:39:21', 0, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `active` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `created_at`, `updated_at`, `active`) VALUES
(1, 'ewald69', '1', '1973-08-30 07:00:49', '2024-01-05 01:49:38', 1),
(2, 'a', '1', '1991-05-04 22:13:16', '2023-12-28 14:51:03', 1),
(3, 'haleigh42', 'b503965f2dc629dc772e81b5a07ca1f1a19c0569', '2005-04-29 10:43:43', '1976-03-15 06:17:36', 1),
(4, 'erik81', '2439b2b2ca2eea482dccb3aee92f99585614f930', '1990-08-10 03:05:58', '2024-01-10 08:49:58', 1),
(5, 'mmarks', '6c700ac55e0f2be57b1fb47b170f662aafe3eb32', '1996-05-10 08:37:44', '2019-06-07 19:56:47', 1),
(6, 'johnnie.volkman', '3152e8a03f9bdc46e0255b85cc7458ca20013e61', '2015-09-24 09:56:38', '2019-01-30 04:02:16', 0),
(7, 'hveum', '326ec6a6b3940b0af6cdbf2d0e600bf406502f4c', '2005-02-02 16:36:02', '2020-06-07 03:27:29', 1),
(8, 'melyna.jacobi', '0a82b5e263d8b2a072c3c25c693254eaa25702a0', '2004-03-30 23:47:34', '1973-12-08 13:22:38', 0),
(9, 'irath', 'e85205bedc6568400f0655e7898ce35921a8ad2a', '2023-09-18 14:22:13', '1974-03-20 22:44:47', 0),
(10, 'miller.beulah', '991b751b4e121bd18708f5a993e194f992e31758', '2011-08-01 05:01:31', '1973-01-02 19:41:19', 1),
(11, 'nruecker', '032b848768925ba43a8337b8144fdb794c5ce5be', '1972-12-07 23:44:38', '1970-10-12 17:13:58', 1),
(12, 'hauck.elenor', 'a4af544d3e37c40357800f824ecac86573435272', '1991-10-07 09:05:37', '1991-12-28 09:36:49', 1),
(13, 'qkonopelski', 'a4939472f582a195cad190439238412b29c03e33', '1992-08-19 20:49:48', '2017-11-10 11:07:16', 0),
(14, 'ole82', 'f5bae9e0974f2777ce923df50301469fe3063d4e', '2002-11-14 02:58:09', '2018-01-03 20:52:58', 1),
(15, 'nmetz', 'fbb3b8bcef910f126cf6f46c43339ddc45334114', '1984-05-24 00:34:20', '2016-07-23 09:43:38', 1),
(16, 'raheem42', 'ae00507d491096867ad4ad2ee48690489334e0bb', '1973-01-30 04:12:13', '2020-03-01 09:00:27', 0),
(17, 'rdietrich', '04addd374478d33ce86902e669740b804d5e6ff7', '2018-07-06 09:15:22', '2010-11-05 22:52:43', 1),
(18, 'nichole.dickinson', '94ab7c47c70bcc1ed982d736059944f9a14f9e3b', '2015-05-26 15:17:36', '1995-02-17 07:16:25', 0),
(19, 'marquardt.heloise', '9f0d3715b6f2737cd7ccd1362a2748a4a63af386', '1998-11-22 07:07:07', '1970-11-09 09:25:30', 1),
(20, 'jazmyne.collins', 'b32d576e45da9b8560a21dce99d0c8930375ab82', '1999-06-23 05:50:56', '1997-09-23 08:31:30', 0),
(21, 'carmel26', '211e2633a8a19af7e0ad1734a083a45452d77d2c', '2020-01-28 00:26:52', '2006-10-02 08:00:59', 1),
(22, 'flatley.jaunita', '3c07c3c04a3eec0de3edf43017431b11b9e50148', '1972-09-24 11:29:38', '1994-12-03 02:09:24', 0),
(23, 'srodriguez', 'a20f36917940e9eba8253b00a9fba025386c5fff', '2011-02-10 02:38:53', '2007-01-01 12:18:39', 1),
(24, 'ccasper', '80e3b47b3f7fd3e68e84d6f639f8e85d646054cf', '1981-05-23 06:20:36', '1985-12-22 08:41:34', 1),
(25, 'tyshawn.mcglynn', '70be519fe5d51ae28fc4a62980b95b14d7bbcf9c', '2005-08-22 21:07:27', '2010-11-07 07:51:14', 1),
(26, 'hrobel', '18032e43fe094ab12e365cba7ff142663bc9d0ed', '1985-12-31 19:35:58', '1975-04-23 11:23:53', 1),
(27, 'gleason.brenden', 'ae62c7243184771dc0d9bb6a22a26880c6263e85', '1979-11-27 12:58:38', '1987-11-24 16:18:24', 0),
(28, 'keaton90', '8005f5e39741e5f2f70b44c8c738b31fe83bc88a', '2022-11-01 07:07:55', '2017-02-26 14:47:45', 0),
(29, 'jeanette94', 'f743d48767194688e8fd0fce4e0247222ed62723', '2000-11-18 02:24:18', '2014-08-04 16:53:34', 0),
(30, 'ufeil', 'ce61874e10c768d7fb711b9bf75a2a0cf33859e7', '2022-08-12 21:37:09', '1991-03-23 15:10:46', 1),
(31, 'white.leonor', '847ab4742e03207416d492aa8dc0a9830eb9a3e7', '1977-07-15 15:31:33', '2005-09-18 12:35:26', 0),
(32, 'langosh.larue', 'a224c0e0abc1e6928f251de9df9a4bdc93d90f85', '2005-10-14 12:57:03', '1987-03-03 10:34:33', 1),
(33, 'kreiger.alverta', 'b801cc107e0de6586cf80cbeeaee64a3d66f6351', '1997-08-04 15:15:14', '1975-10-28 09:11:15', 1),
(34, 'patsy34', 'a7017cb9e9d62269fb1e12c0b8d37f7a1d95db87', '2017-10-28 01:53:22', '2019-08-10 02:41:35', 0),
(35, 'schneider.geovanny', '7c23a94c20d1c10db4e7737b2c659c0d5f592a4a', '2010-07-06 23:57:48', '1992-05-22 21:22:35', 0),
(36, 'pmills', '6e0de31e447cae256509495962bb00a936bb7f10', '1986-04-10 03:28:47', '1991-11-21 21:28:07', 1),
(37, 'crawford.yundt', '7966e38d795b922399d48b676d29ba1046ad283f', '1983-07-09 06:59:21', '2000-01-10 15:35:37', 0),
(38, 'mills.robert', 'b59b336f880313b27ee61ff848d552190a620856', '1996-08-04 17:38:02', '2013-12-31 05:21:02', 1),
(39, 'jayce63', '5b77f9916edb03bc655b4b8acee04b409a89fd52', '2014-03-08 11:52:35', '1998-01-10 00:29:22', 1),
(40, 'owisozk', '8e5e8546476ea975393f0694cc545793ba17d96a', '1973-12-28 23:55:24', '2009-04-04 07:11:26', 0),
(41, 'oyost', '30edeb37184295f1f885a2af8cae512511d62ea2', '1995-09-06 19:53:27', '1975-09-13 23:18:55', 0),
(42, 'desmond.dickens', '46243bb455dc57281f3732e3a93bb86ff89b57f5', '2022-12-12 23:17:44', '2008-08-19 11:08:00', 0),
(43, 'chauncey04', '57a68738d79e97225978f3c70da56e30a7643035', '2023-11-26 05:31:38', '1981-12-16 17:19:47', 0),
(44, 'queenie.champlin', '363e74a38250c935128662b5d110d4c37ebc6ceb', '2023-02-03 08:20:22', '2003-11-24 06:45:05', 1),
(45, 'vella.stracke', 'fb983fd2ab7b4358d2195f09082781faf5dc70ec', '2019-04-29 03:21:20', '1970-09-11 17:29:17', 1),
(46, 'ollie.gusikowski', '1849dbbfbaf6b435bb6624fa35824fe460602ceb', '1971-05-02 11:14:48', '1983-11-28 19:31:27', 0),
(47, 'robin62', 'b7b01672352f8329d0ed235414082685a449b8c2', '2013-07-03 19:52:30', '1970-10-13 21:11:33', 1),
(48, 'oma79', 'ff7d17025e59a6a834735b13c1439f87fd03fb94', '1982-11-02 23:43:35', '1977-10-17 09:34:49', 0),
(49, 'xlegros', '573c62affabc774cd43ad9190d8827ae464fe381', '2013-10-23 03:31:14', '2003-03-16 03:33:03', 1),
(50, 'caufderhar', '88077fcf755b25fcebd7976cfc79e0cc02b4dc01', '1980-08-24 08:01:21', '1975-01-28 16:23:34', 1),
(51, 'mante.jena', 'a8b9000c3f0592af838142ad022c3adad4ff5b1d', '1991-03-31 04:29:01', '1983-09-11 19:15:23', 0),
(52, 'vcarroll', 'f9ce81367c8772370a4f72187e292843fba71e67', '1974-11-23 10:18:21', '1974-01-01 21:32:31', 0),
(53, 'benjamin.hilll', 'd1fc8f265167b7f1c4c5ced619031feab3de4948', '1983-11-06 17:53:36', '2008-08-23 10:16:28', 0),
(54, 'stiedemann.santiago', 'ccca4829a7740af8a9ad359182c29fc30da23ed7', '2023-01-06 19:25:59', '2010-03-09 02:53:07', 1),
(55, 'cruickshank.reymundo', '0b530c95f9268ae5723525a460e692fd143df526', '2002-01-19 06:56:10', '1987-04-05 05:58:11', 1),
(56, 'effie21', 'a024ab4f652ce750606ebeac043c6de645d5fc0f', '1982-11-23 07:28:07', '1994-12-26 01:09:48', 1),
(57, 'medhurst.agustina', '8666a8ec28bc8f762a9cecbb3c888278f52607ec', '2017-12-17 06:48:29', '1984-10-03 20:48:17', 0),
(58, 'amaya58', '963bcaf64ab49e564e4458d3751b76bbf6c765a8', '1994-06-30 22:02:36', '2015-03-23 12:31:31', 1),
(59, 'una.kshlerin', 'a4d8836d1cb2ad29913a2fe25a50382bf3d204be', '1976-04-14 23:17:03', '2009-02-25 16:10:52', 0),
(60, 'ghintz', '554854b7ea9547d5c97660a58c4d129cf18b5f32', '2017-09-27 08:42:15', '2001-01-12 13:34:50', 0),
(61, 'darion72', '2d1e655a937b746701314b0bae4dfc4757c24467', '1997-10-07 03:44:22', '2008-10-11 17:54:59', 1),
(62, 'murphy.vivienne', '68bbaf7a377a242138f56e39c71ccc07fb538f91', '1999-01-18 00:56:51', '1970-09-10 11:58:52', 0),
(63, 'ewell09', '17bfd8b2671eb79893d8955fb9c24d78a4ae7713', '2011-12-11 22:17:35', '2016-12-07 03:05:57', 0),
(64, 'czemlak', 'cf3a101e27a029fe97efffc3e09aad2cce6f201d', '1976-05-21 16:43:10', '1973-12-18 16:13:35', 1),
(65, 'sister95', '483c4d16791a179b35b3455e33f64edc3a14d925', '2012-05-31 03:35:19', '2014-12-02 14:18:43', 1),
(66, 'jacobi.eileen', 'f7a463e275f675c634eb2b31fa648ad733b377ec', '1983-08-31 04:50:21', '1994-11-30 18:58:42', 0),
(67, 'haley.swift', '23fc35f0c13b1f5a1abe8626cb331aed0e23348b', '1974-05-13 05:28:17', '2004-07-23 02:26:57', 0),
(68, 'nathaniel.bruen', '14cfb7e6a5dfd174397d7dc4a4a926cadc5d5699', '2000-07-26 14:30:25', '1975-08-18 13:02:18', 0),
(69, 'yjohns', '0c02515a4ae94a95decdd2be1763126e19dca15c', '2017-09-21 04:36:27', '2021-10-29 08:58:05', 1),
(70, 'mccullough.gisselle', '423e280f9c7a44b542ee27be07c0cd3da01c4ad8', '1979-06-01 14:28:07', '1997-02-10 08:10:37', 1),
(71, 'kassulke.katelynn', '034bed11a14e93cefcb6d04a46e9b864759375a2', '2002-02-06 17:28:34', '2003-06-14 11:05:31', 1),
(72, 'alexie23', 'ebf63c6faa43f7d8935f994865c0468294e3b00d', '1999-12-06 06:42:12', '2019-12-02 02:41:50', 1),
(73, 'arden.zemlak', '1194c9c0dbfdcb689265983eb775b94a496f187e', '2012-04-15 21:11:28', '1977-02-21 20:22:18', 1),
(74, 'xrunolfsdottir', 'fe9ce578f4201c90ceee0eb382c1d784941a8703', '1971-05-04 12:22:09', '1990-10-10 15:37:44', 1),
(75, 'raul75', '13723bdb2d90d59103e02211df200c819c86dc23', '2003-02-23 05:15:31', '1972-10-29 20:27:18', 0),
(76, 'georgiana28', '0bd5fc5b7fad3e485d1a5aca232068a92d17dc06', '1979-10-27 22:49:51', '2004-09-20 21:40:18', 0),
(77, 'cormier.dean', 'e1855a25c7b5fe6d68b891dcf697496493942fce', '1992-01-20 16:34:17', '1982-05-19 00:43:34', 0),
(78, 'katelin.dooley', 'ae22e58b5e06f0a1f86ccba03ea06f1d380a0e04', '1978-07-17 12:04:24', '1976-04-10 13:01:06', 0),
(79, 'worn', '95348d8544709cc3ce5b16f5f3329ae104aa8ef0', '1976-10-08 04:13:35', '2012-12-12 05:16:15', 1),
(80, 'yconnelly', '096d44a31535cd7bc8b325d70aba0e433d73cfba', '1977-03-07 16:30:15', '1985-04-17 02:33:47', 1),
(81, 'mariano97', 'f0b949e2a628c120d4cc26d52da0075dc9dd9b3f', '1995-02-11 18:43:24', '1988-11-24 05:35:59', 0),
(82, 'valentine.gulgowski', 'ccd2a2054a70952596df1babca191d597cc05ade', '1981-11-09 02:20:20', '2004-08-29 09:42:54', 1),
(83, 'qsteuber', '3f7dfbab9fe21e74989f528a271e5972d62f4293', '1977-04-07 10:17:18', '2004-09-29 07:21:27', 1),
(84, 'henri86', 'cc61b33b9bb5d42a77df436b5b678a3e9a209aca', '1972-09-22 11:14:04', '1999-10-06 06:42:33', 1),
(85, 'sharris', 'cceefda8e8474c4dfce32d6272531f9b8c14f312', '1987-06-30 01:43:07', '1986-08-10 14:28:16', 0),
(86, 'letha.cassin', '9f0db24308070dc01a4b5a5594f6df67a6713061', '1989-05-01 06:27:20', '2006-11-12 04:16:57', 0),
(87, 'okuneva.dovie', '44fde7c37d102526a478b9a10c5285ec1423ce65', '1985-10-04 13:57:59', '1998-06-09 14:03:58', 0),
(88, 'yking', '18af1268ea7d2248e0b95850254b42ac69815187', '1978-12-19 20:42:51', '1976-02-25 16:19:47', 1),
(89, 'octavia.bayer', '128c0391461d8b51eb1bc7724aa9a34d9bfbf99c', '2023-03-12 19:06:08', '1994-10-23 05:08:29', 1),
(90, 'ashields', '580db9cb1a133380733d929571a142504576c7de', '2005-04-24 06:08:19', '2023-09-10 15:31:55', 1),
(91, 'angeline.wiza', 'b2525ed7207ca5fa0d5f88d0112b9493925c6f93', '1978-07-20 20:20:15', '2008-12-21 21:50:55', 1),
(92, 'xcollins', 'd94993dc8e244d85f8b47f41f26062e38861faa8', '2012-01-20 14:01:15', '1990-12-18 11:40:31', 0),
(93, 'bartoletti.mathew', '7b9d6144b405c57a29ea3e97e93e4776d74e923b', '2012-10-26 11:43:44', '2008-08-14 03:49:58', 1),
(94, 'vidal.wiegand', 'fc09fe2004490751361072f9b380f1b74701c4a3', '2022-03-20 03:39:22', '2001-01-05 13:26:10', 1),
(95, 'augustine07', 'b658a0510ae74974a253d7ae088353491ba7418f', '1970-11-08 03:32:09', '2005-03-31 15:04:32', 1),
(96, 'elsie82', '18ba60fa7e8ce667413e4abaff30481bdaa12d2d', '1973-01-24 06:28:04', '1999-12-11 08:16:25', 0),
(97, 'kprosacco', '481013de0b7d340ade6d46dcb484fd6d262281a8', '2006-02-20 01:34:17', '2020-09-01 08:05:30', 0),
(98, 'luther50', '6974098bdc458d2bddec0f388e3cfcc324c620fe', '2011-11-13 21:12:05', '1978-07-06 15:34:13', 1),
(99, 'francis.abernathy', '6255038cc03292c32a2f5cc4d9e34b269cb58a2d', '2008-03-06 06:27:10', '1972-07-20 19:37:00', 1),
(100, 'kirstin90', 'd775a17fd94c27c6a38b691c9d5361b266f1e189', '1995-02-24 18:51:58', '2004-12-05 01:32:49', 1),
(101, 'uwunsch', '955e22077e4e08efa18b72b1b9ec43c96626f475', '2019-12-07 16:46:11', '2001-06-04 13:16:04', 0),
(102, 'russ.lindgren', '6af18453099089987ee252115c12d4ab8a662491', '2014-03-24 01:05:35', '1972-06-09 11:17:28', 1),
(103, 'vanessa.reilly', 'f1a3f6c8760f5b44ae5768b6bc1b25b835273571', '1986-05-02 09:23:42', '1985-06-12 19:26:23', 0),
(104, 'carlotta.reichel', '14a08bb175f721cbbcf09e426f9eb1811a2efe12', '2016-12-18 04:05:36', '1989-10-21 10:15:53', 1),
(105, 'nicolette11', '8cc515a36b053bd286c1d7978f7f0dd02fd25c36', '1989-10-03 21:28:00', '2022-12-31 21:48:18', 0),
(106, 'nwisoky', '707b28882ca17b658d94263d775185549bae3151', '1975-06-05 12:39:05', '1976-04-21 12:08:48', 1),
(107, 'eliane63', '8416cb7f41378ccb17436bbca6ba4ad2abb1f263', '2009-03-05 03:42:32', '1999-10-08 10:43:17', 0),
(108, 'o\'keefe.everette', '2b3e016f6980a8dd985d177f4001916799acf0c7', '2003-02-27 09:02:38', '1984-05-06 19:20:17', 0),
(109, 'dora97', '4727455df92a4f393071d87bdb3c250f24e4d283', '1997-06-21 22:22:49', '1994-01-28 08:57:00', 0),
(110, 'gage.dooley', '7fb6e6caaa91400f06599712196c981b86e5916b', '2010-11-17 12:31:08', '1970-01-05 05:59:28', 0),
(111, 'corbin39', '97e14abb265e1e0dab7d1a1ff834fdc241c3a8d3', '1997-12-14 13:02:19', '1999-01-11 21:15:03', 0),
(112, 'kbahringer', 'c48e6a690ed0954b19e2630eccb8dce173d3cdf0', '2017-04-12 10:49:47', '1971-04-05 14:58:41', 1),
(113, 'friesen.quincy', 'f75c2a7a583ec8586d5b6dfcd32f66c498cef27d', '1983-06-27 19:34:47', '2021-12-23 23:04:54', 0),
(114, 'armani56', '12175e2923a33588d99fc7e78b13f5f348cf5026', '2016-12-17 18:02:09', '1987-05-19 21:26:00', 0),
(115, 'gerlach.mona', '0ac7b4203225bdf306f760994e5c2b7b12f99e04', '1989-11-03 12:42:04', '1995-05-19 01:44:15', 1),
(116, 'adams.jeramie', '15b6ecc437452da1faebfad7b8137a213083dbad', '1999-10-13 02:37:38', '2012-01-22 12:01:28', 1),
(117, 'vtreutel', 'e9905db537427c6e22be1199297f719f5292086b', '2014-12-04 06:56:15', '1978-04-05 20:41:58', 0),
(118, 'vpaucek', '6297accf4bc57f3546d947cbdc1143ed3d563b20', '2009-02-13 18:49:24', '2014-02-12 12:39:01', 1),
(119, 'kemmer.patsy', '5e2f1be095b99e4c39f06e9fa528fae184d41f44', '1975-11-15 04:28:01', '2003-10-27 04:11:54', 1),
(120, 'laurine84', '31cf6ae7844dd4eedf1a42d75320a5128b47b5c1', '1977-01-03 05:18:39', '1976-07-17 12:09:51', 0),
(121, 'ekreiger', 'f077bae4cf183318aa76165050c0486573d1aff5', '1977-05-16 13:55:17', '2021-11-08 14:49:30', 0),
(122, 'ro\'hara', '01d22b869cdade8df78374a7d496e5d0e72a209c', '1978-04-24 03:02:13', '2017-10-18 20:57:09', 0),
(123, 'lisa70', '690dda25e026d738d26de9c030f03e66f5adba10', '1972-10-03 04:13:30', '1993-11-27 07:26:27', 1),
(124, 'freddy27', 'ca1efb287332eb70567dd823dc4614407a7c90fe', '1987-03-24 18:08:33', '1970-04-05 17:36:47', 1),
(125, 'zboncak.mason', '425cfaa1c60812a5816150bdbf82775d0dbcc7ab', '2013-01-01 10:15:31', '1985-04-25 11:29:22', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD KEY `fk_category_place_id` (`place_id`);

--
-- Indexes for table `friend`
--
ALTER TABLE `friend`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD KEY `fk_source_friend_id` (`source_friend_id`),
  ADD KEY `fk_target_friend_id` (`target_friend_id`);

--
-- Indexes for table `place`
--
ALTER TABLE `place`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD KEY `fk_user_id` (`user_id`);

--
-- Indexes for table `tag`
--
ALTER TABLE `tag`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD KEY `fk_tag_place_id` (`place_id`),
  ADD KEY `fk_friend_id` (`friend_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=78;

--
-- AUTO_INCREMENT for table `friend`
--
ALTER TABLE `friend`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `place`
--
ALTER TABLE `place`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- AUTO_INCREMENT for table `tag`
--
ALTER TABLE `tag`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=130;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `category`
--
ALTER TABLE `category`
  ADD CONSTRAINT `fk_category_place_id` FOREIGN KEY (`place_id`) REFERENCES `place` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `friend`
--
ALTER TABLE `friend`
  ADD CONSTRAINT `fk_source_friend_id` FOREIGN KEY (`source_friend_id`) REFERENCES `user` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_target_friend_id` FOREIGN KEY (`target_friend_id`) REFERENCES `user` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `place`
--
ALTER TABLE `place`
  ADD CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `tag`
--
ALTER TABLE `tag`
  ADD CONSTRAINT `fk_friend_id` FOREIGN KEY (`friend_id`) REFERENCES `user` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_tag_place_id` FOREIGN KEY (`place_id`) REFERENCES `place` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
