CREATE TABLE `customer` (
  `customer_id` int PRIMARY KEY AUTO_INCREMENT,
  `name` text,
  `address` text,
  `contact` text,
  `age` int
);

CREATE TABLE `ram` (
  `ram_id` int PRIMARY KEY AUTO_INCREMENT,
  `ram_number` int
);

CREATE TABLE `brand` (
  `brand_id` int PRIMARY KEY AUTO_INCREMENT,
  `name` text,
  `year_of_manufacture` int,
  `hard_disk_type` text,
  `customer_id` int,
  `ram_id` int
);

ALTER TABLE `brand` ADD FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`);

ALTER TABLE `brand` ADD FOREIGN KEY (`ram_id`) REFERENCES `ram` (`ram_id`);
