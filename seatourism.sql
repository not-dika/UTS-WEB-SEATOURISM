-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 09, 2025 at 08:45 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `seatourism`
--

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

CREATE TABLE `bookings` (
  `id` int(11) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `destination` varchar(255) NOT NULL,
  `additional_requirement` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`id`, `full_name`, `email`, `destination`, `additional_requirement`) VALUES
(1, 'John Doe', 'john.doe@example.com', 'Bali', 'Vegan meals preferred');

-- --------------------------------------------------------

--
-- Table structure for table `destination_highlights`
--

CREATE TABLE `destination_highlights` (
  `id` int(11) NOT NULL,
  `destination` varchar(100) DEFAULT NULL,
  `best_time_to_visit` varchar(100) DEFAULT NULL,
  `avg_temperature` varchar(50) DEFAULT NULL,
  `must_visit_attractions` text DEFAULT NULL,
  `avg_daily_budget` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `destination_highlights`
--

INSERT INTO `destination_highlights` (`id`, `destination`, `best_time_to_visit`, `avg_temperature`, `must_visit_attractions`, `avg_daily_budget`) VALUES
(2, 'Vietnam', 'October - April', '25-30°C (77-86°F)', 'Ha Long Bay, Hanoi Old Quarter, Ho Chi Minh City', '$40 - $80'),
(3, 'Bali', 'April - October', '26-30°C (79-86°F)', 'Ubud Monkey Forest, Tanah Lot Temple, Uluwatu Temple', '$45 - $90'),
(4, 'Singapore', 'February - April', '27-32°C (81-90°F)', 'Marina Bay Sands, Gardens by the Bay, Sentosa Island', '$100 - $200'),
(5, 'Cambodia', 'November - February', '25-30°C (77-86°F)', 'Angkor Wat, Phnom Penh Royal Palace, Siem Reap', '$35 - $70'),
(7, 'Thailand', 'November - February', '26-32°C (79-90°F)', 'Bangkok Grand Palace, Ayutthaya Historical Park, Chiang Mai Old City', '$50 - $100');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bookings`
--
ALTER TABLE `bookings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `destination_highlights`
--
ALTER TABLE `destination_highlights`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bookings`
--
ALTER TABLE `bookings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `destination_highlights`
--
ALTER TABLE `destination_highlights`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
