-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 01, 2025 at 07:10 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hostel`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(10) NOT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `Password` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `Name`, `Password`) VALUES
(1, 'Dormitory Haven', 'Dormitory25');

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `id` int(10) NOT NULL,
  `Book_Date` varchar(10) DEFAULT NULL,
  `room_no` int(10) DEFAULT NULL,
  `Student_Name` varchar(10) DEFAULT NULL,
  `Email` varchar(30) DEFAULT NULL,
  `Degree` varchar(10) DEFAULT NULL,
  `Year` varchar(10) DEFAULT NULL,
  `Department` varchar(60) DEFAULT NULL,
  `Roll_Number` int(10) DEFAULT NULL,
  `Status` varchar(10) DEFAULT NULL,
  `Rent` varchar(15) DEFAULT NULL,
  `Month` varchar(15) DEFAULT NULL,
  `Due_Date` varchar(10) DEFAULT NULL,
  `Payment_Date` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`id`, `Book_Date`, `room_no`, `Student_Name`, `Email`, `Degree`, `Year`, `Department`, `Roll_Number`, `Status`, `Rent`, `Month`, `Due_Date`, `Payment_Date`) VALUES
(1, '25-02-2025', 2, 'Priyanka', 'priyanka2005@gmil.com', 'BE', 'III year', 'Electronics and Communication Engineering', 62, 'Paid', '50,000', 'Per Semester', '2025-03-12', '10-03-2025'),
(2, '25-02-2025', 3, 'Dhaniya', 'dhaniya2006@gmail.com', 'BTech', 'II Year', 'Artificial Intelligence and Machine Learning', 88, 'Paid', '55,000', 'Per Semester', '2025-03-11', '10-03-2025'),
(3, '25-02-2025', 4, 'Harsha', 'harsha2004@gmail.com', 'BTech', 'IV Year', 'Electronics and Electrical Engineering', 102, 'Paid', '55,000', 'Per Semester', '2025-03-29', '20-03-2025'),
(4, '25-02-2025', 4, 'Nithiya', 'nithiya2007@gmail.com', 'BE', 'I year', 'Biomedical Engineering', 81, 'Paid', '60,000', 'Per Semester', '2025-04-05', '04-03-2025'),
(5, '25-02-2025', 1, 'Hema', 'hema2003@gmail.com', 'BTech', 'IV Year', 'Computer Science and Engineering', 77, 'Processing', '70,000', 'Per Semester', '2025-04-03', NULL),
(6, '25-02-2025', 2, 'Perma', 'perma2005@gmail.com', 'BE', 'II Year', 'Information Technology', 59, 'Booked', NULL, NULL, NULL, NULL),
(7, '28-02-2025', 2, 'Priyanka', 'priyanka2005@gmil.com', 'BE', 'III year', 'Electronics and Communication Engineering', 62, 'Booked', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `complaints`
--

CREATE TABLE `complaints` (
  `id` int(11) NOT NULL,
  `student_name` varchar(100) DEFAULT NULL,
  `room_number` varchar(10) DEFAULT NULL,
  `complaint_type` varchar(50) DEFAULT NULL,
  `issues` text DEFAULT NULL,
  `complaint_date` varchar(10) DEFAULT NULL,
  `Status` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `complaints`
--

INSERT INTO `complaints` (`id`, `student_name`, `room_number`, `complaint_type`, `issues`, `complaint_date`, `Status`) VALUES
(1, 'Priyanka', '2', 'maintenance', 'The air conditioner is not cooling properly.', '26-02-2025', 'Approved'),
(2, 'Priyanka', '2', 'food', 'The food is often cold and lacks variety.', '26-02-2025', 'Rejected'),
(3, 'Harsha', '4', 'maintenance', 'Lot of Problems', '27-02-2025', 'Complained'),
(4, 'Harsha', '4', 'food', 'There is a Insets in food', '27-02-2025', 'Complained');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL,
  `student_name` varchar(100) DEFAULT NULL,
  `room_no` varchar(10) DEFAULT NULL,
  `feedback_type` varchar(50) DEFAULT NULL,
  `overall_rating` varchar(50) DEFAULT NULL,
  `cleanliness` varchar(50) DEFAULT NULL,
  `food_quality` varchar(50) DEFAULT NULL,
  `issues` text DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`id`, `student_name`, `room_no`, `feedback_type`, `overall_rating`, `cleanliness`, `food_quality`, `issues`, `date`) VALUES
(1, 'Priyanka', '2', 'maintenance', 'Average', 'Good', 'None', 'The floor looks like it hasn\'t been cleaned properly.', '26-02-2025'),
(2, 'Priyanka', '2', 'food', 'Excellent', 'None', 'Good', 'Satisified', '26-02-2025'),
(3, 'Priyanka', '2', 'maintenance', 'Good', 'Good', 'None', 'There is a leakage in the bathroom sink.', '26-02-2025');

-- --------------------------------------------------------

--
-- Table structure for table `food_plan`
--

CREATE TABLE `food_plan` (
  `id` int(11) NOT NULL,
  `day` varchar(20) DEFAULT NULL,
  `breakfast` varchar(50) DEFAULT NULL,
  `lunch` varchar(50) DEFAULT NULL,
  `snacks` varchar(50) DEFAULT NULL,
  `dinner` varchar(50) DEFAULT NULL,
  `Status` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `food_plan`
--

INSERT INTO `food_plan` (`id`, `day`, `breakfast`, `lunch`, `snacks`, `dinner`, `Status`) VALUES
(1, 'Monday', 'Idly with Sambar & Chutney', 'Full Meals', 'Samosa with Tea/Milk', 'Dosa with Sambar & Chutney', 'New'),
(2, 'Tuesday', 'Idiyapam', 'Meals', 'Chips with Tea/Milk', 'Chapathi with Kuruma', 'New'),
(3, 'Wednesday', 'Ven Pongal with Sambar & Chutney', 'Meals', 'Bonda with Tea/Milk', 'Uppuma with Sambar & Chutney', 'New'),
(4, 'Thursday', 'Dosa with Sambar & Chutney', 'Meals', 'Crunchy Snack with Tea/Milk', 'Poori with Masala', 'New'),
(5, 'Friday', 'Idly with Sambar & Chutney', 'Full Meals', 'Samosa with Tea/Milk', 'Parotta', 'New'),
(6, 'Saturday', 'Bread with Jam and Puttu', 'Meals', 'Bonda with Tea/Milk', 'Dosa with Sambar & Chutney', 'Updated'),
(7, 'Sunday', 'Chapathi with Kuruma', 'Meals', 'Crunchy Snack with Tea/Milk', 'idly with Sambar & Chutney', 'New');

-- --------------------------------------------------------

--
-- Table structure for table `request`
--

CREATE TABLE `request` (
  `id` int(10) NOT NULL,
  `Registered_Date` varchar(10) DEFAULT NULL,
  `Order_Item` varchar(20) DEFAULT NULL,
  `Quantity` int(20) DEFAULT NULL,
  `Urgency_Level` varchar(10) DEFAULT NULL,
  `Supplier` varchar(30) DEFAULT NULL,
  `Expected_Date` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `request`
--

INSERT INTO `request` (`id`, `Registered_Date`, `Order_Item`, `Quantity`, `Urgency_Level`, `Supplier`, `Expected_Date`) VALUES
(1, '24-02-2025', 'Masala Items', 20, 'High', 'Murgan', '02-03-2025'),
(2, '24-02-2025', 'Vegetables', 120, 'Low', 'Kandha', '10-03-2025');

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `id` int(10) NOT NULL,
  `Date` varchar(10) NOT NULL,
  `Room_Number` varchar(10) DEFAULT NULL,
  `Occupancy` int(10) DEFAULT NULL,
  `Total_Capacity` int(20) DEFAULT NULL,
  `Status` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`id`, `Date`, `Room_Number`, `Occupancy`, `Total_Capacity`, `Status`) VALUES
(1, '21-02-2025', '1', 0, 5, 'New'),
(2, '21-02-2025', '2', 1, 4, 'New'),
(3, '21-02-2025', '3', 1, 4, 'New'),
(4, '22-02-2025', '4', 2, 4, 'New'),
(5, '27-02-2025', '5', 0, 4, 'New'),
(6, '27-02-2025', '6', 0, 4, 'New');

-- --------------------------------------------------------

--
-- Table structure for table `schedule_timing`
--

CREATE TABLE `schedule_timing` (
  `id` int(11) NOT NULL,
  `breakfast_from_time` varchar(10) DEFAULT NULL,
  `breakfast_to_time` varchar(10) DEFAULT NULL,
  `lunch_from_time` varchar(10) DEFAULT NULL,
  `lunch_to_time` varchar(10) DEFAULT NULL,
  `snacks_from_time` varchar(10) DEFAULT NULL,
  `snacks_to_time` varchar(10) DEFAULT NULL,
  `dinner_from_time` varchar(10) DEFAULT NULL,
  `dinner_to_time` varchar(10) DEFAULT NULL,
  `study_from_time` varchar(10) DEFAULT NULL,
  `study_to_time` varchar(10) DEFAULT NULL,
  `Status` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `schedule_timing`
--

INSERT INTO `schedule_timing` (`id`, `breakfast_from_time`, `breakfast_to_time`, `lunch_from_time`, `lunch_to_time`, `snacks_from_time`, `snacks_to_time`, `dinner_from_time`, `dinner_to_time`, `study_from_time`, `study_to_time`, `Status`) VALUES
(1, '07:45 AM', '08:30 AM', '01:00 PM', '01:45 PM', '05:00 PM', '05:30 PM', '06:30 PM', '07:15 PM', '06:30 PM', '07:15 PM', 'Updated');

-- --------------------------------------------------------

--
-- Table structure for table `stock`
--

CREATE TABLE `stock` (
  `id` int(10) NOT NULL,
  `Registered_Date` varchar(10) DEFAULT NULL,
  `Product_Item` varchar(20) DEFAULT NULL,
  `Quantity` int(20) DEFAULT NULL,
  `Supplier` varchar(30) DEFAULT NULL,
  `Received_Date` varchar(10) DEFAULT NULL,
  `Remarks` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stock`
--

INSERT INTO `stock` (`id`, `Registered_Date`, `Product_Item`, `Quantity`, `Supplier`, `Received_Date`, `Remarks`) VALUES
(1, '24-02-2025', 'Room Cleaning', 10, 'Raja', '23-02-2025', 'No damages reported in the stock.'),
(2, '24-02-2025', 'Oil', 20, 'Murgan', '22-02-2025', 'No damages reported in the stock.');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(10) NOT NULL,
  `Register_Date` varchar(10) DEFAULT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Date_of_Birth` varchar(15) DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `Phone_Number` bigint(10) DEFAULT NULL,
  `City` varchar(20) DEFAULT NULL,
  `State` varchar(10) DEFAULT NULL,
  `Current_Degree` varchar(10) DEFAULT NULL,
  `Year` varchar(10) DEFAULT NULL,
  `Department` varchar(80) DEFAULT NULL,
  `Roll_Number` int(30) DEFAULT NULL,
  `Profile` varchar(60) DEFAULT NULL,
  `Aadhaar` varchar(15) DEFAULT NULL,
  `Password` varchar(15) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `Register_Date`, `Name`, `Email`, `Date_of_Birth`, `Gender`, `Phone_Number`, `City`, `State`, `Current_Degree`, `Year`, `Department`, `Roll_Number`, `Profile`, `Aadhaar`, `Password`, `status`) VALUES
(1, '22-02-2025', 'Priyanka', 'priyanka2005@gmil.com', '2005-10-10', 'Female', 9795847468, 'Namakkal', 'TamilNadu', 'BE', 'III year', 'Electronics and Communication Engineering', 62, 'g1.jpg', '868685489589', 'Priya98', 'Unblocked'),
(2, '22-02-2025', 'Dhaniya', 'dhaniya2006@gmail.com', '2006-01-10', 'Female', 8939832983, 'Chennai', 'TamilNadu', 'BTech', 'II Year', 'Artificial Intelligence and Machine Learning', 88, 'g1.jpg', '893782912982', 'Dhaniya12', 'Unblocked'),
(3, '22-02-2025', 'Harsha', 'harsha2004@gmail.com', '2004-12-01', 'Female', 7878219812, 'Madurai', 'TamilNadu', 'BTech', 'IV Year', 'Electronics and Electrical Engineering', 102, 'g2.jpg', '892178219821', 'Harsha12', 'Unblocked'),
(4, '22-02-2025', 'Nithiya', 'nithiya2007@gmail.com', '2007-01-10', 'Female', 9783892389, 'Coimbatore', 'TamilNadu', 'BE', 'I year', 'Biomedical Engineering', 81, 'g2.jpg', '789128821788', 'Nithiya12', 'Unblocked'),
(5, '25-02-2025', 'Hema', 'hema2003@gmail.com', '2003-08-01', 'Female', 7893789189, 'Bangalore', 'TamilNadu', 'BTech', 'IV Year', 'Computer Science and Engineering', 77, 'g5.jpg', '892373489324', 'Hema12', 'Unblocked'),
(6, '25-02-2025', 'Perma', 'perma2005@gmail.com', '2005-08-08', 'Female', 8983278398, 'Chennai', 'TamilNadu', 'BE', 'II Year', 'Information Technology', 59, 'g1.jpg', '979685489679', 'Perma98', 'Unblocked');

-- --------------------------------------------------------

--
-- Table structure for table `warden`
--

CREATE TABLE `warden` (
  `id` int(10) NOT NULL,
  `Register_Date` varchar(10) DEFAULT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Date_of_Birth` varchar(15) DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `Phone_Number` bigint(10) DEFAULT NULL,
  `City` varchar(20) DEFAULT NULL,
  `State` varchar(10) DEFAULT NULL,
  `Work_Exp` varchar(20) DEFAULT NULL,
  `Profile` varchar(60) DEFAULT NULL,
  `Aadhaar` varchar(15) DEFAULT NULL,
  `Password` varchar(15) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `warden`
--

INSERT INTO `warden` (`id`, `Register_Date`, `Name`, `Email`, `Date_of_Birth`, `Gender`, `Phone_Number`, `City`, `State`, `Work_Exp`, `Profile`, `Aadhaar`, `Password`, `status`) VALUES
(1, '21-02-2025', 'Deepa', 'deepa1977@gmail.com', '1977-06-21', 'Female', 9783681718, 'Mudurai', 'TamilNadu', '2 Years', 'warden1.jpg', '681928919812', 'Deepa12', 'Unblocked');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `complaints`
--
ALTER TABLE `complaints`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `food_plan`
--
ALTER TABLE `food_plan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `request`
--
ALTER TABLE `request`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `schedule_timing`
--
ALTER TABLE `schedule_timing`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `warden`
--
ALTER TABLE `warden`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `book`
--
ALTER TABLE `book`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `complaints`
--
ALTER TABLE `complaints`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `food_plan`
--
ALTER TABLE `food_plan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `request`
--
ALTER TABLE `request`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `rooms`
--
ALTER TABLE `rooms`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `schedule_timing`
--
ALTER TABLE `schedule_timing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `stock`
--
ALTER TABLE `stock`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `warden`
--
ALTER TABLE `warden`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
