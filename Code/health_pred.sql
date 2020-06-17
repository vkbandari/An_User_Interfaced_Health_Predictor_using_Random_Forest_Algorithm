
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
--  Database : `health_predictor`
--

-- --------------------------------------------------------

--
-- Table structure for table `doctor_reg`
--

CREATE TABLE `doctor_reg` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(15) NOT NULL,
  `phnumber` varchar(50) NOT NULL,
  `hname` varchar(50) NOT NULL,
  `haddress` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `landmark` varchar(50) NOT NULL,
  `age` varchar(50) NOT NULL,
  `specailist` varchar(50) NOT NULL,
  `specification` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `date_of_reg` varchar(50) NOT NULL,
  `image` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctor_reg`
--

INSERT INTO `doctor_reg` (`id`, `name`, `email`, `password`, `phnumber`, `hname`, `haddress`, `city`, `landmark`, `age`, `specailist`, `specification`, `gender`, `date_of_reg`, `image`) VALUES
(1, 'poornima', 'poornima@gmail.com', 'doctor@1234', '4561239871', 'venkaateswara', 'tirupati, 123', 'tirupati', 'temple', '29', 'cardiologist', '', 'female', '2019-03-12 11:50:28.071682', ''),
(2, 'Dilip', 'dilip@gmail.com', 'doctor@1234', '9988774455', 'Apollo', 'bangalore', 'bangalore', 'Near GRT', '35', 'CARDIOLOGY', 'heart disease', 'male', '2020-02-24 14:22:17.934436', ''),
(3, 'Durga', 'durga@gmail.com', 'doctor@1234', '9876541234', 'medicare', 'mulugu road', 'warangal', 'busstop', '45', 'General', 'malaria', 'male', '2020-02-24 14:22:17.934436', '');

-- --------------------------------------------------------

--
-- Table structure for table `paitent_precautions`
--

CREATE TABLE `paitent_precautions` (
  `id` int(15) NOT NULL,
  `username` varchar(50) NOT NULL,
  `disease` varchar(20) NOT NULL,
  `precautions` varchar(1000) NOT NULL,
  `patient_a_id` int(10) NOT NULL,
  `user_email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `paitent_precautions`
--

INSERT INTO `paitent_precautions` (`id`, `username`, `disease`, `precautions`, `patient_a_id`, `user_email`) VALUES
(1, 'user', 'Dengue', '\r\n     hi good', 42, 'user1234@gmail.com'),
(2, 'user', 'Dengue', '\r\n     take a full bed rest\r\n', 42, 'user1234@gmail.com'),
(3, 'user', 'Dengue', '\r\n     health is good', 42, 'user1234@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `reg`
--

CREATE TABLE `reg` (
  `reg_id` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `phone_number` varchar(50) NOT NULL,
  `dob` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `user_type` varchar(50) NOT NULL,
  `reg_timedate` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reg`
--

INSERT INTO `reg` (`reg_id`, `username`, `email`, `password`, `phone_number`, `dob`, `address`, `city`, `user_type`, `reg_timedate`) VALUES
('Admin1546577899017', 'vamshikrishna', 'krishnavamshi.12321@gmail.com', 'vk@1234', '8919765647', '11/18/1993', 'H.no 3-13/b, warangal', 'Telangana', 'admin', 'Fri Jan  4 10:28:19 2019'),
('User1546578023622', 'vishnu', 'vishnu@gmail.com', 'vishnu@1234', '9865478936', '9/22/1994', 'd.no-10-12-15,balaji colony,Tirupati', 'Tirupati', 'user', 'Fri Jan  4 10:30:23 2019'),
('User1546578117244', 'praveen', 'praveen@gmail.com', 'hari@1234', '8659847815', '10/6/1992', 'plot.no 143,sai colony,Bangalore', 'Bangalore', 'user', 'Fri Jan  4 10:31:57 2019'),
('User1561696148372', 'naveen', 'naveen@gmail.com', 'naveen@1234', '7894561230', '2019-03-27', 'tirupati', 'tirupati', 'user', 'Fri Jun 28 09:59:08 2019'),
('User1561781245697', 'rama', 'rama@gmail.com', 'rama@1234', '8855669933', '2019-06-30', 'tirupati', 'tirupati', 'user', 'Sat Jun 29 09:37:25 2019'),
('User1566810473558', 'ramya', 'ramya@gmail.com', 'ramya@1234', '8965321470', '2019-08-26', 'tirupati', 'tirupati', 'user', 'Mon Aug 26 14:37:53 2019'),
('Admin1569215765192', 'malasree', 'malasree@gmail.com', 'malasree@1234', '8523697410', '2019-09-23', 'tpt', 'tpt', 'admin', 'Mon Sep 23 10:46:05 2019'),
('Admin1569215765193', 'nagalakshmi', 'nagalakshmi@gmail.com', 'nagalakshmi@1234', '8524597420', '2019-09-23', 'anathapur', 'anathapur', 'admin', 'Mon Sep 23 10:46:05 2019'),
('User1582374948659', 'mounika', 'mounika@gmail.com', 'mounika@123', '9632587410', '2020-02-22', 'tpt', 'tpt', 'user', 'Sat Feb 22 18:05:48 2020');

-- --------------------------------------------------------

--
-- Table structure for table `user_appointment`
--

CREATE TABLE `user_appointment` (
  `a_id` int(11) NOT NULL,
  `doctor_name` varchar(50) NOT NULL,
  `doctor_email` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `disease` varchar(50) NOT NULL,
  `pnumber` varchar(50) NOT NULL,
  `date_of_appointment` varchar(50) NOT NULL,
  `user_email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_appointment`
--

INSERT INTO `user_appointment` (`a_id`, `doctor_name`, `doctor_email`, `user_name`, `disease`, `pnumber`, `date_of_appointment`, `user_email`) VALUES
(1, 'poornima', '', 'vishnu', 'heart', '9632587410', '2019-03-09', ''),
(2, 'poornima', '', 'ramya', 'heart', '9632587410', '2019-03-09', ''),
(3, 'Durga', '', 'praveen', 'malaria', '9632587410', '2019-03-11', ''),
(4, 'Durga', '', 'naveen', 'dengue', '9632587410', '2019-03-11', ''),
(5, 'Dilip', '', 'naveen', 'dengue', '1238', '2019-03-21', ''),
(6, 'Durga', '', 'mounika', 'heart-disease', '1238', '', ''),
(7, 'Dilip', 'dilip@gmail.com', 'mounika', 'Dengue', '9988774455', '2020-02-24', 'user1234@gmail.com'),
(8, 'Dilip', 'dilip@gmail.com', 'rama', 'typhoid', '9988774455', '2020-02-24', 'user1234@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `doctor_reg`
--
ALTER TABLE `doctor_reg`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `paitent_precautions`
--
ALTER TABLE `paitent_precautions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_appointment`
--
ALTER TABLE `user_appointment`
  ADD PRIMARY KEY (`a_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `doctor_reg`
--
ALTER TABLE `doctor_reg`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `paitent_precautions`
--
ALTER TABLE `paitent_precautions`
  MODIFY `id` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `user_appointment`
--
ALTER TABLE `user_appointment`
  MODIFY `a_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
