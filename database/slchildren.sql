-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 01, 2019 at 01:46 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `slchildren`
--

-- --------------------------------------------------------

--
-- Table structure for table `rating`
--

CREATE TABLE `rating` (
  `rid` int(20) NOT NULL,
  `listening` int(5) NOT NULL,
  `reading` int(5) NOT NULL,
  `speaking` int(5) NOT NULL,
  `writing` int(5) NOT NULL,
  `disability` int(5) NOT NULL,
  `mobility` int(5) NOT NULL,
  `level` varchar(30) NOT NULL,
  `sid` int(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rating`
--

INSERT INTO `rating` (`rid`, `listening`, `reading`, `speaking`, `writing`, `disability`, `mobility`, `level`, `sid`) VALUES
(8, 5, 5, 4, 5, 5, 5, 'EXCELLENT', 1),
(9, 1, 1, 1, 1, 1, 1, 'LOW', 2),
(10, 1, 1, 1, 1, 1, 1, 'LOW', 3),
(11, 3, 2, 2, 2, 2, 3, 'NORMAL', 4),
(12, 4, 4, 3, 3, 3, 3, 'GOOD', 5);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `sid` int(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(100) NOT NULL,
  `tid` int(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`sid`, `name`, `email`, `password`, `tid`) VALUES
(1, 'mayur', 'mayur@gmail.com', '123456', 7),
(4, 'Prasad', 'prasad@gmail.com', '123456', 10),
(3, 'Francis', 'francis@gmail.com', '123456', 9),
(5, 'sebin', 'sebin@gmail.com', '123456', 11);

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `tid` int(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`tid`, `name`, `email`, `password`) VALUES
(1, 'madam', 'madam@slc.com', '123456'),
(2, 'madam', 'madam@slc.org', '123456'),
(3, 'madama', 'madam@sly.com', '123456789'),
(4, 'asdfg', 'sasfasdf@asd.com', '123456789'),
(5, 'madam', 'asdfg@qwer.vom', '123456789'),
(6, 'madam', 'asd@asd.nom', '123456789'),
(7, 'vijit', 'vijit@gmail.com', '123456'),
(8, 'ram', 'ram@gmail.com', '123456'),
(9, 'Jetso', 'jetso@gmail.com', '123456'),
(10, 'Yashwita', 'yashwita@gmail.com', '123456'),
(11, 'sapan', 'sapan@gmail.com', '123456');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `rating`
--
ALTER TABLE `rating`
  ADD PRIMARY KEY (`rid`),
  ADD KEY `sid` (`sid`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`sid`),
  ADD KEY `tid` (`tid`),
  ADD KEY `tid_2` (`tid`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`tid`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `tid` (`tid`),
  ADD KEY `tid_2` (`tid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `rating`
--
ALTER TABLE `rating`
  MODIFY `rid` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `sid` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `teacher`
--
ALTER TABLE `teacher`
  MODIFY `tid` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
