-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- 主機: 127.0.0.1
-- 產生時間： 2019 年 03 月 26 日 18:39
-- 伺服器版本: 10.1.31-MariaDB
-- PHP 版本： 7.2.4

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
-- 資料表結構 `ex_user`
--

CREATE TABLE `ex_user` (
  `id` bigint(11) UNSIGNED NOT NULL,
  `unid` char(33) NOT NULL,
  `name` varchar(50) NOT NULL COMMENT '姓名',
  `email` varchar(255) NOT NULL COMMENT '信箱',
  `pwd` char(32) NOT NULL COMMENT '密碼',
  `age` tinyint(3) UNSIGNED NOT NULL COMMENT '年齡區間',
  `sex` char(1) NOT NULL DEFAULT 'M' COMMENT '性別:M:男;W:女',
  `area_id` int(11) UNSIGNED NOT NULL COMMENT '區域',
  `add_date` datetime NOT NULL COMMENT '加入時間',
  `login_time` datetime NOT NULL COMMENT '登入時間',
  `logout_time` datetime NOT NULL COMMENT '登出時間'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `ex_user`
--

INSERT INTO `ex_user` (`id`, `unid`, `name`, `email`, `pwd`, `age`, `sex`, `area_id`, `add_date`, `login_time`, `logout_time`) VALUES
(1, 'm185ccab81019a39cba16f666f070bb83', '張小姐', 'jellyandjar@yahoo.com.tw', '9fab6755cd2e8817d3e73b0978ca54a6', 35, 'W', 282, '2018-12-30 10:22:00', '2018-12-30 10:22:00', '0000-00-00 00:00:00'),
(2, 'm1b414f0be20777c30e0423f441b09db8', '郭先生', 'jellyandjar@yahoo.com.tw', '9fab6755cd2e8817d3e73b0978ca54a6', 25, 'M', 304, '2018-12-30 10:22:00', '2018-12-30 10:22:00', '0000-00-00 00:00:00'),
(3, 'm8456fba48ba8c14bdd683e92c7414dc8', '劉先生', 'jellyandjar@yahoo.com.tw', '9fab6755cd2e8817d3e73b0978ca54a6', 35, 'M', 304, '2018-12-30 10:22:00', '2018-12-30 10:22:00', '0000-00-00 00:00:00'),
(4, 'mc741ce94208d215dc1a80e40c5456cf1', '陳先生', 'jellyandjar@yahoo.com.tw', '9fab6755cd2e8817d3e73b0978ca54a6', 30, 'M', 282, '2018-12-30 10:22:00', '2018-12-30 10:22:00', '0000-00-00 00:00:00'),
(5, 'mf82803bf01099c75ac76e774d685b2dc', '潘先生', 'jellyandjar@yahoo.com.tw', '9fab6755cd2e8817d3e73b0978ca54a6', 25, 'M', 276, '2018-12-30 10:22:00', '2018-12-30 10:22:00', '0000-00-00 00:00:00'),
(6, 'm9e3954249a75ceccc925c5b11a9ab970', '張小姐', 'jellyandjar@yahoo.com.tw', '9fab6755cd2e8817d3e73b0978ca54a6', 30, 'W', 284, '2018-12-30 10:22:00', '2018-12-30 10:22:00', '0000-00-00 00:00:00'),
(7, 'm199cdc39ee6e65811960a187ccf1fcb9', '鍾先生', 'jellyandjar@yahoo.com.tw', '9fab6755cd2e8817d3e73b0978ca54a6', 30, 'M', 304, '2018-12-30 10:22:00', '2018-12-30 10:22:00', '0000-00-00 00:00:00'),
(8, 'mdfef0a5faf8377eda852a592f32fc71b', '黃先生', 'jellyandjar@yahoo.com.tw', '9fab6755cd2e8817d3e73b0978ca54a6', 30, 'M', 251, '2019-01-05 23:26:05', '2019-01-05 23:26:05', '0000-00-00 00:00:00'),
(9, 'mca3907edc888d46215b3a35c294e73fa', '蕭先生', 'jellyandjar@yahoo.com.tw', '9fab6755cd2e8817d3e73b0978ca54a6', 25, 'M', 304, '2019-01-05 23:26:05', '2019-01-05 23:26:05', '0000-00-00 00:00:00'),
(10, 'm6bb771cd12d1658a7e26b3c63632d8f7', '辛先生', 'jellyandjar@yahoo.com.tw', '9fab6755cd2e8817d3e73b0978ca54a6', 30, 'M', 283, '2019-01-08 11:42:12', '2019-01-08 11:42:12', '0000-00-00 00:00:00'),
(11, '7f16a3540e74b904ed3ee626c79af314', '林先生', 'jellyandjar@yahoo.com.tw', '9fab6755cd2e8817d3e73b0978ca54a6', 35, 'M', 282, '2019-03-26 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00');

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `ex_user`
--
ALTER TABLE `ex_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`unid`,`email`) USING BTREE;

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `ex_user`
--
ALTER TABLE `ex_user`
  MODIFY `id` bigint(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
