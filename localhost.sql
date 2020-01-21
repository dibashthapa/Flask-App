-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 21, 2020 at 11:47 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.4.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `API`
--
CREATE DATABASE IF NOT EXISTS `API` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `API`;

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `meme`
--

CREATE TABLE `meme` (
  `id` int(200) NOT NULL,
  `names` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `url` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `width` int(11) NOT NULL,
  `height` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `meme`
--

INSERT INTO `meme` (`id`, `names`, `url`, `width`, `height`) VALUES
(188390779, 'Woman Yelling At Cat', 'https://i.imgflip.com/345v97.jpg', 680, 438),
(112126428, 'Distracted Boyfriend', 'https://i.imgflip.com/1ur9b0.jpg', 1200, 800),
(181913649, 'Drake Hotline Bling', 'https://i.imgflip.com/30b1gx.jpg', 1200, 1200),
(87743020, 'Two Buttons', 'https://i.imgflip.com/1g8my4.jpg', 600, 908),
(102156234, 'Mocking Spongebob', 'https://i.imgflip.com/1otk96.jpg', 502, 353),
(129242436, 'Change My Mind', 'https://i.imgflip.com/24y43o.jpg', 482, 361),
(124822590, 'Left Exit 12 Off Ramp', 'https://i.imgflip.com/22bdq6.jpg', 804, 767),
(93895088, 'Expanding Brain', 'https://i.imgflip.com/1jwhww.jpg', 857, 1202),
(438680, 'Batman Slapping Robin', 'https://i.imgflip.com/9ehk.jpg', 400, 387),
(119139145, 'Blank Nut Button', 'https://i.imgflip.com/1yxkcp.jpg', 600, 446),
(131087935, 'Running Away Balloon', 'https://i.imgflip.com/261o3j.jpg', 761, 1024),
(196652226, 'Spongebob Ight Imma Head Out', 'https://i.imgflip.com/392xtu.jpg', 822, 960),
(155067746, 'Surprised Pikachu', 'https://i.imgflip.com/2kbn1e.jpg', 1893, 1893),
(1035805, 'Boardroom Meeting Suggestion', 'https://i.imgflip.com/m78d.jpg', 500, 649),
(4087833, 'Waiting Skeleton', 'https://i.imgflip.com/2fm6x.jpg', 298, 403),
(89370399, 'Roll Safe Think About It', 'https://i.imgflip.com/1h7in3.jpg', 702, 395),
(178591752, 'Tuxedo Winnie The Pooh', 'https://i.imgflip.com/2ybua0.png', 800, 582),
(134797956, 'American Chopper Argument', 'https://i.imgflip.com/2896ro.jpg', 640, 1800),
(100777631, 'Is This A Pigeon', 'https://i.imgflip.com/1o00in.jpg', 1587, 1425),
(114585149, 'Inhaling Seagull', 'https://i.imgflip.com/1w7ygt.jpg', 1269, 2825),
(91538330, 'X, X Everywhere', 'https://i.imgflip.com/1ihzfe.jpg', 2118, 1440),
(97984, 'Disaster Girl', 'https://i.imgflip.com/23ls.jpg', 500, 375),
(61579, 'One Does Not Simply', 'https://i.imgflip.com/1bij.jpg', 568, 335),
(123999232, 'The Scroll Of Truth', 'https://i.imgflip.com/21tqf4.jpg', 1280, 1236),
(27813981, 'Hide the Pain Harold', 'https://i.imgflip.com/gk5el.jpg', 480, 601),
(161865971, 'Marked Safe From', 'https://i.imgflip.com/2odckz.jpg', 618, 499),
(101470, 'Ancient Aliens', 'https://i.imgflip.com/26am.jpg', 500, 437),
(124055727, 'Y\'all Got Any More Of That', 'https://i.imgflip.com/21uy0f.jpg', 600, 471),
(175540452, 'Unsettled Tom', 'https://i.imgflip.com/2wifvo.jpg', 680, 550),
(21735, 'The Rock Driving', 'https://i.imgflip.com/grr.jpg', 568, 700),
(91545132, 'Trump Bill Signing', 'https://i.imgflip.com/1ii4oc.jpg', 1866, 1529),
(28251713, 'Oprah You Get A', 'https://i.imgflip.com/gtj5t.jpg', 620, 465),
(135678846, 'Who Killed Hannibal', 'https://i.imgflip.com/28s2gu.jpg', 1280, 1440),
(61520, 'Futurama Fry', 'https://i.imgflip.com/1bgw.jpg', 552, 414),
(61532, 'The Most Interesting Man In The World', 'https://i.imgflip.com/1bh8.jpg', 550, 690),
(101288, 'Third World Skeptical Kid', 'https://i.imgflip.com/265k.jpg', 426, 426),
(6235864, 'Finding Neverland', 'https://i.imgflip.com/3pnmg.jpg', 423, 600),
(132769734, 'Hard To Swallow Pills', 'https://i.imgflip.com/271ps6.jpg', 680, 979),
(84341851, 'Evil Kermit', 'https://i.imgflip.com/1e7ql7.jpg', 700, 325),
(61539, 'First World Problems', 'https://i.imgflip.com/1bhf.jpg', 552, 367),
(563423, 'That Would Be Great', 'https://i.imgflip.com/c2qn.jpg', 526, 440),
(101511, 'Dont You Squidward', 'https://i.imgflip.com/26br.jpg', 500, 333),
(14230520, 'Black Girl Wat', 'https://i.imgflip.com/8h0c8.jpg', 599, 626),
(61556, 'Grandma Finds The Internet', 'https://i.imgflip.com/1bhw.jpg', 640, 480),
(61546, 'Brace Yourselves X is Coming', 'https://i.imgflip.com/1bhm.jpg', 622, 477),
(184801100, 'Me And The Boys', 'https://i.imgflip.com/320xfw.jpg', 720, 476),
(14371066, 'Star Wars Yoda', 'https://i.imgflip.com/8k0sa.jpg', 620, 714),
(101910402, 'Who Would Win?', 'https://i.imgflip.com/1ooaki.jpg', 802, 500),
(16464531, 'But Thats None Of My Business', 'https://i.imgflip.com/9sw43.jpg', 600, 600),
(61527, 'Y U No', 'https://i.imgflip.com/1bh3.jpg', 500, 500),
(5496396, 'Leonardo Dicaprio Cheers', 'https://i.imgflip.com/39t1o.jpg', 600, 400),
(922147, 'Laughing Men In Suits', 'https://i.imgflip.com/jrj7.jpg', 500, 333),
(101287, 'Third World Success Kid', 'https://i.imgflip.com/265j.jpg', 500, 500),
(61585, 'Bad Luck Brian', 'https://i.imgflip.com/1bip.jpg', 475, 562),
(235589, 'Evil Toddler', 'https://i.imgflip.com/51s5.jpg', 500, 332),
(9440985, 'Face You Make Robert Downey Jr', 'https://i.imgflip.com/5mcpl.jpg', 460, 523),
(8072285, 'Doge', 'https://i.imgflip.com/4t0m5.jpg', 620, 620),
(61582, 'Creepy Condescending Wonka', 'https://i.imgflip.com/1bim.jpg', 550, 545),
(61533, 'X All The Y', 'https://i.imgflip.com/1bh9.jpg', 500, 355),
(40945639, 'Dr Evil Laser', 'https://i.imgflip.com/odluv.jpg', 500, 405),
(71428573, 'Say it Again, Dexter', 'https://i.imgflip.com/16iyn1.jpg', 698, 900),
(3218037, 'This Is Where I\'d Put My Trophy If I Had One', 'https://i.imgflip.com/1wz1x.jpg', 300, 418),
(460541, 'Jack Sparrow Being Chased', 'https://i.imgflip.com/9vct.jpg', 500, 375),
(170715647, 'Well Yes, But Actually No', 'https://i.imgflip.com/2tn11b.jpg', 1600, 1218),
(99683372, 'Sleeping Shaq', 'https://i.imgflip.com/1nck6k.jpg', 640, 631),
(444501, 'Maury Lie Detector', 'https://i.imgflip.com/9iz9.jpg', 381, 378),
(100947, 'Matrix Morpheus', 'https://i.imgflip.com/25w3.jpg', 500, 303),
(163573, 'Imagination Spongebob', 'https://i.imgflip.com/3i7p.jpg', 500, 366),
(371382, 'Simba Shadowy Place', 'https://i.imgflip.com/7yk6.jpg', 363, 720),
(157978092, 'Presidential Alert', 'https://i.imgflip.com/2m20oc.jpg', 920, 534),
(89655, 'Uncle Sam', 'https://i.imgflip.com/1x6f.jpg', 620, 833),
(6531067, 'See Nobody Cares', 'https://i.imgflip.com/3vzej.jpg', 620, 676),
(61580, 'Too Damn High', 'https://i.imgflip.com/1bik.jpg', 420, 316),
(61544, 'Success Kid', 'https://i.imgflip.com/1bhk.jpg', 500, 500),
(405658, 'Grumpy Cat', 'https://i.imgflip.com/8p0a.jpg', 500, 617),
(4173692, 'Scared Cat', 'https://i.imgflip.com/2hgfw.jpg', 620, 464),
(61581, 'Put It Somewhere Else Patrick', 'https://i.imgflip.com/1bil.jpg', 343, 604),
(28034788, 'Marvel Civil War 1', 'https://i.imgflip.com/govs4.jpg', 423, 734),
(285870, 'Squidward', 'https://i.imgflip.com/64ku.jpg', 500, 750),
(56225174, 'Be Like Bill', 'https://i.imgflip.com/xh3me.jpg', 913, 907),
(21604248, 'Mugatu So Hot Right Now', 'https://i.imgflip.com/cv1y0.jpg', 620, 497),
(1509839, 'Captain Picard Facepalm', 'https://i.imgflip.com/wczz.jpg', 500, 324),
(61733537, 'Mr Krabs Blur Meme', 'https://i.imgflip.com/10r5wh.jpg', 708, 495),
(101716, 'Yo Dawg Heard You', 'https://i.imgflip.com/26hg.jpg', 500, 323),
(61516, 'Philosoraptor', 'https://i.imgflip.com/1bgs.jpg', 500, 500),
(47235368, 'Good Fellas Hilarious', 'https://i.imgflip.com/s4f1k.jpg', 1600, 1150),
(27920, 'Surprised Koala', 'https://i.imgflip.com/ljk.jpg', 500, 667),
(29617627, 'Look At Me', 'https://i.imgflip.com/hmt3v.jpg', 300, 300),
(259680, 'Am I The Only One Around Here', 'https://i.imgflip.com/5kdc.jpg', 500, 348),
(155518747, 'Pentagon Hexagon Octagon', 'https://i.imgflip.com/2klb17.jpg', 720, 710),
(74191766, 'Arthur Fist', 'https://i.imgflip.com/1866qe.jpg', 583, 328),
(7253945, 'Kevin Hart', 'https://i.imgflip.com/4bh6h.jpg', 560, 371),
(164335977, 'Bird Box', 'https://i.imgflip.com/2puag9.jpg', 1400, 1400),
(1790995, 'And everybody loses their minds', 'https://i.imgflip.com/12dxv.jpg', 620, 349),
(245898, 'Picard Wtf', 'https://i.imgflip.com/59qi.jpg', 500, 350),
(195389, 'Sparta Leonidas', 'https://i.imgflip.com/46rh.jpg', 500, 264),
(109765, 'Ill Just Wait Here', 'https://i.imgflip.com/2cp1.jpg', 491, 550),
(54401824, 'And Just Like That', 'https://i.imgflip.com/we0ps.jpg', 1012, 675),
(19209570, 'What Do We Want', 'https://i.imgflip.com/bfq76.jpg', 480, 352),
(1232104, 'Pepperidge Farm Remembers', 'https://i.imgflip.com/qep4.jpg', 500, 500);

-- --------------------------------------------------------

--
-- Table structure for table `Posts`
--

CREATE TABLE `Posts` (
  `id` int(11) NOT NULL,
  `Email` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `Post` text COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Posts`
--

INSERT INTO `Posts` (`id`, `Email`, `Post`) VALUES
(21, 'dibashthapa55@gmail.com', '                     \r\n            this is dibash and i want to say hi'),
(22, 'dibashthapa55@gmail.com', '                     \r\n            This is dibash and i am testing the site'),
(23, 'dibashthapa55@gmail.com', '1\' OR \'1\'= \'1'),
(24, 'dibashthapa55@gmail.com', '                     \r\n            /<script>alert(\"hello world\")</script>/');

-- --------------------------------------------------------

--
-- Table structure for table `Quiz`
--

CREATE TABLE `Quiz` (
  `id` int(100) NOT NULL,
  `difficulty` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `questions` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `correct_answers` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `incorrect_answers` text COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tasks`
--

CREATE TABLE `tasks` (
  `id` int(11) NOT NULL,
  `tasks` text COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `tasks`
--

INSERT INTO `tasks` (`id`, `tasks`) VALUES
(49, 'Hello This is dibash'),
(50, 'This is malificient');

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `id` int(11) NOT NULL,
  `Name` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `Email` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `Password` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` text COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`id`, `Name`, `Email`, `Password`, `image`) VALUES
(1, 'Dibash', 'dibashthapa55@gmail.com', '12345678', 'binary.png'),
(6, 'Rojal', 'rojal@gmail.com', '12345678', 'momo.jpg'),
(7, 'Samir', 'samir@gmail.com', 'asdf', 'default.png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Posts`
--
ALTER TABLE `Posts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tasks`
--
ALTER TABLE `tasks`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Posts`
--
ALTER TABLE `Posts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `tasks`
--
ALTER TABLE `tasks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
