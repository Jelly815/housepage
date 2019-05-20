-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- 主機: 127.0.0.1
-- 產生時間： 2019-05-20 03:25:10
-- 伺服器版本: 10.1.36-MariaDB
-- PHP 版本： 5.6.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `myweb`
--

-- --------------------------------------------------------

--
-- 資料表結構 `ex_record_items_stay`
--

CREATE TABLE `ex_record_items_stay` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `record_items_id` bigint(20) UNSIGNED NOT NULL COMMENT 'ex_record_items.id',
  `type_key` char(15) NOT NULL COMMENT '紀錄類型',
  `type_value` int(11) NOT NULL COMMENT '紀錄次數(值)'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='搜尋物件停留時間';

--
-- 資料表的匯出資料 `ex_record_items_stay`
--

INSERT INTO `ex_record_items_stay` (`id`, `record_items_id`, `type_key`, `type_value`) VALUES
(1, 1, 'stay_time', 180),
(2, 2, 'stay_time', 180),
(3, 3, 'stay_time', 20),
(4, 4, 'stay_time', 15),
(5, 5, 'stay_time', 21),
(6, 6, 'stay_time', 30),
(7, 7, 'stay_time', 60),
(8, 8, 'stay_time', 35),
(9, 9, 'stay_time', 50),
(10, 10, 'stay_time', 60),
(11, 11, 'stay_time', 111),
(12, 12, 'stay_time', 180),
(13, 13, 'stay_time', 20),
(14, 14, 'stay_time', 30),
(15, 15, 'stay_time', 180),
(16, 16, 'stay_time', 10),
(17, 17, 'stay_time', 20),
(18, 18, 'stay_time', 30),
(19, 19, 'stay_time', 40),
(20, 20, 'stay_time', 50),
(21, 21, 'stay_time', 180),
(22, 22, 'stay_time', 10),
(23, 23, 'stay_time', 20),
(24, 24, 'stay_time', 30),
(25, 25, 'stay_time', 700),
(26, 26, 'stay_time', 600),
(27, 27, 'stay_time', 500),
(28, 28, 'stay_time', 400),
(29, 29, 'stay_time', 300),
(30, 30, 'stay_time', 15),
(31, 31, 'stay_time', 30),
(32, 1, 'stay_time', 30),
(33, 1, 'stay_time', 65),
(34, 1, 'stay_time', 120),
(35, 1, 'stay_time', 30),
(36, 1, 'stay_time', 65),
(37, 1, 'stay_time', 120),
(38, 1, 'stay_time', 30),
(39, 2, 'stay_time', 30),
(40, 2, 'stay_time', 65),
(41, 2, 'stay_time', 120),
(42, 2, 'stay_time', 30),
(43, 12, 'stay_time', 30),
(44, 12, 'stay_time', 65),
(45, 12, 'stay_time', 120),
(46, 12, 'stay_time', 30),
(47, 15, 'stay_time', 30),
(48, 15, 'stay_time', 65),
(49, 15, 'stay_time', 120),
(50, 15, 'stay_time', 30),
(51, 21, 'stay_time', 30),
(52, 21, 'stay_time', 65),
(53, 21, 'stay_time', 120),
(54, 21, 'stay_time', 30),
(55, 25, 'stay_time', 30),
(56, 25, 'stay_time', 65),
(57, 25, 'stay_time', 300),
(58, 25, 'stay_time', 150),
(59, 25, 'stay_time', 120),
(60, 26, 'stay_time', 30),
(61, 26, 'stay_time', 65),
(62, 26, 'stay_time', 300),
(63, 26, 'stay_time', 150),
(64, 26, 'stay_time', 120),
(65, 26, 'stay_time', 40),
(66, 26, 'stay_time', 110),
(67, 26, 'stay_time', 200),
(68, 26, 'stay_time', 80),
(69, 32, 'stay_time', 20),
(70, 33, 'stay_time', 600),
(71, 33, 'stay_time', 300),
(72, 33, 'stay_time', 60),
(73, 34, 'stay_time', 600),
(74, 34, 'stay_time', 300),
(75, 34, 'stay_time', 60),
(76, 35, 'stay_time', 20),
(77, 36, 'stay_time', 600),
(78, 36, 'stay_time', 300),
(79, 36, 'stay_time', 60),
(80, 37, 'stay_time', 600),
(81, 37, 'stay_time', 300),
(82, 37, 'stay_time', 60),
(83, 38, 'stay_time', 600),
(84, 38, 'stay_time', 300),
(85, 38, 'stay_time', 60),
(86, 39, 'stay_time', 600),
(87, 39, 'stay_time', 300),
(88, 39, 'stay_time', 60),
(89, 40, 'stay_time', 600),
(90, 40, 'stay_time', 300),
(91, 40, 'stay_time', 60),
(92, 41, 'stay_time', 300),
(93, 41, 'stay_time', 100),
(94, 41, 'stay_time', 200),
(95, 42, 'stay_time', 300),
(96, 42, 'stay_time', 400),
(97, 42, 'stay_time', 500),
(98, 42, 'stay_time', 600),
(99, 42, 'stay_time', 200),
(100, 43, 'stay_time', 300),
(101, 43, 'stay_time', 400),
(102, 43, 'stay_time', 500),
(103, 43, 'stay_time', 600),
(104, 43, 'stay_time', 200),
(105, 43, 'stay_time', 100),
(106, 44, 'stay_time', 300),
(107, 44, 'stay_time', 400),
(108, 44, 'stay_time', 500),
(109, 44, 'stay_time', 600),
(110, 44, 'stay_time', 200),
(111, 44, 'stay_time', 100),
(112, 44, 'stay_time', 60),
(113, 44, 'stay_time', 150),
(114, 45, 'stay_time', 180),
(115, 45, 'stay_time', 120),
(116, 45, 'stay_time', 100),
(117, 46, 'stay_time', 180),
(118, 46, 'stay_time', 60),
(119, 46, 'stay_time', 30),
(120, 47, 'stay_time', 150),
(121, 48, 'stay_time', 300),
(122, 48, 'stay_time', 200),
(123, 48, 'stay_time', 100),
(124, 48, 'stay_time', 50),
(125, 48, 'stay_time', 30),
(126, 49, 'stay_time', 300),
(127, 49, 'stay_time', 200),
(128, 49, 'stay_time', 100),
(129, 49, 'stay_time', 60),
(130, 49, 'stay_time', 60),
(131, 50, 'stay_time', 100),
(132, 51, 'stay_time', 150),
(133, 52, 'stay_time', 150),
(134, 53, 'stay_time', 300),
(135, 53, 'stay_time', 300),
(136, 54, 'stay_time', 400),
(137, 54, 'stay_time', 400),
(138, 55, 'stay_time', 20),
(139, 56, 'stay_time', 300),
(140, 56, 'stay_time', 150),
(141, 56, 'stay_time', 100),
(142, 56, 'stay_time', 60),
(143, 56, 'stay_time', 30),
(144, 57, 'stay_time', 150),
(145, 58, 'stay_time', 150),
(146, 59, 'stay_time', 300),
(147, 59, 'stay_time', 150),
(148, 59, 'stay_time', 100),
(149, 59, 'stay_time', 60),
(150, 59, 'stay_time', 30),
(151, 7, 'stay_time', 45),
(152, 7, 'stay_time', 100),
(153, 60, 'stay_time', 60),
(154, 61, 'stay_time', 60),
(155, 60, 'price', 1),
(156, 60, 'map', 1),
(157, 60, 'parking', 1),
(158, 60, 'description', 1),
(159, 60, 'unit', 1),
(160, 61, 'price', 1),
(161, 61, 'description', 1),
(162, 61, 'style', 1),
(163, 61, 'map', 1),
(164, 61, 'direction', 1),
(165, 61, 'parking', 1),
(166, 79, 'price', 1),
(167, 79, 'stay_time', 18);

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `ex_record_items_stay`
--
ALTER TABLE `ex_record_items_stay`
  ADD PRIMARY KEY (`id`),
  ADD KEY `record_items_id` (`record_items_id`,`type_value`) USING BTREE;

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `ex_record_items_stay`
--
ALTER TABLE `ex_record_items_stay`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=168;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
