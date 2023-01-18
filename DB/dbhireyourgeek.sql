-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 17, 2022 at 07:15 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbhireyourgeek`
--

-- --------------------------------------------------------

--
-- Table structure for table `project`
--

CREATE TABLE `project` (
  `proid` int(11) NOT NULL,
  `rid` int(11) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  `project` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `project`
--

INSERT INTO `project` (`proid`, `rid`, `cid`, `project`) VALUES
(1, 6, 3, '/media/RAD%20REPORT%20FAIR%20(1).pdf');

-- --------------------------------------------------------

--
-- Table structure for table `tblbid`
--

CREATE TABLE `tblbid` (
  `bidid` int(11) NOT NULL,
  `rid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `duedate` date NOT NULL,
  `amt` int(11) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblbid`
--

INSERT INTO `tblbid` (`bidid`, `rid`, `cid`, `duedate`, `amt`, `status`) VALUES
(1, 2, 1, '2022-03-30', 20000, '100 percent complete'),
(2, 5, 2, '2022-05-18', 10000, '100 percent complete'),
(3, 6, 3, '2022-05-29', 50000, '100 percent complete');

-- --------------------------------------------------------

--
-- Table structure for table `tblbuyer`
--

CREATE TABLE `tblbuyer` (
  `bid` int(11) NOT NULL,
  `bname` varchar(50) NOT NULL,
  `baddress` varchar(50) NOT NULL,
  `bemail` varchar(50) NOT NULL,
  `bcontact` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblbuyer`
--

INSERT INTO `tblbuyer` (`bid`, `bname`, `baddress`, `bemail`, `bcontact`) VALUES
(1, 'Sijo John', 'aynikkal', 'sijo@gmail.com', 8080808080),
(2, 'carol jo', 'ABC villa', 'carol@gmail.com', 8908908908),
(3, 'Arun', 'Arun\r\nadrs', 'arun@mail.com', 9090909090),
(4, 'Chandu', 'Chan\r\nAdrs', 'chan@mail.com', 9999999999);

-- --------------------------------------------------------

--
-- Table structure for table `tblcoder`
--

CREATE TABLE `tblcoder` (
  `cid` int(11) NOT NULL,
  `cname` varchar(50) NOT NULL,
  `caddress` varchar(50) NOT NULL,
  `cemail` varchar(50) NOT NULL,
  `ccontact` bigint(20) NOT NULL,
  `cqualification` varchar(50) NOT NULL,
  `cexperience` varchar(50) NOT NULL,
  `cbio` varchar(100) NOT NULL,
  `cimg` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblcoder`
--

INSERT INTO `tblcoder` (`cid`, `cname`, `caddress`, `cemail`, `ccontact`, `cqualification`, `cexperience`, `cbio`, `cimg`) VALUES
(1, 'cera', 'Rose villa', 'cera@gmail.com', 8080808080, 'Mtech', '2 year', '/media/banner2%20(3).jpg', '/media/lady%20(1).jpg'),
(2, 'Fiza', 'Fiza\r\nAdrs', 'fiza@mail.com', 9898989898, 'BCA', '2', '/media/WhatsApp%20Image%202022-04-19%20at%2012.04.45%20PM%20(1)%20(3)%20(1).jpeg', '/media/pexels-gabriel-peter-719396_i6VmABy.jpg'),
(3, 'Khadheeja', 'Kha\r\nAdrs', 'kha@mail.com', 8888888888, 'MCA', '4', '/media/WhatsApp%20Image%202022-04-19%20at%2012.04.45%20PM%20(1)%20(4)_urGniqF.jpeg', '/media/pexels-gabriel-peter-719396_i6VmABy.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `tbllogin`
--

CREATE TABLE `tbllogin` (
  `uname` varchar(50) NOT NULL,
  `pwd` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbllogin`
--

INSERT INTO `tbllogin` (`uname`, `pwd`, `utype`, `status`) VALUES
('sijo@gmail.com', 'sijo@123', 'buyer', '1'),
('admin@gmail.com', 'admin', 'admin', '1'),
('cera@gmail.com', 'cera@123', 'coder', '1'),
('carol@gmail.com', 'carol@123', 'buyer', '1'),
('arun@mail.com', 'Arun@12345', 'buyer', '1'),
('fiza@mail.com', 'Fz@12345', 'coder', '1'),
('chan@mail.com', 'Chan@12345', 'buyer', '1'),
('kha@mail.com', 'Kha@12345', 'coder', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tblpayment`
--

CREATE TABLE `tblpayment` (
  `pid` int(11) NOT NULL,
  `wid` int(11) NOT NULL,
  `date` date NOT NULL,
  `amt` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblpayment`
--

INSERT INTO `tblpayment` (`pid`, `wid`, `date`, `amt`) VALUES
(1, 3, '2022-03-15', 20000),
(2, 4, '2022-05-12', 10000),
(3, 5, '2022-05-16', 50000);

-- --------------------------------------------------------

--
-- Table structure for table `tblrequest`
--

CREATE TABLE `tblrequest` (
  `rid` int(11) NOT NULL,
  `bid` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `duedate` date NOT NULL,
  `rfile` varchar(100) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblrequest`
--

INSERT INTO `tblrequest` (`rid`, `bid`, `title`, `description`, `duedate`, `rfile`, `status`) VALUES
(2, 1, 'Melanomma', 'A cancer detection project', '2022-04-10', '/media/homeapplogo_OpZoeEy.jpg', '100 percent complete'),
(3, 2, 'Quality Control', 'An organization management based python project', '2022-04-10', '/media/userimages_lumbar-spine-ct-2.jpg', 'Requested'),
(4, 1, 'Pet care', 'An python project for pet care shop', '2022-03-30', '/media/userimages_lumbar-spine-ct-2.jpg', 'Requested'),
(5, 3, 'Website', 'E-commerce Website', '2022-05-19', '/media/WhatsApp%20Image%202022-04-19%20at%2012.04.45%20PM%20(1)%20(3)%20(1)_OMmcDjO.jpeg', '100 percent complete'),
(6, 4, 'ANDROID APP ', 'Djhgjhg jhguj\r\nhgjh', '2022-06-01', '/media/WhatsApp%20Image%202022-04-19%20at%2012.04.45%20PM%20(1)%20(4)_urGniqF_ZN2VGyT.jpeg', '100 percent complete');

-- --------------------------------------------------------

--
-- Table structure for table `tblwork`
--

CREATE TABLE `tblwork` (
  `wid` int(11) NOT NULL,
  `bidid` int(11) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblwork`
--

INSERT INTO `tblwork` (`wid`, `bidid`, `date`, `status`) VALUES
(3, 1, '2022-03-15', 'Completed'),
(4, 2, '2022-05-12', 'Completed'),
(5, 3, '2022-05-16', 'Completed');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `project`
--
ALTER TABLE `project`
  ADD PRIMARY KEY (`proid`);

--
-- Indexes for table `tblbid`
--
ALTER TABLE `tblbid`
  ADD PRIMARY KEY (`bidid`);

--
-- Indexes for table `tblbuyer`
--
ALTER TABLE `tblbuyer`
  ADD PRIMARY KEY (`bid`);

--
-- Indexes for table `tblcoder`
--
ALTER TABLE `tblcoder`
  ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `tblpayment`
--
ALTER TABLE `tblpayment`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `tblrequest`
--
ALTER TABLE `tblrequest`
  ADD PRIMARY KEY (`rid`);

--
-- Indexes for table `tblwork`
--
ALTER TABLE `tblwork`
  ADD PRIMARY KEY (`wid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `project`
--
ALTER TABLE `project`
  MODIFY `proid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tblbid`
--
ALTER TABLE `tblbid`
  MODIFY `bidid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tblbuyer`
--
ALTER TABLE `tblbuyer`
  MODIFY `bid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tblcoder`
--
ALTER TABLE `tblcoder`
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tblpayment`
--
ALTER TABLE `tblpayment`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tblrequest`
--
ALTER TABLE `tblrequest`
  MODIFY `rid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tblwork`
--
ALTER TABLE `tblwork`
  MODIFY `wid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
