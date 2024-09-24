-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 06, 2024 at 01:11 AM
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
-- Database: `social_media_platform`
--

-- --------------------------------------------------------

--
-- Table structure for table `logs`
--

CREATE TABLE `logs` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `comment` text NOT NULL,
  `classification` enum('Hate Speech','Offensive Language','Neither') NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `logs`
--

INSERT INTO `logs` (`id`, `username`, `comment`, `classification`, `timestamp`) VALUES
(1, 'user', 'I dont like black people', 'Hate Speech', '2024-08-12 07:13:08'),
(2, 'user', 'I dont like black people', 'Hate Speech', '2024-08-12 07:43:28'),
(3, 'shreyas', 'you are beutiful', 'Neither', '2024-08-12 09:10:54'),
(4, 'shreyas', 'Go back to your country', 'Hate Speech', '2024-08-12 09:11:18'),
(5, 'shreyas', 'bitch', 'Offensive Language', '2024-08-12 09:11:30'),
(10, 'user', 'hello', 'Neither', '2024-08-12 18:10:42'),
(11, 'user', 'You are genius', 'Neither', '2024-08-12 18:10:55'),
(12, 'user', 'You are motherfucker', 'Offensive Language', '2024-08-12 18:11:05'),
(13, 'shreyas', 'You are such an idiot', 'Hate Speech', '2024-08-13 17:23:21'),
(14, 'shreyas', 'You are such a moron', 'Hate Speech', '2024-08-13 17:23:33'),
(15, 'shreyas', 'I hate you face', 'Hate Speech', '2024-08-13 17:23:57'),
(16, 'shreyas', 'You are beautiful', 'Neither', '2024-09-05 20:06:12');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('admin','user') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `role`) VALUES
(1, 'admin', 'adminpass', 'admin'),
(2, 'user', 'userpass', 'user'),
(3, 'shreyas', '123', 'user');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `logs`
--
ALTER TABLE `logs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `logs`
--
ALTER TABLE `logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
