-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- 主機: 127.0.0.1
-- 產生時間： 2019-03-12 10:42:17
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
-- 資料表結構 `ex_record_items_obj`
--

CREATE TABLE `ex_record_items_obj` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `user_id` char(33) NOT NULL COMMENT 'ex_user.unid',
  `items` text NOT NULL COMMENT '物件JSON',
  `is_like` tinyint(1) UNSIGNED NOT NULL DEFAULT '0' COMMENT '0:不喜歡;1:喜歡'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `ex_record_items_obj`
--
ALTER TABLE `ex_record_items_obj`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `record_items_id` (`user_id`) USING BTREE;

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `ex_record_items_obj`
--
ALTER TABLE `ex_record_items_obj`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
