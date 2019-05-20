-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- 主機: 127.0.0.1
-- 產生時間： 2019-05-20 12:09:07
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
-- 資料表結構 `ex_around`
--

CREATE TABLE `ex_around` (
  `id` int(11) UNSIGNED NOT NULL,
  `name` varchar(50) NOT NULL,
  `sort` int(11) UNSIGNED NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='生活機能';

--
-- 資料表的匯出資料 `ex_around`
--

INSERT INTO `ex_around` (`id`, `name`, `sort`) VALUES
(1, '近便利商店', 0),
(2, '近傳統市場', 0),
(3, '近百貨公司', 0),
(4, '近公園綠地', 0),
(5, '近學校', 0),
(6, '近醫療機構', 0),
(7, '近夜市', 0),
(8, '重劃區', 0),
(9, '景觀宅', 0),
(10, '制震宅', 0),
(11, '低首付', 0),
(12, '預售屋', 0),
(16, '新成屋', 0),
(17, '住家用', 0),
(15, '捷運宅', 0),
(18, '明星學區', 0),
(19, '創意空間', 0),
(20, '低公設', 0),
(21, '商業用', 0),
(22, '預推案', 0);

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `ex_around`
--
ALTER TABLE `ex_around`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `ex_around`
--
ALTER TABLE `ex_around`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
